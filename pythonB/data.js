//参照型のデータ型

//array(配列)

let fruits = ["りんご","バナナ","みかん"];

console.log(fruits[0]);
console.log(fruits[1]);

fruits.push("ぶどう");
fruits[1] = "メロン";//[ 'りんご', 'メロン', 'みかん', 'ぶどう' ]

console.log(fruits);//[ 'りんご', 'バナナ', 'みかん', 'ぶどう' ]


//object(オブジェクト)

let student = {
    name:"佐藤" ,
    age:20,
    score:85
};

console.log(student.name);//佐藤
console.log(student.score);//85

student.score = 90;
student.grade = "A";

console.log(student)//{ name: '佐藤', age: 20, score: 90, grade: 'A' }

console.log(student.score)// 90
console.log(student.grade)// A