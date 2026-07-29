# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:47:21 2026

@author: Yegane
"""

shopping = ["نان","شیر","تخم مرغ","برنج"]
print(shopping)
shopping.append("ماست")
shopping.remove("شیر")
print("تعداد کالاهای موجود در لیست: ",len(shopping))
if "برنج" in shopping:
    print("برنج در لیست وجود دارد")
else:
    print("برنج در لیست وجود ندارد")
shopping.sort()
product = input("کالایی که میخواهید حذف شود را وارد نمایید: ")
if product in shopping:
    shopping.remove(product)
    print("کالای موردنظر با موفقیت حذف شد")
else:
    print("کالای وارد شده در لیست موجود نیست")
