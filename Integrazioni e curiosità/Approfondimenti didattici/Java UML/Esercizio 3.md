Obiettivo


Riprendere il progetto realizzato nel secondo esercizio e farlo evolvere senza creare un nuovo progetto. La classe Animale rimarrà la classe di base dello Zoo e verrà creata una nuova classe specifica per una giraffa. In questa attività verranno applicati i concetti di costruttore, overloading, incapsulamento ed ereditarietà.


Situazione dello Zoo

Nello Zoo arriva un nuovo animale: una giraffa chiamata Kira. Al momento della registrazione conosciamo soltanto il nome e la specie. Età e peso verranno inseriti successivamente, quando saranno disponibili.

Per questo motivo nella classe Animale utilizzeremo due costruttori diversi: uno quando conosciamo tutti i dati dell'animale e uno quando conosciamo inizialmente soltanto nome e specie.

1. Riprendere il progetto precedente

Partire direttamente dal progetto realizzato nel secondo esercizio. Non creare un nuovo progetto.

Controllare che la classe Animale possieda gli attributi private, i getter, i setter e il metodo saluta().


2. Mantenere il costruttore completo

Mantenere il costruttore già presente, che permette di creare un Animale quando sono disponibili tutti i dati.


3. Aggiungere il secondo costruttore

Aggiungere un secondo costruttore alla classe Animale. Questo costruttore deve ricevere soltanto nome e specie.


Questo costruttore viene utilizzato quando un animale viene registrato nello Zoo prima che siano disponibili tutti i suoi dati. I due costruttori hanno una firma diversa e rappresentano quindi un esempio di overloading.


4. Creare la classe Giraffa

Creare una nuova classe chiamata Giraffa. La classe Giraffa deve estendere la classe Animale. (Utilizzare la parola chiave extends). La Giraffa dovrà avere anche un comportamento specifico , quindi creare il metodo mangiaFoglie().


5. Creare il costruttore di Giraffa

Creare nella classe Giraffa un costruttore che riceva soltanto il nome.

All'interno del costruttore utilizzare super() per richiamare il costruttore della classe Animale che riceve nome e specie.

In questo modo la classe Giraffa utilizza il costruttore a due parametri della classe Animale. La specie viene impostata come "Giraffa", mentre età e peso restano inizialmente ai loro valori di partenza.


6. Creare Kira
Nel main creare la nuova giraffa utilizzando il costruttore appena realizzato. Successivamente visualizzare il nome, la specie, l'età e il peso utilizzando i getter ereditati da Animale.

Osservare che Kira è stata creata con informazioni ancora incomplete.


7. Completare i dati di Kira

Utilizzare i setter ereditati da Animale per completare successivamente le informazioni di Kira.


Impostare l'età a 4 anni e il peso a 520 kg:

Visualizzare nuovamente i dati attraverso i getter e verificare che i valori siano cambiati.


Osservare che l'oggetto Kira è stato prima creato con informazioni parziali e poi completato successivamente.


8. Utilizzare i metodi ereditati e il metodo specifico


Richiamare il metodo saluta() della classe Animale utilizzando l'oggetto kira.


Richiamare anche il metodo mangiaFoglie() definito direttamente nella classe Giraffa.


9. Prova finale

Il programma finale deve contenere la classe Animale e la classe Giraffa. Nel main deve essere possibile creare Kira, visualizzarne i dati tramite i getter, completare età e peso tramite i setter, richiamare saluta() e mangiaFoglie().