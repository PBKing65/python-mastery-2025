



class Todo:
            def __init__(self, text):
                self.text = text
                self.erledigt = False

            
            def erledigen(self):
                self.erledigt = True
                print("Aufgabe erledigt")

def main():

    todos = [
            Todo("Python lernen"),
            Todo("Einkaufen gehen"),
            Todo("Sport machen"),
            Todo("Freunde treffen"),
            Todo("schlafen"),
    ]

    todos[0].erledigen()
    todos[2].erledigen()
    todos[4].erledigen()

    

    print("=== Alle Aufgaben-Texte ===")
    texte = [todo.text for todo in todos]
    print(texte)

    print("=== Nur erledigte Aufgben ===")
    erledigt =[todo for todo in todos if todo.erledigt]
    for t in erledigt:
        print("✓", t.text)

    print("\n=== Nur offene Aufgaben (als neue Liste)===")
    offen = [t for t in todos if not t.erledigt]
    for t in offen:
         print("o",t.text)
    

if __name__ == "__main__":
    main()
