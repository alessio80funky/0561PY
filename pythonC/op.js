//比較演算子と論理演算子

let age = 20;
let score = 75;

console.log(age > 18);//true
console.log(score >= 80);//false

if(age > 18 || score >= 80){
    console.log("合格");
}else{
    console.log("不合格");
}

if(age < 18 && score < 70){
    console.log("未成年者で不合格");
}else{
    console.log("条件を満たしていません");
}