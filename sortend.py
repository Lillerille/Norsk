# Richárd Bagi, Norsk Projekt 2019

from splittare import splittare
import re
import tkinter as tk

class Node:
    """This class implements a node to a singly linked list."""

    def __init__(self,elem = None):
        """Create element properties"""
        self._Elem = elem # arbirtary element in list
        # self._Su = None
        # self._Ve = None
        # self._Ov = None
        # self._Aj = None
        # self._Av = None
        # self._Ta = None
        # self._Co = None
        # self._Pr = None
        # self._In = None
        # self._et = None
        # self._te = None
        # self._sk = None
        # self._ere = None
        # self._fere = None
        self._NE = None # pointer, NextElement

class LinkedList:
    """This class implements a singly linked list."""

    def __init__(self):
        self._FE = None # first element in list
        self._NE = None

    def addFirst(self, item):
        """This method inserts the given element at the beginning of this list."""
        _NFE = Node(item)
        _NFE._NE = self._FE
        self._FE = _NFE             # Redefine previous First Element as New First Element

    def addLast(self, item):
        """This method inserts the given element at the end of this list."""
        _LE = Node(item)
        if self._FE is None:
            self._FE = _LE
            return                  # If the list is empty we set first element = last element
        _OldLE = self._FE
        while(_OldLE._NE):
            _OldLE = _OldLE._NE     # We find the last but one element
        _OldLE._NE = _LE
        return

    def clear(self):
        """Remove all elements from this list."""
        _First = self._FE
        if _First == None:
            return None
        else:
            while(_First):
                self._FE = _First._NE
                _First = None
                _First = self._FE
            return

    def getlist(self,index):
        """Return the content of all elements up to given index."""
        if self.size() == 0:
            return  []
        else:
            _n = self.size()
            _lista = [0]*n
            _temp = self._FE
            _count = 0
            while(_temp):
                if (_count == index-1):
                    _lista[_count] = _temp._Elem
                    return _lista
                _lista[_count] = _temp._Elem
                _count +=1
                _temp = _temp._NE
            return []

    def get(self,index):
        """Return the element at the specified position in this list.
        Return null if index is out of bounds."""
        if self.size() == 0:
            return None
        else:
            _temp = self._FE
            _count = 0
            while(_temp):
                if (_count == index-1):
                    return _temp._Elem
                _count +=1
                _temp = _temp._NE
            return None

    def size(self):
        """Return the number of elements in a linked list."""
        _temp = self._FE
        _count = 0
        while(_temp):
            _count += 1
            _temp = _temp._NE
        return _count

def _syntax(lista):
    """This  private function tries to find the word class based on the context.
    Retrurn the word class."""
    
    return

