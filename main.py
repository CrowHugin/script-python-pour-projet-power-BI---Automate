from zipfile import ZipFile 
from urllib import request

URL = "https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip"

response = request.urlretrieve(URL, "eCO2mix_RTE_En-Cours-TR.zip")

file = "eCO2mix_RTE_En-Cours-TR.zip"
  
# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    zip.printdir() 
  
    # extraire tous les fichiers
    print('extraction...') 
    zip.extractall() 
    print('Terminé!')

