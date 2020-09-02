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

pastas = ['audio', 'video/outros-takes', 'imagens/fotos']

createFolderFromList(pastas, 'teste1')