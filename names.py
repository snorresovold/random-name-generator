import random

FIRSTNAME = ["Snorre", "Espen", "Mats", "Patrick"]
LASTNAME = ["Søvold", "Solheim", "Jøssang", "Vårem"]

print("1: lage et tilfeldigt navn")
print("2: legge til fornavn")
print("3: legge til etternavn")


while True:
    x = int(input("Hva vil du? "))

    if x == 1:
        name = random.choice(FIRSTNAME) + " " + random.choice(LASTNAME)
        print(name)

    elif x == 2:
        n_fname = input("hvilket fornavn? ")
        FIRSTNAME.append(n_fname)

    elif x == 3:
        n_lname = input("hvilket etternavn? ")
        LASTNAME.append(n_lname)