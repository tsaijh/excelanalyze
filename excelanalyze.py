from os import getcwd,listdir,mkdir
from numpy import mean,min,max
from pandas import read_csv,concat
from matplotlib.pyplot import plot,savefig,legend,ylabel,fill_between,ylim
path = getcwd()
filelist = listdir(path)
for index in filelist:
    if 'csv' in index:
        if 'fore' in index:
            before = index
        elif 'fter' in index:
            after = index
        else:
            continue
try:
    print(before)
    print(after)
except:
    input('the data is non-existent')
while 1>0:
    try:
        number = int(input('average : '))
        if number>0:
            lower = float(input('the lower limit on Y-axis(1000 is automation) : '))
            if int(lower) != 1000:
                upper = float(input('the upper limit on Y-axis : '))
            break
        else:
            continue
    except:
        continue
namelist = [before,after]
name = ['before','after']
data = []
color = ['black','red']
color1 = ['gray','pink']
for filename in range(2):
    transietpicture = []
    dataframe = read_csv(path + '/' + namelist[filename])
    col = int((len(dataframe.columns)-1) / 2)
    for index in range(1,col+1):
        dataframe.loc[0, str('normalize%d' % index)] = sum(dataframe.iloc[0:number, 4 * index - 2]) / number
        dataframe.loc[:, str('%s training mean%d(%%)' % (name[filename],index))] = (dataframe.iloc[:, 4 * index - 2] - dataframe.loc[
            0, str('normalize%d' % index)]) / dataframe.loc[0, str('normalize%d' % index)]*100
        colname = dataframe.pop(str('normalize%d' % index))
        dataframe.insert(4 * index - 1, colname.name, colname)
        colname = dataframe.pop(str('%s training mean%d(%%)' % (name[filename],index)))
        dataframe.insert(4 * index, colname.name, colname)
        transietpicture.append(colname)
    data.append(dataframe)
    plot(dataframe.iloc[:,0],mean(transietpicture,axis=0), color=color[filename], label = name[filename])
    fill_between(dataframe.iloc[:,0],max(transietpicture,axis=0),min(transietpicture,axis=0),color = color1[filename],alpha=0.5)
mkdir(path+'/compare/')
legend()
ylabel('(%)')
if lower != 1000:
    ylim(lower,upper)
savefig(path+'/compare/'+'figure.png')
data[0] = data[0].iloc[:,2:]
compare = concat([data[1],data[0]],axis=1)
compare.to_csv(path+'/compare/compare results.csv',index = False)