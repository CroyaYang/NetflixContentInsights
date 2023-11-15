# NetflixContentInsights
KM6312 Group Work Project

Netflix Content Insights: A Comprehensive Analysis of Movies and TV Shows

DATASET FROM: https://www.kaggle.com/datasets/shivamb/netflix-shows

# 目录结构
| folders               |                   |
|-----------------------|-------------------|
| dataset               |                         |
| ├── original          | original dataset   |
| └── preprocessed       | 划分Train/Val/Test+简单预处理后数据集 |
| Category_Predict      | Task3 model       |
| Rating_Predict        | Task4 model       |
| Instructions          | guideline from teacher |
# Task3(暂缓)
## Predict category according to description&title

compare the following models performance:

SVM;Decision Trees;Fastext;CNN

## Problem：

每个作品的类别往往有多个。举个例子，《真爱至上》会有三个类别：爱情，喜剧，都市。这使得分类任务不是简单的一维输出分类，而是多标签分类问题。

第一种解决思路：为了简化任务回到简单的一维输出分类任务，在数据集处理部分保留每个作品的多个类别中的第一个类别。这样要预测的标签就是唯一的。但会造成新的问题：不符合实际生活需要，类别数目超过40个，准确率极低。

所以目前采取第二种解决方案：对于每个样本，目标标签应该是一个二进制向量，表示每个可能的类别是否存在。例如，如有三个类别：爱情，喜剧，都市，则样本标签是 [1, 1, 1] 表示作品属于这三个类别，而 [0, 1, 0] 表示只属于喜剧类别。

如此，任务被确定为多标签文本分类任务，Extreme Multi-label Text Classification，简称XMTC，即对于一个给定的文本，可能有多个标签，我们需要设计模型预测其标签。

*所以，在这个任务中，模型输出层的激活函数应该采用sigmoid，而不是softmax。因为每个类别都是独立的，而不是互斥的。


take tensorfow as an example:

	model.add(Dense(num_classes, activation='sigmoid'))

*由于这是多标签分类任务，单一标签的准确率accuracy不足以评估整体性能。故而考虑采用其他指标，如F1-score，平均准确率等。

*多标签文本分类任务难度略大，暂且搁置，先做下一个模型。

# Task4(ON GOING)

单一标签分类问题，根据作品标题title和描述description预测它的分级rating。

原始数据集中分级rating有14种，并且每个类别的数量差异过大（最多的类别有3000+数据，最少的类别只有20+数据）

所以为缓解类别不均衡，就根据14种分级的目标群众年龄，重新划分为'Teens', 'Adults', 'Older Kids', 'Kids'四个类别，保存在target_age列中。

任务即，根据作品标题title和描述description预测它的target_age。

compare the following models performance:

SVM;Decision Trees;Fastext;CNN

*现面临问题：尝试了多个模型后（CNN LSTM SVM NB ResNet MLP..）得到验证集和测试集准确率均在50%+，即始终存在验证集准确率不高并持平、学不到东西的问题。初步推测依然由于数据集类别不平衡，所以在数据集拆分环节采用了分层拆分方法，但没有帮助。然后采用K-Fold交叉验证方法，但没有本质上缓解这个问题。需要周六和老师沟通如何解决，可能此数据集本身不太适合做预测或分类工作。

*但我有找到一个在此数据集基础上多一列作品评分的数据集。最后的下下策是更换任务，预测作品评分。先准备其他考试了orz

# 简要Github使用
### 通过git clone得到本地仓库
	git clone https://github.com/YANGKeyan/NetflixContentInsights.git

### 在本地仓库（文件夹）工作完成后，要上传文件：
	git pull origin main

	git add 要上传/更新的文件名称

	git commit -m "说明更改了什么"

	git push

