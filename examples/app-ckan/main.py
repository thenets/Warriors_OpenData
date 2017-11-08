# Basic libs
import requests, json

# CKAN API
from ckanapi import RemoteCKAN

# Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Setup CKAN remote
    ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    dadosgovbr = RemoteCKAN('http://dados.gov.br', user_agent=ua)
    
    # Get all organizations
    organizations_name = dadosgovbr.action.organization_list()
    
    # Get full data of each organization
    # FOR DEBUG: http://dados.gov.br/api/3/action/organization_show?id=agencia-nacional-de-aguas-ana
    organizations = {}
    for name in organizations_name:
        organizations[name] = dadosgovbr.action.organization_show(id=name)
        break
    print(str(organizations['agencia-nacional-de-aguas-ana']['display_name']).encode('ASCII','ignore').decode('ASCII'))
    
    return render_template('home.html', organizations=organizations)

@app.route('/simple')
def simple():
    return "This is a simple string return."

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9007)