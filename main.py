import processing.GearBuilder as GearBuilder
import processing.menus as menus
from flask import Flask
import pickle
import requests
import requests.auth
import json
from flask_bootstrap import Bootstrap
import flaskwebserver.webserver as webserver
import manifest
import os


if os.path.isfile(r'C:\Users\Jake\Downloads\WinPython-64bit-3.5.3.0Qt5\notebooks\Manifest.content') == False:
    manifest.get_manifest()
    manifest.all_data = manifest.build_dict(manifest.hashes)
    with open('manifest.pickle', 'wb') as data:
        pickle.dump(manifest.all_data, data)
    print("'manifest.pickle' created!\nDONE!")
else:
    print('Pickle Exists')


# initialise the app:
app = Flask(__name__)
app.secret_key = r'its a secret'
bootstrap = Bootstrap(app)

oauth_session = requests.Session()

# Add you API-KEY-HERE!
API_KEY = "apiKey"
HEADERS = {"X-API-Key": API_KEY }

# Open Manifest:
with open(r'C:\Users\Jake\Downloads\WinPython-64bit-3.5.3.0Qt5\notebooks\manifest.pickle', 'rb') as data:
	all_data = pickle.load(data)

@app.route('/')
@app.route('/index')
def index():
	return webserver.index()
    
@app.route('/vault')
def vault():
	return webserver.vault()

@app.route('/callback/bungie')
def bungie_callback():
    return webserver.bungie_callback()

webserver.create_self_signed_cert(r'C:\Users\Jake\Downloads\WinPython-64bit-3.5.3.0Qt5\notebooks\BuildBuilder-master')

# Main program - call app:	
if __name__ == '__main__':
	# User needs to add these:
	context = (webserver.CERT_FILE, webserver.KEY_FILE)
	app.run(debug=True, port=5000, ssl_context=context)

