#
# AUTHOR: Josephine Nguyen
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# #-----------------------------------------------------------*/
# #IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append(row)

#loop your data to allow each instance to be your test set
incorrect_predictions = 0
for i, instance in enumerate(db):
    X = []
    Y = []
    #add the training features to the 2D array X removing the instance that will beused for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to float to avoid warning messages
    #--> add your Python code here
    #X =
    for index in range(len(db)):
        if index != i:
            row = db[index]
            X.append([float(row[0]), float(row[1])])


    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each feature value to float to avoid warning messages
    #--> add your Python code here
    # + = 1
    # - = 2
    for index in range(len(db)):
        if index != i:
            row = db[index]
            if row[2] == '+':
                Y.append(1.0)
            else:
                Y.append(2.0)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [[float(instance[0]), float(instance[1])]]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict(testSample)[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    actual_class = -1
    if instance[2] == '+':
        actual_class = 1.0
    else:
        actual_class = 2.0

    if class_predicted != actual_class:
        incorrect_predictions = incorrect_predictions +1

#print the error rate
print("error rate = " + str(incorrect_predictions/len(db)))