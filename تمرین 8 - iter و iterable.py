# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 03:39:25 2026

@author: Yegane
"""

students = ["علی","زهرا","محمد","رضا"]
it = iter(students)
print(next(it))
print(next(it))
print(next(it))

print("تمام اعضا: ")
for i in students:
    print(i)

print("""
      تفاوت for با next:
          بجای اینکه یکی یکی برای چاپ اعضای لیست next بزنیم
          از for استفاده میکنیم که خودش این کار رو برای ما انجام میده
          """)

print("----------------------------------- چالش -----------------------------------")
students = ["علی","زهرا","محمد","رضا"]
it = iter(students)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("""
      خطای StopIteration میده
      چون لیست تموم شده
      """)