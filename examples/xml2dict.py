import requests, xmltodict, unicodedata, collections

# XML url
XML_URL = 'https://raw.githubusercontent.com/servicosgovbr/cartas-de-servico/master/cartas-servico/v3/lista-completa-servicos.xml'

# Get XML from URL
with requests.Session() as session:
    request = session.get(XML_URL)
    content = request.content
    
    # Parse XML to dict
    CONTENT_DICT = xmltodict.parse(content)
    
    # Encode (remove special characters)
    def normalize_dict(d):
        # Check if is iterable but not string
        try:
            if(not isinstance(d, str)):
                # Recursive method call
                for i in d:
                    print('class', d.__class__)
                    normalize_dict(i)
            
        except Exception as e:
            print(e)
            if(isinstance(d, str)):
                d = unicodedata.normalize('NFKD', str(d)).encode('ASCII','ignore').decode('ASCII')
                print(d)
            
    normalize_dict(CONTENT_DICT)
                
        

# Example of output
# print(CONTENT_DICT)