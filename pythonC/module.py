#import math

#print(math.pi) #3.141592653589793

from math import pi

print(pi) #3.141592653589793


import datetime as d

print(d.datetime.now()) #現在の日時を出力
print(d.date.today()) #現在の日付を出力

import random

print(random.randint(1, 10)) #1から10までのランダムな整数を出力
print(random.random()) #0.0から1.0までのランダムな浮動小数点数を出力
print(random.uniform(1.0, 10.0)) #1.0から10.0までのランダムな浮動小数点数を出力

from mod import keisan as k

print(k(5)) #10

