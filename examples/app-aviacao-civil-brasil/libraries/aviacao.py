from .csv2dict import csv2dict as csv2dict

def get_aeronaves ():
    # Example
    content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/oco.csv', '~')
    return str(content[2])




















