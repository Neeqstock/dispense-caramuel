# CIDR, supernetting e VLSM: differenze ed esempio pratico

Questa guida segue un blocco di indirizzi IP dal livello globale, dove le reti vengono annunciate e aggregate, fino alla suddivisione interna di una rete aziendale.

> **Nota:** gli indirizzi e gli operatori citati nell'esempio sono usati a scopo didattico. Non rappresentano un'assegnazione reale a un provider o a un'azienda.

## 1. Differenze in breve

- **CIDR (Classless Inter-Domain Routing):** usa prefissi di lunghezza variabile, scritti con la notazione slash (per esempio `/16`), superando la suddivisione rigida in classi IP.
- **Supernetting:** aggrega più reti contigue in un prefisso più ampio, così da poter annunciare una rotta riassuntiva. È una tecnica resa possibile dall'indirizzamento CIDR.
- **VLSM (Variable-Length Subnet Mask):** suddivide una rete in sottoreti di dimensioni diverse, assegnando a ciascuna la maschera più adatta alle esigenze.

In breve: il supernetting unisce reti; il VLSM suddivide una rete in sottoreti di dimensioni differenti.

## 2. Esempio: dall'aggregazione globale alla rete aziendale

### Fase 1: assegnazione dei blocchi agli operatori

La IANA distribuisce blocchi di indirizzi ai registri Internet regionali (RIR), che a loro volta li assegnano ai registri locali (LIR) e agli operatori secondo le procedure previste.

Per semplificare l'esempio, consideriamo un blocco `80.0.0.0/8` e una sua porzione, `80.20.0.0/16`, assegnata a un operatore. La notazione `/16` indica che i primi 16 bit identificano il prefisso di rete.

### Fase 2: suddivisione del blocco in reti più piccole

L'operatore suddivide `80.20.0.0/16` in quattro reti `/18`, ciascuna corrispondente a una macro-area:

1. `80.20.0.0/18` — Milano
2. `80.20.64.0/18` — Torino
3. `80.20.128.0/18` — Venezia
4. `80.20.192.0/18` — Bologna

Queste quattro reti sono contigue e allineate: insieme coprono esattamente l'intervallo `80.20.0.0`–`80.20.255.255`, cioè il blocco `80.20.0.0/16`.

### Fase 3: supernetting e annuncio della rotta aggregata

Se le condizioni di instradamento e le policy lo consentono, l'operatore può annunciare verso l'esterno la rotta aggregata `80.20.0.0/16` invece delle quattro rotte `/18`.

I router che ricevono l'annuncio apprendono così un solo prefisso per raggiungere quel blocco. All'interno della rete, i router dell'operatore continuano a instradare il traffico verso la sottorete corretta.

Questa aggregazione riduce il numero di rotte da propagare, ma non è automatica: i prefissi devono essere aggregabili e la configurazione di routing deve consentirlo.

### Fase 4: VLSM nella rete aziendale

Consideriamo ora una rete aziendale `80.20.10.0/24`, con 256 indirizzi complessivi, da `80.20.10.0` a `80.20.10.255`.

Le esigenze sono:

1. **Sviluppo:** 100 host
2. **Amministrazione:** 50 host
3. **Marketing:** 20 host
4. **Collegamento punto-punto tra router:** 2 indirizzi host

#### Se si usa FLSM

Con FLSM (*Fixed-Length Subnet Mask*), tutte le sottoreti avrebbero la stessa dimensione. Dividendo il `/24` in quattro sottoreti `/26`, ciascuna avrebbe 64 indirizzi complessivi e 62 indirizzi host utilizzabili.

Queste sottoreti non sarebbero sufficienti per Sviluppo, che richiede 100 host. Inoltre, sarebbero sovradimensionate per il collegamento tra router, che richiede soltanto 2 indirizzi host.

#### Se si usa VLSM

Con VLSM, si assegnano le sottoreti in ordine decrescente di dimensione. La tabella distingue gli indirizzi totali del blocco dagli indirizzi host utilizzabili: in una normale sottorete IPv4, il primo indirizzo identifica la rete e l'ultimo è l'indirizzo broadcast.

| Reparto | Host richiesti | Prefisso | Indirizzi totali | Indirizzi host utilizzabili | Blocco assegnato | Host utilizzabili nel blocco |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Sviluppo | 100 | `/25` | 128 | 126 | `80.20.10.0`–`80.20.10.127` | `80.20.10.1`–`80.20.10.126` |
| Amministrazione | 50 | `/26` | 64 | 62 | `80.20.10.128`–`80.20.10.191` | `80.20.10.129`–`80.20.10.190` |
| Marketing | 20 | `/27` | 32 | 30 | `80.20.10.192`–`80.20.10.223` | `80.20.10.193`–`80.20.10.222` |
| Collegamento router | 2 | `/30` | 4 | 2 | `80.20.10.224`–`80.20.10.227` | `80.20.10.225`–`80.20.10.226` |

Restano liberi gli indirizzi da `80.20.10.228` a `80.20.10.255`, per un totale di 28 indirizzi. Questo spazio può essere ulteriormente suddiviso in sottoreti allineate, per esempio un `/30`, un `/29` e un `/28`.

## 3. Riepilogo: supernetting e VLSM

| Aspetto | CIDR e supernetting | VLSM |
| --- | --- | --- |
| Operazione | Aggrega più prefissi contigui in un prefisso più ampio | Suddivide un blocco in sottoreti di dimensioni diverse |
| Esempio | Quattro reti `/18` aggregate in una `/16` | Una rete `/24` suddivisa in `/25`, `/26`, `/27` e `/30` |
| Ambito tipico | Annunci e tabelle di routing, per esempio con BGP | Progettazione delle sottoreti di una rete aziendale o di un provider |
| Obiettivo | Ridurre il numero di rotte annunciate | Assegnare lo spazio IP in modo aderente al numero di host necessario |

**In sintesi:** CIDR è il metodo di indirizzamento a prefissi; il supernetting usa i prefissi per aggregare rotte, mentre il VLSM permette di suddividere una rete in sottoreti di dimensioni diverse.
