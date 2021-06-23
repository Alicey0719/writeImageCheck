import numpy as np
import cv2
import glob
import shutil

def fmove(bf_path, af_path):
    shutil.move(bf_path,af_path)

def w_check(bf_path,af_path):
    img = cv2.imread(bf_path,cv2.IMREAD_GRAYSCALE)
    # print(np.min(img))
    # print(img)
    if np.min(img) > 230:
        fname = bf_path.split('/')
        fname = fname[len(fname)-1]
        fmove(bf_path,af_path+'/'+fname)

def file_list(path):
    files = glob.glob(path+'/*.png')
    return files

def main():
    bf_path = '.'
    af_path = './w'

    print('- Start -')
    files = file_list(bf_path)
    print('FileCount:',len(files))

    for f in files:
        w_check(f, af_path)

    print('- finish -')


main()
# w_check('./cell_south-002_digit_6_3_3.png')
# w_check('./cell_south-072_digit_8_20_0.png')
