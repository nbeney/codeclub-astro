from main import number_to_words, number_up_to_999_to_words


def test_zero():
    assert number_to_words("0") == "zero"


def test_positive():
    assert number_to_words('1') == 'one'
    assert number_to_words('12') == 'twelve'
    assert number_to_words('123') == 'one hundred twenty-three'
    assert number_to_words(
        '1234') == 'one thousand and two hundred thirty-four'
    assert number_to_words(
        '12345') == 'twelve thousand and three hundred forty-five'
    assert number_to_words(
        '123456') == 'one hundred twenty-three thousand and four hundred fifty-six'
    assert number_to_words(
        '1234567') == 'one million, two hundred thirty-four thousand and five hundred sixty-seven'
    assert number_to_words(
        '12345678') == 'twelve million, three hundred forty-five thousand and six hundred seventy-eight'
    assert number_to_words(
        '123456789') == 'one hundred twenty-three million, four hundred fifty-six thousand and seven hundred eighty-nine'
    assert number_to_words(
        '1234567890') == 'one billion, two hundred thirty-four million, five hundred sixty-seven thousand and eight hundred ninety'
    assert number_to_words(
        '12345678901') == 'twelve billion, three hundred forty-five million, six hundred seventy-eight thousand and nine hundred one'
    assert number_to_words(
        '123456789012') == 'one hundred twenty-three billion, four hundred fifty-six million, seven hundred eighty-nine thousand and twelve'
    assert number_to_words(
        '1234567890123') == 'one trillion, two hundred thirty-four billion, five hundred sixty-seven million, eight hundred ninety thousand and one hundred twenty-three'
    assert number_to_words(
        '12345678901234') == 'twelve trillion, three hundred forty-five billion, six hundred seventy-eight million, nine hundred one thousand and two hundred thirty-four'
    assert number_to_words(
        '123456789012345') == 'one hundred twenty-three trillion, four hundred fifty-six billion, seven hundred eighty-nine million, twelve thousand and three hundred forty-five'
    assert number_to_words(
        '1234567890123456') == 'one quadrillion, two hundred thirty-four trillion, five hundred sixty-seven billion, eight hundred ninety million, one hundred twenty-three thousand and four hundred fifty-six'
    assert number_to_words(
        '12345678901234567') == 'twelve quadrillion, three hundred forty-five trillion, six hundred seventy-eight billion, nine hundred one million, two hundred thirty-four thousand and five hundred sixty-seven'
    assert number_to_words(
        '123456789012345678') == 'one hundred twenty-three quadrillion, four hundred fifty-six trillion, seven hundred eighty-nine billion, twelve million, three hundred forty-five thousand and six hundred seventy-eight'
    assert number_to_words('1234567890123456789') == 'one quintillion, two hundred thirty-four quadrillion, five hundred sixty-seven trillion, eight hundred ninety billion, one hundred twenty-three million, four hundred fifty-six thousand and seven hundred eighty-nine'


def test_small_zero():
    assert number_up_to_999_to_words(0) == "zero"


def test_small_single_digit():
    assert number_up_to_999_to_words(5) == "five"


def test_small_two_digits():
    assert number_up_to_999_to_words(10) == "ten"
    assert number_up_to_999_to_words(19) == "nineteen"
    assert number_up_to_999_to_words(23) == "twenty-three"


def test_small_three_digits():
    assert number_up_to_999_to_words(100) == "one hundred"
    assert number_up_to_999_to_words(123) == "one hundred twenty-three"
    assert number_up_to_999_to_words(999) == "nine hundred ninety-nine"


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
