# Python Tutorial

##Inhalt

##Einleitung
Python ist eine einfach zu lernende, aber mächtige Programmiersprache mit einer eleganten Syntax. Als **interpretierte Sprache** ist sie sowohl für Skripte als auch für die Erweiterung von anpassbaren Applikationen hervorragend geeignet.  

Dieses Tutorial stellt die Grundkonzepte und Eigenschaften der Sprache Python vor. Ziel ist nicht die umfangreiche und vollständige Behandlung sämtlicher Sprachmerkmale von Python, sondern die Vermittlung der wichtigsten Eigenschaften, um einen Eindruck von dem zu bekommen, was Python ist, und wie es in der professionellen Entwicklungsumgebung eingesetzt werden kann.  

***
Dieses Tutorial behandelt Python in der Version 3.7. Einzelne Beispiele, insbesondere jene aus Kapitel Grafische Benutzeroberflächen sind nicht mit älteren Versionen (2.7.x) kompatibel. 
***

## Prozesse 

Programmieren ist nichts anderes, als einen Arbeitsablauf (Prozess) aufzuschreiben. Ein Prozess ist eine Menge an Schritten, denen du folgen musst, um eine Aufgabe auszuführen.
Ohne einen Ablaufplan können Computer keine Aufgaben ausführen. Als Programmierer musst du dem Computer sagen, welche Schritte er ausführen soll, in welcher Reihenfolge und wie oft er sie ausführen soll, und du musst ihn auf alle Ausnahmen, die auftreten und zu einem Fehler führen können, vorbereiten. Alle diese Informationen sind in einem Programm (Software, Skript, App, Anwendung) beschrieben.
Prozess
Ein Programm ist ein festgeschriebener Arbeitsablauf, den du verwendest, um dem Computer zu sagen, was er machen soll, wann er es machen soll und wie er es machen soll.
Legen wir los und sagen unserem Computer, was er zu tun hat. 
Die Kommandozeile
In der Einleitung stand, dass Python eine interpretierte Sprache ist. Dies bedeutet, dass der geschriebene Programmcode nicht zuerst in unleserlichen binären Computercode (001011001010) übersetzt (kompiliert) werden muss, sondern dass der menschenlesbare Code direkt ausgeführt (interpretiert) wird. Python unterscheidet sich dadurch von anderen Programmiersprachen wie z.B. Java oder C#.

> **Übung: Erste Schritte**
> Suche im Windows-Startmenu nach _Python command line_ und starte die Kommandozeile.  
> ![startmenu](screenshots/startmenu.PNG)
> ![startmenu](screenshots/commandline.PNG)
> 
>
> Nun können wir unsere Anweisungen in Textform eingeben.
> Tippe nacheinander folgende Befehle ein, bestätige jeweils mit Enter.
> ```
> 'hello world'
> 1234
> 1 + 2 + 3 + 4
> '1' + '2' + '3' + '4'
> 1 + 2 + '3' + '4'
> text1 = 'hello'
> text2 = 'world'
> text1 + text2
> zahl1 = 123
> zahl2 = 987.654
> zahl1 – zahl2
> zahl1 + text1
> str(zahl2) + text1.upper()
> text1.replace('o', 'OO')
> text1.replace('o', 'O'*zahl1)
> round(zahl2, 0)
> int(zahl2) #hello world
> text2[2]
> TEXT2
> (text1 + text2)[3:-3]
> 3/2
> 3//2
> 3/2.0
> 3/0
> ```
> Mit dem Befehl exit() kannst du die Kommandozeile schliessen.

