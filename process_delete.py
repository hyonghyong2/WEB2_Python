#!C:\Python38\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
 
os.remove('data/'+pageId)
 
#Redirection
print("Location: ex_index.py")
print()