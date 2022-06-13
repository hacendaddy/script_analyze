# Exercici d'analítiques per ciència de dades.

<small> (Analytics exercice for data science) </small>

> Català
>> Treballem per a una empresa que crea solucions “Data Science” per a projectes de tot
> > tipus. L'equip directiu vol centrar-se en els propers anys en el món dels e-sports, de ràpid
> > creixement, i ha decidit començar amb un que no els resultat una mica més conegut, el FIFA.<br><br>
> > Ens han demanat que dissenyem eines per treballar amb aquest tipus de dades, tant en
> > termes d'anàlisi exploratòria de dades com a llarg termini. Per això, ens han proporcionat un
> > conjunt de dades que inclou tota la informació sobre els jugadors i les jugadores del videojoc
> > entre els anys 2016 i 2022.

> English
>> We work for a company that creates "Data Science" solutions for all kinds of projects.
> > The management team wants to focus in the coming years on the world of fast
> > growth e-sports, and has decided to start with one called FIFA.<br><br>
> > We have been asked to design tools to work with this type of data, both in
> > terms of long-term exploratory data analysis. That’s why they provided us with one
> > dataset that includes all the information about in game players
> > between 2016 and 2022.
<hr>

<table border="0">
 <tr>
    <td><b style="font-size:30px">Com executar el codi</b></td>
    <td><b style="font-size:30px">How to run the code</b></td>
 </tr>
 <tr>
    <td>
        <ol>
            <li>Clonem el repositori <code>git clone https://github.com/paucamos/PAC4.git </code></li>
            <li>Entrem dins la carpeta PAC4 <code>cd PAC4</code></li>
            <li>Creem un entorn virtual <code>virtualenv {NOM_DEL_VENV}</code></li>
            <li>Activem l'entorn virtual <code>source {NOM_DEL_VENV}/bin/activate</code></li>
            <li>Instal·lem les dependencies del fitxer <code>requirements.txt</code>:
                <ul><li><code>pip -r install requirements.txt</code></li></ul>
            </li>
            <li>Executem el <code>main.py</code> (Exercicis 1-5)
                <ul><li><code>python3 main.py</code></li></ul>
            </li>
            <li>Executem el <code>ex6.py</code> (Exercici 6)
                <ul><li><code>python3 ex6.py > ex6.md</code></li></ul>
            </li>
        </ol>
    </td>
    <td>
        <ol>
            <li> Clone the repository <code> git clone https://github.com/paucamos/PAC4.git </code> </li>
            <li> Enter the PAC4 <code> cd PAC4 </code> folder </li>
            <li> We create a virtual environment <code> virtualenv {NAME_OF_VENV} </code> </li>
            <li>Activate the virtual environment <code>source {NAME_OF_VENV}/bin/activate</code></li>
            <li> Install the <code> requirements.txt </code> file dependencies:
                <ul> <li> <code> pip -r install requirements.txt </code> </li> </ul>
            </li>
            <li> Run <code> main.py </code> (Exercises 1-5)
                <ul> <li> <code> python3 main.py </code> </li> </ul>
            </li>
            <li> Run <code> ex6.py </code> (Exercise 6)
                <ul> <li> <code> python3 ex6.py> ex6.md </code> </li> </ul>
            </li>
        </ol>
    </td>

 </tr>
</table>
<hr>

## Testing  <br>
Public Tests: <code>python3 -m tests.test_public</code> <br>
Private Tests: <code>python3 -m tests.test_custom</code> <br>

## Style  <br>
Per obtenir una nota d'estil, necesitem un Linter.
* <code>sudo apt install pylint</code>
* Executem el linter posicionan-nos al directori que volguem: <code>cd modules</code>
* <code>pylint *.py</code>

REPO: https://github.com/paucamos/PAC4





