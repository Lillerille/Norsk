# Richárd Bagi, Projekt 2019

from inpfil import inpfil
import re

def nopunk(string):
    """Den här funktionen tar emot en sträng och plockar bort skiljetecken
    och siffror samt byter stora bokstäver till små. Den returnerar en ny
    sträng med endast ord."""
    string = re.sub(r'\d', '', string)
    string = re.sub(r'[^a-z|A-Z|åäöæø|ÅÄÖÆØ|\s|-]',' ',string)
    string = re.sub(r'-\s{2,}', ' ', string)
    string = re.sub(r'\s\w*-\s', ' ', string)
    string = re.sub(r'-{2,}', ' ', string)
    string = re.sub(r'\s{2,}', ' ', string)
    if string.endswith(' '):
        string = string[:-1]
    string = string.lower()
    return string

# Testkod
assert nopunk("A set! Of 44 characters to potentially-     match, so w? is all alphanumeric characters- and other animals, and the... Trai56ling? */+ Period . adds to that set of\n\n\n\n\n\n\ncharacters.") == 'a set of characters to potentially match so w is all alphanumeric and other animals and the trailing period adds to that set of characters'
assert nopunk("Hej, och-   välkommen!? Ælmøs... væzØr*") == 'hej och välkommen ælmøs væzør'
assert nopunk("Kh85ÖäÅm") == 'khöäåm'

