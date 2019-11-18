const me = {
  name: '수연', // key가 한 단어일 때
  'phone number': '01055555555',    // key가 여러 단어일 때
  Products:{
    iphone:'xs',
    watch:'series5',
    macbook:'pro2019'
  }
}


me.name       // "수연"
me['name']    // "수연"
// key 값이 여러 단어일 때 []로 접근
me['phone number']  // "01055555555"

me.Products    // {iphone: "xs", watch: "series5", macbook: "pro2019"}
me.Products.iphone // "xs"
console.log(me.Products['iphone'])