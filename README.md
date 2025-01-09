# Attack/Defense Infrastructure

![Infrastruttura](assets/infrastruttura.png)

Questa infrastruttura è stata progettata e implementata per gestire competizioni Capture The Flag (CTF) di tipo Attack/Defense. Combina strumenti di containerizzazione, amministrazione di rete e gestione dei punteggi per simulare scenari reali di cybersecurity.

## Introduzione

**A/D (Attack/Defense)** è un gioco strutturato secondo le regole dei CTF, che permette ai partecipanti di:

- **Sviluppare competenze**: Migliorare le conoscenze pratiche in cybersecurity.
- **Favorire il lavoro di squadra**: Promuovere collaborazione e strategia.
- **Incoraggiare il pensiero critico**: Risolvere problemi sotto pressione.
- **Simulare scenari reali**: Affrontare sfide di sicurezza informatica simili a quelle del mondo reale.

## Struttura della Competizione

### Regole principali:
- **Durata**: 8 ore.
- **Fasi**:
  - **T+0**: Accesso alle VM con rete chiusa (fase di analisi e personalizzazione).
  - **T+1h**: Apertura della rete e inizio degli attacchi e difese.
  - **T+6h**: Congelamento della classifica.
  - **T+8h**: Fine competizione.

### Obiettivi:
- **Attaccare**: Sfruttare vulnerabilità nei servizi avversari per catturare flag.
- **Difendere**: Proteggere i propri servizi da attacchi esterni.
- **Mantenere**: Garantire la disponibilità dei servizi per ottenere punti SLA.

## Configurazione e Avvio

### Requisiti:
- **Proxmox** per gestire le VM.
- **Docker** per implementare i servizi vulnerabili.
- **Gameserver** per gestire la gara e i punteggi.

### Avvio dei Container:
Eseguire i seguenti comandi per avviare i servizi vulnerabili:
```bash
docker compose up --build -d

```

### Configurazione e Avvio del Gameserver:
	1.	Modificare il file config.yml per impostare i parametri della competizione.
	2.	Eseguire i seguenti comandi:


```bash
./control.py setup
./control.py start
```


	3.	Al termine della gara, ripristinare lo stato iniziale con:
```bash
./control.py reset
```


### Sistema di Punteggio

I punti vengono assegnati in base a tre criteri:
	1.	Invio di flag rubate: Tramite il servizio di flag submission.
	2.	Difesa delle proprie flag: Impedendo agli avversari di catturarle.
	3.	Punti SLA (Service Level Agreement): Per ogni servizio attivo e funzionante.

Dettagli Tecnici
	•	Firewall: Configurato tramite OPNsense, con regole specifiche per abilitare l’accesso VPN e prevenire blocchi non autorizzati.
	•	Overlay Network: Implementata con WireGuard per la comunicazione tra le VM.
	•	Checker: Garantisce l’integrità dei servizi e aggiorna il punteggio in base allo stato dei servizi e alle flag catturate.

### Crediti

Progetto sviluppato da:
	•	Francesco Balassone
	•	Francesco Riccio

Con il supporto di:
	•	Sofia Della Penna, Raffaele D’Ambrosio, Alessio Foggia

Sponsor:
	•	Brigata Nerd (Clanto), per il server fisico.

	“Strong men, strong fates. Weak men, weak fates. There is no other way.” – Luciano Spalletti, Scudetto 2023
