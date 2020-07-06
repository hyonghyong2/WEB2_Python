#!C:\Python38\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value
 
opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()
 
os.rename('data/'+pageId, 'data/'+title)
 
#Redirection
print("Location: ex_index.py?id="+title)
print()