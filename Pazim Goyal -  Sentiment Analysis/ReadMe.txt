project sentiment analysis on product review
By Pazim Goyal
---------------------------------------------------------------------------------------------------------------------------------

Programming Language used:  Python
External Libraries Used:
1.	Pandas (For reading CSV File from storage)
2.	Matplotlib (For Graphs)
Preprocessing, and all the three algorithms are implemented without the use of any datamining Library

Files in Folder:
1)	Python Files (.py) 
a)	Preprocessing.py (Preprocessing File)
b)	NaiveBayes.py (Naïve Bayes Algorithm Implementation)
c)	SVM (SVM Algorithm Implementation)
d)	KNN (KNN Algorithm Implementation) 
e)	Main.py  (Imported all the files in one file )
2)	Dataset: (.CSV)
a)	Training.csv (Training Dataset with 20000 reviews)
b)	Testing.csv (Testing Dataset with 10000 reviews)
c)	Testing_small.csv (Testing Dataset with 50 reviews to see results of knn as it can take hours for full dataset)
3)	StopWords.txt Text file Containing all the Stop Words

To See the Results Separately  run each algorithm separately.
If you want to see all the results together run main.py  (please close the graph after every algorithm so that python could process next algorithm)



Knn could be very slow for huge testing dataset so to speed up the process I added a separate dataset with few reviews if you want to see just the estimate results.
