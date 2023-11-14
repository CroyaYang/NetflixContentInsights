# NetflixContentInsights
KM6312 Group Work Project

Netflix Content Insights: A Comprehensive Analysis of Movies and TV Shows

DATAET FROM: https://www.kaggle.com/datasets/shivamb/netflix-shows
# 目录结构
| folders               |                   |
|-----------------------|-------------------|
| dataset               |                         |
| ├── original          | original dataset   |
| └── preprocess        | 划分Train/Val/Test+简单预处理后数据集 |
| Category_Predict      | Task3 model       |
| Rating_Predict        | Task4 model       |
| Instructions          | guideline from teacher |

# Task3(GOING)
Predict category according to description&title

SVM;Decision Trees;Fastext;CNN

Problem：

每个作品的类别往往有多个。举个例子，真爱至上会有三个类别：爱情，喜剧，都市。这使得我们的分类任务不是简单的一维输出分类，而是多标签分类问题。

在第一版的解决思路中，为了简化我们的任务，回到简单的一维输出分类任务，我在数据集处理部分保留了每个作品的多个类别中的第一个类别，这样我们要预测的标签就是唯一的。但这样会造成新的问题：不符合实际生活，类别数目超过40个，导致准确率极低。

所以目前采取第二个解决方案。对于每个样本，标签应该是一个二进制向量，表示每个可能的类别是否存在。例如，如果有三个类别：爱情，喜剧，都市，则样本的标签可能是 [1, 1, 1] 表示这个作品属于这三个类别，而 [0, 1, 0] 表示只属于喜剧类别。

# Github使用
### 通过git clone得到本地仓库
	git clone https://github.com/YANGKeyan/NetflixContentInsights.git

### 在本地仓库（文件夹）工作完成后，要上传文件：
	git pull origin main

	git add 要上传/更新的文件名称

	git commit -m "说明更改了什么"

	git push

