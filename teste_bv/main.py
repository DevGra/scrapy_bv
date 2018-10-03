#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, zipfile, StringIO, os, shutil

path_download = '/var/tmp/download/'
if not os.path.isdir(path_download):
    os.mkdir(path_download)

path_pasta = '/var/tmp/arquivos_teste'
if not os.path.isdir(path_pasta):
    os.mkdir(path_pasta)

path_pasta_pdf = path_pasta+'/pdf'
if not os.path.isdir(path_pasta_pdf):
    os.mkdir(path_pasta_pdf)

path_pasta_txt = path_pasta+'/txt'
if not os.path.isdir(path_pasta_txt):
    os.mkdir(path_pasta_txt)

url = 'http://download.inep.gov.br/microdados/microdados_aneb_prova_brasil_2013.zip'

r = requests.get(url, stream=True)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall(path_download.encode('utf-8'))

for folderName, subfolders, filenames in os.walk(path_download):

    for files in filenames:
        if files.endswith('.pdf'):
            shutil.copy(os.path.join(folderName, files), path_pasta_pdf)

        if files.endswith('.txt'):
            shutil.copy(os.path.join(folderName, files), path_pasta_txt)





