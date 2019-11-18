const numbers = [1,2,3,4,5]

// 양의 정수로만 인덱스접근 가능

// reverse() : 원본이 뒤집힘

numbers[0]    //1
numbers[-1]   //undefined -> 정확한 양의 정수만 가능
numbers.length    //5

//원본 파괴!
numbers.reverse()   // [5,4,3,2,1]
numbers             // [5,4,3,2,1]
numbers.reverse()   // [1,2,3,4,5]
numbers             // [1,2,3,4,5]

// push - 배열 길이 return
numbers.push('a')   // 6
numbers             // [1,2,3,4,5,'a']

// pop - 배열 가장 마지막 요소 제거 후, 제거 요소 return 
numbers.pop()       // 'a'
numbers             // [1,2,3,4,5]

// unshift - 배열 가장 앞에 요소 추가
numbers.unshift('a')     // 6 (배열의 새로운 length)
numbers                  // ['a',1,2,3,4,5]

// shif - 배열의 가장 첫번째 요소 제거 후 return
numbers.shift()         //'a'
numbers                 // [1,2,3,4,5]

//((()))
//{{{}}}
// extensions => rainbow brackets & indent rainbow

numbers.push('a','b')
numbers                 // [1,2,3,4,5,'a','b']
numbers.unshift('a')    // ['a',1,2,3,4,5,'a','b']

// 중복된 요소가 존재하는 경우 처음 찾은 요소의 index return!
numbers.indexOf('a')    // 0
numbers.indexOf('b')    // 8
numbers.indexOf('c')    // 찾는 요소가 없으면 -1


/* 
  join - 배열의 요소를 join 함수 인자를 기준으로 묶어서 문자열로 return!
*/

numbers.join()          // "a,1,2,3,4,5,a,b" (기본값은 ',')
numbers.join('-')       // "a-1-2-3-4-5-a-b"
numbers.join('')        // "a12345ab"