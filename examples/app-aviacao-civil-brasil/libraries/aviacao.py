from .csv2dict import csv2dict as csv2dict

def getAeronaves (indexed_by='aeronave_modelo'):
    ''' Return list of Aeronaves
    
    - codigo_ocorrencia
    - aeronave_matricula
    - aeronave_operador_categoria
    - aeronave_tipo_veiculo
    - aeronave_fabricante
    - aeronave_modelo
    - aeronave_tipo_icao
    - aeronave_motor_tipo
    - aeronave_motor_quantidade
    - aeronave_pmd
    - aeronave_pmd_categoria
    - aeronave_assentos
    - aeronave_ano_fabricacao
    - aeronave_pais_fabricante
    - aeronave_pais_registro
    - aeronave_registro_categoria
    - aeronave_registro_segmento
    - aeronave_voo_origem
    - aeronave_voo_destino
    - aeronave_fase_operacao
    - aeronave_tipo_operacao
    - aeronave_nivel_dano
    - aeronave_dia_extracao
    - total_fatalidades
    '''
    # Get content from remote
    content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/anv.csv', '~')
    
    # Search for "aeronave" by "indexed_by"
    aeronaves = {}
    for i in content:
        aeronaves[i[indexed_by]] = {}
        for k in i.keys():
            aeronaves[i[indexed_by]][k] = i[k]
    
    return aeronaves


def getOcorrencias (indexed_by='codigo_ocorrencia'):
    ''' Return list of Ocorrências
    
    - codigo_ocorrencia
    - aeronave (dict)
    - ocorrencia_classificacao
    - ocorrencia_tipo
    - ocorrencia_latitude
    - ocorrencia_longitude
    - ocorrencia_cidade
    - ocorrencia_uf
    - ocorrencia_pais
    - ocorrencia_aerodromo
    - ocorrencia_dia
    - ocorrencia_horario
    - ocorrencia_saida_pista
    - ocorrencia_dia_extracao
    - investigacao_aeronave_liberada
    - investigacao_status
    - divulgacao_relatorio_numero
    - divulgacao_relatorio_publicado
    - divulgacao_dia_publicacao
    - total_recomendacoes
    - total_aeronaves_envolvidas
    '''
    # Get content from remote
    ocorrencias_dict = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/oco.csv', '~')
    aeronaves_dict = getAeronaves('codigo_ocorrencia')
    
    # Get all "ocorrencias"
    ocorrencias = {}
    for i in ocorrencias_dict:
        ocorrencias[i[indexed_by]] = {}
        for k in i.keys():
            ocorrencias[i[indexed_by]][k] = i[k]
    
        # Get aeronave data
        if(indexed_by == 'codigo_ocorrencia'):
            ocorrencias[i[indexed_by]]['aeronave'] = aeronaves_dict[ocorrencias[i[indexed_by]]]
        
    return ocorrencias















