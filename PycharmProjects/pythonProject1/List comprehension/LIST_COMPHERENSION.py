salary = [1000, 1200, 1300, 1500]
salary2 = []
for i in salary:
    salary2.append(i-(i*0.1))
#List comphrension umenshaet, uproshaet kod
salary3 = [i-(i*0.1) for i in salary]
print(salary2)
print(salary3)

name = "pasha", 'sasha'
n = [x*2 for x in name]
print(n)

my = ['2', '33', 'jordan', 'pavel']
my2 = [i+'2' for i in my]
print(my2[-1])

#beskonechnoe sikl for
#a = ['hello', 'bye']
#for i in a:
#   print(a)
#   a.append('privet')

#sozdat uslovie v liste comprehension
salary3 = [i-(i * 0.1) for i in salary if i > 1000]
print(salary3)


