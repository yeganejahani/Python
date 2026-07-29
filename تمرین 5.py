# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 02:23:15 2026

@author: Yegane
"""

library = {
    "books":[
        ("Python","Ahmadi",2023),
        ("Network+","Karimi",2022),
        ("Python","Ahmadi",2023)
    ],
    "subjects":{"Python","Network","Programming"}
    }
print("تعداد کتاب‌های موجود در books: ",len(library["books"]))
print("عنوان اولین کتاب:",library["books"][0][0])
library["books"].append(("Linux","Rahimi",2024))
library["subjects"].add("Security")
print("تعداد موضوع‌های موجود: ",len(library["subjects"]))
for i in library["books"]:
    print("عنوان",":",i[0])
    print("نویسنده",":",i[1])
    print("سال",":",i[2])
for i in library["subjects"]:
    print(i)
if "Python" in library["subjects"]:
    print("موضوع Python در مجموعه وجود دارد")
else:
    print("موضوع Python در مجموعه وجود ندارد")
print(library)

print("----------------------------------- چالش -----------------------------------")
library.update({"manager":"Ali Ahmadi"})
print(library)