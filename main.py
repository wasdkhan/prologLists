import re
problemNumber = int(raw_input('Enter Problem Number: '))
def listinput():
  input = raw_input('Enter your list: ')
  list = []
  if input == 'def': 
    list = ['a','b','c','d','e']
    print list
    return list
  else:
    elements = re.findall(r'[\w]+',input)
    for elem in elements: list.append(elem)
    return list
list = listinput()
if problemNumber == 1:
  print list[len(list)-1]
if problemNumber == 2:
  print list[len(list)-2]
if problemNumber == 3:
  index = int(raw_input('Enter list element position: '))
  print list[index-1]
if problemNumber == 4:
  print len(list)
if problemNumber == 5:
  list.reverse()
  print list