## Grundlagen der Programmierung
Datentypen und Operatoren
Jede Eingabe wird von Python einem Datentyp zugeordnet. Es gibt Texte (strings) und Zahlen (integers und floats). Daneben gibt es noch eine ganze Reihe weiterer Datentypen, von denen wir später noch einige kennen lernen werden. Jeder Datentyp hat bestimmte Eigenschaften und lässt nur gewisse Operationen zu.
•	Mit Zahlen können wir rechnen, sie runden oder eine Fliesskommazahl in eine Ganzzahl umwandeln.
Mathematische Grundoperatoren 
```python
print(2 * 3 + 4 - (5 / 6))
print(2 * (3 + 4) - 5 / 6)
print(5 / 3)  # Dezimaldivision
print(5 // 3)  # Ganzzahldivision
print(5 % 3)  # Modulo, liefert den Rest einer Division

```
•	Texte (immer mit Hochkommata gekennzeichnet) können wir zusammenfügen (concatenate), in Grossbuchstaben umwandeln, Buchstaben austauschen oder einen Auszug (substring) davon anzeigen u.v.m.
Textoperatoren 
```python
print("text1" + "text2"[1:3] + "text3".upper())

text = "1234"
zahl = 1234
print(text + str(zahl))
```
Variablen
Alle Datentypen können wir in eine Variable zwischenspeichern. Dazu wählen wir einen beliebigen Variablennamen (deklarieren, z.B. text1), und weisen einen Wert zu (initialisieren). Wir können diesen Wert zu einem beliebigen Zeitpunkt wieder aufgreifen, indem wir ihn über seinen Variablennamen aufrufen.
•	Python ist case sensitive. Also immer aufpassen mit Gross- und Kleinschreibung
•	Bei Operationen mit verschiedenen Datentypen ist Vorsicht geboten. Manchmal ist eine Typenumwandlung (casting) notwendig.
•	Mit # können wir Kommentare einfügen, die von Python ignoriert werden.
Ein für den Ablauf eines Programms unentbehrlicher Datentyp ist der Boolean. Dieser Datentyp kann nur zwei verschiedene Werte annehmen, nämlich True und False. Insbesondere bei Verzweigungen haben Boolesche Werte grosse Bedeutung.
Programmierparadigmen
Wir haben gelernt, dass ein Programm eine Menge an Schritten ist, die ein Computer auszuführen hat, um eine bestimmte Aufgabe zu erledigen. Abgesehen davon, dass wir mit dem Computer in einer für ihn verständlichen Sprache kommunizieren müssen (in unserem Fall Python), ist es uns weitgehend freigestellt, nach welchem Paradigma (Denkmuster) wir das tun möchten.
Am eingängigsten für Programmier-Newbies und daher auch erste Wahl in diesem Kurs ist sicherlich die Imperative Programmierung: Die Befehlsabfolge eines Skripts wird gradlinig – mit grösseren oder kleineren Umwegen – von oben nach unten abgearbeitet.
Obwohl wir in diesem Tutorial nicht näher auf das Paradigma der Objektorientierten Programmierung (OOP) eingehen, müssen an dieser Stelle doch noch drei Begriffe eingeführt werden, die uns immer wieder begegnen:
Eine Variable eines bestimmten Typs ist immer ein Objekt. Dieses hat spezifische Eigenschaften und Fähigkeiten. Ein Objekt wird immer nach einer exakten Bauanleitung erstellt. Diese Anleitung nennt man Klasse, die Erstellung Instanziierung.
In der realen Welt wäre also ein Schokoladenkuchen (=Objekt) ein nach einem bestimmten Rezept (=Klasse) zubereitetes (=instanziiertes) Gebäck.
Collections
Ein Hauptzweck von Programmierung ist es, wiederkehrende Aufgaben automatisiert ausführen. Dazu ist es nützlich, wenn wir diese Aufgaben zuerst auflisten und dann der Reihe nach abarbeiten.
List
Eine Liste (array) ist immer mit zwei eckigen Klammern gekennzeichnet. Sie kann eine beliebige Anzahl an Einträgen (elements) enthalten, die sich dynamisch verändern lassen.
woche = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
Auch für Listen gibt es zahlreiche mögliche Operationen. In der Liste woche fehlen der Samstag und der Sonntag. Im Beispiel sehen wir dies sofort, doch in einem grösseren Skript ist es manchmal sinnvoll zu prüfen, ob ein bestimmtes Element in einem Array vorhanden ist:
'Sonntag' in woche
Wir fügen das Wochenende noch hinzu:
woche.append('Samstag')
woche.append('Sonntag')
Ein Eintrag in einer Liste kann auch direkt angesprochen werden, wenn wir seine Position (index) innerhalb der Liste kennen. Der Mittwoch ist der dritte Wochentag, deshalb steht er an dritter Stelle.
woche[2]

Index
Da in Programmiersprachen die Nummerierung nicht bei eins, sondern bei null beginnt, hat der Mittwoch den Index 2.

Natürlich lassen sich Listen auch sortieren. Wir überschreiben die Variable woche mit einer sortierten Liste der Wochentage.
woche = sorted(woche)
An Indexposition 2 steht nun nicht mehr der Mittwoch, sondern der Freitag.
Aus einer Liste entfernt werden könne Einträge über ihre Indexposition oder über ihren Wert:
woche.pop(2)  # entfernt den Eintrag mit Index 2, also den Freitag
woche.remove('Mittwoch')  # entfernt den Mittwoch
Jeder Text (string) ist gleichzeitig eine Liste seiner einzelnen Buchstaben. Dies wird deutlich, wenn wir versuchen ein einzelnes Wort zu sortieren:
lt = sorted('swisstopo')
Set
Eine Liste kann mehrere identische Elemente haben. Die einfachste Möglichkeit, Duplikate aus einer Liste zu entfernen, ist sie in ein Set umzuwandeln. Ein Set ist im Gegensatz zu einer Liste weniger dynamisch und lässt keine doppelten Einträge zu.
lt = set(lt)

Nun können wir beispielsweise bestimmen, wie viele verschiedene Buchstaben im Wort swisstopo vorkommen:
len(lt)
Sehr hilfreich sind Sets bei Operationen der Mengenlehre:
set('Landestopografie') & set('swisstopo')  # gemeinsame Buchstaben
set('Landestopografie') ^ set('swisstopo')  # nur in einem der beiden Begriffe
len(set('Landestopografie') | set('swisstopo'))  # Anzahl verschiedener Buchstaben insgesamt
Tupel
Ein Tupel ist eine unveränderliche Liste mit einer fixen Anzahl an Elementen. Sinnvoll ist dies z.B., wenn wir die Koordinaten eines Punktes in einer Liste – oder eben in einem Tupel – speichern wollen:
bern2d = (600000, 200000)
bern3d = (600000, 200000, 500)

Tupeln werden wir auch bei der Berechnung von Zeiten und Daten wieder begegnen.
Dictionary
Dictionaries sind tatsächlich so etwas wie Nachschlagewerke: Wird nach einem bestimmten Schlüsselwort (key) gefragt, erhält man den dafür hinterlegten Wert (value) zurück. Dictionaries werden mit geschwungenen Klammern gekennzeichnet. Key und Value werden mit einem Doppelpunkt getrennt.
anreden = {'de':'hoi', 'fr':'salut', 'it':'ciao'}

