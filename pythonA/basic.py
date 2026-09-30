#変数
name = "Alessio"
#出力のコマンド
print(name)
#pythonのテンプレート文字列
print(f"My name is {name}")

#pythonの巻子
def sayHello():
    print(name)
    
#関数の呼び出し
sayHello()

#pythonの引数と戻り値
def add(a, b):
    return a + b 

result = add(10, 5)

print(result)#15