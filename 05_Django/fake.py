from faker import Faker

myfake = Faker('ko_KR') 
print(myfake.name()) 
print(myfake.address()) 
print(myfake.text()) 
print(myfake.sentence()) 
print(myfake.random_number())




