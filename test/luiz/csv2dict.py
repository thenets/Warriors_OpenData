import csv, requests, unicodedata

# CSV2DICT
def csv2dict (csv_url, csv_delimiter):
    # Set CSV URL
    CSV_URL = csv_url

    with requests.Session() as session:
        # Outout CONTENT_LIST
        CONTENT_LIST = []

        # Get CSV from remote
        request = session.get(CSV_URL)
        encoded_content = request.content.decode(request.encoding)

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
            
# Example
content = csv2dict('https://raw.githubusercontent.com/nosbielcs/opendata_aig_brazil/master/data/oco.csv', '~')
print(content[2])   
        