from googletrans import Translator


text1 = "subscribe my channel"

text2 = "suscríbete a mi canal"

text3 = "kanalıma abone ol"


translator = Translator()


print(translator.detect(text1))
print(translator.detect(text2))
print(translator.detect(text3))


text1 = "subscribe my channel"

text2 = "suscríbete a mi canal"

text3 = "kanalıma abone ol"



translator = Translator()


print("Translated From Spanish : ", translator.translate(text2))
print("Translated From Turkish : ", translator.translate(text3))


print("Translate English to ESP : ", translator.translate(text1, src='en', dest='es'))

print("Translate En to Tur : ", translator.translate(text1, src='en', dest='tr'))