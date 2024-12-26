from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import torch
import numpy as np

model = SentenceTransformer("bert-base-nli-mean-tokens")
qqq=cosine_similarity(model.encode(['how to have a world expedition travel','how to have a Global Flavors Journey']))


with open("./data/cluster.json",'r',encoding='utf-8')as fp:
    data = json.load(fp)
q=0
for i in range(len(data)):
    if 'hierarchy' in data[i].keys() or 'augment' in data[i].keys():
        q=q+1
def list_txt(path, list=None):
    '''

    :param path: 储存list的位置
    :param list: list数据
    :return: None/relist 当仅有path参数输入时为读取模式将txt读取为list
             当path参数和list都有输入时为保存模式将list保存为txt
    '''
    if list != None:
        file = open(path, 'w')
        file.write(str(list))
        file.close()
        return None
    else:
        file = open(path, 'r')
        rdlist = eval(file.read())
        file.close()
        return rdlist






# def calculate_bert_similarity(text1, text2):
#     model = SentenceTransformer("bert-base-nli-mean-tokens")
#     embeddings = model.encode([text1, text2])
#     similarity = cosine_similarity(embeddings)
#     return similarity[0][1]
model = SentenceTransformer("bert-base-nli-mean-tokens")


# text1 = "Sell Fine Art Online. Sell yourself first by creating an online profile that highlights your creativity, experience, and passion for art. Join online artist communities and research the terms and conditions of each site. Make yourself public by advertising yourself, using Twitter and Facebook, and blogging about your artwork. Create a mailing list to keep in touch with past customers. Take good pictures of your artwork and license it properly. Consider creating your own website to optimize for search engines and sell directly from it. Expect this to be a gradual process and attend relevant art shows to show your work."
# text2 = "Pick a Stage Name. Understand the purpose of a stage name and how it can help you brand your performance persona, separate your personal and professional life, differentiate yourself, and avoid prejudice. Choose a name that reflects your persona and have a story behind it. Do research about the name and make sure it is searchable. Choose a name that will grow with you and one that you won't get tired of quickly."
#
# bert_similarity = calculate_bert_similarity(text1, text2)
# print(bert_similarity)

with open("./data/T.json",'r',encoding='utf-8')as fp:
    data = json.load(fp)
#b标题相似度
a=[]
for i in range(len(data)):
    # b.append(calculate_bert_similarity(data[i]['title'],data[j]['title']))
    a.append(data[i]['title'])
b=cosine_similarity(model.encode(a))


# list_txt(path='./data/savelist.txt', list=b)
# c=[[],[]]
# for i in range(len(b[0])):
#     c[0].append(max(np.delete(b[i], i)))
#     c[1].append(np.argwhere(b[i]==max(np.delete(b[i], i)))[0][0])
# d=np.array(c)


#脚本相似度
e=[]
for i in range(len(data)):
    f=[]
    for j in range(len(data[i]['document'])):
        f.append(data[i]['document'][j]['script'].split('\n'))
    e.append(f)

#n是相似度矩阵，h是索引矩阵
g=[]
h=[]
for i in range(len(e)):
    for j in range(len(e[i])):
        for k in range(len(e[i][j])):
            g.append(e[i][j][k][3:])
            h.append([i,j,k])

m=a+g
n=cosine_similarity(model.encode(m))[:2241,2241:]

#找出title与scripts的最大相似度和所在位置
# p=[[],[]]
# for i in range(len(n)):
#     p[0].append(max(n[i]))
#     p[1].append(np.argwhere(n[i]==max(n[i]))[0][0])
# q=np.array(p)

#查看相似度矩阵有多少大于0.85
# w=[-1]*len(b)
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         if b[i][j]>=0.85:
#             w[i]=w[i]+1

#分主体和辅助，index是索引
obj=[]
aux=[]
index=[[],[]]
for i in range(len(data)):
    if len(data[i]['document'])>1:
        obj.append(data[i])
        index[0].append(i)
    else:
        aux.append(data[i])
        index[1].append(i)

#层次结构
u = [x['title'][7:] for x in aux]
for i in range(len(obj)):
    scr=[]

    for j in range(len(obj[i]['document'])):
        s=obj[i]['document'][j]['script'].split('\n')
        for k in range(len(s)):
            scr.append(s[k][3:])

    hie = cosine_similarity(model.encode(scr+u))[:len(scr),len(scr):]
    if np.max(hie)>=0.80:
        position=np.where(hie == np.max(hie))
        obj[i]['hierarchy']=aux[position[1][0]]
        obj[i]['hierarchy']['link']=scr[position[0][0]]
        u[position[1][0]]=''



    aug = cosine_similarity(model.encode([obj[i]['title']]+ u))[:1, 1:]
    if np.max(aug)>=0.80:
        position=np.where(aug == np.max(aug))
        obj[i]['augment']=aux[position[1][0]]
        u[position[1][0]]=''


with open("./data/cluster.json","w") as f:
    json.dump(obj,f)


print(1)








