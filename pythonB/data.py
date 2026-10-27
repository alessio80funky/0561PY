#参照型のデータ型

#list(配列)
#             0       1       2
fruits = ["りんご","バナナ","みかん"]

print(fruits[0])
print(fruits[1])

fruits.append("ぶどう")
fruits[1] = "メロン"#['りんご', 'メロン', 'みかん', 'ぶどう']

print(fruits)#['りんご', 'バナナ', 'みかん', 'ぶどう']


#dict(辞書型)

student = {
    "name":"佐藤",
    "age": 20,
    "score":85
}

print(student["name"])#佐藤
print(student["score"])#85

student["score"] = 90#'score': 90
student["grade"] = "A"#'grade': 'A'

print(student)#{'name': '佐藤', 'age': 20, 'score': 90, 'grade': 'A'}

print(student["score"])# 90
print(student["grade"])# A

#tuple（タプル）
#要素を変更せずに扱いたいときに使います　＝＞座標、画像のサイズ、色

colors = ("赤","黄色","青")

print(colors[0])# 赤
print(colors[1])# 黄色


data = [("a","b"), ("c","d")] #リストの中にタプルを入れることもあります


#エラー

#colors[0] = "緑"

#Traceback (most recent call last):
  #File "C:\Users\kazuo\OneDrive\デスクトップ\0561PY\pythonB\data.py",line 42, in <module>
    #colors[0] = "緑"
    #~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment