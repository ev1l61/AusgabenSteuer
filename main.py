from tkinter import *
import sqlite3

# Datenbank

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("datenbank.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabelle erzeugen
sql = "CREATE TABLE IF NOT EXISTS eintraege(" \
      "kaufdatum TEXT, " \
      "Artikel TEXT, " \
      "betrag REAL )"
cursor.execute(sql)

# Änderungen speichern
connection.commit()

#neue Einträge hinzufügen
def new_entry():
    datum = eingabe_kaufdatum.get()
    artikel = eingabe_artikel.get()
    betrag = eingabe_betrag.get()
    sql_new = "INSERT INTO eintraege VALUES(?, ?, ?)"
    cursor.execute(sql_new, (datum, artikel, betrag))
    connection.commit()





""" # Verbindung schließen
connection.close() """

# GUI

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action():
    kaufdatum_text = eingabe_kaufdatum.get()
    artikel_text = eingabe_artikel.get()
    betrag_text = eingabe_betrag.get()
    if (kaufdatum_text == "" or artikel_text == "" or betrag_text == "" ):
        info_label.config(text="Bitte füll alle Felder aus")
    else :
        new_entry()

# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Ausgabentracker")

#Frames
ausgabeframe = Frame(fenster, bg="white")
eingabeframe = Frame(fenster)

#Label und Buttons erstellen
eintraege_label = Label(ausgabeframe)

kaufdatum_label = Label(eingabeframe, text="Kaufdatum: ")
artikel_label = Label(eingabeframe, text="Artikelname: ")
betrag_label = Label(eingabeframe, text="Betrag: ")


welcome_label = Label(fenster, text="Ausgaben hinzufügen")
info_label = Label(fenster)

eingabe_kaufdatum = Entry(eingabeframe, bd=5, width=40)
eingabe_artikel = Entry(eingabeframe, bd=5, width=40)
eingabe_betrag = Entry(eingabeframe, bd=5, width=40)

submit_button = Button(fenster, text="Bestätigen", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)


info_label = Label(fenster, text="Ich bin eine Info:\n\
Der Beenden Button schliesst das Programm.")

# Ausgabe
sql_ausg = "SELECT * FROM eintraege"

# Empfang des Ergebnisses
cursor.execute(sql_ausg)

# Ausgabe des Ergebnisses
zeilen = []
for dsatz in cursor:
    zeilen.append(f"{dsatz[0]} | {dsatz[1]} | {dsatz[2]}")

eintraege_label.config(text="\n".join(zeilen))   


# Anordnung Frames, Labels und Eingabefelder
ausgabeframe.pack(ipadx=5, ipady=5, padx=10)
eintraege_label.pack()

eingabeframe.pack(ipadx=5, ipady=5, padx=10)
welcome_label.pack()
kaufdatum_label.grid(row = 2, column = 0)
eingabe_kaufdatum.grid(row = 2, column = 1)
artikel_label.grid(row = 3, column = 0)
eingabe_artikel.grid(row = 3, column = 1)
betrag_label.grid(row = 4, column = 0)
eingabe_betrag.grid(row = 4, column = 1)

submit_button.pack()
exit_button.pack()
info_label.pack()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()