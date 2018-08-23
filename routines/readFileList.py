#!/usr/bin/env python3
# ************************************************** #
# Author: Jie Chen, jiechen@link.cuhk.edu.hk
# ************************************************** #

fileName = "/media/jiechencyz/Experiments_1/P120_Lena_stackProcess/merged/interferograms/unw_list"
fileList = []
with open(fileName, 'r') as fileHandle:
    try:
        for line in fileHandle:
            fileList.append(line)
    finally:
        fileHandle.close()
