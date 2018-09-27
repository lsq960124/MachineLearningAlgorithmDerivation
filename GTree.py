# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:46:00 2018

@author: Adam
"""
import pandas as pd 
import numpy as np


dataSet = [['青绿','蜷缩','浊响','清晰','凹陷','硬滑','是'],
           ['乌黑','蜷缩','沉闷','清晰','凹陷','硬滑','是'],
           ['乌黑','蜷缩','浊响','清晰','凹陷','硬滑','是'],
           ['青绿','蜷缩','沉闷','清晰','凹陷','硬滑','是'],
           ['浅白','蜷缩','浊响','清晰','凹陷','硬滑','是'],
           ['青绿','稍蜷','浊响','清晰','稍凹','软粘','是'],
           ['乌黑','稍蜷','浊响','稍糊','稍凹','软粘','是'],
           ['乌黑','稍蜷','浊响','清晰','稍凹','硬滑','是'],
           ['乌黑','稍蜷','沉闷','稍糊','稍凹','硬滑','否'],
           ['青绿','硬挺','清脆','清晰','平坦','软粘','否'],
           ['浅白','硬挺','清脆','模糊','平坦','硬滑','否'],
           ['浅白','蜷缩','浊响','模糊','平坦','软粘','否'],
           ['青绿','稍蜷','浊响','稍糊','凹陷','硬滑','否'],
           ['浅白','稍蜷','沉闷','稍糊','凹陷','硬滑','否'],
           ['乌黑','稍蜷','浊响','清晰','稍凹','软粘','否'],
           ['浅白','蜷缩','浊响','模糊','平坦','硬滑','否'],
           ['青绿','蜷缩','沉闷','稍糊','稍凹','硬滑','否']]

labels = ['色泽','根蒂','敲声','纹理','脐部','触感','好瓜']

data = pd.DataFrame(dataSet,columns=labels)
data = data.set_index('好瓜')

def Ent(data,col):
    number = len(data)
    label = data.index.value_counts()
    ent = 0
    for x in label:
        ent += -(x/number)*np.log2(x/number)
    return ent

indexEnt= Ent(data,data.index.name)

def GainEntTree(data,indexEnt):
    LabelData=list(data.index)
    if LabelData.count(LabelData[0])==len(LabelData):
        return LabelData[0]
    if len(data.columns)==0:
        return data.index.value_counts().sort_values(ascending=False).index[0]
    if len(data.columns)>0:
        GainEntlist=[]
        columnslist = data.columns
        lendata=len(data)
        for i in data.columns:
            Gain=[]
            ColValueCounts=data[i].value_counts()
            ColValueCountsindex=ColValueCounts.index
            ColValueCountsvalues=ColValueCounts.values
            for j in range(len(ColValueCountsindex)):
                D = data[data[i]==ColValueCountsindex[j]].index.value_counts()
                ent=sum([-(z/lendata)*np.log2(z/ColValueCountsvalues[j]) for z in D])
                Gain.append(ent)
            GainEntlist.append(sum(Gain))
        GainEntlist=[indexEnt-x for x in GainEntlist]
        x=dict(zip(columnslist,GainEntlist))
        top=sorted(x.items(),key=lambda item:item[1],reverse=True)[0][0]
        myTree={top:{}}
        for value in set(data[top]):
            newdata=data[data[top]==value].drop(top,axis=1)
            myTree[top][value]=GainEntTree(newdata,Ent(newdata,newdata.index.name))
        return myTree

GainEntTree(data,indexEnt)            






        





































  
