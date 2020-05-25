使用faster-rcnn来训练自己的数据
===
此代码的运行环境为ubuntu+python3.6+cuda9.2+torch0.3.0+torchvision0.2.1+GTX1080ti
---

**建议在torch0.4.0及以下版本运行，否则可能导致运行bug。不建议在windows下进行操作，会出现一个调用so包的问题。**

前期准备
---
1、数据集是NWPU VHR-10 dataset航空遥感数据集，此数据集包括650张图片和对应标签，150张测试图片(未标注)。由于测试图片未标注，本文将数据集中的550张图片作为训练集，100张图片作为测试集。划分后的数据集放在以下链接[NWPU VHR-10 dataset](https://pan.baidu.com/s/1_VVA7uWcocrzbPiRI7HYvA 
)，提取码**sbcq**;  
2、Data\pretrained_model中的预训练模型[vgg16_caffe.pth](https://pan.baidu.com/s/1B2Y2gFRaYg1IqvukmKrbzQ)下载，提取码**sea6**;  
3、训练后的模型Output/[faster_rcnn_150_275.pth](https://pan.baidu.com/s/1-JaGpYsP921Ovn59VcmqHw)下载，提取码**r9cf**，这是我进行150次迭代训练后的模型，文件较大约1.5G,不想训练的话可以直接下载进行预测看看效果。  


代码运行流程
---
1、前期准备完成1，2两项后，现在开始代码运行；  
2、进入lib文件夹 ：命令行输入cd lib，编译程序需要用到的组件如nms与roi-pooling：sh make.sh，**此步很重要，重要！**，不然后面会找不到_nms库；   
3、开始运行trainval_net.py文件；  
4、待模型训练好后，运行demo.py进行预测，预测结果保存在demo/result/下；  
5、**注：**在训练自己的数据集时前，需要在Data/picture_data/下生成一个train.txt文件，此文件包含了训练图片的名称(没有图片格式后缀)，需要先运行下make_train_txt.py生成train.txt文件。  


参考
---
[https://github.com/Liu-Yicheng/Faster-rcnn](https://github.com/Liu-Yicheng/Faster-rcnn)



