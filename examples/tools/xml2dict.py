import requests, xmltodict, xmltodict, json, unicodedata

import sys
print(sys.getdefaultencoding())

# XML url
XML_URL = 'https://raw.githubusercontent.com/servicosgovbr/cartas-de-servico/master/cartas-servico/v3/lista-completa-servicos.xml'

# Get XML from URL
with requests.Session() as session:
    request = session.get(XML_URL)
    content = request.content
    
    # Parse to JSON to fix encode
    xml_dict = xmltodict.parse(content)
    j = json.dumps(xml_dict)
    j_encoded = j
    CONTENT_DICT = json.loads(j_encoded)
    
    with open('../test.txt', 'w') as f:
        f.write(j)

# Example of output
print(CONTENT_DICT)
