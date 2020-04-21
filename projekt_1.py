


def cteniSlovniku(nazevSlovniku):
    slovaSlovniku = []
    vlozenySoubor = open(nazevSlovnkiu, "r")
    for radek in vlozenySoubor:
        slovo = radek.strip()
        slovaSlovniku.append(slovo)
    vlozenySoubor.close()
    return slovaSlovniku

def cteniTextu(nazevTextovehoDokumentu):
    slova = []
    vlozenySoubor = open(nazevTextovehoDokumentu, "r")
    for radek in vlozenySoubor:
        slovaVRadku = radek.strip().split()
        for slovo in slovaVRadku:
            slova.append(slovo.strip(" .,!/':;-_?").lower())
     vlozenySoubor.close()
    return slova



def hledaniChyb(slovaSlvoniku, slovaTextu):
    chybnaSlova = []
    for slovo in slovaTextu:
        if slovo not in slovaSlovniku:
            chybnaSlova.append(slovo)
    return chybnaSlova


def vypisChyb(seznamChyb):
    print("Slova s pravopisnou chybou jsou: ")
    for slovo in seznamChyb:
        print(slovo)




def main():
    print("Vítejte v kontrole pravopisu")
    slovnik = input("Zadejte prosím soubor slovníku: ")
    text = input("Zadejte prosím soubor s textem ke kontrole: ")
    vypisSlovniku = cteniSlovniku(slovnik)

    vypisTextu = cteniTextu(text)
    seznamChyb = hledaniChyb(vypisSlovniku, vypisTextu)
    vypisChyb(seznamChyb)




main()