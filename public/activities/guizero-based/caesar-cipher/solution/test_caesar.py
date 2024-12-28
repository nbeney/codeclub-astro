from caesar import encode_caesar, decode_caesar


def test_encode_caesar():
    assert encode_caesar("hello", 3) == "khoor"
    assert encode_caesar("HELLO", 3) == "KHOOR"
    assert encode_caesar("world", 7) == "dvysk"
    assert encode_caesar("WORLD", 7) == "DVYSK"
    assert encode_caesar("hello, world!", 10) == "rovvy, gybvn!"
    assert encode_caesar("HELLO, WORLD!", 10) == "ROVVY, GYBVN!"


def test_decode_caesar():
    assert decode_caesar("khoor", 3) == "hello"
    assert decode_caesar("KHOOR", 3) == "HELLO"
    assert decode_caesar("dvysk", 7) == "world"
    assert decode_caesar("DVYSK", 7) == "WORLD"
    assert decode_caesar("rovvy, gybvn!", 10) == "hello, world!"
    assert decode_caesar("ROVVY, GYBVN!", 10) == "HELLO, WORLD!"


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
