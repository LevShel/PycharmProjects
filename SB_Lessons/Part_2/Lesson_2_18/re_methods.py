import re  # Regular Expressions == регулярные выражения

text = 'AV - Analytics Vidhya AV'
text_2 = 'AV is largest Analytics community of India. India!'

print('=' * 40, '\n re.match')
result = re.match(r'AV', text)  # поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону:', result)
print(result.group(0))
print(result.start())
print(result.end())

result = re.match(r'Analytics', text)
print('Поиск в начале строки по шаблону:', result)

print('=' * 40, '\n re.search')
result = re.search(r'Analytics', text)  # поиск в строке по шаблону
print('Поиск в строке по шаблону:', result)
print(result.group(0))

print('=' * 40, '\n re.findall')
result = re.findall(r'AV', text)  # все совпадения по шаблону
print('Все совпадения по шаблону:', result)
result = re.findall(r'\b[aeiouAEIOU]\w+', text_2)  # все слова, начинающиеся с гласной
print('Все слова, начинающиеся с гласной:', result)

print('=' * 40, '\n re.sub')
result = re.sub(r'India', 'the World', text_2) # замена всех найденных шаблонов
print('Замена всех найденных шаблонов:', result)

print('=' * 40, '\n re.compile')
pattern = re.compile('AV')
result = pattern.findall(text)
print(result)
result_2 = pattern.findall(text_2)
print(result_2)

