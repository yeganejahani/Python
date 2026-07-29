# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:55:29 2026

@author: Yegane
"""

book = {
        "title":"Python",
        "author":"Ahmadi",
        "publisher":"Danesh",
        "year":2024,
        "pages":350
        }
print(book)
print("نام کتاب: ",book["title"])
print("تعداد کلیدها: ",len(book))
book.update({"year":2025})
book["price"] = 450000
del book["publisher"]
print("کلیدها: ",book.keys())
print("مقادیر: ",book.values())
for i in book:
    print(i,":",book[i])

print("----------------------------------- چالش -----------------------------------")
student = {
    "نام":input("نام خود را وارد کنید:"),
    "نام خانوادگی":input("نام خانوادگی خود را وارد کنید:"),
    "سن ":int(input("سن خود را وارد کنید:")),
    "رشته":input("رشته خود را وارد کنید:"),
    "معدل":float(input("معدل خود را وارد کنید:")),
    }
for info in student:
    print(info,":",student[info])
