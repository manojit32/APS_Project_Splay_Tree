import matplotlib.pyplot as plt
import sys
import splay
import bst
import time
sys.setrecursionlimit(30002)
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
plotly.offline.init_notebook_mode()
mmax=10000
def insert_del_opp(mmax):
    bt=[]
    st=[]
    maxl=[]
    while(mmax<26001):
        b=bst.BST()
        start=time.process_time()
        for i in range(1,mmax):
            b.insert(i)
        #for i in range(1,mmax):
        #    b.search(i)
        for i in range(mmax-1,0):
            b.remove(i)
        end=time.process_time()
        t1=end-start
        bt.append(t1)
        #print(bt)
        s=splay.Splay()
        start=time.process_time()
        for i in range(1,mmax):
            s.insert(i)
        #for i in range(1,mmax):
        #   s.search(i)
        for i in range(mmax,1):
            s.remove(i)
        end=time.process_time()
        t1=end-start
        st.append(t1)
        #print(st)
        maxl.append(mmax)
        mmax=mmax+2000
    return (maxl,bt,st)

def insert_del_opp_plot():
    mmax=10000
    sys.setrecursionlimit(30002)
    (maxl,bt,st)=insert_del_opp(mmax)    
    # plt.plot(maxl,bt,'o-',label="BST")
    # plt.plot(maxl,st,'x-',label="Splay")
    # plt.legend()
    # plt.show()
    trace1 = go.Scatter(
                    x = maxl,
                    y = bt,
                    mode = "lines+markers",
                    name = "BST",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
    trace2 = go.Scatter(
                    x = maxl,
                    y = st,
                    mode = "lines+markers",
                    name = "Splay",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'))
    data = [trace1, trace2]
    layout = dict(title = 'Insert integers in increasing order,and delete them in reverse order',
                xaxis= dict(title= 'Number of nodes',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Time (in seconds)',ticklen= 5,zeroline= False)
                )
    fig = dict(data = data, layout = layout)
    iplot(fig,image='png')

def insert_del_same(mmax):
    bt=[]
    st=[]
    maxl=[]
    while(mmax<26001):
        b=bst.BST()
        start=time.process_time()
        for i in range(1,mmax):
            b.insert(i)
        #for i in range(1,mmax):
            # b.search(i)
        for i in range(1,mmax):
            b.remove(i)
        end=time.process_time()
        t1=end-start
        bt.append(t1)
        #print(bt)
        s=splay.Splay()
        start=time.process_time()
        for i in range(1,mmax):
            s.insert(i)
        # for i in range(1,mmax):
        #     s.search(i)
        for i in range(1,mmax):
            s.remove(i)
        end=time.process_time()
        t1=end-start
        st.append(t1)
        #print(st)
        maxl.append(mmax)
        mmax=mmax+2000 
    return maxl,bt,st
# st=[33.29972300000001, 50.539084, 71.49798800000002, 95.31989099999998, 118.95224799999994, 147.4706490000001, 180.0806630000002, 214.99696600000016, 251.58281699999998]
# bt=[54.200059, 78.26101100000001, 110.964494, 143.786, 179.89194499999996, 222.326914, 270.32453699999996, 324.64937699999996, 381.7795540000002, 449.7263029999999]
def insert_del_same_plot():
    mmax=10000
    sys.setrecursionlimit(30002)
    maxl,bt,st=insert_del_same(mmax)
    '''plt.plot(maxl,bt,'o-',label="BST")
    plt.plot(maxl,st,'x-',label="Splay")
    plt.legend()
    plt.show()'''
    trace1 = go.Scatter(
                    x = maxl,
                    y = bt,
                    mode = "lines+markers",
                    name = "BST",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'))
    trace2 = go.Scatter(
                    x = maxl,
                    y = st,
                    mode = "lines+markers",
                    name = "Splay",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'))
    data = [trace1, trace2]
    layout = dict(title = 'Insert integers in increasing order,and delete them in same order',
                xaxis= dict(title= 'Number of nodes',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Time (in seconds)',ticklen= 5,zeroline= False)
                )
    fig = dict(data = data, layout = layout)
    iplot(fig,image='png')



