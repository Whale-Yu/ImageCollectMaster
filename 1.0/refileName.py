# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/6/17 12:47
# @Author :yujunyu
# @Site :
# @File :refileName.py
# @software: PyCharm

import os
#
# ls=os.listdir("C:\Users\yujunyu\Desktop\apple")for k,i in enumerate(ls):
#     if "jpg" in i:
#         os.rename(i, "apple_" + str(k) + ".jpg")

# import os
# ls=os.listdir("apple")
# k=1
# for i in ls:
#     if "jpg" in i:
#         os.rename(i,"fall_"+str(k)+".jpg")
#         k+=1
import os
from PIL import Image

# Image extension supported.
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp', 'jpeg', 'JPEG','xml'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def is_valid_image(img_path: str) -> bool:
    bvalid = True
    try:
        Image.open(img_path).verify()
    except:
        bvalid = False
    return bvalid

def rename(img_path: str, index: int) -> None:
    filelist = os.listdir(img_path)
    total_num = len(filelist)
    count = 0
    for item in filelist:
        if allowed_file(item):
            filename_suffix = '.' + item.rsplit('.', 1)[1]
            src = os.path.join(os.path.abspath(img_path), item)
            dst = os.path.join(os.path.abspath(img_path), '00' + format(str(index), '0>4s') + filename_suffix)
            try:
                os.rename(src, dst)
                print('converting %s to %s' % (src, dst))
                index = index + 1
                count = count + 1
            except:
                index = index + 1
                continue
    print('total %d to rename & converted %d jpgs' % (total_num, count))

if __name__ == '__main__':
    img_dir = 'Annotations'
    index = 0
    rename(img_dir, index)