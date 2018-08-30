#!/usr/bin/env python3
# ************************************************** #
# Author: Jie Chen, jiechen@link.cuhk.edu.hk
# ************************************************** #

import isce
import isceobj
from isceobj.Image.Image import Image
import gdal
import timeSeriesIO as ts
import matplotlib.pyplot as plt

# import xml.etree.ElementTree as ET

def getImageSize(infile):
    ds = gdal.Open(infile + ".vrt")
    b = ds.GetRasterBand(1)
    return b.XSize, b.YSize


if __name__ == '__main__':
    listFile = "/media/jiechencyz/Experiments_1/P120_Lena_stackProcess/merged/interferograms/unw_list"
    with open(listFile, 'r') as fileHandle:
        try:
            for fileName in fileHandle:
                fileName = fileName.rstrip()
                imageWidth, imageLength = getImageSize(fileName)
                unw = ts.load_mmap(fileName, imageWidth, imageLength, quiet=True, map='BIL',
                                   nchannels=2, channel=2, conv=False)
                # print(unw[1000:1004, 1000:1005])
                # print(getImageSize(fileName))
        finally:
            fileHandle.close()
    obj = Image()
    obj.load(fileName + ".xml")
    obj.setAccessMode('read')
    obj.createImage()
    imageOut = obj.memMap('r', 1)
    plt.imshow(imageOut, cmap='jet', vmin=-60, vmax=-30)
    plt.colorbar()
    plt.show()