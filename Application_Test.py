import pandas as pd
import time
import splay1
import bst1
import random
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
plotly.offline.init_notebook_mode()
df4=pd.read_csv("unique_tracks.txt",sep="<SEP>",header=None,engine='python')
df6=df4[[2,3]]
df6=df6.dropna()
s1=splay1.Splay()
import bst1
b1=bst1.BST()
for i in range(0,int(df6.size/2)):
    b1.insert(df6.iat[i,0],df6.iat[i,1])
for i in range(0,int(df6.size/2)):
    s1.insert(df6.iat[i,0],df6.iat[i,1])

def rand_uniq_1000():
    data =range(1, int(df6.size/2))
    import sys
    sys.setrecursionlimit(500000)
    tmm=[]
    tmm1=[]
    for j in range(10):
        dels = random.sample(data, 100000)
        start1=time.process_time()
        for i in dels:
            if df6.iat[i,1]:
                s1.search(df6.iat[i,0])
        end=time.process_time()
        if(len(tmm)>0):
            t=tmm[len(tmm)-1]
            tmm.append(end-start1+t)
        else:
            tmm.append(end-start1)
        start2=time.process_time()
        for i in dels:
            if df6.iat[i,1]:
                b1.search(df6.iat[i,0])
    #     end=time.process_time()
    #         tm.append(end-start)
        end=time.process_time()
        if(len(tmm1)>0):
            t=tmm1[len(tmm1)-1]
            tmm1.append(end-start2+t)
        else:
            tmm1.append(end-start2)
    return tmm,tmm1
#print(tm)
#print(tm1)
def rand_uniq_1000_graph():
    tm,tm1=rand_uniq_1000()
    size=[100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    '''plt.plot(size,tm)
    plt.plot(size,tm1)
    plt.show()'''
    trace1 = go.Scatter(
                    x = size,
                    y = tm1,
                    mode = "lines+markers",
                    name = "BST",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
    trace2 = go.Scatter(
                    x = size,
                    y = tm,
                    mode = "lines+markers",
                    name = "Splay",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'))
    data = [trace1, trace2]
    layout = dict(title = 'Search for n random and all unique elements, where n ranges from 100000 to 1000000',
                xaxis= dict(title= 'Number of searches',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Time (in seconds)',ticklen= 5,zeroline= False)
                )
    fig = dict(data = data, layout = layout)
    iplot(fig,image='png')
def rand_1000_uniq_10():
    tmm=[]
    tmm1=[]
    
    for j in range(10):
        pretty_uneven_accesses10=[]
        base = random.randint(0, int(df6.size/2) - 10)
        for i in range(100000):
                pretty_uneven_accesses10.append(random.randint(base, base + 10))
        start1=time.process_time()
        for i in pretty_uneven_accesses10:
            if df6.iat[i,1]:
                s1.search(df6.iat[i,0])
        end=time.process_time()
        if(len(tmm)>0):
            t=tmm[len(tmm)-1]
            tmm.append(end-start1+t)
        else:
            tmm.append(end-start1)
        start2=time.process_time()
        for i in pretty_uneven_accesses10:
            if df6.iat[i,1]:
                b1.search(df6.iat[i,0])
    #     end=time.process_time()
    #         tm.append(end-start)
        end=time.process_time()
        if(len(tmm1)>0):
            t=tmm1[len(tmm1)-1]
            tmm1.append(end-start2+t)
        else:
            tmm1.append(end-start2)
    return tmm,tmm1
def rand_1000_uniq_10_graph():
    tmm,tmm1=rand_1000_uniq_10()
    size=[100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    '''plt.plot(size,tmm,label='Splay')
    plt.plot(size,tmm1,label='BST')
    plt.legend()
    plt.show()'''
    trace1 = go.Scatter(
                    x = size,
                    y = tmm1,
                    mode = "lines+markers",
                    name = "BST",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
    trace2 = go.Scatter(
                    x = size,
                    y = tmm,
                    mode = "lines+markers",
                    name = "Splay",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'))
    data = [trace1, trace2]
    layout = dict(title = 'Search for n random elements which consists of 10 unique elements and n ranges from 100000 to 1000000',
                xaxis= dict(title= 'Number of searches',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Time (in seconds)',ticklen= 5,zeroline= False)
                )
    fig = dict(data = data, layout = layout)
    iplot(fig,image='png')
def rand_1000_uniq_4():
    tmm=[]
    tmm1=[]
    
    for j in range(10):
        pretty_uneven_accesses4=[]
        base = random.randint(0, int(df6.size/2) - 4)
        for i in range(100000):
                pretty_uneven_accesses4.append(random.randint(base, base + 4))
        start1=time.process_time()
        for i in pretty_uneven_accesses4:
            if df6.iat[i,1]:
                s1.search(df6.iat[i,0])
        end=time.process_time()
        if(len(tmm)>0):
            t=tmm[len(tmm)-1]
            tmm.append(end-start1+t)
        else:
            tmm.append(end-start1)
        start2=time.process_time()
        for i in pretty_uneven_accesses4:
            if df6.iat[i,1]:
                b1.search(df6.iat[i,0])
    #     end=time.process_time()
    #         tm.append(end-start)
        end=time.process_time()
        if(len(tmm1)>0):
            t=tmm1[len(tmm1)-1]
            tmm1.append(end-start2+t)
        else:
            tmm1.append(end-start2)
    return tmm,tmm1
def rand_1000_uniq_4_graph():
    tmm,tmm1=rand_1000_uniq_4()
    size=[100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    '''plt.plot(size,tmm,label='Splay')
    plt.plot(size,tmm1,label='BST')
    plt.legend()
    plt.show()'''
    trace1 = go.Scatter(
                    x = size,
                    y = tmm1,
                    mode = "lines+markers",
                    name = "BST",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
    trace2 = go.Scatter(
                    x = size,
                    y = tmm,
                    mode = "lines+markers",
                    name = "Splay",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'))
    data = [trace1, trace2]
    layout = dict(title = 'Search for n random elements which consists of 4 unique elements and n ranges from 100000 to 1000000',
                xaxis= dict(title= 'Number of searches',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Time (in seconds)',ticklen= 5,zeroline= False)
                )
    fig = dict(data = data, layout = layout)
    iplot(fig,image='png')