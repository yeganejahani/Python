# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 03:16:30 2026

@author: Yegane
"""

scores = [12,18,9,20,15,7,19,14]
passed = list(filter(lambda x: x >= 10, scores))
print("نمرات قبولی: ",passed)
print("تعداد قبول‌شدگان: ",len(passed))

print("----------------------------------- چالش -----------------------------------")
numbers = [5,8,11,14,17,20,23]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)