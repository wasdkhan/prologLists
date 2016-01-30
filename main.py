import re
problemNumber = int(raw_input('Enter Problem Number: '))
def listinput():
  input = raw_input('Enter your list: ')
  plist = []
  if input == 'def': 
    plist = ['a','b','c','d','e']
    print plist
    return plist
  else:
    elements = re.findall(r'[\w]+',input)
    for elem in elements: plist.append(elem)
    return plist
plist = listinput()
if problemNumber == 1:
  print plist[len(plist)-1]
if problemNumber == 2:
  print plist[len(plist)-2]
if problemNumber == 3:
  index = int(raw_input('Enter list element position: '))
  print plist[index-1]
if problemNumber == 4:
  print len(plist)
if problemNumber == 5:
  plist.reverse()
  print plist
if problemNumber == 6:
  newList = plist[:]
  newList.reverse()
  print plist == newList
  
