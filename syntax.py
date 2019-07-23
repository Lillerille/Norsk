# Richárd Bagi, Norsk Projekt 2019

def syntax_sva(lista, dictionary):
    """Find the word class that might be either substantive, verb or adjective based on their
    endings with the help of the context. Return the word class."""
    if lista[5] in dictionary:
        return dictionary[lista[5]]
    else:
        output = ""
        if ((lista[4] is "verb") and (lista[6] is "konj") and (type(lista[7]) is not int) and (lista[7] is not "verb")):
            output = "sub"
        elif ((lista[4] is "verb") and (lista[6] is "konj") and (lista[7] is "adv") and (lista[8] is not "verb")):
            output = "sub"
        elif ((lista[4] is "verb") and (lista[6] is "konj") and (lista[7] is "verb")):
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
        elif ((lista[3] is "pron") and (lista[4] is ("adj" or "adv")) and (lista[6] is "konj")):
            output = "sub"
        elif ((lista[0] is "verb") and ((lista[1] and lista[2] and lista[3] and lista[4]) is ("adv" or "adj" or "konj"))):
            output = "verb"
        elif ((lista[1] is "verb") and ((lista[2] and lista[3] and lista[4]) is ("adv" or "adj" or "konj"))):
            output = "verb"
        elif ((lista[2] is "verb") and ((lista[3] and lista[4]) is ("adj" or "adv"))):
            output = "verb"
        elif ((lista[3] is "verb") and (lista[4] is ("adj" or "adv"))):
            # har virkelig åpnet
            output = "verb"
        elif ((lista[3] is not ("sub" or "oklart")) and (lista[4] is "verb")):          # and (type(lista[3]) is not int) excluded since
            output = "sub"                                                              # the element must have been checked before
        elif ((lista[2] is not ("sub" or "oklart")) and (lista[3] is "verb") and (lista[4] is ("adj" or "adv"))):
            output = "sub"
        elif ((lista[2] is not ("sub" or "oklart")) and (lista[4] is "verb") and (lista[3] is ("adj" or "adv"))):
            # bisats
            output = "sub"
        elif ((lista[3] and lista[4]) is ("prepo" or "part")):
            output = "sub"
        elif ((lista[3] is ("prepo" or "part")) and (lista[4] is "pron")):
            output = "sub"
        elif lista[4] is "":
            if ((lista[6] is "pron") and (lista[7] is not "konj")):
                output = "verb"
            elif lista[6] is ("tall" or "oklart"):
                output = "verb"
            elif ((lista[6] is "pron") and (lista[7] is "konj") and (type(lista[8]) is int)):
                if lista[9] is ("pron" or "prepo" or "part" or "adv"):
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
        elif (((lista[4] and lista[6]) is "pron") and (lista[3] is ("prepo" or "part" or "adv"))):
            output = "sub"
        elif (((lista[4] and lista[1]) is "pron") and (lista[2] is "verb") and (lista[3] is ("prepo" or "part"))):
            output = "sub"
        elif ((lista[3] is "verb") and (lista[4] is ("adv" or "adj")) and (lista[6] is ("pron" or "prepo"))):
            output = "verb"
        elif ((lista[2] is "verb") and ((lista[3] and lista[4]) is ("adv" or "adj")) and (lista[6] is ("pron" or "prepo" or "part"))):
            output = "verb"
        elif ((lista[1] is "verb") and ((lista[2] and lista[3] and lista[4]) is ("adv" or "adj")) and (lista[6] is ("pron" or "prepo" or "part"))):
            output = "verb"
        elif ((lista[0] is "verb") and ((lista[1] and lista[2] and lista[3] and lista[4]) is ("adv" or "adj")) and (lista[6] is ("pron" or "prepo" or "part"))):
            output = "verb"
        elif ((lista[3] is "verb") and (lista[4] is ("adv" or "adj")) and ((lista[6] and lista[7]) is ("prepo" or "pron" or "part"))):
            output = "verb"
        elif ((lista[2] is "verb") and ((lista[3] and lista[4]) is ("adv" or "adj")) and ((lista[6] and lista[7]) is ("prepo" or "pron" or "part"))):
            output = "verb"
        elif ((lista[1] is "verb") and ((lista[2] and lista[3] and lista[4]) is ("adv" or "adj")) and ((lista[6] and lista[7]) is ("prepo" or "pron" or "part"))):
            output = "verb"
        elif ((lista[0] is "verb") and ((lista[1] and lista[2] and lista[3] and lista[4]) is ("adv" or "adj")) and ((lista[6] and lista[7]) is ("prepo" or "pron" or "part"))):
            output = "verb"
        elif ((lista[4] is ("prepo" or "part")) and (lista[6] is ("adj" or "adv"))):
            output = "adj"
        elif lista[4] is ("prepo" or "part"):
            output = "sub"
        elif ((lista[4] is "pron") and (lista[6] is "konj") and (lista[7] is not ("sub" or "tall" or "adj" or "adv"))):
            output = "verb"
        elif ((lista[4] is "pron") and (lista[6] is "konj") and (lista[7] is ("sub" or "tall" or "adj" or "adv"))):
            output = "sub"
        elif ((lista[4] is "pron") and ((lista[6] is "pron") or ((lista[6] is "adv") and (lista[7] is "pron")))):
            output = "verb"
        elif ((lista[3] is "verb") and (lista[4] is ("prepo" or "part")) and ((type(lista[6]) is int) or (lista[6] is ("sub" or "verb")))):
            output = "adj"
        elif ((lista[2] is "verb") and (lista[3] is ("adv" or "adj")) and (lista[4] is ("prepo" or "part")) and (type(lista[6]) is int)):
            output = "adj"
        elif ((lista[2] is "verb") and (lista[3] is ("prepo" or "part")) and (lista[4] is ("adj" or "tall"))):
            output = "sub"
        elif ((lista[1] is "verb") and (lista[2] is ("adv" or "adj")) and (lista[3] is ("prepo" or "part")) and (lista[4] is ("adj" or "tall"))):
            output = "sub"
        elif ((lista[3] is ("pron" or "sub")) and (lista[4] is "verb") and (lista[6] is ("part" or "prepo")) and (lista[7] is "pron")):
            output = "sub"
        elif ((lista[2] is ("pron" or "sub")) and ((lista[3] or lista[4]) is "verb") and ((lista[3] or lista[4]) is ("adj" or "adv")) and (lista[6] is ("part" or "prepo")) and (lista[7] is "pron")):
            output = "sub"
        elif ((lista[4] is ("pron" or "sub")) and (lista[6] is ("prepo" or "part")) and (lista[7] is "pron") and (lista[8] is "pron")):
            output = "verb"
        elif ((lista[4] is ("pron" or "sub")) and ((lista[6] and lista[7]) is ("adv" or "prepo" or "part")) and (lista[8] is "pron") and (lista[9] is "pron")):
            output = "verb"
        elif ((lista[3] is ("pron" or "sub")) and (lista[4] is "adv") and (lista[6] is ("prepo" or "part")) and (lista[7] is "pron") and (lista[8] is "pron")):
            output = "verb"
        elif ((lista[2] is ("pron" or "sub")) and ((lista[3] and lista[4]) is "adv") and (lista[6] is ("prepo" or "part")) and ((lista[7] and lista[8]) is "pron")):
            output = "verb"
        elif ((lista[1] is ("pron" or "sub")) and ((lista[2] and lista[3] and lista[4]) is "adv") and (lista[6] is ("prepo" or "part")) and ((lista[7] and lista[8]) is "pron")):
            output = "verb"
        elif ((lista[0] is "verb") and ((lista[1] and lista[2] and lista[3]) is ("adv" or "part" or "prepo" or "adj" or "konj" or "tall")) and (lista[4] is "sub")):
            output = "sub"
        elif ((lista[1] is "verb") and ((lista[2] and lista[3]) is ("adv" or "adj" or "part" or "prepo" or "tall")) and (lista[4] is "sub")):
            output = "sub"
        elif ((lista[2] is "verb") and (lista[3] is ("adv" or "adj" or "tall")) and (lista[4] is "sub")):
            output = "sub"
        elif ((lista[6] is "pron") and (lista[7] is not "verb")):
            output = "verb"
        elif ((lista[6] is "pron") and ((lista[7] is "verb") or (type(lista[7]) is int))):
            output = "sub"
        elif (lista[6] is "tall"):
            output = "verb"
        elif ((lista[4] is "tall") and ((lista[6] is "verb") or (type(lista[6]) is int))):
            output: "sub"
        elif ((lista[4] is "tall") and (lista[6] is ("adj" or "adv")) and ((lista[7] is "verb") or (type(lista[7]) is int))):
            output: "sub"
        elif ((lista[4] is "oklart") and (lista[6] is "pron") and (lista[7] is ("adv" or "adj" or "part" or "prepo"))):
            output = "verb"
        elif ((lista[3] is "konj") and (lista[4] is "oklart") and (lista[6] is "pron")):
            output = "verb"
        elif ((lista[3] is "oklart") and (lista[4] is ("adv" or "adj")) and (lista[6] is ("pron" or "prepo" or "part"))):
            output = "verb"
        elif ((lista[4] is ("adv" or "adj")) and ((lista[6] is ("pron" or "tall" or "sub")) or (type(lista[6]) is int))):
            output = "verb"
        elif ((lista[4] is "pron") and ((lista[6] is "adj") or (type(lista[6]) is int)) and ((lista[7] is "verb") or (type(lista[7]) is int))):
            output = "sub"
        elif ((lista[3] is "pron") and (lista[4] is ("sub" or "oklart")) and ((lista[6] is "verb") or (type(lista[6]) is int))):
            # consequently from the case above
            output = "adj"
        elif ((lista[4] is "konj") and (lista[6] is ("adv" or "adj" or "pron" or "prepo" or "part"))):
            output = "verb"
        elif ((lista[4] is "adv") and (lista[6] is "adv")):
            output = "verb"
        elif ((lista[4] is "adv") and (lista[6] is ("prepo" or "part")) and (lista[7] is "adv")):
            output = "verb"
        elif ((lista[4] is "pron") and (lista[6] is ("adv" or "adj"))):
            output = "verb"
        elif ((lista[4] is "pron") and (lista[6] is ("prepo" or "part")) and (lista[7] is ("adv" or "adj"))):
            output = "verb"
        elif (((lista[3] and lista[4]) is "pron") and (lista[6] is not "verb")):
            output = "verb"
        elif (((lista[3] and lista[4]) is "pron") and (lista[6] is "verb")):
            output = "sub"
        else:
            output = "oklart"
        return output

def syntax_gen(i, dictionary):
    """Find the word class of the rest of the words based on the context.
    Return the word class."""
    output = ""
    while True:
        if lista[i-1][1] is ("adj" or "adv" or "konj"):
            pass
        # elif lista[i-1][0] is ("den" or "det" or "de" or "der" or "min" or "din" or "sin" or "hans" or "hennes" or "vår" or "deres"):
        #     output = ""
    return
