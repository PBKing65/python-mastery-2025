import json
from pathlib import Path
from typing import List, Dict

TODO_FILE = Path("todos.json")

def lade_todos() -> List[Dict[str, str]]:
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text(encoding="utf-8"))
    return []

def speichere_todos(todos: List[Dict[str, str]]) -> None:
    TODO_FILE.write_text(json.dumps(todos, indent=2, ensure_ascii=False), encoding="utf-8")

def main() -> None:
    print("🚀 Day 3 – Deine erste persistente To-do-Liste\n")
    todos = lade_todos()

    while True:
        print("\nDeine Aufgaben:")
        if not todos:
            print("   → noch nichts zu tun – super!")
        else:
            for i, aufgabe in enumerate(todos, 1):
                status = "✓" if aufgabe["erledigt"] else "○"
                print(f"   {i}. {status} {aufgabe['text']}")

        print("\nWas möchtest du?")
        print("1 → Neue Aufgabe | 2 → Erledigen | 3 → Beenden")
        wahl = input("→ ").strip()

        if wahl == "1":
            text = input("Aufgabe eingeben: ").strip()
            if text:
                todos.append({"text": text, "erledigt": False})
                speichere_todos(todos)
        elif wahl == "2" and todos:
            try:
                nr = int(input(f"Welche Nummer (1–{len(todos)})? "))
                if 1 <= nr <= len(todos):
                    todos[nr-1]["erledigt"] = True
                    speichere_todos(todos)
            except ValueError:
                pass
        elif wahl == "3":
            print("Bis morgen! Du rockst das! 💪")
            break

if __name__ == "__main__":
    main()