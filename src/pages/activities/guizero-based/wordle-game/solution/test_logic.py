from logic import compare_words, COLOR_CORRECT, COLOR_MISPLACED, COLOR_WRONG

CORR = COLOR_CORRECT
MISP = COLOR_MISPLACED
WRNG = COLOR_WRONG


def test_all_correct():
    assert compare_words("hello", "hello") == [CORR, CORR, CORR, CORR, CORR]


def test_all_misplaced():
    assert compare_words("abcde", "bcdea") == [MISP, MISP, MISP, MISP, MISP]


def test_all_wrong():
    assert compare_words("abcde", "fghij") == [WRNG, WRNG, WRNG, WRNG, WRNG]


def test_mixed_correct_wrong():
    assert compare_words("abcxx", "abcyy") == [CORR, CORR, CORR, WRNG, WRNG]


def test_mixed_misplaced_wrong_without_rep():
    assert compare_words("abxxx", "yyyab") == [MISP, MISP, WRNG, WRNG, WRNG]


def test_mixed_misplaced_wrong_with_rep():
    assert compare_words("ababx", "yyyab") == [MISP, MISP, WRNG, WRNG, WRNG]


def test_mixed_correct_misplaced_wrong_without_rep():
    assert compare_words("abxcc", "baxzz") == [MISP, MISP, CORR, WRNG, WRNG]


def test_mixed_correct_misplaced_wrong_with_rep():
    assert compare_words("abxab", "baxzz") == [MISP, MISP, CORR, WRNG, WRNG]


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
