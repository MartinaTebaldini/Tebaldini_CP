from googletrans import Translator
translator = Translator()
word = True
while word != "nothing":
  word = input("gimme a word or phrase ")
  langaugeis = translator.translate(word, dest = "it")
  print(langaugeis)
