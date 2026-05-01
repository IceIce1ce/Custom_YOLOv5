import glob
import shutil
import os

src_img_dir = "output"
dst_imt_dir = "images"
src_text_dir = "output"
dst_text_dir = "labels"
for jpgfile in glob.iglob(os.path.join(src_img_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_img_dir)
for textfile in glob.iglob(os.path.join(src_text_dir, "*.txt")):
    shutil.copy(textfile, dst_text_dir)
