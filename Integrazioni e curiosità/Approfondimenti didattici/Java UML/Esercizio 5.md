Obiettivo
Riprendere il progetto realizzato nei precedenti esercizi e modificarlo introducendo due nuovi concetti: la classe astratta e l’interfaccia.

Lo Zoo sta crescendo e la classe Animale è diventata troppo generica. Non vogliamo più permettere al programma di creare un semplice Animale, perché ogni animale dello Zoo deve appartenere a una specie precisa.


1.Trasformare Animale in una classe astratta

Modificare la classe Animale trasformandola in una classe astratta.
Mantenere gli attributi private, i getter, i setter, i costruttori e il metodo saluta() già presenti.

Aggiungere alla classe Animale un metodo astratto che rappresenti il verso dell’animale.
Il metodo dovrà essere presente nella classe Animale, ma non dovrà contenere una propria implementazione.

2. Capire cosa cambia
Provare a creare nel main un oggetto direttamente dalla classe Animale.
Osservare il comportamento del compilatore.
Una classe astratta non può essere istanziata direttamente.
Verificare invece che Animale possa ancora essere utilizzata come tipo di riferimento per un oggetto appartenente a una classe concreta.

3. Completare le classi degli animali

Ora che Animale possiede un metodo astratto, tutte le classi concrete che estendono Animale devono implementarlo.
Modificare quindi la classe Giraffa e la classe Leone, aggiungendo ciascuna la propria versione del metodo relativo al verso.

Il comportamento dovrà essere diverso in base all’animale.
Utilizzare @Override per indicare che il metodo viene realizzato nella sottoclasse.

4. Rendere concreti anche gli altri animali dello Zoo
Nel terzo e nel quarto esercizio erano presenti anche animali generici come Leo, Mia e Dumbo.
Poiché Animale è ora una classe astratta, non sarà più possibile creare direttamente oggetti di tipo Animale.

Creare quindi le classi concrete Tigre ed Elefante(Leone esiste già), entrambe estese da Animale.

Ogni classe dovrà avere un proprio costruttore e dovrà implementare il metodo relativo al verso dell’animale.

Modificare quindi il main sostituendo gli oggetti generici con oggetti delle rispettive classi concrete.


5. Utilizzare ancora la lista dello Zoo

Mantenere la ArrayList<Animale> già utilizzata nell’esercizio precedente.
Inserire nella lista gli animali concreti presenti nello Zoo.

Ricordare che una classe astratta non può essere istanziata, ma può comunque essere utilizzata come tipo di una ArrayList.

Utilizzare un ciclo for-each per attraversare la lista e far eseguire a ogni animale il proprio verso.

Osservare il comportamento del programma: il riferimento è di tipo Animale, ma ogni animale deve eseguire la propria versione del metodo.


6. Creare l’interfaccia Volante

Nello Zoo arriva una nuova aquila.
Un’aquila è un animale, ma possiede anche una capacità particolare: può volare.

Creare quindi un’interfaccia chiamata Volante.
L’interfaccia dovrà contenere il metodo che rappresenta la capacità di volare.

Ricordare che un’interfaccia definisce un contratto: stabilisce che cosa una classe deve saper fare, lasciando alla classe il compito di stabilire come farlo.

7. Creare la classe Aquila

Creare la classe Aquila.
L’Aquila deve estendere Animale e implementare l’interfaccia Volante.
La classe dovrà quindi:

    avere un costruttore coerente con la gerarchia già realizzata;
    implementare il metodo astratto ereditato da Animale;
    implementare il metodo richiesto dall’interfaccia Volante.


Aggiungere inoltre un comportamento specifico dell’aquila.

8. Utilizzare l’interfaccia come tipo

Ora vogliamo capire perché l’interfaccia può essere utile anche tra classi molto diverse.

Creare una nuova classe chiamata Drone.
Il Drone non è un animale e quindi non deve estendere Animale.
Deve però implementare l’interfaccia Volante.

Implementare quindi il comportamento richiesto dall’interfaccia.

Nel main creare un oggetto Aquila e un oggetto Drone.
Creare poi una variabile di tipo Volante e utilizzarla per riferirsi prima all’Aquila e successivamente al Drone.
Utilizzare la stessa variabile per richiamare il metodo di volo.
Osservare che non è necessario conoscere la classe concreta dell’oggetto: è sufficiente sapere che rispetta il contratto Volante.