from modules.module1 import *

say_hello()

liq = ['123', 22, 2.1, 22]

liq.append('GOOO!!')

print(liq)

liq.pop()

print(liq)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M[1])
print(M[1][2])

supern = [row[0] for row in M]
superM = [row[1] for row in M]
superMMM = [row[2] for row in M]

print(supern)
print(superM)
print(superMMM)
