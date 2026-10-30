Punto di partenza

Partire direttamente dal progetto del terzo esercizio. Non creare un nuovo progetto. Sono già presenti Animale, Giraffa e Kira.


1. Creare una seconda classe figlia

Creare una classe Leone che estenda Animale. Il costruttore deve ricevere il nome e la
specie e utilizzare super(). Creare inoltre il metodo ruggisci().

2. Creare Simba

Nel main creare un oggetto Leone chiamato Simba e completarne età e peso tramite i setter.(età 6 e peso 190 kg.)
Richiamare il metodo ruggisci() per verificare il funzionamento del metodo specifico del Leone.


3. Creare la lista dello Zoo

Creare un ArrayList capace di contenere oggetti Animale e  aggiungere alla lista i
quattro animali già presenti nel terzo esercizio e il nuovo Simba:

4. Visualizzare gli animali

Usare un ciclo for-each per leggere la lista e visualizzare almeno nome e specie di ogni animale.


5. Up casting

Creare un riferimento di tipo Animale che punti all'oggetto Kira.

Osservare che una Giraffa può essere trattata come Animale e attraverso il riferimento Animale stampa in output nome e specie.


6. Down casting

Partendo dal riferimento Animale, tornare a trattare l'oggetto come Giraffa.

E quindi richiama il metodo mangia foglie attraverso il riferimento giraffa.


7.Prelevare Simba dalla ArrayList

Prelevare l’elemento della lista (utilizzando “get”) dove abbiamo caricato il nostro animale Simba e  visualizzare nome e specie con i metodi di Animale.

8. Down casting di Simba
Trasformare il riferimento in Leone e Richiamare il
metodo specifico del Leone(ruggisci).


Il progetto deve contenere Animale, Giraffa e Leone. Nel main devono essere presenti Kira e Simba, inseriti in un ArrayList<Animale>. Visualizzare gli animali, realizzare un esempio di up casting e due di down casting.