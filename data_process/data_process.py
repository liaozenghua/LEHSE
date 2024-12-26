import csv
import re
import json
with open('./data/wikihowAll.csv',encoding ='utf_8') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row for row in reader]

for i in range(len(column)):

    headline=column[i]['headline']
    headline=re.split('\n|,\n', headline)[1:]
    column[i]['headline']=headline

    text=column[i]['text']
    print(text)
print(column[0])

with open('./data/wikihowSep.csv',encoding ='utf_8') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row for row in reader]

    for i in range(len(column)):

        text=column[i]['text']
        if text!='' and text[0]==' ':
            text=text[1:]
        text=re.sub('\n+', '\n', text)
        if text!='' and text[-1]=='\n':
            text=text[:-1]
        if text!='' and text[-1]==';' :
            text=text[:-1]
        column[i]['text']=text

        headline=column[i]['headline']
        headline= re.sub('\n+', '', headline)
        column[i]['headline'] = headline

b=[]
t=[]
for i in range(len(column)):
    if column[i]["title"]=='' or column[i]["text"]=='' or column[i]["sectionLabel"]=='' or column[i]["headline"]=='':
        b.append(column[i])
        t.append(column[i]["title"])
    print(i)

r=[]
for i in range(len(column)):
    if column[i]["title"] in t:
        r.append(column[i])
        print(i)

for i in r:
    column.remove(i)
    print(i)



data=[]
for i in range(len(column)):
    b=False
    for j in range(len(data)):
        if data[j]['title']==column[i]['title'] and data[j]['part']==column[i]['sectionLabel']:
            data[j]['text']=data[j]['text']+'\nheadline: '+column[i]['headline']+'\ntext: '+column[i]['text']
            b=True
            break
    if b==False:
        data.append({'title':column[i]['title'],'part':column[i]['sectionLabel'],'text':'headline: '+column[i]['headline']+'\ntext: '+column[i]['text']})
    print(i)
#
with open("./data/data.json","w") as f:
#     json.dump(data,f)

with open("./data/data.json",'r',encoding='utf-8')as fp:
    data = json.load(fp)

b=[]
for i in range(len(data)):
    if type(data[i]['title'])!=str or data[i]['text']=='' or data[i]['part']=='' or data[i]['title']=='' or type(data[i]['text'])!=str or type(data[i]['part'])!=str:
        b.append(i)

lis = [n for i, n in enumerate(data) if i not in b]


data=lis
D=[]
for i in range(len(data)):
    b=False
    for j in range(len(D)):
        if D[j]['title'] == data[i]['title']:
            try:
                D[j]['text'] = D[j]['text'] + '\npart: ' + data[i]['part'] + '\n' + data[i]['text']
            except:
                print(i)
            b=True
            break
    if b==False:
        try:
            D.append({'title': data[i]['title'],'text': 'title: '+data[i]['title']+'\npart: ' + data[i]['part'] + '\n' + data[i]['text']})
        except:
            print(i)
    print(i)


with open("./data/D.json","w") as f:
    json.dump(D,f)




print(2)