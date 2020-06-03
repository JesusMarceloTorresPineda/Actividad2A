from random import randint
from tkinter import *
import random
import math 
import matplotlib.pyplot as plt
import numpy as np


aleatorios=[]

for i in range(10):
    numero = random.randint(11,20)
    numero2 = random.randint(1,10)
    aleatorios.append([numero, numero2])

b = sorted(aleatorios, key = lambda x : x[0])
c = sorted(aleatorios, key = lambda x : x[1])

print(aleatorios)
print(b)
print(c)

# a = [('Al', 2),('Bill', 1),('Carol', 2), ('Abel', 3), ('Zeke', 2), ('Chris', 1)]  
# b = sorted(sorted(a, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)  
# print(b)  
# [('Abel', 3), ('Al', 2), ('Carol', 2), ('Zeke', 2), ('Bill', 1), ('Chris', 1)]