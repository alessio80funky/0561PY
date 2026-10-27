#try...except (try..exceptはJSのtry...catchと同じ意味)

#try:
  # age = int(input("年齢を入力してください: "))
   #print(f"あなたの年齢は{age}歳です。")
#except:#catchの代わりにexceptを使う
    #print("エラーが発生しました")

import json

try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    total = 0

    for item in data:
        total += item["price"] * item["quantity"]


except FileNotFoundError:
    print("エラー: data.jsonファイルが見つかりません。")

except json.JSONDecodeError:    
    print("エラー: data.jsonファイルの内容が正しくありません。")

except KeyError as e:
    print(f"エラー: データに必要なキーが存在しません。キー: {e}")

except TypeError as e:
    print(f"エラー: 価格または数量の型が正しくありません。詳細: {e}")

except IndentationError as e:
    print(f"エラー: インデントの問題があります。詳細: {e}")

else:
        print(f"合計金額: {total}円")
