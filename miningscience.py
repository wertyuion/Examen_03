import csv
import pandas as pd
import re
from Bio import Entrez 

def download_pubmed(keyword): 
    """ Función para la extaccion de articulos desde pubmed """
    
     
    from Bio import Entrez
 
    
    Entrez.email = "natasha.deleg@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed",
                        term= keyword,
                        usehistory="y")
    record=Entrez.read(handle)
    id_list = record["IdList"]# generar lista 
    record["Count"]
    webenv=record["WebEnv"]
    query_key=record["QueryKey"]
    handle=Entrez.efetch(db="pubmed",
                      rettype='medline',
                      retmode="text",
                      retstart=0,
                      retmax=543, webenv=webenv,
    query_key=query_key)
    out_handle = open(keyword+".txt", "w")
    ndata=handle.read()
    out_handle.write(ndata)
    out_handle.close()
    handle.close()
    return 

def map_science(tipo):
    #if tipo == "AD":
    with open(tipo) as f:
        my_text = f.read()
    my_text = re.sub(r'\n\s{6}', ' ', my_text)  
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    unique_zipcodes = list(set(zipcodes))
    zip_coordinates = {}
    with open('zipcodes_coordinates.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
         zip_coordinates[row['ZIP']] = [float(row['LAT']), float(row['LNG'])]
    zip_code = []
    zip_long = []
    zip_lat = []
    zip_count = []
    for z in unique_zipcodes:
    # if we can find the coordinates
        if z in zip_coordinates.keys():
            zip_code.append(z)
            zip_lat.append(zip_coordinates[z][0])
            zip_long.append(zip_coordinates[z][1])
            zip_count.append(zipcodes.count(z))
    import matplotlib.pyplot as plt
    #%matplotlib inline
    fig = plt.figure()
    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
    plt.colorbar()
# only continental us without Alaska
    plt.xlim(-125,-65)
    plt.ylim(23, 50)
# add a few cities for reference (optional)
    ard = dict(arrowstyle="->")
    plt.annotate('Misuri', xy = (-93.219489, 36.560353), 
                   xytext = (-93.219489, 36.560353), arrowprops = ard)
    plt.annotate('Minong', xy = (-91.803653, 46.123003), 
                   xytext = (-91.803653, 46.123003), arrowprops= ard)
    plt.annotate('Alaska', xy = (-131.693301, 56.37075), 
                   xytext = (-131.693301, 56.37075), arrowprops= ard)
    plt.annotate('Pensilvania', xy = (-75.781445 , 40.539070), 
                   xytext = (-75.781445, 40.539070), arrowprops= ard)
    plt.annotate('Maine', xy = (-68.589614, 45.183587), 
                   xytext = (-68.589614, 45.183587), arrowprops= ard)
    plt.annotate('Indiana', xy = (-85.849206, 41.479526), 
                   xytext = (-85.849206, 41.479526), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    fig.savefig("img/mapas.jpg")
    return 


    




