import csv, requests, unicodedata, hashlib, os

# CSV2DICT
def csv2dict (csv_url, csv_delimiter):
    ''' csv2dict
    Get CSV from URL and convert to Python dict().
    
    Params:
        - csv_url: URL from remote
        - csv_delimiter: Delimiter (example: '~' or '.')
    '''
    # Set CSV URL
    CSV_URL = csv_url

    with requests.Session() as session:
        # Outout CONTENT_LIST
        CONTENT_LIST = []
        
        # Get hash from content
        hash_object = hashlib.sha512(str(CSV_URL).encode('utf-8'))
        hex_dig     = hash_object.hexdigest()
        
        # Create cache dir if not exist
        cache_path = '__pycache__/csv2dict/'
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        
        # Check cached file and load if exists
        cache_file = cache_path + str(hex_dig)
        if(os.path.exists(cache_file)):
            encoded_content = open(cache_file, 'r', encoding='utf-8').read()

        # Get CSV from remote if cache doesn't exist
        else:
            request = session.get(CSV_URL)
            encoded_content = request.content.decode(request.encoding)
            open(cache_file, 'w', encoding='utf-8').write(encoded_content)
                
        # Create list of all elements
        cr = csv.reader(encoded_content.splitlines(), delimiter=csv_delimiter)
        lines = list(cr)

        # CSV header (colunm names)
        colunm_names = lines.pop(0)

        # Fix encode
        for l_i, line in enumerate(lines):
            for c_i, colunm in enumerate(line):
                lines[l_i][c_i] = unicodedata.normalize('NFKD', colunm).encode('ASCII','ignore').decode('ASCII')

        # Create CONTENT_LIST
        for l_i, line in enumerate(lines):
            tmpItem = {}
            for c_i, colunm in enumerate(line):
                tmpItem[colunm_names[c_i]] = lines[l_i][c_i]
            CONTENT_LIST.append(tmpItem)
    
        return CONTENT_LIST
            