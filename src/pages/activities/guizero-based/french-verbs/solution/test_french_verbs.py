from french_verbs import is_first_group_verb, conjugate


def test_is_first_group_verb():
    assert is_first_group_verb("manger") == True
    assert is_first_group_verb("aller") == False
    assert is_first_group_verb("finir") == False
    assert is_first_group_verb("parler") == True


def test_conjugate_present():
    assert conjugate("manger", "present") == [
        "je mange",
        "tu manges",
        "il,elle,on mange",
        "nous mangeons",
        "vous mangez",
        "ils,elles mangent"
    ]


def test_conjugate_imparfait():
    assert conjugate("manger", "imparfait") == [
        "je mangeais",
        "tu mangeais",
        "il,elle,on mangeait",
        "nous mangions",
        "vous mangiez",
        "ils,elles mangeaient"
    ]


def test_conjugate_future():
    assert conjugate("manger", "future") == [
        "je mangerai",
        "tu mangeras",
        "il,elle,on mangera",
        "nous mangerons",
        "vous mangerez",
        "ils,elles mangeront"
    ]


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
