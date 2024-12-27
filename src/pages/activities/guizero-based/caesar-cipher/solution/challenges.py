_EASY = """L'p nqrzq lq d zruog ri vshoov dqg eurrpv,
Zkhuh Krjzduwv lv d sodfh ri klgghq urrpv.
Dq ruskdqhg erb zlwk d oljkwqlqj vfdu,
L'p wkh zlcdug ghvwlqhg wr jr idu.
Zlwk iulhqgv olnh Khuplrqh dqg Urq eb pb vlgh,
Zh idfhg gdun irufhv dqg wkh ulvlqj wlgh.
Zkr dp L, zlwk d ghvwlqb judqg,
Lq d vhulhv ri errnv, d ehoryhg eudqg?

VFUROO WR ERWWRP IRU WKH DQVZHU.










DQVZHU: Kduub Srwwhu"""

_MEDIUM = """TY ESP CPLWX ZQ ACZRCLXXTYR T LX CPYZHYPO
L WLYRFLRP GPCDLETWP HSPCP DZWFETZYD LCP QZFYO
YLXPO LQEPC L DYLVP MFE YZE ZYP ESLE STDDPD
XJ DJYELI TD NWPLY YZ NFCWJ MCLNPD ZC XTDDPD
TYOPYELETZY TD XJ VPJ TY L HZCWO ZQ NZOP
HTES WTMCLCTPD RLWZCP EZ XLVP ACZRCLXD PIAWZOP
HSLE LX T HTES L NZXXFYTEJ GLDE
L DNCTAETYR WLYRFLRP ESLE TD DFCP EZ WLDE

DNCZWW EZ MZEEZX QZC ESP LYDHPC










LYDHPC: AJESZY"""

_HARD = """FJXMR WWIBL CPBZO BQPEF AABKC OLJPF DEQFK QEBTL OIALC PBZOB QPFYO
FKDQE BIFDE QTFQE HBVPX KAZFM EBOPF QTFPQ XKAQR OKVLR OJBPP XDBPP
XCBKL KBBAQ LAFPZ BOKZO XZHFK DJVZL ABPXK BKFDJ XQFZX OQFDR XOAVL
ROAXQ XPLZI LPBQL QEBEB XOQTE XQXJF FKQEB OBXIJ LCQEB RKHKL TKMOL
QBZQF KDVLR OPBZO BQPIF HBXDR XOAFX KPQLK BUUUU"""

_CHALLENGES_LIST = [
    ("Easy", _EASY),
    ("Medium", _MEDIUM),
    ("Hard", _HARD),
]

_CHALLENGES_DICT = {name: ciphertext for name, ciphertext in _CHALLENGES_LIST}


def names():
    return [name for name, ciphertext in _CHALLENGES_LIST]


def ciphertext_for(name):
    return _CHALLENGES_DICT[name]
