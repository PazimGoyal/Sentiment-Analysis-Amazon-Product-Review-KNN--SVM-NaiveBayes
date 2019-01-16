from preprocessing import *
start=time.clock()
print('\nS.V.M\n')
poss = dict()
negs=dict()
print("Counting Vocabulary for SVM")
poss.clear()
negs.clear()
for row_index,row in df.iterrows():
    if row['gb']==1:
        for i in row['text']:
            if i not in poss:
                poss[i]=1
                negs[i]=0
            else:   
                poss[i]+=1
    else:
        for i in row['text']:
            if i not in negs:
                poss[i]=0
                negs[i]=1
            else:   
                negs[i]+=1
print("Total Vocabulary Count  : {} ".format(len(poss)))

#---------------------------------testing-----------------------------

result=[]
result.clear()

for s in review2:
    count1=0
    count2=0
    for v in s:
        if poss.get(v,0)>negs.get(v,0):
            count1=count1+1
        elif poss.get(v,0)<negs.get(v,0):
            count2=count2+1        
    if count1>count2:
        result.append(1)
    else:
        result.append(0)

dfpos=DataFrame({'real':abcd.real.values,'count':result,'rev':abcd.text})
dfpos.to_csv('predictions2.csv')

true=0
false=0
for row_index,row in dfpos.iterrows():
    if row['real'] == row['count']:
        true =true+1
    else:
        false=false+1
print("Accuracy for SVM : {} %".format((true*100)/(true+false)))
print("Time taken for SVM : {} seconds".format(time.clock()-start))        
print("Results stored in prediction2.csv")

labels = 'Accuracy','error'
sizes = [true,false]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()




