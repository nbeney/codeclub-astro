from guizero import *
from resources import path_for
from caesar import encode_caesar, decode_caesar, NUM_LETTERS
import challenges

IMAGE_TOP_SECRET = path_for("top-secret.png")


def on_change_plaintext():
    global mode
    mode = on_change_plaintext

    plaintext = textbox_plaintext.value
    key = int(combo_key.value)
    textbox_ciphertext.value = encode_caesar(plaintext, key)


def on_change_key():
    global mode
    mode()


def on_change_challenge():
    global mode
    mode = on_change_ciphertext

    name = combo_challenges.value
    ciphertext = challenges.ciphertext_for(name)

    textbox_plaintext.value = ""
    textbox_ciphertext.value = ciphertext
    combo_key.value = "1"


def on_change_ciphertext():
    global mode
    mode = on_change_ciphertext

    ciphertext = textbox_ciphertext.value
    key = int(combo_key.value)
    textbox_plaintext.value = decode_caesar(ciphertext, key)


if __name__ == "__main__":
    app = App(title="Caesar Cipher", width=700, height=700)

    Text(app, text="")  # spacer

    Picture(app, image=IMAGE_TOP_SECRET, width=440, height=97)

    Text(app, text="")  # spacer

    Text(app, text="Plaintext", size=18)
    textbox_plaintext = TextBox(
        app, multiline=True, width="fill", height=8, command=on_change_plaintext)

    Text(app, text="")  # spacer

    Text(app, text="Key", size=18)
    keys = list(range(1, NUM_LETTERS))
    combo_key = Combo(app, options=keys, command=on_change_key)

    Text(app, text="")  # spacer

    Text(app, text="Ciphertext", size=18)
    textbox_ciphertext = TextBox(
        app, multiline=True, width="fill", height=8, command=on_change_ciphertext)

    Text(app, text="")  # spacer

    Text(app, text="Challenges", size=18)
    combo_challenges = Combo(
        app, options=challenges.names(), command=on_change_challenge)

    textbox_plaintext.value = "Type your secret message here...\nThe encrypted message will appear hereunder."
    on_change_plaintext()

    app.display()
