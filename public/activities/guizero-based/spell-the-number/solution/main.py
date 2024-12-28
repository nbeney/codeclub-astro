from guizero import *
from resources import path_for
import pyttsx3

IMAGE_LOGO = path_for("logo.png")
IMAGE_VOICE = path_for("voice-command.png")


def number_up_to_999_to_words(number):
    ONES = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    TENS = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if number < 10:
        return ONES[number]
    elif number < 20:
        return TEENS[number - 10]
    elif number < 100:
        return TENS[number // 10] + "-" + ONES[number % 10] if number % 10 != 0 else TENS[number // 10]
    else:
        return ONES[number // 100] + " hundred " + number_up_to_999_to_words(number % 100) if number % 100 != 0 else ONES[number // 100] + " hundred"


def number_to_words(number_str):
    GROUPS = [
        "", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion",
        "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion",
        "septendecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion", "duovigintillion", "trevigintillion",
        "quattuorvigintillion", "quinvigintillion", "sexvigintillion", "septenvigintillion", "octovigintillion", "novemvigintillion",
        "trigintillion", "untrigintillion", "duotrigintillion", "tretrigintillion", "quattuortrigintillion", "quintrigintillion",
        "sextrigintillion", "septentrigintillion", "octotrigintillion", "novemtrigintillion", "quadragintillion", "unquadragintillion",
        "duoquadragintillion", "trequadragintillion", "quattuorquadragintillion", "quinquadragintillion", "sexquadragintillion",
        "septenquadragintillion", "octoquadragintillion", "novemquadragintillion", "quinquagintillion", "unquinquagintillion",
        "duoquinquagintillion", "trequinquagintillion", "quattuorquinquagintillion", "quinquinquagintillion", "sexquinquagintillion",
        "septenquinquagintillion", "octoquinquagintillion", "novemquinquagintillion", "sexagintillion", "unsexagintillion",
        "duosexagintillion", "tresexagintillion", "quattuorsexagintillion", "quinsexagintillion", "sexsexagintillion",
        "septensexagintillion", "octosexagintillion", "novemsexagintillion", "septuagintillion", "unseptuagintillion",
        "duoseptuagintillion", "treseptuagintillion", "quattuorseptuagintillion", "quinseptuagintillion", "sexseptuagintillion",
        "septenseptuagintillion", "octoseptuagintillion", "novemseptuagintillion", "octogintillion", "unoctogintillion",
        "duooctogintillion", "treoctogintillion", "quattuoroctogintillion", "quinoctogintillion", "sexoctogintillion",
        "septenoctogintillion", "octooctogintillion", "novemoctogintillion", "nonagintillion", "unnonagintillion", "duononagintillion",
        "trenonagintillion", "quattuornonagintillion", "quinnonagintillion", "sexnonagintillion", "septennonagintillion",
        "octononagintillion", "novemnonagintillion", "centillion"
    ]

    # Strip commas, underscores and spaces.
    number_clean = number_str.strip()
    number_clean = number_clean.replace(",", "")
    number_clean = number_clean.replace("_", "")
    number_clean = number_clean.replace(" ", "")

    if not number_clean.isdigit():
        return "Invalid input"

    if number_clean == "0":
        return "zero"

    # Split number into groups of 3 digits.
    groups = []
    while number_clean:
        groups.append(number_clean[-3:])
        number_clean = number_clean[:-3]

    if len(groups) > len(GROUPS):
        return "Number too large"

    result = []
    for idx, group in enumerate(groups):
        if group == "000":
            continue
        words = number_up_to_999_to_words(int(group))
        if idx == 0:
            result.append(words)
        else:
            result.append(words + " " + GROUPS[idx])
    result.reverse()

    match len(result):
        case 1:
            return result[0]
        case 2:
            return " and ".join(result)
        case _:
            return ", ".join(result[:-1]) + " and " + result[-1]


def on_change():
    output_text.value = number_to_words(input_text.value)


def on_voice():
    pyttsx3.speak(output_text.value)


if __name__ == "__main__":
    app = App(title="Spell the Number", width=600, height=700)

    Picture(app, align="top", image=IMAGE_LOGO, width=600, height=250)

    Text(app)  # spacer

    box = Box(app, width="fill")

    Text(box, align="right", text="  ")  # spacer

    PushButton(
        box, align="right", text="", image=IMAGE_VOICE, command=on_voice
    )

    Text(box, align="right", text="")  # spacer

    input_text = TextBox(
        box, align="right", text="1,234,456,789", width="fill", height=3,
        multiline=True, scrollbar=True, command=on_change
    )
    input_text.text_size = 20

    Text(app)  # spacer

    output_text = TextBox(
        app, text="", width="fill", height="fill",
        multiline=True, scrollbar=True, enabled=False
    )
    output_text.text_size = 20

    on_change()

    app.display()
