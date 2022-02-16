from os import getcwd,listdir,mkdir
from os.path import exists
from shutil import move
path = getcwd()
filelist = listdir(path)
number = 1
while 1>0:
    for file in filelist:
        A = '_'+str(number*20-20)+'_'
        if A in file:
            if not exists(path+'/'+str(number)):
                mkdir(path+'/'+str(number))
            move(file, path + '/' + str(number))
    if not exists(path+'/'+str(number)):
        break
    number += 1