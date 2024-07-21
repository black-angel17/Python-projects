
import clipboard



from translate import Translator

def translate_to_tamil(word):
    translator = Translator(to_lang="ta")
    translation = translator.translate(word)
    return translation

checker = ''

while True:
    clipboard_text = clipboard.paste()
    if checker ==clipboard_text:
        continue
    else:

        word  = clipboard_text
        translated_word = translate_to_tamil(word)
        print( "Translated word in Tamil:", str(clipboard_text),"===", translated_word)
        checker = clipboard_text
        