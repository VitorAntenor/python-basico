import threading
import numpy as np
import pandas as pd

valor1= 5
valor2= 6
valor3= 7

def funcao():
      global soma 
      soma = valor1 + valor2 + valor3
      print('Soma: ', soma)

def media():
      medias = soma/3
      print("A média dos valores é: ", medias )

print("********************")
print("THREAD 1:")
print('Iniciando soma:')
threading.Thread(target = funcao).start()
print('Terminando a soma.')
print("********************")

print("THREAD 2:")
print('Iniciando cálculo da média:')
threading.Thread(target = media).start()
print('Terminando cálculo da média.')
print("********************")
