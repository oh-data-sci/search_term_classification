background
===
# introduction
this project was built as a part of a job application to join the award-winning data science team at adthena. the team made an assessment project and sent to me. presumably other candidates as well. the [project description](Adthena_Technology_Data-Scientist_Assignment.pdf) is found at the bottom of this document. though i was given a week to complete it, they estimated that it could be solved in 4-6 hours.

# assignment
## data scientist - technical assignment 
many thanks for your continued interest in joining adthena. to understand if you are a good fit for adthena and if we are a good fit for you, we would like to work together on a test assignment. please complete this task as if you are already working as part of our team at adthena. the assignment is as much about testing our ability to work together as it is your ability to implement features/products. please take the opportunity to ask any questions during the assignment as you would in a normal working environment. 

### technology requirement 
you should complete the test using python duration 

### deadline
the assignment should be returned to us within 1 week. we believe it should not take you more than 4 to 6 hours working on it. if you need extra time due to other commitment please let us know. 

### submission 
submit your code in any format you wish along with your source code. you could also submit your code using github, bitbucket or similar platforms. 

### documentation 
please provide a readme.txt. this should contain details of the steps necessary to install the software that is required to train & test the model. additionally, the readme.txt should contain details of the steps necessary to train and test the model. these steps should be such that they can be called from the command line and it should be possible to specify the data for training/prediction. please save these predictions in a csv that follows the same format as given in trainset.csv, with any pre-processing occurring in the training/prediction process. 

### contact 
please feel free to contact with any questions shaohong bai (shaohong.bai@adthena.com.) or vasanth john (vasanth.john@adthena.com) 
data scientist technical assignment 


## search term categorisation 
at adthena we analyse millions of search terms in the search advertising landscape. in order to enrich our in-house data set, we would like to associate metadata to the search terms in our data, such as assigning each search term with a category or categories. for example, the search term cricket nets' could be assigned to the category: `sports & fitness -> sporting goods -> cricket equipment`.

### data introduction 
a sample of labeled search term category data is provided in the csv file, `trainset.csv`. the file contains the two columns, the search term and the search term category. the search term category has been indexed. there are 606,823 examples in the data set with 1,419 different search term categories. there are roughly 427 examples in each category. 

## data files 
```
https://s3-eu-west-1.amazonaws.com/adthena-ds-test/trainset.csv
https://s3-eu-west-1.amazonaws.com/adthena-ds-test/candidatetestset.txt 
```

## problem description 
in this test we would like you to construct a classification model that can accurately categorise search terms. you are free to use whatever model that you feel is appropriate for the problem. 
we would like you to provide us with a detailed description of the work that you have done in constructing this model. this document should include the following details: 

1. a description of the type of model you selected for the problem, along with details explaining why you selected this type of model. 
2. a description of any pre-processing steps that you took prior to training the model. 
3. a description of the methods you considered when evaluating the performance of model. 
4. a description of the runtime complexity of the model, as well as the memory overhead of the model at both during model training and predicting against new cases. 
5. a description of the weaknesses of the selected model for the given problem, along with possible improvements that you would consider in the future. 

the ability to write clean reusable code is an important part of this role. we would also like you to provide us with the code to train & test the model, including any pre-processing etc. which is necessary to train and test the model. we have constructed a hold-out set with which we will evaluate your model. the search terms in this hold-out set are provided in the file, `candidatetestset.txt`. please use your classification model to generate predictions for each of the search terms in the hold-out set. 

adthena 
