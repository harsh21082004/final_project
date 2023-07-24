from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    return translator.translate(english_text)

def frenchToEnglish(french_text):
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    translation = translator.translate(french_text)
    return translation