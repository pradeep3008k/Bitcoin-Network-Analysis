import networkx as nx
import numpy as np
import random as rand
import matplotlib.pyplot as plt
f=open("bitcoin.csv",'r')
f=f.readlines()
l=list(f)
g=[]
for i in range(len(l)):
    a=l[i].split(',')
    g.append([int(a[0]),int(a[1]),int(a[2])])
g.sort(key = lambda x: x[1])
dict={}
for i in g:
    if i[2]>=5 and i[1]<=50:
        if i[1] in dict:
            dict[i[1]][0]+=1
            dict[i[1]][1].add(i[0])
        else: 
            dict[i[1]]=[1,{i[0]}]
ls=[]
for i in dict:
    ls.append([dict[i][0],i])
ls.sort(reverse=True)
spset=set()
lr=[]
dict1 = dict.copy()
for i in range(10):
    if len(spset)==0:
        a=ls[0][1]
        lr.append(a)
        for i in dict[a][1]:
            spset.add(i)
        '''print('\n')
        print(ls)
        print('\n')'''
        ls.remove(ls[0])
        del dict[a]
    else:
        del ls
        ls=[]
        for j in dict:
            dict[j][1]=dict[j][1]-spset
            dict[j][0]=len(dict[j][1])
            ls.append([len(dict[j][1]),j])
        ls.sort(reverse=True)
        a=ls[0][1]
        lr.append(a)
        for i in dict[a][1]:
            spset.add(i)
        #print('\n')
        #print(ls)
        #print('\n')
        ls.remove(ls[0])
        del dict[a]
print(lr)

def make_Graph(lr,spset):
    G = nx.DiGraph()
    colour_list = []
    for i in dict1:
        #G.add_node(i)
        s = dict1[i][1]
        for j in s:
            #G.add_node(j)
            G.add_edge(j,i)
    #pos = nx.kamada_kawai_layout(G)
    #nx.draw(G.pos1,with_labels = True)
    for i in G.nodes():
        if i in lr:
            colour_list.append("red")
        elif i in spset:
            colour_list.append("cyan")
        else:
            colour_list.append("yellow")
    pos = nx.random_layout(G)
    nx.draw(G,pos,with_labels = True)
    nx.draw_networkx_nodes(G, pos,node_color=colour_list)
    #nx.draw_networkx_nodes(G,pos,nodelist = list(spset),node_color = "g")
    plt.show()

make_Graph(lr,spset)
