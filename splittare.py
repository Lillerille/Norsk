# Richárd Bagi, Projekt 2019

from nopunc import nopunk

def splittare(string):
    """Den här funktionen tar emot en sträng och delar upp orden i den
    i listelement. Returnerar en lista."""
    lista = string.split(' ')
    return lista

# Testkod
assert splittare('Hej och välkommen') == ['Hej', 'och', 'välkommen']
assert splittare(nopunk("Hej, och-   välkommen!? Ælmøs... væzØr*")) == ['hej', 'och', 'välkommen', 'ælmøs', 'væzør']
