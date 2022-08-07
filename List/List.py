import random



fav_movies = ["Batman","A","B"]

print(fav_movies)

print(len(fav_movies))


numbers = []

for i in range(5):
    
    if (random.randint(0,10))%2==0:
        numbers.append(i) # append insereaza la final
 
print(numbers)

numbers2 = []
for i in range(5):
    
    if (random.randint(0,10))%2==0:
        numbers2.insert(1,i) # insereaza la un loc specific


while len(fav_movies)>1:
    del(fav_movies[1])

print(fav_movies)


if numbers.index(3) != None:
    print(numbers.index(3)) # index cauta in lista elementul 3 in acest exemplut
else:
    print("Nu exista")