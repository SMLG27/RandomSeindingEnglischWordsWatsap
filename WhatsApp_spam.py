
import pyautogui
from nltk.corpus import words
import time
import random
import pyperclip


word_list = words.words()

def spammm(how_much):
    return_list = []
    for e in range(how_much):
        return_list.append(word_list[random.randint(1, 236736)])
    return convert(return_list)

def convert(wordd):
    text = ' '.join(wordd)
    if text is not None:
        return text
    else:
        return word_list[random.randint(1, 236736)]


def _workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')



if __name__ == '__main__':

    for e in range(2000):  # how many lines with words
        output_message = spammm(random.randint(1, 10))  # how many words in ole line
        for_output = str(output_message)
        pyautogui.write(for_output)
        # time.sleep(1)
        pyautogui.press('enter')



































































