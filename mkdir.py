import datetime
import os
import sys

os.system(f'mkdir {datetime.datetime.now().date()}')

with open('hodi.txt','a+')as file:
    file.write(f'{sys.platform}')
