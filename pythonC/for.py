#for

for i in range(5):
    print(i)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
#apple
#banana
#orange

#while

count = 0

while count < 5:
    print(count)
    count = count + 1 #インクリメント演算子の代わりに使える、ループの処理の最後に必ず書く必要があるでなければ無限ループが発生する

print("終了")