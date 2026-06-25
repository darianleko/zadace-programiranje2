def pozdrav(ime):
    return "Pozdrav " + ime + "!"
dobrodosao = lambda ime: "Dobrodošao " + ime + "!"
def pozovi_funkciju(funkcija):
    print(funkcija("Darian"))
pozovi_funkciju(pozdrav)
pozovi_funkciju(dobrodosao)
