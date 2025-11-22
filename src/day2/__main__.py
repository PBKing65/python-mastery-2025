def main():
    print("🚀 DAY 2 - Willkommen zum echten Python-Spaß!\n")

    # 1. Listen – dein erstes "Array"
    lieblings_essen = ["Pizza", "Burger", "Sushi", "Döner"]
    print("Deine Top-4-Lieblingsessen:", lieblings_essen)
    lieblings_essen.append("Schokolade")
    print("Jetzt mit Schokolade:", lieblings_essen)

    # 2. String-Magie
    name = input("\nWie heißt du? ")
    print(f"Hallo {name.upper()}! Dein Name hat {len(name)} Buchstaben.")
    print(f"Und rückwärts: {name[::-1]} 😄")

    # 3. Eigene Funktion
    def motivieren(tag: int):
        print(f"Tag {tag}: Ich werde heute Python-Rockstar!")

    print("\nDeine Motivation für die nächsten 7 Tage:")
    for tag in range(1, 8):
        motivieren(tag)

    # 4. Mini-Zahlenraten-Spiel (dein erstes echtes Spiel!)
    print("\n🎲 Kleines Zahlenraten-Spiel (1–10)")
    geheimzahl = 7
    versuch = int(input("Dein Tipp: "))

    if versuch == geheimzahl:
        print("🎉 GENAU RICHTIG du bist ein Genie!")
    elif versuch < geheimzahl:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")

    print("\nDay 2 komplett  du rockst das!")

if __name__ == "__main__":
    main()