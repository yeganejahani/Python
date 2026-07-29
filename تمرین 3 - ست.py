# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:36:57 2026

@author: Yegane
"""

group1 = {"علی","زهرا","محمد","رضا"}
group2 = {"محمد","رضا","سارا","نگار"}
print("group1 =",group1)
print("group2 = ",group2)
group1.add("امیر")
group1.remove("زهرا")
print("تعداد اعضای group1: ",len(group1))
if "محمد" in group1:
    print("محمد در group1 است")
else:
    print("محمد در group1 نیست")
print("اشتراک: ",group1.intersection(group2))
print("اجتماع: ",group1.union(group2))

print("----------------------------------- چالش -----------------------------------")
numbers = [5,8,3,8,2,5,10,3,7]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)