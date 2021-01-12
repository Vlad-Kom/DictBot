from googletrans import Translator
from utils.db_api.sqlite import Database
import re

translator = Translator()

def check_word(word):
    lst = word.split()
    for word in lst:
        if not word.isalpha():
            return False
    word = " ".join(lst)
    return word


def has_cyrillic(text):
    for sym in text:
        if not bool(re.search(r'[а-яА-ЯёЁ ]', sym)):
            return False
    return True


def has_latin(text):
    for sym in text:
        if not bool(re.search(r'[a-zA-Z ]', sym)):
            return False
    return True


def translate_word(id_user, word):
    # translator = Translator()
    result = check_word(word)
    if not result:
        return 0

    if len(result.split()) > 3:
        return 1

    if has_latin(result):
        result = translator.translate(result, src="en", dest="ru")
    elif has_cyrillic(result):
        result = translator.translate(result, src="ru", dest="en")
    else:
        return 2

    if (result.extra_data['all-translations'] is None):
        return 2
    str = []
    str2 = [result.text.lower()]
    for lst in result.extra_data['all-translations']:
        str.append("\n" + translator.translate(lst[0], dest='ru').text + ":")
        for wrd in lst[1][:2]:
            if not wrd == result.text.lower():
                str2.append(wrd)
        str.append(', '.join(str2))
        str2 = []

    db = Database()
    if db.check_word(id=id_user, word=word) is None:
        db.add_word(id=id_user, word=word, lang=result.src)
    else:
        db.zero_value_word(id=id_user, word=word)
    return ' '.join(str)


def game_translate_word(word):
    # translator = Translator()
    if has_latin(word):
        word = translator.translate(word, src="en", dest="ru")
    elif has_cyrillic(word):
        word = translator.translate(word, src="ru", dest="en")
    str = []
    str2 = [word.text.lower()]
    for lst in word.extra_data['all-translations']:
        str.append("\n" + translator.translate(lst[0], dest='ru').text + ":")
        for wrd in lst[1][:2]:
            if not wrd == word.text.lower():
                str2.append(wrd)
        str.append(', '.join(str2))
        str2 = []

    return ' '.join(str)
