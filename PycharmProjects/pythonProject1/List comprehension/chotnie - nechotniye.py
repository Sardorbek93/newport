nums = [i for i in range (1,11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]
print(chotnie, nechotnie)
# == ravno
# != neravno

names = ["Pavel", "Jordan", "sasha", "SPiridon", "pasha"]
names2 = [name for name in names if name[0].lower() == "p"]
print(names2)

#
