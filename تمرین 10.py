# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 03:56:02 2026

@author: Yegane
"""

with open("students.txt","w",encoding="utf-8") as file:
    file.write("علی \n")
    file.write("زهرا \n")
    file.write("محمد \n")
with open("students.txt","r",encoding="utf-8") as file:
    data = file.read()
    print(data)
with open("students.txt","a",encoding="utf-8") as file:
    file.write(input("نام را وارد کنید:"))
with open("students.txt","r",encoding="utf-8") as file:
    data = file.read()
    print(data)
with open("students.txt","r",encoding="utf-8") as file:
    i = 1
    for name in file:
        print(i,"-",name)
        i += 1