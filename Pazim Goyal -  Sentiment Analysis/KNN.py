from preprocessing import *
print('\nKNN\n')

count = dict()
listwords=[]
listcount=df['gb'].tolist()
print("Counting Vocabulary")

for row_index,row in df.iterrows():
    for i in list(set(row['text'])):
        if i not in count:
            count[i]=1
        else:   
            count[i]=count[i] + 1

tfidf=[]
length=len(review)
print("Creating TF-IDF Matrix ")
## custom tfidf matrics
tempall=dict()
for row_index,row in df.iterrows():
        tempeach=list(set(row['text']))
        tempall.clear()
        for j in tempeach:
            first=row['text'].count(j)
            second=len(row['text'])
            tempall[j]=(first/second)*(log(length/count[j]))
        tfidf.append(tempall.copy())
print("TF-IDF Matrix Created")







#---------------------------------testing-----------------------------

result=[]
result.clear()
tempresult=[]
firstno=range(len(tfidf))
abcde=pandas.read_csv(file_name3,names=['text','real'])
finalscore=[]
print("Testing Using KNN.. It may take time in hours due to large database")
for i in abcde.text:
        i=i.replace(","," ").replace("."," ").replace(";"," ").replace("#"," ").replace(")"," ")
        testwords= [w for w in  i.lower().split(" ") if w not in setz] #taking a review and pazim  splitting it to words and removing all the stop words
        testunique=list(set(testwords))
        tempall.clear()
        tempscore=[]
        count1,count2=0,0
        for j in testunique:
                first=i.count(j)
                second=len(i)
                tempall[j]=(first/second)*(log(length/count.get(j,1)))
        for k in tfidf:
                score=0.0
                for n in list(set(testunique+list(k.keys()))):
                        ans=k.get(n,0)-tempall.get(n,0)
                        score+=(ans*ans) 
                tempscore.append((sqrt(score),listcount[tfidf.index(k)]))
        tempscore.sort()
        for e,a in tempscore:
                if a==1:
                        count1+=1
                elif a==0:
                        count2+=1
        if count1>count2:        
                finalscore.append(1)
        else:
                finalscore.append(0)
        tempscore.clear()


dfpos=DataFrame({'real':abcde.real.values,'count':finalscore,'rev':abcde.text})
dfpos.to_csv('predictions3.csv')

true=0
false=0
for row_index,row in dfpos.iterrows():
    if row['real'] == row['count']:
        true =true+1
    else:
        false=false+1


print("Accuracy for KNN : {} %".format((true*100)/(true+false)))
print("Time taken for KNN : {} seconds".format(time.clock()-start))        
print("Results stored in prediction3.csv")

        
            
        
        

labels = 'Accuracy','error'
sizes = [true,false]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

        

        

