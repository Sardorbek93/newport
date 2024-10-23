class Noname:
    def __init__(self, job):
        self.job = job
    def punkt (self, word):
        return f'Слово: {word}'
c = Noname (job= "teacher") #c, b = Noname (job = "teacher"), Noname (job = programmer")  МОЖНО И ТАК
b = Noname (job = "programmer")
print(c)  #напечатили все что в Ноунейм. Ноунейм равен С
print(c.punkt("privet")) # д
print(b.punkt('POKA'))
print(c.job)
print(b.job)