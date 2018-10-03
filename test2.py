#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import zipfile
import StringIO
import os
import shutil


path_pasta = '/var/tmp/arquivos_teste'
path_pasta_pdf = '/var/tmp/arquivos_teste/pdf'
path_pasta_txt = '/var/tmp/arquivos_teste/txt'
path_download = '/var/tmp/download/arquivos_microdados'

#for filename in os.listdir(path_download):
#    print(filename)

#for folderName, subfolders, filenames in os.walk('/var/tmp/download/teste'):
for folderName, subfolders, filenames in os.walk('/var/tmp/download/teste/metadados'):
    # print("Nome da pasta: "+ folderName)
    # print("Nome da subpasta: "+ folderName + ' em: ' + str(subfolders))
    # print("Nome do arquivo: "+ folderName + ' em: ' + str(filenames))
    # print()
    # print()

    for subfolder in subfolders:
        print(subfolder)
        print()
    for arq in filenames:
        if arq.endswith('.txt'):
            shutil.copy(os.path.join(folderName, arq), path_pasta_txt)

        if arq.endswith('.pdf'):
            shutil.copy(os.path.join(folderName, arq), path_pasta_pdf)