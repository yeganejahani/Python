# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:04:31 2026

@author: Yegane
"""

students = ("رضا","علی","محمد","زهرا","علی")
print(students)
print("تعداد اعضا: ",len(students))
print("سومین دانش‌آموز: ",students[2])
print("تعداد تکرار نام علی: ",students.count("علی"))
print("اندیس نام رضا: ",students.index("رضا"))
print("دو عضو اول: ",students[0:2])
for names in students:
    print(names)
students_list = list(students)
students_list.append("سارا")
name = input("نام را وارد کنید: ")
if name in students_list:
    print("اندیس نام وارد شده: ",students_list.index(name))
else:
    students_list.append(name)