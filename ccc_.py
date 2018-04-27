import pandas as pd
import numpy as np
import codecs
import os
filename = "input/lvl2-0.inp"
output_file = "output.txt"

images = []
line_cnt = 0

with codecs.open(filename, "r", "utf-8") as f:
    temp = f.read().splitlines()
    stats = temp[0].split(" ")
    line_cnt += 1
    for i in range(int(stats[2])):
        img_desc = temp[line_cnt].split(" ")
        tmp_img = np.empty((int(img_desc[1]), int(img_desc[2])))
        line_cnt += 1
        for x in range(int(img_desc[1])):
            tmp_img[x] = temp[line_cnt + x].split(" ")
        images.append([img_desc, tmp_img])
        line_cnt += int(img_desc[1])

timestamps = []
for img in images:
    print((img[1]))
    if (img[1] > 0).any():
        timestamps.append(int(img[0][0]))

with codecs.open(output_file, "w", "utf-8") as f:
    for ts in sorted(timestamps):
        f.write(str(ts) + os.linesep)