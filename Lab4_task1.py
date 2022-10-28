def get_count_char(str_):
    slovar = {}
    text = str_.split()
    text = str_.lower()
    for word in text:
        for symbol in word:
            if (symbol.isalpha()):
                if symbol in slovar:
                    slovar[symbol] += 1
                else:
                    slovar[symbol] = 1

    return slovar


new_sentens = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(new_sentens))