Alle Elemente in einem Dictionary können spezifisch abgefragt werden:
anreden['it']  # liefert den für den Key 'it' hinterlegten Wert
anreden.keys()  # liefert eine Liste mit allen Schlüsselwörtern
anreden.values()  # Liste mit allen Werten
anreden.items()  # verschachtelte Liste mit Key/Value-Tupel
Das letzte Beispiel zeigt, dass Listen, Sets und Dictionaries eng verwandt sind und vielseitig miteinander kombiniert und ineinander verschachtelt (nested) werden können.
 
Entwicklungsumgebung
Bisher haben wir auf der Kommandozeile gearbeitet, und alle Eingaben wurden sofort verarbeitet und die Resultate ausgegeben. Dies vermittelt zwar das Gefühl, ein wahrer Hacker zu sein, ist aber wenig nachhaltig. Unsere Skripte wollen wir speichern können, um sie z.B. später auszuführen oder einer anderen Person zur Nutzung zu übergeben.
Es ist möglich, in einem einfachen Texteditor wie Notepad ein Pythonskript zu programmieren. Da dies nicht sehr komfortabel ist, gibt es eine Reihe verschiedener Texteditoren, die für das Programmieren mit Python optimiert sind. In letzter Zeit hat sich PyCharm als IDE’s (integrated development environment) etabliert.
•	https://www.jetbrains.com/pycharm/download/
Übung: IDE
Mache dich mit der Oberfläche von PyCharm vertraut. Probiere anhand der Beispiele von oben ein paar Zeilen Pythoncode zu programmieren. Führe deinen Code aus. Nutze den Befehl print() zur Ausgabe deiner Resultate. Speichere dein Skript regelmässig.
Ein Pythonskript ist eine Textdatei mit der Dateiendung py. Ein als Datei abgespeichertes Pythonskript lässt sich auf verschiedene Arten ausführen:
•	Direkt im PyCharm über den entsprechenden Button
•	Mit Doppelklick auf die Datei im Windows Explorer
•	Über die Windows Kommandozeile
Kontrollstrukturen
Schleifen
Schleifen (loops) erlauben, Listen effizient abzuarbeiten. Beim sogenannten Iterieren wird eine bestimmte Operation für jedes Element in einer Liste einmal ausgeführt.
liste = [1, 2, 3, 4, 5]
for zahl in liste:
	quadratzahl = zahl ** 2
	print(quadratzahl)
Bei jedem Schleifendurchlauf wird die Quadratzahl der aktuellen Zahl berechnet und angezeigt, bis alle Zahlen in der liste einmal an der Reihe waren. Den eingerückten Codeabschnitt nennt man Anweisungsblock. 
Anweisungsblock
Ein Anweisungsblock ist immer genau vier Leerschläge eingerückt. Python ist hier sehr strikt und verzeiht es nicht, wenn diese Regel nicht eingehalten wird.
Das Beispiel oben nennt man for-Schleife, da der Schleifendurchlauf für eine bestimmte Anzahl Elemente ausgeführt wird. Die Anzahl Elemente ergibt sich aus der Listenlänge.
Übung: for-Schleife
Berechne mit einer for-Schleife die Summe der Elemente in der Liste [1, 2, 3, 4, 5, 6].
 Innerhalb eines Anweisungsblocks können wir auf Variablen von ausserhalb des Blocks zugreifen und diese verändern. Dazu wird eine Variable vor dem Block initialisiert (z.B. summe = 0) und dieser Wert bei jedem Schleifendurchlauf um die aktuelle Zahl erhöht.
Häufig gibt es auch den Fall, dass wir zu Beginn nicht genau wissen, wie oft eine Anweisung ausgeführt werden soll. Die Anzahl Durchläufe hängt dann von einer Bedingung ab.
zahl = 1
while zahl <= 10:
	print(zahl)
	zahl += 0.0123456
print("Schleife fertig")
Eine while-Schleife wird solange ausgeführt, wie die Bedingung erfüllt ist. Danach geht es im Skript ausserhalb des Anweisungsblocks weiter.
Endlosschleife
while-Schleifen sind sehr anfällig für Programmierfehler. Wenn nämlich das Abbruchkriterium fehlt, bleibt das Skript im Block gefangen und befindet sich in einer Endlos-Schleife. Abgebrochen werden kann eine Endlos-Schleife mit Ctrl+C.
Verzweigungen
Die Prüfung, ob eine Bedingung erfüllt ist oder nicht, ist einer der wichtigsten Mechanismen bei der Programmierung. Damit werden die Weichen gestellt, was das Programm unter gewissen Umständen tun soll.
Verzweigungen werden mit if, elif und else eingeleitet. Es ist erlaubt, dass if alleine steht und keine weiteren Prüfungen stattfinden sollen. Beliebig viele alternative Bedingungen können mit elif geprüft werden. Falls bis dahin noch keine der Bedingungen erfüllt wurde, wird der Anweisungsblock nach else ausgeführt.
for zahl in range(10):
	if zahl == 3:
		print(zahl, "juhee, drei")
	elif zahl == 7:
		print(zahl, "yepee, sieben")
	elif zahl == 9:
		print(zahl, "yes, neun")
	else:
		print(zahl, "eine andere Zahl")
