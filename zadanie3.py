dict = {'apple':'яблоко', 'red':'красный', 'cat':'кот', 'sky':'небо', 'laptop':'ноутбук'}
print('Весь словарь:')
for key in dict:
    print(key, dict[key])
print()

for i in dict.keys():
    c = i
print('Перевод последнего слова -',dict[c])
