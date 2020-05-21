import os

image_path = 'F:/yiming/image/'
label_path = 'F:/yiming/label/'


# 获取该目录下所有文件，存入列表中
image = os.listdir(image_path)
label = os.listdir(label_path)
n = 0
m=0
for i in image:
    # 设置旧文件名（就是路径+文件名）
    image_oldname = image_path + image[n][:-4]+'.jpg'
    label_oldname = label_path + image[n][:-4]+'.xml'

    # 设置新文件名
    #newname = path + str(n) + '.png'
    image_newname = image_path + str(m).zfill(3)+'.jpg'
    label_newname = label_path + str(m).zfill(3)+'.xml'

    # 用os模块中的rename方法对文件改名
    os.rename(image_oldname, image_newname)
    os.rename(label_oldname, label_newname)
    print(image_oldname, '======>', image_newname)
    print('\n')
    print(label_oldname, '======>', label_newname)
    print('\n\n')

    n += 1
    m+=1