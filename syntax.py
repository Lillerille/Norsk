# Richárd Bagi, Norsk Projekt 2019

def syntax(lista, dictionary):
    """Find the word class based on the context. Return the word class."""
    if lista[5] in dictionary:
        return dictionary[lista[5]]
    else:
        output = ""
        if ((lista[4] is "verb") and (lista[6] is "konj") and (type(lista[7]) is not int) and (lista[7] is not "verb"))):
            output = "sub"
        elif ((lista[4] is "verb") and (lista[6] is "konj") and (lista[7] is "adv") and (lista[8] is not "verb")):
            output = "sub"
        elif ((lista[4] is "verb") and (lista[6] is "konj") and (type(lista[7]) is not int) and (lista[7] is "verb"))):
            output = "verb"
        elif ((lista[4] is "verb") and (lista[6] is "konj") and (lista[7] is "adv") and (lista[8] is "verb")):
            output = "verb"
        elif ((lista[0] is "pron") and ((lista[1] and lista[2] and lista[3] and lista[4]) is ("adj" or "adv" or "tall" or "konj"))):
            output = "sub"
        elif ((lista[1] is "pron") and ((lista[2] and lista[3] and lista[4]) is ("adj" or "adv" or "tall" or "konj"))):
            output = "sub"
        elif ((lista[2] is "pron") and ((lista[3] and lista[4]) is ("adj" or "adv" or "tall"))):
            output = "sub"
        elif ((lista[3] is "pron") and (lista[4] is ("adj" or "tall"))):
            output = "sub"
        elif ((lista[3] is "pron") and (lista[4] is "adv") and (lista[6] is "konj")):
            output = "sub"
        elif ((lista[0] is "verb") and ((lista[1] and lista[2] and lista[3] and lista[4]) is ("adv" or "konj"))):
            output = "verb"
        elif ((lista[1] is "verb") and ((lista[2] and lista[3] and lista[4]) is ("adv" or "konj"))):
            output = "verb"
        elif ((lista[2] is "verb") and ((lista[3] and lista[4]) is "adv")):
            output = "verb"
        elif ((lista[3] is "verb") and (lista[4] is "adv")):
            output = "verb"
        elif ((lista[3] and lista[4]) is "prepo"):
            output = "sub"
        elif ((lista[3] is "prepo") and (lista[4] is "pron")):
            output = "sub"
        elif lista[4] is "":
            if ((lista[6] is "pron") and (lista[7] is not "konj")):
                output = "verb"
            elif lista[6] is "tall":
                output = "verb"
            elif ((lista[6] is "pron") and (lista[7] is "konj") and (type(lista[8]) is int)):
                if lista[9] is ("pron" or "prepo"):
                    output = "verb"
                else:
                    output = "sub"
            else:
                output = "sub"
        elif lista[4] is "prepo":
            output = "sub"
        elif (((lista[4] and lista[6]) is "pron") and (type(lista[7]) is int)):
            output = "verb"
        elif (((lista[4] and lista[2]) is "pron") and (lista[3] is "verb")):
            output = "sub"
        elif (((lista[4] and lista[6]) is "pron") and (lista[3] is ("prepo" or "adv"))):
            output = "sub"
        
        else:
            output = "oklart"
        return output

# if verb + ikke + ? + (prepo+pron)/pron = > verb  
# if prepo ? pron => 
# if conj pron ? => verb
# if ? pron/tall => verb
# if ? ... => subj
# verb (pron/tall/adj/arv) subj ? => subj
