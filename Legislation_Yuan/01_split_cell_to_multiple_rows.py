import pandas as pd
import numpy as np
from itertools import chain
import csv

df = pd.read_csv('Legislation_Yuan/test_file/LY_test_edu.csv')


def chainer(s):
    return list(chain.from_iterable(s.str.split('\n')))

#split the 'string' saved in education. 
#because each of the 'items' was separated by \n, specify that whenever we encounter a '\n', we want to split the string.
#because we
lens = df['education'].str.split('\n').map(len)

res = pd.DataFrame({'name': np.repeat(df['name'], lens),
    'party': np.repeat(df['party'], lens), 
    'education': chainer(df['education'])})
#question: why my code renders two extra unexpected rows>

res.to_csv('Legislation_Yuan/test_file/LY_test_edu_splited.csv', index=False)



#why this code doesn't work!?
#I modified it from stackoverflow...
#https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe

df = df.set_index(['education']).apply(lambda x: x.str.split('\n').explode()).reset_index()


#this block is to try to see what went wrong with the code for exlosion(?)
#I can see that the problem might have something to do with the fact that there are one more \n than I had expected. But, still, why did it have two extra rows!?!?!?!
with open('Legislation_Yuan/test_file/LY_test_edu.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

