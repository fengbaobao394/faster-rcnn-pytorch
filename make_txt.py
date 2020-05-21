import os
import glob


IMAGE_LIST_FILE = "text.txt"
#img_path='Data/picture_data/JPEGImages/'
img_path="F:/yiming/image/"
txt_path='Data/picture_data/'
IMAGE_NUM = len(glob.glob(img_path + '*.jpg'))
f = open( os.path.join(txt_path, IMAGE_LIST_FILE), 'w')
for i in range (IMAGE_NUM):
    print(i)
    f.write(str(i).zfill(3) + '\n')
#f.close()
print('FINISHED!')


