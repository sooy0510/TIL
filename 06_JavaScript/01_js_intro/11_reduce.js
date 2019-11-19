const tests = [90, 80, 77, 13, 58]
const sum1 = tests.reduce(function (total, score) {
  return total += score
})
console.log(sum1)

// const sum2 = tests.reduce((total, score) => total += score)
// console.log(sum2)