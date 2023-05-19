from translate import Translator

translator = Translator(to_lang="es") #set the target language to Spanish
translation = translator.translate("hello. i am a test. this is not the full thing") #the text you want to translate
print(translation)
