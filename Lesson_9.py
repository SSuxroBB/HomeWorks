# 1 vs 2 
names = ['Jon', 'James', 'Tom', 'Jacob', 'Antony']
n = 0
for name in names:
    print(f"Hi {name}")
    n=n+1
print(f"Code repeated {n} times")

print("*****************************************")
# 3
numbers = list(range(11, 100, 2))
for num in numbers:
    print(f"{num} => ning kubi = {num**3} ga teng")
    
print("*****************************************")    
# 4
movies = []
print("What are your 5 favorite movies?")
for k in range(5):
    movies.append(input(f"{k+1} - movie: "))
print(movies)   

print("*****************************************") 
# 5
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
names = []
for n in range(n_people):
    names.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(names)