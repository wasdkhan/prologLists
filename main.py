import re
problemNumber = int(raw_input('Enter Problem Number: '))
if problemNumber == 1:
  input = raw_input('Enter your list: ')
  elements = re.findall(r'[\w]+',input)
  list = []
  for elem in elements: list.append(elem)
  print list[len(list)-1]
