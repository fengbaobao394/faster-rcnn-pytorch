使用faster-rcnn来训练自己的数据
===
此代码的运行环境为ubuntu+python3.6+cuda9.2+torch0.3.0+torchvision0.2.1
---

**建议在torch0.4.0及以下版本运行，否则可能导致运行bug。不建议在windows下进行操作，会出现一个调用so包的问题。**

前期准备
---
1、数据集是NWPU VHR-10 dataset航空遥感数据集，此数据集包括650张图片和对应标签，150张测试图片(未标注)。由于测试图片未标注，本文将数据集中的550张图片作为训练集，100张图片作为测试集。划分后的数据集放在以下链接[NWPU VHR-10 dataset](https://pan.baidu.com/s/1_VVA7uWcocrzbPiRI7HYvA 
)，提取码**sbcq**。
\<br>2、



