import os 
import sys
import json
import urllib.request
from pathvalidate import sanitize_filename

def createFolderFromList(folders, baseFolder=''):
    baseFolder = sanitize_filename(baseFolder)

    for folder in folders:
        folderName = os.path.join(baseFolder, folder)
        os.makedirs(folderName, True)

def downloadFilesFromList(files, baseFolder=''):
    baseFolder = sanitize_filename(baseFolder)

    for file in files:
        link = files["from"]
        destination = file["to"]
        fileName = link.rplit("/", 1)[-1]
        fullPathFile = os.path.join(baseFolder, destination, fileName)

        if not os.path.isfile(fullPathFile):
            print(f'BAIXANDO...{link}')
            urllib.request.urlretrieve(link, fullPathFile)

links = {"from": "http://127.0.0.1:5500/samples/cdtv-mao-no-codigo-prproj", "to": ""}


#pastas = ['audio', 'video/outros-takes', 'imagens/fotos']
#createFolderFromList(pastas, 'teste1')

downloadFilesFromList(links, "teste1")