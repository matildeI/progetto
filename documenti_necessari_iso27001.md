# Documentazione per la Certificazione ISO/IEC 27001:2022
*Lista dei documenti obbligatori e delle policy operative richieste dallo standard*

Questo documento elenca e descrive in dettaglio la documentazione necessaria per ottenere la certificazione **ISO/IEC 27001:2022**, basandosi direttamente sull'analisi del testo ufficiale della norma (Clausole 4-10 ed Annex A).

La documentazione si suddivide in due macro-categorie:
1. **Documenti del Sistema di Gestione (Clausole 4-10):** Obbligatori per dimostrare la conformità ai processi di governance della sicurezza.
2. **Politiche e Procedure di Controllo (Annex A):** Richieste per dimostrare l'implementazione pratica dei controlli tecnici, fisici ed organizzativi.

---

## 1. Documenti del Sistema di Gestione (Capitoli 4-10)

Questi documenti regolano il funzionamento complessivo del SGSI (Sistema di Gestione della Sicurezza delle Informazioni).

### 1.1 Campo di Applicazione dell'SGSI (Scope)
* **Riferimento Standard:** Clausola 4.3 (*"The scope shall be available as documented information"*).
* **Contenuto:** Descrive i confini dell'SGSI. Specifica quali sedi fisiche, quali rami aziendali, quali sistemi informatici e quali servizi/prodotti software (es. l'infrastruttura Cloud del SaaS di punta) sono inclusi nel perimetro di certificazione.

### 1.2 Politica per la Sicurezza delle Informazioni
* **Riferimento Standard:** Clausola 5.2 (*"The information security policy shall: be available as documented information"*).
* **Contenuto:** È il manifesto strategico della sicurezza, firmato dall'alta direzione. Definisce gli impegni aziendali (integrità, riservatezza e disponibilità dei dati), gli obiettivi generali e la struttura organizzativa per raggiungerli. Deve essere comunicata a tutto il personale.

### 1.3 Processo di Valutazione del Rischio (Risk Assessment Methodology)
* **Riferimento Standard:** Clausola 6.1.2 (*"The organization shall retain documented information about the information security risk assessment process"*).
* **Contenuto:** Stabilisce la metodologia formale per identificare e valutare i rischi. Definisce la scala di probabilità e impatto, i criteri di accettabilità del rischio per l'azienda (Risk Appetite) e la frequenza delle revisioni.

### 1.4 Processo di Trattamento del Rischio (Risk Treatment Process)
* **Riferimento Standard:** Clausola 6.1.3 (*"The organization shall retain documented information about the information security risk treatment process"*).
* **Contenuto:** Descrive le regole per gestire i rischi che superano la soglia di accettabilità (es. mitigazione tramite controlli, trasferimento assicurativo, accettazione o cessazione dell'attività a rischio).

### 1.5 Registro dei Rischi (Risk Register) e Risultati del Risk Assessment
* **Riferimento Standard:** Clausola 8.2 (*"The organization shall retain documented information of the results of the information security risk assessments"*).
* **Contenuto:** L'applicazione pratica del Risk Assessment. Contiene la lista reale degli asset (dati clienti, repository, server) associati alle minacce e vulnerabilità specifiche, con il relativo calcolo del livello di rischio iniziale e residuo.

### 1.6 Piano di Trattamento dei Rischi (Risk Treatment Plan - RTP)
* **Riferimento Standard:** Clausola 8.3 (*"The organization shall retain documented information of the results of the information security risk treatment"*).
* **Contenuto:** Un piano d'azione dettagliato che specifica per ciascun rischio da mitigare: i controlli scelti (dall'Annex A o esterni), il responsabile dell'implementazione, le scadenze temporali e il budget approvato.

### 1.7 Dichiarazione di Applicabilità (Statement of Applicability - SoA)
* **Riferimento Standard:** Clausola 6.1.3 d) (*"produce a Statement of Applicability..."*).
* **Contenuto:** Il documento fulcro dell'audit. Mappa tutti i 93 controlli dell'Annex A indicando: se il controllo è applicato o meno, la giustificazione tecnica dell'inclusione/esclusione, lo stato attuale (implementato, in corso) e il metodo di implementazione.

### 1.8 Obiettivi di Sicurezza delle Informazioni
* **Riferimento Standard:** Clausola 6.2 (*"The organization shall retain documented information on the information security objectives"*).
* **Contenuto:** Elenco di target misurabili per la sicurezza (es. "Risoluzione dei bug critici di sicurezza entro 48 ore", "Uptime minimo dell'infrastruttura SaaS pari al 99.9%"). Deve indicare le risorse necessarie e come verranno valutati i risultati.

### 1.9 Prove di Competenza (Competence Evidence)
* **Riferimento Standard:** Clausola 7.2 d) (*"retain appropriate documented information as evidence of competence"*).
* **Contenuto:** Record che attestano le capacità professionali del team nel perimetro di sicurezza. Include CV, certificazioni dei tecnici (es. AWS, CISSP), e i record di avvenuta partecipazione ai corsi di formazione sulla sicurezza.

### 1.10 Pianificazione e Controllo Operativo
* **Riferimento Standard:** Clausola 8.1 (*"Documented information shall be available to the extent necessary to have confidence that the processes have been carried out as planned"*).
* **Contenuto:** Evidenze dell'esecuzione controllata dei processi aziendali (es. verbali di approvazione dei rilasci software, checklist di deploy, audit log delle modifiche infrastrutturali).

### 1.11 Monitoraggi, Misure e Risultati delle Valutazioni
* **Riferimento Standard:** Clausola 9.1 (*"Documented information shall be available as evidence of the results [of monitoring and measurement]"*).
* **Contenuto:** Dati e metriche che dimostrano il funzionamento dei controlli nel tempo (es. log di tentativi di accesso falliti, grafici di utilizzo della CPU, scansioni antivirus centralizzate, report periodici di vulnerabilità).

