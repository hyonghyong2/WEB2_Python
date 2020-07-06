import os, html_sanitizer
sanitizer=html_sanitizer.Sanitizer()

def getList(): 
  files = os.listdir('data')
  listStr = ''
  for item in files:
      item=sanitizer.sanitize(item)
      listStr = listStr + '<li><a href="ex_index.py?id={name}">{name}</a></li>'.format(name=item)
  return listStr