def Ankunft_Begrüßung():
    print("Willkommen zu meinem Mini_rechner")

def Teilung(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        print("Erreur : division par zéro")



def Anzeige():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Verteilung")

    choix = input(" geben sie Ihre wahl ein (1-4) : ")
    while choix not in ["1", "2", "3", "4"]:
        choix = input("Choix invalide. Entrez votre choix (1-4) : ")

    return choix

Begrüßung=Ankunft_Begrüßung()
num1 = float(input("Geben sie der erste Nummer ein : "))
num2 = float(input("Geben sie den zweite Nummer ein : "))
choix=Anzeige()   

match choix:
    case '1':
        result = num1+ num2
    case '2':
        result = num1- num2
    case '3':
        result = num1* num2
    case '4':
        result = Teilung(num1, num2)
    case _:
        print("Choix invalide.")


print(f"le resultat est {result}")