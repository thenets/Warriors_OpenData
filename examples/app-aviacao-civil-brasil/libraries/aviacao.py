from .csv2dict import csv2dict as csv2dict

def getAeronaves ():
    # Get content from remote
    content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/anv.csv', '~')
    
    # Get all "fabricantes"
    aeronaves = []
    for i in content:
        aeronaves.append(i['aeronave_modelo'])
    aeronaves = list(set(aeronaves)) # remove equals
        
    return aeronaves

def getFabricantes ():
    # Get content from remote
    content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/anv.csv', '~')
    
    # Get all "fabricantes"
    fabricantes = []
    for i in content:
        fabricantes.append(i['aeronave_fabricante'])
    fabricantes = list(set(fabricantes)) # remove equals
        
    return fabricantes




