•	range(10) ist eine Kurzschreibweise für eine Liste [0,1,2,3,4,5,6,7,8,9]. Auch hier gilt wieder: Die Nummerierung beginnt bei 0, dafür ist die 10 nicht inklusive.
•	Im Gegensatz zur Initialisierung einer Variablen = besteht der Vergleichsoperator aus zwei Gleichheitszeichen ==.
Vergleichsoperatoren
Neben dem ist-gleich-Operator gibt es zahlreiche weitere Vergleichsoperatoren:
Operator	Bedeutung	Beispiel
==	ist gleich	"a" == 'a'
!=	ist ungleich	"a" != "b"
<	ist kleiner als	1 < 2
<=	ist kleiner gleich	2 <= 2
>	ist grösser als	1 > 2
>=	ist grösser gleich	4 >= 3
in	ist in einer Collection enthalten	"e" in "Hello" 
7 in range(10) 
"a" in ["b","c","d"]
Das Resultat eines Vergleichs ist immer entweder wahr oder falsch. In Computerslang heisst das, dass ein Ausdruck nach True oder False evaluiert. Diese Booleans sind im Code aber häufig nicht direkt als solche ersichtlich, sondern verstecken sich hinter der eigentlichen Expression.
Artversandt sind spezielle Funktionen, die als Resultat einen Boolean zurückgeben:
Funktion	Bedeutung	Beispiel
.startswith()	String beginnt mit	"Hello".startswith("h")
.endswith()	String endet mit	"World".endwith("d")
Die verschiedenen Vergleichsoperatoren lassen sich beliebig kombinieren oder negieren. Dazu werden die Befehle and, or und not verwendet. Einzelne Bedingungen können mit Klammern gruppiert werden.
  TODO: andere Übung überlegen
•	Wird in Python eine Ganzzahl (integer) durch eine andere Ganzzahl dividiert, ist das Resultat auch eine Ganzzahl (immer abgerundet). Bsp.: 3/2=1. Dies hängt mit dem Datentyp zusammen, den Python nicht automatisch von einem int in einen float umwandelt.
•	Zahlen können mit str(1234) in Strings umgewandelt (gecastet) werden.
Bei einer Kombination von Schleifen und Bedingungen kann der Schleifendurchlauf mit dem Befehl break aktiv unterbrochen werden.
zahl = 1
while zahl <= 10:
	print(zahl)
	if zahl == 5:
		print("Abbruchkriterium erfuellt")
		break
	zahl += 1
print("Schleife fertig")
Artverwandt ist der Befehl continue. Damit werden allfällige restliche Befehle im Anweisungsblock übersprungen, und die Schleife startet mit dem nächsten Element von vorne neu.
Benutzereingaben
Bravo, ihr habt eure ersten eigenständig laufenden Programme geschrieben! Es ist aber – mit Verlaub – noch sehr langweilig, da es im Ablauf sehr starr ist und der Benutzer keine Möglichkeit hat, mit der Software zu interagieren.
Ein Skript beginnt meistens mit der Variablendeklaration und -initialisierung. Häufig möchten die Variablenwerte nicht fix als Konstanten ins Skript integriert, sondern dynamisch vom Benutzer eingegeben werden. Diese so genannten Parameter können auf zwei Arten dem Skript übergeben werden:
1.	Der Benutzer kennt die benötigten Parameter und gibt die Werte an, bevor er das Skript startet
2.	import sys
3.	user_param = sys.argv[1]
print("Deine Eingabe war: {}".format(user_param))
4.	Das Skript fordert den Benutzer zur Laufzeit auf, eine Eingabe zu tätigen
5.	user_param = input("Bitte eine Zahl eingeben: ")
print("Deine Eingabe war: {}".format(user_param))
•	Mit dem Befehl import können wir die Standardfunktionalität von Python beliebig erweitern. Das Modul sys beinhaltet z.B. viele Funktionen des Betriebssystems, um mit diesem kommunizieren zu können.
•	Wird das Skript in der Windows Kommandozeile gestartet, werden alle Benutzereingaben in der Liste sys.argv gespeichert. Der erste Eintrag (an der nullten Indexposition) ist immer der Dateiname des Skripts selbst. Ab dem zweiten Eintrag (ab Index 1) folgen die Parameter. Wenn es mehrere Parameter gibt, werden diese bei der Eingabe auf der Kommandozeile mit einem Leerschlag getrennt. Enthält der Parameter selber Leerschläge, gehören Anführungszeichen drum.
•	Der Userinput wird von Python immer als String interpretiert, auch wenn eine Zahl eingegeben wird. Der Input muss also gegebenenfalls zuerst in den richtigen Datentyp gecastet werden.

Übung: Benutzereingaben
Schreibe je ein Skript für Möglichkeit 1 und 2, das folgendes kann:
•	Der Benutzer soll einen Radius als Parameter eingeben
•	Das Skript berechnet Durchmesser, Umfang und Fläche des Kreises
 Importiere das Modul math und nutze die Konstante pi für die Kreiszahl.
Fehlerbehandlung
Um zu verhindern, dass ein Skript abstürzt, weil der Benutzer eine falsche Eingabe gemacht hat (oder weil wir einen Bug in die Software eingebaut haben) gibt es das Konstrukt des Error Handlings.
try:
	1 / 0
except Exception as e:
	print e
finally:
	print("Ich werde auf jeden Fall ausgefuehrt")
Das Error Handling sowie ausführliche Tests des eigenen Codes sind sehr wichtige Bestandteile eines Programms bzw. der Entwicklungsphase. Die Konzepte dazu sind aber sehr umfangreich und eher schwerverdaulich, so dass wir uns in diesem Tutorial mit der einfachen try/except/finally Struktur begnügen.
Lesen und schreiben von Dateien
Bei den bisher geschriebenen Skripten ist das Resultat immer eine Ausgabe auf dem Bildschirm. In vielen Fällen ist es aber gewünscht, die Resultate z.B. in eine Datei zu schreiben. Wir sollten also das Schreiben und Lesen von Dateien mittels Python beherrschen.
datei = r"D:\tutorial\textfile.txt"
with open(datei, "r") as r:
	inhalt = r.readlines()
