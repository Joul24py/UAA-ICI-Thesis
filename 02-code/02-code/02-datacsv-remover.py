'''
Archivo Python que "refresca" (elimina) un data.csv
cada 10 segundos (para no saturar a la memoria)
'''
import os
import time

while True:
    time.sleep(5)
    os.remove('data.csv')