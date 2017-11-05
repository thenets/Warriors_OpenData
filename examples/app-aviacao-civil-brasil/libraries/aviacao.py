from .csv2dict import csv2dict as csv2dict

def getAeronaves ():
    # Get content from remote
    content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/anv.csv', '~')
    
    # Get all "fabricantes"
    aeronaves = {}
    for i in content:
        aeronaves[i['aeronave_modelo']] = {}
        aeronaves[i['aeronave_modelo']]['modelo']           = i['aeronave_modelo']
        aeronaves[i['aeronave_modelo']]['assentos']         = i['aeronave_assentos']
        aeronaves[i['aeronave_modelo']]['fabricante']       = i['aeronave_fabricante']
        aeronaves[i['aeronave_modelo']]['tipo_veiculo']     = i['aeronave_tipo_veiculo']
        aeronaves[i['aeronave_modelo']]['motor_tipo']       = i['aeronave_motor_tipo']
        aeronaves[i['aeronave_modelo']]['motor_quantidade'] = i['aeronave_motor_quantidade']
            
        
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




















