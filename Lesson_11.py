# 1
num = float(input("Juft son kiriting: "))
if num%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")
   
print("*****************************************")  
# 2  
yosh = int(input("Yoshingiz nechida? "))
if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

print("*****************************************")
# 3
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x} = {y}")
elif x < y:
    print(f"{x} < {y}")
else:
    print(f"{x} > {y}")
    
print("*****************************************")    
# 4      
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

print("*****************************************")    
# 5         
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

print("*****************************************")    
# 6  
users = ['alisher','aziza','yasina','umar']
login = input("Yangi login tanlang: ")
if login in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")

print("*****************************************")    
# 7    
num = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (num%n):
        print(f"{num} soni {n} ga qoldiqsiz bo'linadi")