# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 04:41:28 2026

@author: Yegane
"""

with open("text.txt","w",encoding="utf-8") as file:
    file.write("Python Programming")
with open("text.txt","r",encoding="utf-8") as file:
    count = 0
    ch = file.read(1)
    while ch != "":
        print(ch)
        count += 1
        ch = file.read(1)
print("تعداد کاراکترها: ",count)
