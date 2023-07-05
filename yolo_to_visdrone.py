import os
import pandas as pd
from PIL import Image

YOLO_LABELS_PATH = "VisDrone2019-DET-test-dev/labels/"
VISANN_PATH = "VisDrone2019-DET-test-dev/annotations/"
VISIMG_PATH = "VisDrone2019-DET-test-dev/images/"

def convert(bbox, img_size):
    dw = 1 / (img_size[0])
    dh = 1 / (img_size[1])
    x = bbox[0] - bbox[2]/2
    y = bbox[1] - bbox[3]/2
    x = x / dw
    y = y / dh
    w = bbox[2] / dw
    h = bbox[3] / dh
    return (x, y, w, h)

def ChangeToVisDrone():
    if not os.path.exists(VISANN_PATH):
        os.makedirs(VISANN_PATH)

    for file in os.listdir(YOLO_LABELS_PATH):
        image_path = VISIMG_PATH + '/' + file.replace('txt', 'jpg')
        label_file = YOLO_LABELS_PATH + '/' + file
        out_file = open(VISANN_PATH + '/' + file, 'w')
        bbox = pd.read_csv(label_file, header=None, delimiter=' ').values
        img = Image.open(image_path)
        img_size = img.size
        for row in bbox:
            label = convert(row[1:5], img_size)
            out_file.write(",".join(str(f'{int(x)}') for x in label) + "," + str(row[5]) + ',' + str(int(row[0] + 1)) + ',-1,-1' + '\n')
        out_file.close()

if __name__ == '__main__':
    ChangeToVisDrone()