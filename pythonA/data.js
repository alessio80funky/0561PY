//プリミティブ型

let name = "\"山田\" "//string  文字列
///注意点
//'山田" ー＞記述の間違い同じクォーテーションを使うな必ず
//"'山田'"/'"山田"' こちらの記述は可能 
//"\"山田\" "/'\'山田\'' OK エスケープシーケンス
//""山田"" / ''山田'' NG

let num = 10
let num2 = 10.5

let isStudent = true 
///注意点
//true/false  頭文字は小文字です

console.log(typeof(name))//string
console.log(typeof(num))//number
console.log(typeof(num2))//number
console.log(typeof(isStudent))//boolean