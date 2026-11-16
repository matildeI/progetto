import json
import re #tag formattazione
from pathlib import Path #percorsi cartelle
from docxtpl import DocxTemplate, RichText #compilare file docx
from jinja2 import Template


def formatta_testo(testo_grezzo, contesto): 
    #prende un singolo testo da paragrafi, non funziona.

    testo_compilato = Template(testo_grezzo).render(contesto) 

    rt = RichText()
    tokens = re.split(r"(<b>.*?</b>|<i>.*?</i>|<u>.*?</u>)", testo_compilato, flags=re.DOTALL)

    #questo solo per formattare
    for token in tokens:
        if not token:
            continue
        if token.startswith("<b>") and token.endswith("</b>"):
            rt.add(token[3:-4], bold=True)
        elif token.startswith("<i>") and token.endswith("</i>"):
            rt.add(token[3:-4], italic=True)
        elif token.startswith("<u>") and token.endswith("</u>"):
            rt.add(token[3:-4], underline=True)
        else:
            rt.add(token)

    return rt


def chiedi_booleano(etichetta, required=True, valore_attuale=None): 
    default_str = "s" if valore_attuale is True else ("n" if valore_attuale is False else "") 
    prompt = f"{etichetta} (s/n) [{default_str}]: " if default_str else f"{etichetta} (s/n): "

    while True:
        risposta = input(prompt).strip().lower()
        if risposta == "" and default_str != "":
            return default_str == "s"
        if risposta == "" and not required:
            return None
        if risposta in ("s", "si", "sì", "y", "true"):
            return True
        if risposta in ("n", "no", "false"):
            return False
        print("  -> Risposta non valida. Digita 's' per sì oppure 'n' per no.")


def chiedi_testo(etichetta, required=True, valore_attuale=""):
    ha_default = valore_attuale not in (None, "")
    prompt = f"{etichetta} [{valore_attuale}]: " if ha_default else f"{etichetta}: "

    while True:
        risposta = input(prompt).strip()
        if risposta == "" and ha_default:
            return valore_attuale
        if risposta == "" and not required:
            return ""
        if risposta != "":
            return risposta
        print("  -> Questo campo è obbligatorio, inserisci un valore.")


def chiedi_select(options, required=True, valore_attuale=""):
    for idx, opt in enumerate(options, start=1):
        print(f"    {idx}. {opt}")

    ha_default = valore_attuale in options
    prompt = f"  Scegli numero [{valore_attuale}]: " if ha_default else "  Scegli numero: "

    while True:
        risposta = input(prompt).strip()
        if risposta == "" and ha_default:
            return valore_attuale
        if risposta == "" and not required:
            return ""
        if risposta.isdigit() and 1 <= int(risposta) <= len(options):
            return options[int(risposta) - 1]
        print(f"  -> Inserisci un numero da 1 a {len(options)}.")


def chiedi_array_oggetti(domanda_obj):
    item_schema = domanda_obj.get("item_schema", {})
    required = domanda_obj.get("required", False)
    valori_esistenti = domanda_obj.get("value", [])

    campi_booleani = set()
    if valori_esistenti and isinstance(valori_esistenti[0], dict):
        for k, v in valori_esistenti[0].items():
            if isinstance(v, bool):
                campi_booleani.add(k)

    ha_dati_validi = any(
        any(v not in ("", None, False) for k, v in riga.items() if k not in campi_booleani)
        for riga in valori_esistenti
        if isinstance(riga, dict)
    )

    if ha_dati_validi:
        print(f"  Trovati {len(valori_esistenti)} elementi già compilati.")
        mantieni = input("  Vuoi mantenerli senza riscriverli? [S/n]: ").strip().lower()
        if mantieni in ("", "s", "si", "sì"):
            return valori_esistenti

    if not required:
        compila = input("  Campo opzionale: vuoi inserire degli elementi? [s/N]: ").strip().lower()
        if compila not in ("s", "si", "sì"):
            return []

    nuova_lista = []
    indice = 1
    while True:
        print(f"\n  --- Inserimento elemento #{indice} ---")
        nuovo_oggetto = {}
        for sub_key in item_schema.keys():
            etichetta_pulita = sub_key.replace("_", " ").capitalize()
            if sub_key in campi_booleani or sub_key.endswith("_inclusa"):
                nuovo_oggetto[sub_key] = chiedi_booleano(f"    {etichetta_pulita}?", required=True, valore_attuale=True)
            else:
                nuovo_oggetto[sub_key] = chiedi_testo(f"    {etichetta_pulita}", required=True)

        nuova_lista.append(nuovo_oggetto)
        indice += 1

        altro = input("\n  Vuoi aggiungere un altro elemento a questa tabella? [s/N]: ").strip().lower()
        if altro not in ("s", "si", "sì"):
            break

    return nuova_lista


