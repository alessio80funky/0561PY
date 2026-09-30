#プリミティブ型

name = '山田' #str  文字列 
#注意点：
#'山田" ー＞記述の間違い同じクォーテーションを使うな必ず
#"'山田'"/'"山田"' こちらの記述は可能
#//"\"山田\" "/'\'山田\'' OK   エスケープシーケンス使えます
#//""山田"" / ''山田'' NG

age = 18 #整数型　int (integer)
height = 181.5 #少数型 float
#注意点：数値が二つ

is_student = True #真偽値型　bool (boolean)
#注意点：
#True/False  は頭文字は大文字です

print(type(name))#<class 'str'>
print(type(age))#<class 'int'>
print(type(height))#<class 'float'>
print(type(is_student))#<class 'bool'>
