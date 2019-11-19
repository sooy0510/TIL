// Object -> String
const jsonData = JSON.stringify({     // JSON -> String
  수연: '롤롤',
  선아: '스나',
})
console.log(jsonData)   //{"수연":"롤롤","선아":"스나"}
console.log(typeof jsonData) //string


// String -> Object
const parseData = JSON.parse(jsonData)
console.log(parseData)  //{"수연":"롤롤","선아":"스나"}
console.log(typeof parseData) //object


/* 
  [Object vs JSON 간단정리]
  - Object : JavaScript 의 Key-Value 페어의 자료구조
  - JSON : 데이터를 표현하기 위한 단순 문자열(string)
 */