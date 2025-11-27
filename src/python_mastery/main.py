

def main():
    print("Day 7 - Listen Deep Dive\n")

    zahlen =[10,20,5,50,30]
    namen = ["Peter", "Lisa", "Tom"]

    print("Erste Zahl", zahlen[0])
    print("Letzte Zahl", zahlen[-1])
    print("Zweiter Name", namen[1])

    print("Anzahl Zahlen", len(zahlen))
    print("Anzahl Namen", len(namen))

# Element überschreiben
    zahlen[2] = 999
    print("Zahlen nach Überschreiben", zahlen)

#Element anhängen
    namen.append("Anna")
    print("Namen nach Append", namen)

# Element eifügen
    zahlen.insert(1,15)
    print("Die Zahl 15 eingefügt zweischen 10 und 20", zahlen)





if __name__ == "__main__":
    main()
