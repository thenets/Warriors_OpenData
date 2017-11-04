import requests, xmltodict, unicodedata

# XML url
XML_URL = 'https://raw.githubusercontent.com/servicosgovbr/cartas-de-servico/master/cartas-servico/v3/lista-completa-servicos.xml'

# Get XML from URL
with requests.Session() as session:
    request = session.get(XML_URL)
    
    print(request.encoding)
    exit(1)
    
    # Encode (remove special characters)
    encoded_content = unicodedata.normalize('NFKD', str(request.content))

    # Parse XML to dict
    CONTENT_DICT = xmltodict.parse(encoded_content)

# Example of output
print(CONTENT_DICT)