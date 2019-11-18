// 선언식
// 코드가 실행되기 전에 로드됨
// console.log(add(3,2))
// function add(num1, num2){
//   return num1 + num2
// }

// console.log(add(1,2))

// //console.log(sub(3,2))

// // 표현식(변수에 담는것)
// const sub = function(num1, num2){
//   return num1 = num2
// }
// console.log(sub(2,1))

// // 타입 확인하면 둘 다 function 으로 동일!
// // 작동 방법만 다름
// console.log(typeof add)
// console.log(typeof sub)


// 화살표 함수(Arrow function)
// const iot1 = function(name){
//   return `hello! ${name}!!`
// }
// console.log(iot1("수연"))

// // 1. function 키워드 삭제
// const iot1 = (name) => { return `hello! ${name}` }
// console.log(iot1("수연"))

// // 2. ()생략 (함수 매개변수 하나일 경우)
// const iot1 = name => { return `hello! ${name}` }
// console.log(iot1("수연"))

// // 3, {}, return 생략(바디에 표현식 1개)
// const iot1 = name => `hello! ${name}`
// console.log(iot1("수연"))

// [실습] 3단계에 걸쳐 화살표 함수로 바꿔보기
// let square = function(num){
// 	return num ** 2
// }
// console.log(square(3))

// 1. function 키워드 생략
// square = (num) => { return num ** 2}
// console.log(square(2))

// // 2. ()생략 (매개변수 1개)
// square = num => { return num ** 2}

// // 3. {}, return 생략(바디 부분 표현식 1개)
// square = num => num ** 2


// // 인자가 없는경우 ()혹은 _ 로 표시 가능!
// 원하는 로직있을 때 사용 ex) 버튼 클릭
// let noArgs = () => 'No args!!'
// noArgs = _ => 'No args!!'
// console.log(noArgs())

// 5-1. object를 return을 명시적으로 적어준다
// let returnObject = () => { return {key: 'value'} }
// console.log(returnObject)
// console.log(returnObject())
// console.log(typeof returnObject())

// 5-2. return을 적지 않으려면 괄호 붙이기
// let returnObject = () => ({key:'value'})
// console.log(returnObject)
// console.log(returnObject())
// console.log(typeof returnObject())


// // 6. 기본 인자 부여하기 (Default Args)
// // 인자 개수와 상관없이 반드시 괄호를 붙인다
const sayHello = (name='수연') => `hi! ${name}`
console.log(sayHello('선아'))