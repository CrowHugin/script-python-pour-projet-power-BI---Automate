from zipfile import ZipFile 
from urllib import request
import shutil

#---------Downalod du fichier--------
URL = "https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip"
response = request.urlretrieve(URL, "eCO2mix_RTE_En-Cours-TR.zip")
file = "eCO2mix_RTE_En-Cours-TR.zip"
  

#----------extraire le fichier sous format xls--------------

with ZipFile(file, 'r') as zip: 
    # extraire tous les fichiers
    print('extraction...') 
    zip.extractall() 
    print('Terminé!')



#---------------Copier le fichier sous format xlsx------------------------------
shutil.copyfile("eCO2mix_RTE_En-cours-TR.xls","donnes.xlsx")
