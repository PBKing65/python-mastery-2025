# Datei: main.py

class Katze:
    # Das ist der Konstruktor – wird aufgerufen, wenn du Katze() schreibst
    def __init__(self, name, alter):
        self.name = name        # self.name ist eine Instanzvariable
        self.alter = alter

    # Eine Methode (Funktion innerhalb der Klasse)
    def miauen(self):
        print(f"{self.name} sagt: Miau!")

    def geburtstag(self):
        self.alter = self.alter + 1
        print(f"{self.name} ist jetzt {self.alter} Jahre alt!")


# ─────── Hier startet das Programm ───────
if __name__ == "__main__":
    # Wir erzeugen zwei echte Katzen-Objekte
    meine_katze = Katze("Luna", 3)
    deine_katze = Katze("Mogli", 5)

    # Jetzt benutzen wir sie
    print("Wir haben zwei Katzen:")
    meine_katze.miauen()
    deine_katze.miauen()

    meine_katze.geburtstag()
    deine_katze.geburtstag()