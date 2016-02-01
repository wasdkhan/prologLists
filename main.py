import re

problemNumber = int(raw_input('Enter Problem Number: '))

def listinput():
  input = raw_input('Enter your list: ')
  plist = []
  if input == 'def': 
    plist = ['a','b','c','d','e']
  elif input == 'nest':
    plist = ['a', ['b', ['c', 'd'], 'e']]
  elif input == 'peat':
    plist = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
  else:
    elements = re.findall(r'\w+',input)
    for elem in elements: plist.append(elem)
  print plist
  return plist

plist = listinput()

def collapse(clist):
  nlist = []
  for elem in clist:
    if type(elem) is list:
      nlist.extend(collapse(elem))
    else:
      nlist.append(elem)
  return nlist

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
  nlist = plist[:]
  nlist.reverse()
  print plist == nlist

if problemNumber == 7:
  print collapse(plist)    

if problemNumber == 8:
  last = plist[0]
  nlist = [last]
  for i in range(len(plist)):
    curr = plist[i]
    if curr != last: nlist.append(curr)
    last = plist[i]
  print nlist

if problemNumber == 9:
  last = plist[0]
  currlist = []
  nlist = []
  for i in range(len(plist)):
    curr = plist[i]
    if curr == last:
      currlist.append(curr)
    else:
      nlist.append(currlist)
      currlist = [curr]
    last = plist[i]
  nlist.append(currlist)
  print nlist

if problemNumber == 14:
  nlist = []
  for elem in plist:
    nlist.extend([elem,elem])
  print nlist
