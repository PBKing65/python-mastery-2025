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


def main():
    print("Day 5 - Ich baue meine erste Todo-Klasse selbst!\n")

    aufgabe1 = Todo("Python lernen")
    aufgabe2 = Todo("Einkaufen gehen")
    aufgabe3 = Todo("Sport machen")

    aufgabe1.anzeigen()
    aufgabe2.anzeigen()
    aufgabe3.anzeigen()

    print("\nIch erledige jetzt die Aufgabe...")
    aufgabe1.erledigen()

    print("\nAktueller Stand:")
    aufgabe1.anzeigen()
    aufgabe2.anzeigen()
    aufgabe3.anzeigen()



if __name__ == "__main__":
    main()
