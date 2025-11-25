class Todo:
    def __init__(self, text):
        self.text = text
        self.erledigt = False

    def anzeigen(self):
        status = "✓" if self.erledigt else "○"
        print(f"{status} {self.text}")

    def erledigen(self):
        self.erledigt = True
        print("✓ Aufgabe erledigt!")

class TodoListe:
    def __init__(self):
        self.aufgaben = []

    def hinzufügen(self,text):
        neueAufgabe = Todo(text)
        self.aufgaben.append(neueAufgabe)
        print(f"→ Hinzugefügt: {text}")

    def alle_anzeigen(self):
        print("\n=== Alle Aufgaben ===")
        if not self.aufgaben:
            print("Noch nichts zu tun - super!")
        else:
            for aufgabe in self.aufgaben:
                aufgabe.anzeigen()

    def erledigte_anzeigen(self):
        print("\n=== Erledigte Aufgaben ===")
        erledigte = [a for a in self.aufgaben if a.erledigt]
        if not erledigte:
            print("Noch nichts erledigt")
        else:
            for aufgabe in erledigte:
                aufgabe.anzeigen()



def main():
    print("Day 6 - Ich baue meine erste TodoListe Klasse!\n")

    liste = TodoListe()

    liste.hinzufügen("Python lernen")
    liste.hinzufügen("Einkaufen gehen")
    liste.hinzufügen("Sport machen")

    liste.alle_anzeigen()

    print("\nIch erledige die erste Aufgabe...")
    liste.aufgaben[0].erledigen()

    liste.alle_anzeigen()
    liste.erledigte_anzeigen()



if __name__ == "__main__":
    main()
