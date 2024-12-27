TENSES = ["Present", "Imparfait", "Future"]


def is_first_group_verb(verb):
    if verb in ["aller"]:
        return False
    else:
        return verb.endswith("er")


def conjugate(verb, tense):
    match tense:
        case "present":
            base = verb[:-2]
            return [
                combine("je", base, "e"),
                combine("tu", base, "es"),
                combine("il,elle,on", base, "e"),
                combine("nous", base, "ons"),
                combine("vous", base, "ez"),
                combine("ils,elles", base, "ent"),
            ]
        case "imparfait":
            base = verb[:-2]
            return [
                combine("je", base, "ais"),
                combine("tu", base, "ais"),
                combine("il,elle,on", base, "ait"),
                combine("nous", base, "ions"),
                combine("vous", base, "iez"),
                combine("ils,elles", base, "aient"),
            ]
        case "future":
            return [
                combine("je", verb, "ai"),
                combine("tu", verb, "as"),
                combine("il,elle,on", verb, "a"),
                combine("nous", verb, "ons"),
                combine("vous", verb, "ez"),
                combine("ils,elles", verb, "ont"),
            ]
        case _:
            return [f"{tense.capitalize()} is not yet supported!"]


def combine(subject, base, suffix):
    if subject == "je" and base[0] in "aeiou":
        subject_adjusted = "j'"
    else:
        subject_adjusted = subject

    if subject_adjusted == "j'":
        space = ""
    else:
        space = " "

    if base[-1] == "g" and suffix[0] in "ao":
        suffix_adjusted = "e" + suffix
    else:
        suffix_adjusted = suffix

    return subject_adjusted + space + base + suffix_adjusted