def sortend(lista):
    """Sort the elements of input list to word class after endings.
    Returns a list of lists with the sorted elements."""
    sub = LinkedList()
    verb = LinkedList()
    adj = LinkedList()
    adv = LinkedList()
    pron = LinkedList()
    tall = LinkedList()
    konj = LinkedList()
    inter = LinkedList()
    prepo = LinkedList()
    usikker = LinkedList()
    resten = Linkedlist()
    # te = Linkedlist()
    # skaper = Linkedlist()
    # ere = Linkedlist()
    # fe = Linkedlist()
    
    subre = re.compile(r"([a-zåæø]*((år|året|årene|morgen|måned|kveld|dag|minutt|sekund|uke|(sekunde|minutte|uke|månede|dage|kvelde|morgene)([tnr]|ne)|natt|natt(a|en)|nette(r|ne))|(mål|måle(t|ne))|(by|bye(n|r|ne))|(((en|all)er|lo|strate|litur|ele|kirur|al)gi|((en|all)er|lo|strate|litur|ele|kirur|al)gie([nr]|ne))|(else|else([ntra]|ne))|(hete([nr]|ne))|(ing|inge([nr]|ne))|(ikk|ikken|(?<!s)ikker|ikkene)|(skap|skap((e[tn]|(ne))|a))|(sjon|sjone([nr]|ne))|(ment|mente([tra]|(ne)))|(en|ene)|(ett|ette(t|ne))|(mel|melen|mle(r|ne))|(neste|neste([nr]|ne))|(iste|iste([nr]|ne))|([lg]ås|[gl]åsen|gåsa|gj[eæ]ss|[gl]åser|[gl]åsene|gj[æe]ssene)|(ang|angen|[ea]nger|[ea]ngene)|((f|sl)ange|(f|sl)angen|(f|sl)anger|(f|sl)angene)|(age|age([rn]|ne))|(lager|lageret|lagret|lagre|lagrene|lagerene)|(areal|eale([tr]|ne))|(brev|brev(et|er|ene|a))|(f|fe([tn]|ne)|afer)|(am|ame|ame([nr]|ne)|amme([nrt]|ne))|(([ts]|eni)ør|([ts]|eni)øre([nr]|ne))|(yre|yre([tnr]|ne))|(ed|ede([trn]|ne))|(ti|ti(e([tnr]|ne)|[tn]))|(an|a(n|nn)e([nr]|ne))|(m[ae]n|mannen|mennene)|(ende([nr]|ne))|((til|for)hør(et|ene))|(ramme([nr]|ene))|((?<!be)stemme([nr]|ne))|(erne))[s]*$)")
    # főnevek               oki
    # ska kollas efter adjektiven
    verbre = re.compile(r"([a-z|åæø]*((ere[rs])|(r[ui]ste|r[ui]ste[rs]|r[ui]stet|r[ui]stets)|(niste|nistet|nister|nistes|nistets)|((kl|[lj])age|(kl|l)age[rs]|(kl|l)aget|(kl|l)agets)|(styre|styr(er|te|t)[s]*)|(øre|kjør|hør(e|er|te|t)[s]*)|([fg]å|[fg](å[rs]|ikk|tt)[s]*|mått(e|et)[s]*|må[s]*)|(virke|virke[rts][s]*)|([aeiouyåæø][bcdfhjklmnprstz](e|e[rs]|te|es|t|ts))|(([vg]|ei|ai|øy|au|eu)(e|s|e[rs]|de|des|d|ds))|(nå|når|nås|nådde|nåddes|nådd|nådds))$)")
    # TODO: |([bcdfhjklmnprstz]+(e[rts]|ts))
    # igék                  oki
    orevre = re.compile(r"([a-z|åæø]*((be|be[rs]|ba|bas|bad|bads|bedt|bedts)|(bit[se]|bite[rs]|b(e|ei)(t|ts)|bitt[s]*)|(bind[se]|binde[rs]|band(t|ts)|bunde(t|ts))|(bety|bety[rs]|bet(yd|ø)d[s]*)|(bli|bl(i|ive)[rs]|blivs|bl(e|ei)[s]*|blit(t|ts))|(bre|bre[rs]|bred(t|t[es]|tes))|(brek(k[se]|ker|kes|et|ets)|brakk|brakks)|(bren(n[se]|nes|ner|t|ts)|brant|brants)|(bring([se]|e[rs])|brak(t[es]|tes|t|))|(brist(e[rst]|[es])|bras(t|ts))|(bryt(e|e[rs]|s)|brø(t|ts)|brut(t|ts))|(burde|burde(s|t|ts)|bør|børs)|(by|by[rs]|bø[dy]|bø[dy]s|b(ydd|ydt)|b(ydd|ydt)s)|(bær[se]|bære[rs]|bar|bars|båre(t|ts))|(dett[se]|dette[rst]|datt|datts|dettets)|(dra|drage|dra[rs]|drage[rs]|dro|drog|(dro|drog)s|dra(tt|dd)|dra(tt|dd)s)|(drikk[se]|drikke[rs]|drakk|drakks|drukke(t|ts))|(driv[es]|drive[rs]|dr(e|ei)v|dr(e|ei)vs|dreve(t|ts))|(dø|dø[rs]|døde|dødes|død(d|ds))|(et[es]|ete[sr]|åt|åts|ett|etts)|((?<!((en|all)er|lo|strate|litur|ele|kirur|al))(gi|give|gi[rs]|give[rs]|ga|gav|gavs|git(t|ts)))|(gidd[es]|gidde[rst]|gadd|gadds|giddets)|(gjeld[se]|gjelde[rs]|gj[ae]ld(t|ts))|(gjør[se]|gjøre[rs]|gjør|gjor(de|t)[s]*)|(g[nl]i|g[nl]i[rs]|g[nl]e(d|i)[s]*|g[nl]idd[s]*)|(glipp[se]|glippe[trs]|glapp[s]*|glippets)|(grav[se]|grave[rs]|grov[s]*|grav(d|ds))|(grip[se]|gripe[rs]|gr(e|ei)p[s]*|grepe(t|ts))|(gråt[se]|gråte[rs]|grå(t|tt)[s]*)|(gys[es]|gyse[rs]|gjøs|gyss)|(gyt[se]|gyte[rs]|g(jøt|ytte)[s]*)|(gyt(t|ts))|(gå|gå[rs]|(gikk|gått)[s]*)|(fall[es]|falle[rs]|fal(t|ts))|(finn[es]|finne[rs]|fan(t|ts)|funne(t|ts))|(fly|fly[rs]|fløy|fløys|fløye(t|ts))|(flyt[se]|flyte[rs]|flø(t|yt)|flø(t|yt)s|flyt(t|ts))|(frys[se]|fryse[rs]|frø[y]*s|frosse(t|ts))|(fyk[se]|fyke[rs]|fø[y]*k[s]*|føke(t|ts))|(følg[se]|følge[rs]|fulgt[e]*[s]*)|(ha(v[se]|ve[rs]|[rs])|ha(dde|tt)[s]*)|(heng[et][s]*|hengs|henger|hang[s]*)|(hiv[es]|hive[rs]|(h(e|ei)v|hevet)[s]*)|(hjelp[es]|hjelpe[rs]|(hjalp|hjulpet)[s]*)|(h[uo]gg[se]|h[uo]gge[rs]|(h[uo]gg|hogget|hugd)[s]*)|(hold[es]|holde[rs]|hold(t|ts))|(jag[es]|jage[rs]|(jog|jagd)[s]*)|(kling[es]|klinge[rs]|(klang|kling(et|t))[s]*)|(k[rl]yp[se}|k[rl]ype[rs]|(k[rl](ø|øy)p|k[rl]øpet)[s]*)|(klyv[se]|klyve[rs]|(kl(ø|øy)v|kløvet)[s]*)|(knekk[se]|knekke[rs]|(knakk|knekket)[s]*)|(knip[se]|knipe[rs]|(kn(e|ei)p|knepet)[s]*)|(komme|komme[rs]|(kom|kommet)[s]*)|(kunne[ts]|kunnets|kan)|(kved[se]|kvede[rs]|kva(d|det)[s]*)|(kve(kk|pp)e|kve(kk|pp)e[rst][s]*|kve(kk|pp)s|kva(kk|pp)e[s]*)|(la|late|la(r|ter|tes|ts|s)|(lot|latt)[s]*)|(le|le[rs]|(lo|ledd)[s]*)|(legge|legge[rs]|leggs|(la|lagt)[s]*)|(li|lide|(li|lide)[rs]|lids|(led|lidd)[s]*)|(ligge[rs]*|liggs|(lå|ligget)[s]*)|(lyde[rs]*|lyds|(lød|lydt)[s]*)|(ly[gv]e[rs]*|ly[gv]s|(løy|løyet)[s]*)|(løpe[rs]*|løps|(lø(p|pt))[s]*)|(låte[rs]*|låts|(låt|lått)[s]*)|(ny[st]e[rs]*|(n(ø|øy)[st]|ny[st]t)[s]*)|(rinne[rs]*|rinns|(r(an|unne)t)[s]*)|(pipe[rs]*|pips|(p(e|ei)p|pepet)[s]*)|(rekke[rs]*|rekks|(rakk|rukket)[s]*)|(renne[rs]*|renns|(r[ea]nt)[s]*)|((ri|ride)[rs]*|rids|(re[di]|ridd)[s]*)|(rive[rs]*|rivs|(r(e|ei)v|revet)[s]*)|(ryke[rs]*|ryks|(r(ø|øy)k|røket)[s]*)|(se[rs]|(så|sett)[s]*)|(selge[rs]|selgs|solgt[e]*[s]*)|(sette[rs]*|setts|satt[e]*[s]*)|(si|si(er|s|es)|(sa|sagt)[s]*)|(sige[rs]*|(s(e|ei)g|seget)[s]*)|(sitte[rs]*|(satt|sittet)[s]*)|(skite[rs]*|skits|(skjet|skitt)[s]*)|(skjelve[rs]*|(skalv|skljelvet)[s]*)|(skjære[rs]|skjærs|(skar|skåret)[s]*)|(skli[rs]*|(skle[di]|sklidd)[s]*)|(skrid[es]|skride[rs]|(skre[di]|skridd)[s]*)|(skrik[es]|skrike[rs]|(skr(e|ei)k|skreket)[s]*)|(skriv[es]|skrive[rs]|(skr(e|ei)v|skrevet)[s]*)|(skryt[es]|skryte[rs]|(skrøt|skrytt)[s]*)|(skvett[es]|skvette[rs]|(svkatt|skvettet)[s]*)|(skulle|skal|skullet)|(sky[v]t[se]|sky[vt]e[rs]|(skj(ø|øy)t|sk(jø|øy)v|skjøvet|skutt)[s]*)|(sleng[es]|slenge[rs]|(slang|slengt)[s]*)|(slipp[es]|slippe[rs]|(slapp|sluppet)[s]*)|(slit[es]|slite[rs]|(sl(e|ei)t|slitt)[s]*)|(slå|slå(r|ss)|(slo|slått)[s]*)|(smell[es]|smelle[rs]|sm[ea]lt[s]*)|(smyg[es]|smyge[rs]|(sm(ø|øy)g|smøget)[s]*)|(smør[es]|smøre[rs]|(smurte|smurt)[s]*)|(snik[es]|snike[rs]|(sn(e|ei)k|sneket)[s]*)|(snyt[es]|snyte[rs]|(sn(ø|øy)t|snytt)[s]*)|(sov[se]|sove[rst]|sov|sovets)|(spinn[es]|spinne[sr]|(spant|spunnet)[s]*)|(spre(kk|tt)[es]|spre(kk|tt)e[rs]|(spra(kk|tt)|spr(ukk|ett)et)[s]*)|(spring[se]|springe[rs]|(sprang|sprunget)[s]*)|(spørr[es]|spør|spørs|(spurte|spurt)[s]*)|(stig[es]|stige[rs]|(st(e|ei)g|steget)[s]*)|(stikk[es]|stikke[rs]|(stakk|stukket)[s]*)|(stjel[es]|stjele[rs]|(stjal|stjålet)[s]*)|(strekk[es]|strekke[rs]|(strak(k|te)|str(ukke|ek)t)[s]*)|(strid[es]|stride[rs]|(stred|stridd)[s]*)|(stryk[es]|stryke[rs]|(str(ø|øy)k|strøket)[s]*)|(stå|stå[rs]|st(o|od|ått)[s]*)|(su[pg][es]|su[pg]e[rs]|(sau[pg]|su[pg]d)[s]*)|(sverg[es]|sverge[rs]|(svor|sverget)[s]*)|(svi|svi[sr]|(sve[di]|svidd)[s]*)|(svik[es]|svike[rs]|(sv(e|ei)k|sveket)[s]*)|(synes|syntes)|(syn[kg][es]|syn[kg]e[rs]|(san[kg]|sun[kg]et)[s]*)|(ta[rs]*|tage[rs]*|(tok|tatt)[s]*)|(tell[se]|telle[rs]|(talte|talt)[s]*)|(tigg[es]|tigge[rs]|(tagg|tig(d|get))[s]*)|(t(o|ør)r[es]|(tør|turte|torde|turt|tort)[s]*)|(tre[rs]*|tred[es]|trede[rs]*|tråd(te|t)[s]*)|(treff[es]|treffe[rs]|(traff|truffet)[s]*)|(trå|trå[rs]|(trådte|tro|tråd(t|d))[s]*)|(tving[es]|tvinge[rs]|(tvang|tvunget)[s]*)|(velg[se]|velge[sr]|(valgte|valgt)[s]*)|(vik[es]|vike[rs]|(v(e|ei)k|veket)[s]*)|(ville|vil|vils|ville[ts]|villets)|(vinn[es]|vinne[rs]|(vant|vunnet)[s]*)|((vite|vet|visste|visst)[s]*)|(vri[rs]*|vride[rs]*|(vre[di]|vridd)[s]*)|(være|er|var|vært))$)")
    # rendhagyó igék        oki
    # ska kollas först
    adjre = re.compile(r"([a-zåøæ]*((ig|ig([te]|ste|st|ere))|(bar|bar(t|e))|(full|full([te]|e(re|st|ste)))|(sikker|sikkert|sikre|sikre(re|st|ste))|(ell|ell[te])|(sk|sk(t|e))|sjeld(en|ent|ne|nere|nest|neste)|([st]iv|[ts]iv[te])|(løs|løs[te])|(gammel|gammelt|gamle|eldre|eldst|eldste)|(lit(en|[ae])|smått|små|lille|vesle||mindre|minst)|(lang|lang[te]|leng(re|st|ste))|(som|som(t|me))|(ende)|(dt|dte)|annerledes|likendes|ringe|rosa|søndre|søre|umake|(øde)|(syk|syk([te]|ere|est|este))|(myk|myk([te]|ere|est|este))|(fri|fri(tt|e|ere|est|este))|(blakk|blak(t|ke|kere|kest|keste)|blå|blå(tt|e|ere|est|este)|brun|brun([te]|ere|est|este)|grå|grå(tt|e|ere|est|este)|grøn|grøn([nt]|ne|nere|nest|neste)|gul|gul([te]|ere|est|este)|hvit|hvit([te]|ere|est|este)|klar|klar([te]|ere|est|este)|lilla|l(jo|y)s|l(jo|y)s([te]|ere|est|este)|oran(g|sj)e|rød|rø(tt|de|dere|dest|deste)|svart|svart(e|ere|est|este)|turkis|turkis[te])|(dags|dagse)|(sen|sen([te]|ere|est|este)))$)")
    # melléknevek           oki
    advre = re.compile(r"((inatt|imorgen|idag|ikveld|ikke|mer|mest|fler|flere|flest|få|mere|mange|mye|meget|ofte|ofte(re|st|ste)|aldri|alltid|sjeldsynt|kan(skje|hende)|selve|sjølve|selveste)|[a-zåøæ]*(igens|igvis)$)")
    # határozószók          oki
    # ska kollas innan adjektiven
    pronomre = re.compile(r"((de[nt]|noen|noe|inge[nt]|[smd]eg|oss|dere|deres|de|dem|vi|[smd]i(n|tt|ne)|vår|vår[te]|hans|hennes|jeg|du|ha[nm]|hun|dens|dets|denne|dette|disse|dennes|dettes|disses|selv|sjøl)$)")
    # névmások              oki
    tallre = re.compile(r"([a-zåøæ]*(først|første|én|to|annen|annet|andre|anna|(tre|tredje|fire|fjerde|fem|femte|seks|sjette|syv|sjuende|åtte|åttende|(ni|ti)(ende)*|elleve|ellevte|tolv|tolvte|(tretten|fjorten|femten|seksten|sytten|atten|nitten)(de)*|tjue|tjue(en|ett|nde)|(tretti|førti|femti|seksti|sytti|åtti|nitti)(en|ett|et|ende)*|(hundre)(de)*|(tusen)(de)*|(million)(te)*|milliard(te)*)(del|delen|deler|delene)*|halvannen|halvannet|dobbel|dobbelt|doble)$)")
    # számnevek             oki
    # ska kollas innan adjektiven. "og en" & "og et" saknas men det får vara.
    core = re.compile(r"((og|eller|men|så|å|at|som|da)$)")
    # kötőszavak            oki
    interre = re.compile(r"((nei|ja|adjø|ah|aha|ai|akk|amen|au|basta|bjeff|bravo|bu|bø|eia|faen|fint|gratla|ha|hallo|he|hei|hi|hu|huff|hæ|jada|jaggu|jo|joda|klukk|knegg|konge|kvekk|kykeliky|mjau|morn|neida|nja|no|nøff|pass|puss|pytt|rassh[oø]l|rett|sikkert|særlig|takk|tja|uff|unnskyld|ve|velkommen|voff|æsj|beklager|hilsen|fett|greit|nydelig)$)")
    # interjekciók          oki
    prepre = re.compile(r"((ved|ad|att|attpå|av|bak|bortom|etter|for|foran|formedelst|fra|før|gjennom|hos|i|ifra|ifølge|igjennom|imot|innafor|innen|innenfor|inn|inni|istedenfor|mellom|mot|omkring|oppover|oppå|ovenfor|over|overfor|på|til|uansett|under|uten|utenfor|utenfra|van|yvi)$)")
    # prepozíciók           oki
    usikkerre = re.compile(r"([a-zåøæ]*(et|ets|te|skap|skap(e[rts]|e|ets|er|es|ere|erer)|fe|fer)$)")
    #                       oki

    for i in range(len(lista)):
        if lista[i] == "en":
            tall.addLast(lista[i])
            lista[i] = [lista[i], "tall"]   # Man förändrar elementet innanför listan
                                            # för bättre tidskomplexitet.
        elif lista[i] == "ei":
            tall.addLast(lista[i])
            lista[i] = [lista[i], "tall"]
        elif lista[i] == "er":
            verb.addLast(lista[i])
            lista[i] = [lista[i], "verb"]
        elif orevre.match(lista[i]):
            verb.addLast(lista[i])
            lista[i] = [lista[i], "verb"]
        elif core.match(lista[i]):
            konj.addLast(lista[i])
            lista[i] = [lista[i], "konj"]
        elif interre.match(lista[i]):
            inter.addLast(lista[i])
            lista[i] = [lista[i], "inter"]
        elif prepre.match(lista[i]):
            prepo.addLast(lista[i])
            lista[i] = [lista[i], "prepo"]
        elif pronomre.match(lista[i]):
            pron.addLast(lista[i])
            lista[i] = [lista[i], "pron"]
        elif adjre.match(lista[i]):
            adj.addLast(lista[i])
            lista[i] = [lista[i], "adj"]
        elif advre.match(lista[i]):
            adv.addLast(lista[i])
            lista[i] = [lista[i], "adv"]
        elif adjre.match(lista[i]):
            adj.addLast(lista[i])
            lista[i] = [lista[i], "adj"]
        elif subre.match(lista[i]):
            sub.addLast(lista[i])
            lista[i] = [lista[i], "sub"]
        elif verbre.match(lista[i]):
            verb.addLast(lista[i])
            lista[i] = [lista[i], "verb"]
        elif usikkerre.match(lista[i]):
            usikker.addLast([lista[i], i])
            lista[i] = [lista[i], i]
        else:
            resten.addLast(lista[i])
            lista[i] = [lista[i], "oklart"]
    n = usikker.size()
    usikre = usikker.getlist(n)
    if n>0:
        a = [""]*11
        for i in range(n):
            elem = usikre[i]
            a[5] = elem[1]
            if a[5] < 5:
                j = 0
                while a[5]-j > 0:
                    a[4-j] = lista[a[5]-j-1][1]
                    j += 1
                j = 0
                while (j <= 4 or a[5]+j <= len(lista)):
                    a[6+j] = lista[a[5]+j+1][1]
                    j +=1
            elif a[5] > len(lista)-5:
                j = 0
                while j <= 4:
                    a[4-j] = lista[a[5]-j-1][1]
                    j += 1
                j = 0
                while (j < 5 or len(lista) > a[5]+j):
                    a[6+j] = lista[a[5]+j+1][1]
                    j += 1
             else:
                j = 0
                while j <= 4:
                    a[4-j] = lista[a[5]-j-1][1]
                    j += 1
                j = 0
                while j <= 4:
                    a[6+j] = lista[a[5]+j+1][1]
                    j +=1
            if _syntax(a) == "sub":
                sub.addLast(lista[a[5]])
                lista[a[5]] = [lista[a[5]], "sub"]
            elif _syntax(a) == "verb":
                verb.addLast(lista[a[5]])
                lista[a[5]] = [lista[a[5]], "verb"]
            elif _syntax(a) == "adj":
                adj.addLast(lista[a[5]])
                lista[a[5]] = [lista[a[5]], "adj"]
            else:
                resten.addLast(lista[a[5]])
                lista[a[5]] = [lista[a[5]], "oklart"]
        usikker.clear()
