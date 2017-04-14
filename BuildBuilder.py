# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:38:57 2017

@author: Jake
"""

import requests
import zipfile
import os
import pickle
import json
import sqlite3
import webbrowser

def get_manifest():
     manifest_url = 'http://www.bungie.net/Platform/Destiny/Manifest/'

     #get the manifest location from the json
     r = requests.get(manifest_url)
     manifest = r.json()
     mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']

     #Download the file, write it to 'MANZIP'
     r = requests.get(mani_url)
     with open("MANZIP", "wb") as zip:
         zip.write(r.content)
     print("Download Complete!")

     #Extract the file contents, and rename the extracted file
     # to 'Manifest.content'
     with zipfile.ZipFile('MANZIP') as zip:
         name = zip.namelist()
         zip.extractall()
     os.rename(name[0], 'Manifest.content')
     print('Unzipped!')

hashes = {
    'DestinyActivityDefinition': 'activityHash',
    'DestinyActivityTypeDefinition': 'activityTypeHash',
    'DestinyClassDefinition': 'classHash',
    'DestinyGenderDefinition': 'genderHash',
    'DestinyInventoryBucketDefinition': 'bucketHash',
    'DestinyInventoryItemDefinition': 'itemHash',
    'DestinyProgressionDefinition': 'progressionHash',
    'DestinyRaceDefinition': 'raceHash',
    'DestinyTalentGridDefinition': 'gridHash',
    'DestinyUnlockFlagDefinition': 'flagHash',
    'DestinyHistoricalStatsDefinition': 'statId',
    'DestinyDirectorBookDefinition': 'bookHash',
    'DestinyStatDefinition': 'statHash',
    'DestinySandboxPerkDefinition': 'perkHash',
    'DestinyDestinationDefinition': 'destinationHash',
    'DestinyPlaceDefinition': 'placeHash',
    'DestinyActivityBundleDefinition': 'bundleHash',
    'DestinyStatGroupDefinition': 'statGroupHash',
    'DestinySpecialEventDefinition': 'eventHash',
    'DestinyFactionDefinition': 'factionHash',
    'DestinyVendorCategoryDefinition': 'categoryHash',
    'DestinyEnemyRaceDefinition': 'raceHash',
    'DestinyScriptedSkullDefinition': 'skullHash',
    'DestinyGrimoireCardDefinition': 'cardId'
}


def build_dict(hash_dict):
     #connect to the manifest
     con = sqlite3.connect('manifest.content')
     print('Connected')
     #create a cursor object
     cur = con.cursor()

     all_data = {}
     #for every table name in the dictionary
     for table_name in hash_dict.keys():
         #get a list of all the jsons from the table
         cur.execute('SELECT json from '+table_name)
         print('Generating '+table_name+' dictionary....')

         #this returns a list of tuples: the first item in each tuple is our json
         items = cur.fetchall()

         #create a list of jsons
         item_jsons = [json.loads(item[0]) for item in items]

         #create a dictionary with the hashes as keys
         #and the jsons as values
         item_dict = {}
         hash = hash_dict[table_name]
         for item in item_jsons:   
             item_dict[item[hash]] = item

         #add that dictionary to our all_data using the name of the table
         #as a key. 
         all_data[table_name] = item_dict 
     print('Dictionary Generated!')
     return all_data

if os.path.isfile(r'C:\Users\Jake\Downloads\WinPython-64bit-3.5.3.0Qt5\notebooks\Manifest.content') == False:
    get_manifest()
    all_data = build_dict(hashes)
    with open('manifest.pickle', 'wb') as data:
        pickle.dump(all_data, data)
    print("'manifest.pickle' created!\nDONE!")
else:
    print('Pickle Exists')











response = requests.get('https://www.bungie.net/en/Application/Authorize/12215')
authKeyURL = ''

for resp in response.history:
    authKeyURL = resp.url

authKeyURL -= 'https://jameador13.wixsite.com/buildbuilder?code='

print(authKeyURL)



HEADERS = {"X-API-Key":'be18f1d3b5674727b073af7dd46f5a75'}


with open('manifest.pickle', 'rb') as data:
     all_data = pickle.load(data)

count = 0
all_item_hashes = []
items_and_hashes = {}


for item in all_data['DestinyInventoryItemDefinition']:
    all_item_hashes.append(item)

for num in all_item_hashes:
    if 'itemName' in all_data['DestinyInventoryItemDefinition'][num].keys():
        items_and_hashes[all_data['DestinyInventoryItemDefinition'][num]['itemName']] = num

memberID = requests.get(r'https://www.bungie.net/Platform/Destiny/1/Stats/GetMembershipIdByDisplayName/jam time/', headers=HEADERS)
memberID = memberID.json()
IDnum = memberID['Response']


vault = requests.get('https://www.bungie.net/Platform/Destiny/1/MyAccount/Vault', headers=HEADERS)
vault = vault.json()
print(vault)
vault_hashes = []

for item in vault['Response']['data']['buckets']['items']:
    vault_hashes.append(item['itemHash'])
    
for d in items_and_hashes:
    if items_and_hashes[d] in vault_hashes:
        print(d)




