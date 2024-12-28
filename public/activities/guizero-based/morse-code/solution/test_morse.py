from morse import text_to_morse, morse_to_text


def check(text):
    assert morse_to_text(text_to_morse(text)) == text


def test_character():
    check("A")
    check(".")
    check("?")


def test_word():
    check("HELLO")


def test_sentence():
    check("HELLO WORLD!")


def test_multiline():
    check("HELLO WORLD!\nWHAT'S UP?")


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
