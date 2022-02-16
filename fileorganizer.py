from os import getcwd,listdir,mkdir
from shutil import move
path = getcwd()
filelist = listdir(path)
filelist.remove('fileorganizer.exe')
while True:
    try:
        many = int(input('要把幾個檔案裝一個資料夾 : '))
    except:
        print('請輸入正整數')
        continue
    if many < 1:
        print('請輸入正整數')
    else:
        break

foldernumber = 0
for index,file in enumerate(filelist):
    if index % many == 0:
        foldernumber += 1
        mkdir(path+'/'+str(foldernumber))        
    move(file, path + '/' + str(foldernumber))