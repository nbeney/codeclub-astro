# Define dictionary for letter-to-Morse mappings.
LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
  }

# Define dictionary for Morse-to-letter mappings.
MORSE_TO_LETTER = {v: k for k, v in LETTER_TO_MORSE.items()}

MORSE_WORD_SEP = '/'

def text_to_morse(text):
    text = text.upper()
    text_lines = text.split('\n')
    morse_lines = [_text_to_morse_line(line) for line in text_lines]
    return '\n'.join(morse_lines)

def _text_to_morse_line(text_line):
    text_words = text_line.split(' ')
    morse_words = [_text_to_morse_word(word) for word in text_words]
    return MORSE_WORD_SEP.join(morse_words)
    
def _text_to_morse_word(text_word):
    return ' '.join([LETTER_TO_MORSE[c] for c in text_word if c in LETTER_TO_MORSE])

def morse_to_text(morse):
    morse_lines = morse.split('\n')
    text_lines = [_morse_to_text_line(line) for line in morse_lines]
    return '\n'.join(text_lines)

def _morse_to_text_line(morse_line):
    morse_words = morse_line.split(MORSE_WORD_SEP)
    text_words = [_morse_to_text_word(word) for word in morse_words]
    return ' '.join(text_words)

def _morse_to_text_word(morse_word):
    morse_chars = morse_word.split(' ')
    return ''.join([MORSE_TO_LETTER[word] if word in MORSE_TO_LETTER else ' ' for word in morse_chars])