def esegui_questionario(schema_dati, path_dati):
    titolo = schema_dati.get("metadata", {}).get("titolo", "QUESTIONARIO")
    print("\n" + "=" * 70)
    print(f" {titolo}")
    print(" (Premi INVIO per mantenere i valori già presenti tra parentesi)")
    print("=" * 70)

    for section in schema_dati.get("sections", []):
        print(f"\n{'#' * 70}")
        print(f" {section.get('title', '')}")
        if section.get("description"):
            print(f" {section['description']}")
        print(f"{'#' * 70}")

        for q in section.get("questions", []):
            req_tag = "[OBBLIGATORIO]" if q.get("required") else "[Opzionale]"
            print(f"\n• [{q.get('id', '')}] {q['question']} {req_tag}")
            if q.get("help_text"):
                print(f"  Suggerimento: {q['help_text']}")

            field_type = q.get("field_type", "text")
            required = q.get("required", False)
            valore_attuale = q.get("value")

            if field_type in ("text", "textarea"):
                q["value"] = chiedi_testo("  Risposta", required=required, valore_attuale=valore_attuale)
            elif field_type == "select":
                q["value"] = chiedi_select(q.get("options", []), required=required, valore_attuale=valore_attuale)
            elif field_type == "boolean":
                q["value"] = chiedi_booleano("  Risposta", required=required, valore_attuale=valore_attuale)
            elif field_type == "array_of_objects":
                q["value"] = chiedi_array_oggetti(q)

    with open(path_dati, "w", encoding="utf-8") as f:
        json.dump(schema_dati, f, indent=2, ensure_ascii=False)

    print(f"\nTutte le risposte sono state salvate in: {path_dati}")
    return schema_dati


def estrai_contesto_piatto(schema_dati):
    """Trasforma la struttura a sezioni nel dizionario piatto richiesto da docxtpl."""
    contesto = {}
    for section in schema_dati.get("sections", []):
        for q in section.get("questions", []):
            chiave = q["placeholder_key"].strip("{}").strip()
            valore = q.get("value")

            if q.get("field_type") == "array_of_objects" and isinstance(valore, list):
                righe_pulite = [
                    riga for riga in valore
                    if any(v not in ("", None) for k, v in riga.items() if not isinstance(v, bool))
                ]
                contesto[chiave] = righe_pulite
            elif valore is None:
                contesto[chiave] = ""
            else:
                contesto[chiave] = valore
    return contesto


def scegli_documento(dir_documenti):
    """Mostra le sottocartelle disponibili in 'documenti/' e fa scegliere quale generare."""
    if not dir_documenti.exists():
        raise FileNotFoundError(f"La cartella '{dir_documenti}' non esiste. Creala e inserisci le sottocartelle dei documenti.")

    cartelle = sorted([d for d in dir_documenti.iterdir() if d.is_dir()])
    if not cartelle:
        raise FileNotFoundError(f"Nessuna sottocartella documento trovata in: {dir_documenti}")

    print("\n" + "=" * 50)
    print(" SELEZIONA IL DOCUMENTO DA GENERARE")
    print("=" * 50)
    for idx, cartella in enumerate(cartelle, start=1):
        print(f"  {idx}. {cartella.name}")

    while True:
        scelta = input("\nInserisci il numero del documento: ").strip()
        if scelta.isdigit() and 1 <= int(scelta) <= len(cartelle):
            return cartelle[int(scelta) - 1]
        print(f"  -> Scelta non valida. Inserisci un numero da 1 a {len(cartelle)}.")


def genera_documento():
    base_dir = Path.cwd()
    dir_documenti = base_dir / "documenti"
    path_output_dir = base_dir / "output"

    #sceglie la cartella del documento selezionato
    cartella_doc = scegli_documento(dir_documenti)

    path_dati = cartella_doc / "dati_utente.json"
    path_paragrafi = cartella_doc / "paragrafi.json"
    path_template = cartella_doc / "template.docx"
    path_output = path_output_dir / f"{cartella_doc.name}_compilato.docx"

    # dati utente
    with open(path_dati, "r", encoding="utf-8") as f:
        schema_dati = json.load(f)

    # questionario
    scelta = input(f"\nVuoi compilare/modificare il questionario per '{cartella_doc.name}'? [S/n]: ").strip().lower()
    if scelta in ("", "s", "si", "sì"):
        schema_dati = esegui_questionario(schema_dati, path_dati)

    dati_utente = estrai_contesto_piatto(schema_dati)

    # paragrafi
    with open(path_paragrafi, "r", encoding="utf-8") as f:
        paragrafi_grezzi = json.load(f)

    paragrafi_compilati = {}
    for chiave, valore in paragrafi_grezzi.items():
        if isinstance(valore, list):
            paragrafi_compilati[chiave] = [formatta_testo(voce, dati_utente) for voce in valore]
        else:
            paragrafi_compilati[chiave] = formatta_testo(valore, dati_utente)


    contesto_finale = {**dati_utente, **paragrafi_compilati}

    # controllo segnaposto
    doc = DocxTemplate(path_template)
    variabili_template = doc.get_undeclared_template_variables()
    mancanti = variabili_template - set(contesto_finale.keys())
    if mancanti:
        print(f"\n[ATTENZIONE] Questi segnaposto nel template non sono stati trovati nei JSON: {mancanti}")
        print(f"[INFO] Chiavi lette da paragrafi.json: {list(paragrafi_compilati.keys())}")
        print(f"[INFO] Chiavi lette da dati_utente.json: {list(dati_utente.keys())}\n")

    # salvataggio documento finale
    doc.render(contesto_finale)

    path_output_dir.mkdir(parents=True, exist_ok=True)
    doc.save(path_output)
    print(f"\nDocumento generato con successo in: {path_output}\n")


if __name__ == "__main__":
    genera_documento()