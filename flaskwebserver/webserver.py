from flask import abort, request, redirect, url_for, render_template, session
from datetime import datetime, timedelta
import requests
import requests.auth
import json
import time
import bungieNetActions
import urllib
from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join

oauth_session = requests.Session()

# Add you API-KEY-HERE!
API_KEY = "be18f1d3b5674727b073af7dd46f5a75"
HEADERS = {"X-API-Key": API_KEY }

REDIRECT_URI = 'https://localhost:5000/callback/playstation'
AUTH_URL = 'https://www.bungie.net/en/Application/Authorize/12215?' # AUTH_URL is authorization url for app from bungie
access_token_url = 'https://www.bungie.net/Platform/App/GetAccessTokensFromCode/'
refresh_token_url = 'https://www.bungie.net/Platform/App/GetAccessTokensFromRefreshToken/'

# This function is for linking to the index.html file
def index():
	state =  make_authorization_url()
	state_params = {'state': state}
	url = AUTH_URL + urllib.parse.urlencode(state_params)
	print(url)
	return render_template('index.html', url=url)

def vault():
	userSummary = bungieNetActions.GetCurrentBungieAccount(oauth_session)
	session['destinyMembershipId'] 	= str(userSummary.json()['Response']['destinyAccounts'][0]['userInfo']['membershipId'])
	session['membershipType'] = str(userSummary.json()['Response']['destinyAccounts'][0]['userInfo']['membershipType'])
	session['displayName'] 	= str(userSummary.json()['Response']['destinyAccounts'][0]['userInfo']['displayName'])
	return render_template(
		'vault.html', 
		character = userSummary.json()['Response']['destinyAccounts'][0]['userInfo']['displayName'], 
		lightLevel = userSummary.json()['Response']['destinyAccounts'][0]['characters'][0]['powerLevel'],
		emblemImage = userSummary.json()['Response']['destinyAccounts'][0]['characters'][0]['emblemPath'],
		backgroundImage	= userSummary.json()['Response']['destinyAccounts'][0]['characters'][0]['backgroundPath']
		) 

# This function will generate a random string to be a code that is used for extra protection
def make_authorization_url():
	# Generate a random string for the state parameter
	# Save it for use later to prevent xsrf attacks
	from uuid import uuid4
	state = str(uuid4())
	save_created_state(state)
	return state

def bungie_callback():
	error = request.args.get('error', '')
	if error:
		return "Error: " + error
	state = session.get('state_token')
	if not is_valid_state(state):
		## Uh-oh, this request wasn't started by us!
		print("Uh-oh, this request wasn't started by us!")
		abort(403)
	session.pop('state_token', None)
	code = request.args.get('code')
	authorisation_code = code
	token = get_token(code)
	return redirect(url_for('index'))
	
def get_token(code):
	post_data = {'code': code}
	response = requests.post(access_token_url, json=post_data, headers=HEADERS)
	token_json = response.json()['Response']['accessToken']['value']
	refresh_json = response.json()['Response']['refreshToken']['value']
	refresh_ready = datetime.now() + timedelta(seconds=int(response.json()['Response']['refreshToken']['readyin']))
	refresh_expired = datetime.now() + timedelta(seconds=int(response.json()['Response']['refreshToken']['expires']))
	save_session(token_json)
	return token_json
	
# Update Session:
def save_session(token_json):
	print("Updating session")
	oauth_session.headers["X-API-Key"] = API_KEY
	oauth_session.headers["Authorization"] = 'Bearer ' + str(token_json)
	access_token = "Bearer " + str(token_json)


# Save state parameter used in CSRF protection:	
def save_created_state(state):
	session['state_token'] = state
	pass

def is_valid_state(state):
	saved_state = session['state_token']
	if state == saved_state:
		print("States match, you are who you say you are!")
		return True
	else:
		return False




CERT_FILE = "BuildBuilder.crt"
KEY_FILE = "BuildBuilder.key"

def create_self_signed_cert(cert_dir):
    """
    If datacard.crt and datacard.key don't exist in cert_dir, create a new
    self-signed cert and keypair and write them into that directory.
    """

    if not exists(join(cert_dir, CERT_FILE)) \
            or not exists(join(cert_dir, KEY_FILE)):
            
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "US"
        cert.get_subject().ST = "Texas"
        cert.get_subject().L = "CStat"
        cert.get_subject().O = "BuildBuilder"
        cert.get_subject().OU = "BuildBuilder"
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')

        open(join(cert_dir, CERT_FILE), "w+b").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(join(cert_dir, KEY_FILE), "w+b").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    
    
    
    
    
    
    
    
    