# 1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())

print("*****************************************")    
# 2
car_models = ['Toyota', 'Nexia 3', 'Deepal SL03', 'GM', 'Nissan']
for car in car_models:
    if car!='GM':
        print(car.title())
    else:
        print(car.upper())

print("*****************************************") 
# 3     
login = input("Login: ")
if login.lower() == 'admin':
  print("Welcome Admin, Do you see the user list?")
else:
  print(f"Welcome {login.title()}!")  

print("*****************************************")
# 4
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: 
    print(f"Sonlar teng: {x} = {y}")
else:
    print("Sonlar teng emas:")
    
print("*****************************************")
# 5
num = float(input("Istalgan son kiriting:"))
print("Son manfiy") if num<0 else print("Son musbat")

print("*****************************************")
# 6
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')