### 1.12 Programma e Risultati degli Audit Interni
* **Riferimento Standard:** Clausola 9.2.2 (*"Documented information shall be available as evidence of the implementation of the audit programme(s) and the audit results"*).
* **Contenuto:** Il piano degli audit interni (calendario, perimetro, criteri) e il report finale dell'audit interno condotto prima dell'esame ufficiale, contenente i punti di forza e le Non Conformità rilevate.

### 1.13 Verbale del Riesame della Direzione (Management Review)
* **Riferimento Standard:** Clausola 9.3.3 (*"Documented information shall be available as evidence of the results of management reviews"*).
* **Contenuto:** Il verbale ufficiale dell'incontro formale tra la direzione (CEO, soci) e il CISO. Contiene l'analisi dello stato del SGSI, le decisioni sul trattamento dei rischi, le modifiche alle policy e lo stanziamento formale delle risorse per l'anno successivo.

### 1.14 Registro delle Non Conformità e Azioni Correttive
* **Riferimento Standard:** Clausola 10.2 f) e g) (*"Documented information shall be available as evidence of: the nature of the nonconformities... and the results of any corrective action"*).
* **Contenuto:** Il database in cui vengono censite le anomalie (incidenti di sicurezza, deviazioni dalle policy, rilievi dell'auditor) e le azioni correttive pianificate ed eseguite per rimuovere la causa radice ed evitarne la ripetizione.

---

## 2. Topic-Specific Policies e Procedure Operative (Annex A)

Queste policy sono richieste dal controllo **A.5.1** (*Policies for information security*) e dagli altri specifici controlli tecnologici e organizzativi dell'Annex A.

### 2.1 Inventario e Classificazione degli Asset (A.5.9 & A.5.12)
* **Contenuto:**
  * **Inventario degli Asset:** Un elenco censito di tutte le risorse critiche: hardware (laptop dipendenti), software, infrastruttura cloud (database, VPS), persone e uffici fisici. Deve indicare chiaramente il proprietario (Asset Owner).
  * **Policy di Classificazione:** Definisce le regole per classificare le informazioni (es. *Pubblico, Interno, Confidenziale, Altamente Riservato*) e le relative misure di protezione.

### 2.2 Policy di Controllo Accessi (A.5.15 & A.8.3)
* **Contenuto:** Regole per l'autenticazione logica ai sistemi critici. Stabilisce l'obbligo di autenticazione a più fattori (MFA), le politiche di gestione delle password, la revoca immediata delle credenziali in fase di offboarding del dipendente e la revisione periodica semestrale dei privilegi amministrativi.

### 2.3 Policy di Sviluppo Software Sicuro (Secure SDLC) (A.8.25 - A.8.29)
* **Contenuto:** Regola le fasi del ciclo di sviluppo: criteri per la scrittura di codice sicuro (es. standard OWASP), obbligo di code review indipendenti prima di ogni merge, automazione delle scansioni di vulnerabilità delle librerie e separazione logica e fisica tra ambienti di sviluppo, test e produzione.

### 2.4 Policy di Crittografia e Gestione Chiavi (A.8.24)
* **Contenuto:** Regolamenta l'uso della cifratura in azienda. Impone che i laptop dei dipendenti abbiano la crittografia del disco attiva (BitLocker/FileVault), definisce l'uso obbligatorio di protocolli cifrati per il transito dei dati (HTTPS/TLS) e stabilisce le regole per la custodia delle chiavi API e crittografiche.

### 2.5 Policy di Backup e Disastro Recupero (A.8.13 & A.5.29)
* **Contenuto:** Definisce la frequenza dei backup (es. giornalieri incrementali), i tempi di conservazione (retention policy) e la ridondanza geografica. Deve includere una procedura di test periodico del ripristino per verificare l'effettivo funzionamento dei backup.

### 2.6 Policy sul Lavoro da Remoto e Mobile Device (A.6.7 & A.8.1)
* **Contenuto:** Regole di condotta per lo smart working. Vieta l'uso di computer personali non gestiti (BYOD) per accedere all'ambiente di produzione, impone l'uso di connessioni cifrate (VPN o reti protette) e stabilisce le procedure in caso di smarrimento o furto di un dispositivo aziendale (remote wipe).

### 2.7 Procedure Operative di Gestione IT (Documented Operating Procedures) (A.5.37)
* **Contenuto:** Istruzioni operative per l'amministrazione ordinaria dei sistemi (es. procedura per la patch dei server, gestione dei log di sistema, monitoraggio della capacità dell'infrastruttura).

### 2.8 Procedura di Incident Management e Business Continuity (A.5.24 & A.5.29)
* **Contenuto:**
  * **Incident Management:** Canali di segnalazione dei sospetti incidenti, ruoli del team di risposta (Incident Response Team) e passi operativi per contenere la minaccia, raccogliere le evidenze (A.5.28) e ripristinare il servizio.
  * **Business Continuity:** Piano per garantire il funzionamento aziendale in caso di gravi interruzioni (es. indisponibilità del cloud provider primario).

### 2.9 Accordi di Riservatezza (NDA) e Relazioni con i Fornitori (A.6.6 & A.5.19 - A.5.22)
* **Contenuto:**
  * **NDA:** Accordi legali firmati con i dipendenti all'atto dell'assunzione e con i partner esterni.
  * **Supplier Security Policy:** Requisiti minimi di sicurezza richiesti ai terzisti (es. richiedere certificati ISO 27001 o report SOC 2 ai cloud provider) e le clausole standard da inserire nei contratti commerciali.
