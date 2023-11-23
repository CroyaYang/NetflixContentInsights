# NetflixContentInsights
KM6312 Group Work Project

Netflix Content Insights: A Comprehensive Analysis of Movies and TV Shows

DATASET FROM: https://www.kaggle.com/datasets/shivamb/netflix-shows

# Directory Structure
| folders               |                   |
|-----------------------|-------------------|
| dataset               |                     |
| ├── original          | original dataset   |
| └── Task3preprocessed | processed dataset for category predict |
| Category_Predict      | Task3 model       | 
| ├── models          | models saved for category predict |
| └── demo            | Model deployment with Flask  |
|	├── static      | css&images |
|	└── templates      | html |
| Rating_Predict(quit)    | quit task, plz ignore |
| Class_Instructions      | pics used in md |
| Pics          | guideline from teacher |
# Task1: Exploratory Data Analysis(Done)
# Task2: Clustering(To do)
# Task3: Category_Predict(Done)
## Predict category according to description&title

### 11.13 Problem update：

There are often multiple categories for each production. For example, True Blood will have three categories: romance, comedy, and urban. This makes the categorization task not a simple one-dimensional output classification, but a multi-label classification problem.

The first solution idea: to simplify the task back to simple one-dimensional output categorization, only the first of the multiple categories of each work is kept in the processing part of the dataset, making the label to be predicted unique. However, a new problem is created: it no longer meets real-life needs and leads to very low accuracy because the main category is often not the first one.

### 11.14 update：

So the second solution is currently adopted: for each sample, the target label should be a binary vector indicating whether each category exists or not. For example, if there are three categories: romance, comedy, and urban, the sample label [1, 1, 1] , indicates that the work belongs to these three categories. While [0, 1, 0] indicates that it belongs only to the comedy category. In this way, the task is identified as Extreme Multi-label Text Classification (XMTC), a classical task in text categorization tasks, i.e., for a given text, there may be more than one label, and we need to design models to predict the probability of its different labels.

*So, the activation function for the output layer of the model uses sigmoid instead of softmax. because each category is independent and not mutually exclusive.

*Since this is a multi-label classification task, single label accuracyaccuracy is not sufficient to evaluate the overall performance. Therefore, other metrics such as F1-score, average accuracy, etc. are considered.

### 11.15 update：

Multi-label text categorization task is slightly more difficult, try some models to get test accuracy are around 20%.

### 11.16 update:

Inspired by other XMTC projects, try the OneVsRest approach. That is, converting a multi-class classification problem into a series of binary classification problems.

### 11.18 update:

Tried tfidf processing features + OneVsRest classifier and it worked out fine!👍

![Current resluts](Pics/task3result.png)

The dataset preprocessing for this task was updated accordingly and the folder structure was reclassified.

### 11.23 update：

Simple model deployment was accomplished using Flask, allowing the model to be used as a tool in the form of a web page.

![Template page layout](Pics/demo.png)

# Task4: Rating_Predict(Quit)
## Predict Rating according to description&title
### 11.15 update:

单一标签分类问题，根据作品标题title和描述description预测它的分级rating。

原始数据集中分级rating有14种，并且每个类别的数量差异过大（见预处理记事本可视化情况，最多的类别有3000+数据，最少的类别只有20+数据）

所以为缓解类别不均衡，就根据14种分级的目标群众年龄，重新划分为'Teens', 'Adults', 'Older Kids', 'Kids'四个类别，保存在新列target_ages中。

任务即变化为，根据作品标题title和描述description分类它的target_age。

compare the following models performance:

SVM;Decision Trees;Fastext;CNN

*现面临问题：我们尝试了多个模型后（CNN LSTM SVM NB ResNet MLP..）训练集正常收敛，但网格搜参后每个模型最佳参数情况下得到验证集和测试集准确率均在50%+，验证集存在从头到尾准确率不变、学不到东西的问题。初步推测依然是数据集类别不平衡造成，所以目前数据集拆分更新为分层拆分方法，但没有帮助。然后采用K-Fold交叉验证方法，但没有本质上解决这个问题。可能此数据集本身不太适合做预测或分类工作。也可能是个人采用方法有问题。等下次meeting讨论。

###  11.18 update:

Try to process features with tfidf but in vain.

###  11.22 update:

Try finetune BERT, accuracy score is still poor. 

After reviewing related work, we found that no one has solved this problem yet. The reason for this is inferred to be that the profiles provided by netflix are not closely linked to age grading. So we decided to abandon this task.

# Simple Github Guidance
### Get the local repository via git clone
	git clone https://github.com/YANGKeyan/NetflixContentInsights.git

### To upload a file after working on the local repository (folder):
	git pull origin main

	git add Name of the file to be uploaded/updated

	git commit -m "Description of what was changed"

	git push