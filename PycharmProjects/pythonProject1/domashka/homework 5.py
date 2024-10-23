#homework berem kvadrati kazhdogo chisla
a = [x**2 for x in range (5)]
print(a)

#2 berem 10 procent s kazhdogo chisla
b = [100, 500, 1000, 5000]
c = [d*0.1 for d in b ]
print(c)
#sortirovka nomerov s 1 do 100 v chot ili nechot
nums = [num for num in range (1,101)]
chot = [b for b in nums if b % 2 == 0]
nechot = [b for b in nums if b % 2 != 0]
print(chot, nechot)

                #name
names = ("Sasha", "Pasha", "Garik", "Vadik", "Dima" )
number = (1,2,3,4,5)
obsh = (x for x if names )