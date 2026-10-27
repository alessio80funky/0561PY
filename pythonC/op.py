#比較演算子と論理演算子

age = 18
score = 69

print(age > 18)#True
print(score >= 80)#False

if age >= 18 or score >= 70:
    print("合格")
else:
    print("不合格")

if age < 18 and score < 70:
    print("未成年者で不合格")
else:
    print("条件を満たしていません")
