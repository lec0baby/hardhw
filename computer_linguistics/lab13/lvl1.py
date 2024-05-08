import re
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
from collections import Counter

text = open('txt', 'r').read()
tokens = re.findall

#токенизация сплитом
print(text.split())

#токенизация при помощи регулярных выражений
print(tokens)

#токенизация при помощи NLTK
print(word_tokenize(file))

'''Токенизация сплитом является не совсем токенизацией, данный способ разбивает текст без учета пунктуации. Способ регулярных выражений и 
способ с использованием модуля nltk разбивают текст с учетом пунктуации и оставляет чистые слова.'''

#кол-во слов в тексте разными функциями
print(len(text))

print(Counter(text))

'''Результаты отличные, так как Counter подсчитывает кол-во разных символов в текста, также с учетом знаков препинания, и выдает это в формате словаря. 
Функия len считает кол-во всех символов в тексте и возвращает целое число.'''

#очистка при помощи isalpha
new_text = [i for i in text.split() if i.isalpha()]
print(new_text)

#очистка от стоп-слов
filtered_words = [word for word in text if word not in stopwords.text('english')]