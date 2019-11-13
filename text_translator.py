from googletrans import Translator
translator = Translator()
data = input('Enter the text : ')
lan = input('Enter the output language -> \n (For e.g. : hi : Hindi) ')
print('Original Text :',data)
x = translator.translate(data, dest=lan)
print('Language Detected :',x.src)
print('Translated Text :',x.text)
print('Done!!')
