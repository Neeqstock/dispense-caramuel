Obiettivo

Continuare il progetto della classe Animale realizzato nella prima parte, introducendo i costruttori personalizzati e il concetto di incapsulamento. Gli attributi della classe saranno resi private e gli oggetti verranno inizializzati attraverso un
costruttore.


1. Rendere gli attributi private

Modificare la classe Animale trasformando gli attributi public in private:
Esempio:
private String nome;


Provare ora a eseguire nel main una delle istruzioni utilizzate nella prima parte, per esempio:


a1.nome = "Leo";

Osservare l'errore del compilatore e capire perché un attributo private non può essere modificato direttamente dall'esterno della classe.

2. Creare il costruttore personalizzato


Nella classe Animale creare un costruttore che riceva nome, specie, età e peso e assegni questi valori agli attributi dell'oggetto.

La parola "this" indica l'attributo dell'oggetto corrente e permette di distinguere l'attributo
dal parametro con lo stesso nome.


3. Utilizzare il nuovo costruttore

Nel main creare almeno due animali passando i dati direttamente al costruttore:

Esempio
Animale a1 = new Animale("Leo", "Leone", 5, 180);


Richiamare poi il metodo saluta() per entrambi gli oggetti.


4. Creare getter e setter

Poiché gli attributi sono private, creare per ciascun attributo un metodo getter e un
metodo setter.

Creare quindi:

getNome() e setNome()
.......
........


I getter devono permettere di leggere il valore dell'attributo. I setter devono permettere di modificarlo.


5. Verificare il funzionamento

Visualizzare i dati degli animali utilizzando i getter.

Esempio:

System.out.println("Nome: " + a1.getNome());

.............

Utilizzare poi un setter per modificare un dato, per esempio l'età di a1, e verificare il nuovo valore attraverso il relativo getter.