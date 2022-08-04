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
    out_handle = open("CSB-master/regex/data/pubmed_results.txt", "w")
    ndata=handle.read()
    out_handle.write(ndata)
    out_handle.close()
    handle.close()
    return 

def map_science(tipo):
    """Docstring mining_pubs"""
    #if tipo == "AD":
    with open(zipcodes_coordinates.txt) as f:
        my_text = f.read()
        my_text = re.sub(r'\n\s{6}', ' ', my_text)
        zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
        unique_zipcodes = list(set(zipcodes))
        unique_zipcodes.sort()
        unique_zipcodes[:10]
        zip_coordinates = {}
        with open('data/MapOfScience/zipcodes_coordinates.txt') as f:
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
                    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
                    plt.colorbar()
                    # only continental us without Alaska
                    plt.xlim(-125,-65)
                    plt.ylim(23, 50)
                    # add a few cities for reference (optional)
                    ard = dict(arrowstyle="->")
                    plt.annotate('Moscu', xy = ( 37.6172, 55.7508),xytext = ( 37.6172, 55.7508), arrowprops = ard)
                    plt.annotate('Roma', xy = (12.4942, 41.8905), xytext = (12.4942, 41.8905), arrowprops= ard)
                    plt.annotate('Las vegas', xy = (-115.1372, 36.17497), xytext = (-115.1372, 36.17497), arrowprops= ard)
                    plt.annotate('Pekin', xy = (116.388 , 39.9035),xytext = (116.388 , 39.9035), arrowprops= ard)
                    plt.annotate('Persepolis', xy = (52.8897, 29.9358), xytext = (-116.33, 47.61), arrowprops= ard)
                    plt.annotate('Oaxaca de Juárez', xy = (-96.7203 , 17.0669), xytext = (-96.7203 , 17.0669), arrowprops= ard)
                    params = plt.gcf()
                    plSize = params.get_size_inches()
                    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
                    plt.show()
                    fig.savefig("img/mapas.jpg")
                    return
    




