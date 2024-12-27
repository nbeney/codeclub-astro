from guizero import *
from resources import path_for
from french_verbs import TENSES, is_first_group_verb, conjugate

IMAGE_LOGO = path_for("logo.png")


def on_change():
    verb = textbox_verb.value.lower()
    tense = combo_tense.value.lower()

    ok = is_first_group_verb(verb)

    textbox_verb.bg = "white" if ok else "pink"

    text_result.visible = ok
    if ok:
        text_result.value = "\n".join(conjugate(verb, tense))


if __name__ == "__main__":
    app = App(title="French Verbs", width=600, height=400)

    Picture(app, image=IMAGE_LOGO)

    Text(app, text="")  # spacer

    toolbar = Box(app)

    Text(toolbar, align="left", size=18, text="Verb (1st group):")
    textbox_verb = TextBox(toolbar, align="left",
                           text="manger", command=on_change)
    textbox_verb.text_size = 18

    Text(toolbar, align="left", size=18, text="Tense:")
    combo_tense = Combo(toolbar, align="left",
                        options=TENSES, command=on_change)
    combo_tense.text_size = 18

    Text(app, text="")  # spacer

    text_result = Text(app, size=18)

    on_change()

    app.display()
