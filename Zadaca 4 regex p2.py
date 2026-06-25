import re

prvo_slovo_imena = "D"
prvo_slovo_prezimena = "L"

tekst = input("Unesite string: ")

regex = "^" + prvo_slovo_imena + ".*[0-5].* .*" + prvo_slovo_prezimena + "$|^" + prvo_slovo_imena + ".* .*[0-5].*" + prvo_slovo_prezimena + "$"

result = re.search(regex, tekst)

if result:
    print("String je ispravan.")
    print("Podudaranje:", result.group())
else:
    print("String nije ispravan.")
