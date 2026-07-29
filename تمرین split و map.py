# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 02:57:25 2026

@author: Yegane
"""

scores = []
for i in range(5):
    score = int(input("نمره را وارد کنید: "))
    scores.append(score)
print("لیست نمرات: ",scores)
print("مجموع نمرات: ",sum(scores))
print("میانگین نمرات: ",sum(scores)/len(scores))
print("بیشترین نمره: ",max(scores))
print("بیشترین نمره: ",min(scores))

print("----------------------------------- چالش -----------------------------------")
scores = list(map(int, input("نمرات را وارد کنید: ").split()))
print("لیست نمرات: ",scores)
print("مجموع نمرات: ",sum(scores))
print("میانگین نمرات: ",sum(scores)/len(scores))
print("بیشترین نمره: ",max(scores))
print("بیشترین نمره: ",min(scores))