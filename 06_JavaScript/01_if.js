const userName = prompt('니 이름은 뭐니?') 
let message =''
if(userName === '수연'){
	message = '<h1>내 이름은 이수연!<h1>'
} else if (userName === '선아'){
	message = '<h1>스나<h1>'
} else {
	message = `<h1>${userName}...누구?</h1>`
}
document.write(message)