print(inhalt)
•	Das with open Statement mit dem Parameterwert r erlaubt es, einen Lesezugriff (read) auf eine Datei herzustellen.
•	Die Funktion readlines() liefert eine Liste mit je einem Element pro Zeile
•	Der Zeilenumbruch wird als \n ebenfalls gelesen.
Backslash
In einem String können Backslashes vor bestimmten Buchstaben eine besondere Bedeutung haben (\n für new line, \t für tabulator etc.). Wenn dies nicht gewünscht ist, kann ein kleines r direkt vor den String gesetzt werden. Dann ist ein Backslash einfach ein Backslash.
print("das ist ein \text")
print(r"das ist ein \text")
Sonderzeichen
Sonderzeichen und Umlaute führen beim Programmieren immer wieder zu Problemen. In Variablennamen sind sie sogar verboten. Am besten wäre es, ganz darauf zu verzichten, aber da wir als Programmierer nicht immer die Kontrolle darüber haben (Dateipfade oder -inhalte von Dritten), müssen wir einen Trick anwenden (der meistens, aber leider nicht immer) funktioniert:
In die allererste Zeile des Scripts exakt folgende Zeile einfügen:
# -*- coding: utf-8 -*-
Übung: Textfile lesen und schreiben
Erzeuge eine neue Textdatei mit dem Namen personen.txt. Schreibe einige Personen in die Liste im Format Vorname Nachname.
 im with open Befehl öffnet der Parameterwert w einen Schreibzugriff (write) auf eine Datei. Eine bestehende Datei wird überschrieben, eine neue automatisch angelegt.
 Mit .split(" ") können Vor- und Nachname in ein Tupel mit zwei Einträgen aufgeteilt werden, die nachher über ihren Index [in eckigen Klammern] angesprochen werden können.
 Nutze .strip() um Zeilenumbrüche zu eliminieren.
 Versuche die Namen aus der Datei personen.txt zu laden, die Vornamen auf dem Bildschirm zu zeigen und sie in alphabetischer Reihenfolge in die Datei vornamen_alphabetisch.txt zu schreiben..
 Verwende write() oder writelines() um die Zeilen in das Textfile zu schreiben.
Funktionen
Wie ein Skript als Ganzen dazu dient, wiederkehrende Aufgaben zu automatisieren, dienen Funktionen dazu wiederkehrende Anweisungsfolgen innerhalb des Skripts zu bündeln. Das tönt komplizierter als es ist, und wir sind bisher auch schon zahlreichen Funktionen begegnet.
Die Syntax, das heisst die Grammatik der Programmiersprache, sieht allgemein so aus:
objekt.funktion(parameter)

Funktion 
print("hello world".replace("l", ""))
Das Objekt ist in diesem Fall ein String, die Funktion (Fähigkeit) heisst replace() und benötigt zwei Parameter.
Für die verschiedensten Objektarten bietet Python zahlreiche vorgefertigte Funktionen (built-in) an, z.B. .sum(), .upper(), .open(), .append() u.v.m. Wenn eine Funktion keine Parameter benötigt, müssen die Klammern trotzdem geschrieben werden.
Häufig kommt es vor, dass für ein ganz spezifisches Problem noch keine Funktion zur Verfügung steht. Mit Python können wir massgeschneiderte Funktionen selber programmieren.
# Methodendefinition
def addition(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

# Methodenaufruf
print(addition(4, 9))
•	Eine Funktion wird immer mit dem Befehl def, gefolgt vom Namen und den benötigten Parametern in Klammern definiert.
•	Eine Methode hat meistens einen Rückgabewert, der hinter dem Befehl return steht.
•	Die Methode muss im Skript immer definiert werden, bevor sie aufgerufen wird.
Das Beispiel oben veranschaulicht zwar den Aufbau einer Funktion, sie ergibt aber wenig Sinn, da wir genauso schreiben könnten:
print(4 + 9)
Das folgende Beispiel ist schon viel sinnvoller. Die Funktion prüft, ob eine Zahl eine Primzahl ist.
def primzahl(zahl):
	if zahl < 2:
		return False
	else:
		for i in range(2, zahl):
			if zahl % i == 0:
				return False
	return True


print(primzahl(37))
•	Der Operator % (modulo) liefert den Rest einer Division
•	Wird innerhalb einer Methode der Befehl return erreicht, endet die Methode (ähnlich break) Übung 8: Zeitansage
Übung: Funktion
Erweitere dein Programm aus der Übung zu den Kreisen so, dass du für die Berechnung von Fläche, Umfang und Durchmesser je eine Funktion erstellst und dann aufrufst.
Schreibe zudem eine neue Funktion, die die Benutzereingabe auf Gültigkeit prüft, bevor sie verarbeitet wird. Nutze dazu das Konzept der Fehlerbehandlung try/except.

Übung: Lottosimulation
Wie gross ist die Wahrscheinlichkeit, im Schweizer Zahlenlotto 6 Richtige zu haben?
Zeit und Datum
Zeit und Datum bilden eigene Datentypen, mit denen wir ganz spezifische Berechnungen anstellen können. Dazu wird die Standardfunktionalität von Python mit dem Modul time erweitert.
Berechnungen mit Zeit und Datum können sehr kompliziert sein. In vielen Programmiersprachen hat man sich deshalb darauf geeinigt, einen Zeitpunkt anhand der verstrichenen Sekunden seit dem 1. Januar 1970 (since the Epoch) anzugeben. Auf diese Weise lassen sich verschiedene Zeiten und Zeitdifferenzen am einfachsten berechnen.
In Python gibt es zudem das Zeit-Tupel, das immer aus den folgenden neun Elementen besteht:
•	die ersten drei Elemente (0 bis 2) liefern Jahr, Monat und Tag
•	die nächsten drei Elemente (3 bis 5) liefern Stunde, Minute und Sekunde
•	das nächste Element (6) stellt den Wochentag von 0 bis 6 bereit.
•	die laufende Nummer des Tages innerhalb eines Jahres wird von Element 7 geliefert.
•	Informationen über den Status der Sommerzeit liefert das letzte Element 8.
Wenn wir die Konvertierung zwischen Zeit-Tupel und Sekunden seit 1970 beherrschen, können wir umfangreiche Zeitberechnungen vornehmen.
import time

# Aktuelle Zeit in Sekunden seit 'the Epoch'
print(time.time())

# Aktuelle Zeit als Zeit-Tupel, und einzelne Elemente daraus
print(time.localtime())
print(time.localtime().tm_mon)  # Monat
print(time.localtime().tm_mday)  # Tag

# Umwandlung von Sekunden seit 'the Epoch' in Zeit-Tupel
print(time.localtime(100000))

# Umwandlung von Text, das einem bestimmten Muster entspricht, in Zeit-Tupel
print(time.strptime("02.05.2016", "%d.%m.%Y"))

# Umwandlung eines Zeit-Tupels in Sekunden
print(time.mktime((2016, 4, 29, 0, 0, 0, 4, 120, -1)))

# Umwandlung von Text in Sekunden seit 'the Epoch'
print(time.mktime(time.strptime("29.04.2016", "%d.%m.%Y")))
•	In der Funktion strptime() werden für das Datumsformat Platzhalter verwendet.
•	Auch für die individuelle Ausgabe am Bildschirm können diese Platzhalter zusammen mit der Funktion strftime() eingesetzt werden.
•	Aus einem Zeit-Tupel können wir ein bestimmtes Element über den Index oder über das Schlüsselwort ansprechen. 
•	Ausführliche Übersicht: https://docs.python.org/2/library/time.html#module-time
Übung: Geburtstag
Schreibe dazu ein Programm mit interaktiver Benutzereingabe, das folgende Fragen beantwortet:
•	An welchem Wochentag wurdest du geboren?
•	An welchem Wochentag feierst du deinen 30. Geburtstag?
Web
Im Internet finden sich unendlich viele Daten und Dienste, die wir downloaden oder anzapfen können, um eine bestimmte Anforderung zu lösen.
In der GIS-Welt müssen z.B. häufig Koordinaten von einem System in ein anderes umgerechnet werden. Den Algorithmus zur Transformation müssen wir nicht selber entwickeln, sondern können dazu einen Dienst im Internet nutzen.
Die swisstopo stellt z.B. einen Dienst (Service) zur Verfügung, mit dem solche Koordinatentransformationen vorgenommen werden können.
https://www.swisstopo.admin.ch/de/karten-daten-online/calculation-services/m2m.html
Auf der Webseite heisst es sinngemäss, dass wir über eine bestimmte URL mit der Übergabe der Parameter easting und northig die umgerechneten Koordinaten erhalten.
Anhand des aufgeführten Beispiels wissen wir, dass unsere URL so aussehen muss:
https://geodesy.geo.admin.ch/reframe/wgs84tolv03?easting=7.452&northing=46.928&format=json
Im Browserfenster sehen wir nun das Resultat
{"easting": "601017.990423179", "northing": "197433.9052806796"}
Nun gilt es das, was wir im Internetbrowser können, mit Python nachzustellen. Wir basteln dafür Schritt für Schritt unsere URL mit den Parametern zusammen. Für die Koordinaten werden Variablen verwendet.
Für die Kommunikation mit dem Internet ist das Modul requests bestens geeignet, muss aber zuerst installiert werden.
Mit Modul requests 
import requests

e = 2600000
n = 1200000

# Der Proxy wird innerhalb des Bundesnetzes benötigt, um überhaupt ins Internet zu kommen
proxy = "http://proxy-bvcol.admin.ch:8080"
proxy_dict = {"http": proxy,
              "https": proxy}

service = "http://geodesy.geo.admin.ch/reframe/lv95towgs84"

parameter = {"easting": e,
             "northing": n,
             "format": "json"}

response = requests.get(url=service, params=parameter, proxies=proxy_dict, verify=False)  # die Parameter proxies und verify sind nur innerhalb des Bundesnetzes nötig
result = response.json()

print(result["easting"])
print(result["northing"])

Übung: Webdienste Geodäsie
Das Gebäude von swisstopo hat die WGS84-Koordinaten 46.928°N 7.452°E. Unser Schulungsgebäude liegt bei der LV03-Koordinate 600050m 198760m. Wie weit sind die beiden Gebäude (Luftlinie) voneinander entfernt?

Übung: Webdienste BGDI
Studiere die Dokumentation zu den Webdiensten der Bundes-Geodateninfrastruktur.
https://api3.geo.admin.ch/services/sdiservices.html#search 
Versuche zu einer beliebigen Adresse die Koordinaten zu erhalten.
https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=wabern&type=locations
Grafische Benutzeroberflächen
Wer bis hierhin durchgehalten und die vermittelten Inhalte mehr oder weniger begriffen hat, versteht nun die Grundlagen des Programmierens. In diesem Kapitel geht es nun darum, den möglicherweise komplizierten Programmiercode hinter einer schönen Fassade (GUI = Graphical User interface) zu verbergen.
Zu Mensch-Maschinen-Interaktionen bestehen zahlreiche Philosophien, Konzepte, Frameworks (vorgefertigte Programmiermuster) etc., die von technischer Umsetzung über farbliche Gestaltung bis Ergonomie reichen. Da wir hier in einem Programmier- und nicht in einem Designerkurs sind, werden wir uns eher in der Region der technischen Umsetzung bewegen. Eine ansprechende grafische Gestaltung kann danach immer noch erfolgen.
Das Hauptfenster
In diesem Kurs nutzen wird das Modul tkinter, das bei jeder Pythoninstallation bereits standardmässig installiert ist. Mit ein paar wenigen Zeilen Code steht dann auch schon das Grundgerüst für unser Programm.
Hauptfenster 
# -*- coding: utf-8 -*-

from tkinter import *

class Gui:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()

        # Titel
        self.window.title("GUI")

        # Fenster darstellen
        self.window.mainloop()

# Programm ausführen
Gui()
Lasst euch durch die ominösen class-Definitionen und dieses self nicht beirren. Wir werden später sehen, wofür das gut sein kann. So viel sei verraten, wir begeben uns jetzt allmählich in die Tiefen der Objektorientierten Programmierung.
 
Widgets
Ins Hauptfenster können nun verschiedene so genannte Widgets (Buttons, Labels, Eingabefelder, Checkboxes etc.) gepackt werden.
Widgets 
# -*- coding: utf-8 -*-

from tkinter import *

class Widgets:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()

        # Titel
        self.window.title("Meine Widgets")

        # Label
        self.label = Label(master=self.window, width=50, text="Ich bin ein Label")
        self.label.pack(padx=10, pady=10)

        # Eingabe
        self.eingabe = Entry(master=self.window, width=30)
        self.eingabe.pack(padx=10, pady=10)

        # Button
        self.button = Button(master=self.window, width=10, text="Klick me!")
        self.button.pack(padx=10, pady=10)

        # Fenster fixieren
        self.window.resizable(width=False, height=False)

        # Fenster darstellen
        self.window.mainloop()

# Programm ausführen
Widgets()
 
Layout
Im Beispiel oben haben wir die Widgets einfach nacheinander ins Hauptfenster gepackt (oder zuerst in ein Frame verschachtelt), dabei die Abstände zum vorherigen und nachfolgenden Widget angegeben und die Ausrichtung über side gesteuert. Zudem haben wir die Grösse des Fensters fixiert. Für einfache Anwendungen ist das ausreichend, doch sobald mehr Widgets in einem Fenster enthalten sind, stösst dieses dynamische Packing schnell an seine Grenzen. Komplexere Layouts sind mit dem grid-Pattern möglich.
Übung: Sehtest
•	Erstelle anhand des Beispiels oben das Gerüst für dein Hauptfenster
•	Packe hintereinander vier Label-Widgets mit absteigender Schriftgrösse (z.B. 100, 80, 60, 40) hinein
•	Setzte als Text für jedes der vier Labels drei zufällige Grossbuchstaben
 Das ganze Alphabet als Liste erhälst du z.B. so:
import string
abc = string.ascii_uppercase
 
Form vs. Funktionalität
Widgets dienen der Benutzerinteraktion. Wir müssen also lernen, wie wir den Zustand und/oder die Eigenschaften eines Widgets je nach Interaktion abgreifen und/oder manipulieren können. Wir beginnen also damit, Darstellung und Funktionalität zu kombinieren. Um die Übersicht zu behalten versuchen wir aber, im Code die Teile für Form von den Teilen für Funktion zu trennen.
Wie ganz zu Beginn einmal kurz erwähnt, ist eine Klasse (class) ein Bauplan, hier der Bauplan für unser Programm mit graphischer Benutzeroberfläche. Die erste Methode in einer Klasse heisst immer __init__. Dies ist der so genannte Kontruktor, der die allerwichtigsten Angaben des Bauplans erhält. Wenn eine neue Klasse initiiert wird (d.h. gemäss Bauplan ein neues Objekt erstellt wird), wird __init__ immer automatisch ausgeführt.
Für Programme mit GUI ist dies ziemlich praktisch, da einfach alles, was für die Darstellung (Hauptfenster, Widgets) nötig ist, in der __init__-Methode untergebracht werden kann, und die eigentliche Programmlogik in separate Methoden ausgelagert werden kann.
Form vs. Function 
# -*- coding: utf-8 -*-

import random
from tkinter import *


class FormVsFunction:

    def __init__(self):
        """ Hier steht nur Form.
        """

        window = Tk()
        window.title("Form vs. Funktion")

        Button(master=window, text="Random", command=self.random).pack(padx=5, pady=5)
        self.label = Label(master=window, width=40)
        self.label.pack(padx=5, pady=5)

        window.mainloop()

    def random(self):
		"""Hier steht Funktionalität.
		"""
        self.label.config(text=str(random.randint(1, 100)))


FormVsFunction()
Im Widget Button in der Funktion __init__ ist unter dem Parameter command hinterlegt, welche Funktion beim Klicken ausgeführt werden soll. Damit aber aus __init__ heraus die Funktion random überhaupt angesprochen werden kann, ist das Schlüsselwort self notwendig.  self ist also sozusagen der Bezug auf die übergeordnete class.
Übung: Sehtest mit refresh
•	Erweitere deinen Sehtest durch einen Button, bei dessen Betätigung neue Zufallsbuchstaben angezeigt werden.
•	Versuche Darstellung (in der Funktion __init__) und Logik (z.B. in der Funktion refresh) zu trennen
Übung: Lichtschalter
Programmiere eine kleine Applikation, die einen Lichtschalter simuliert, indem nach Betätigung eines Buttons z.B. Hintergrundfarbe oder Text hin- und her wechseln. Das könnte dann ungefähr so aussehen.
  
Events
Ein Event wird durch den Benutzer ausgelöst, wenn er z.B. mit der Maus einen Button klickt, eine bestimmte Tastenkombination drückt o.ä.
Die einfachste Form solcher Events haben wir bereits kennengelernt, nämlich den Parameter command bei den Buttons. Events können aber noch viel mehr. Ein Event weiss z.B. von sich selbst, auf welchem Widget, zu welcher Zeit und über welches Eingabegerät (Taste, Tastenkombination, Links- oder Rechtsklick) er ausgelöst wurde. Je nach dem kann das Programm darauf reagieren und eine entsprechende Aktion ausführen.
Maus-Events 
# -*- coding: utf-8 -*-

from tkinter import *


class Events:

    def __init__(self):
        self.window = Tk()
        self.window.title("Events")

        self.label = Label(master=self.window, text="Click me!", width=25)
        self.label.pack(pady=20, padx=20)

        self.label.bind(sequence="<Button-1>", func=self.leftclick)
        self.label.bind(sequence="<Button-3>", func=self.rightclick)

        self.window.mainloop()

    def rightclick(self, event):
        event.widget.config(text="Rechts")

    def leftclick(self, event):
        event.widget.config(text="Links")


Events()
Mit bind wird ein spezifischer Eventtyp an ein Widget gebunden, und mit func angegeben, welche Funktion dann ausgeführt werden soll. Der Funktion wird dann der Event event mit allen Informationen darüber als Parameter übergeben. Mit event.widget ist dann innerhalb dieser Funktion das Widget bekannt, auf dem der Event ausgelöst wurde, und die config dieses Widgets (hier der Parameter text) kann manipuliert werden.
Kontrollvariablen
Über Kontrollvariablen können bestimmte Aktionen ausgelöst werden, ohne dass der Benutzer aktiv einen Event auslösen muss. Verschiedene kompatible Widgets werden dazu über eine gemeinsame Kontrollvariable verknüpft und aktualisieren sich dynamisch gegenseitig.
Kontrollvariablen 
# -*- coding: utf-8 -*-

from tkinter import *


class Controlvars:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()
        self.window.title("Kontrollvariablen")

        # Dynamische Variable im Hauptfenster registrieren
        self.dynamischer_text = StringVar()

        # Zwei Labels erstellen, deren Texte sich auf die dynamische Veriable beziehen
        self.label1 = Label(master=self.window, width=20, textvariable=self.dynamischer_text)
        self.label1.pack()

        self.label2 = Label(master=self.window, width=20, textvariable=self.dynamischer_text)
        self.label2.pack()

        # Ein Eingabefeld erstellen, das den dynamischen Text ändert
        self.eingabe = Entry(master=self.window, width=50, textvariable=self.dynamischer_text)
        self.eingabe.pack(pady=10, padx=10)

        # Hauptfenster anzeigen
        self.window.mainloop()


# Programm ausführen
Controlvars()
Messageboxes
Messageboxes sind kleine vordefinierte Fensterchen, die dem Benutzer ein Feedback auf seine getätigten Aktionen geben, und gegebenenfalls eine neue Aktion auslösen.
Es werden drei Arten unterschieden:
•	showinfo: Enthält einen Titel, eine Message und den Button OK
•	askyesno: Enthält einen Titel, eine Message und die Buttons Ja und Nein
•	askretrycancel: Enthält einen Titel, eine Message und die Buttons Wiederholen und Abbrechen
askyesno und askretrycancel liefern einen Boolean zurück, der je nach geklicktem Button True oder False enthält. Im Programm können wir nun entsprechend darauf reagieren.
Messagebox 
import tkinter.messagebox
from tkinter import *


class Messages:

    def __init__(self):
        self.window = Tk()
        self.window.title("Box")

        self.btn_info = Button(master=self.window, text="Infobox", command=self.info)
        self.btn_info.pack(pady=10, padx=10, side=LEFT)

        self.btn_yesno = Button(master=self.window, text="Yes/No", command=self.yesno)
        self.btn_yesno.pack(pady=10, padx=10, side=LEFT)

        self.btn_retry = Button(master=self.window, text="Retry", command=self.retry)
        self.btn_retry.pack(pady=10, padx=10, side=LEFT)

        self.window.mainloop()

    def info(self, message="Ich bin eine Infobox"):
        tkinter.messagebox.showinfo("Info", message)

    def yesno(self, message="Alles paletti?"):
        result = tkinter.messagebox.askyesno("Ja - Nein", message)
        if result:
            self.info(message="Das freut micht!")
        else:
            self.info(message="Das ist aber schade")

    def retry(self, message="Nochmals versuchen?"):
        result = tkinter.messagebox.askretrycancel("Nochmals", message)
        if result:
            self.yesno(message="Besser jetzt?")


Messages()

  








