import base64
import requests
import json
import re
import spotipy


clientId = "1e42620b2b034f63bd21a1ff5b8526c1"
clientSecret = "c587be0ae31d44f387f80d40aec3d3a7"

# Step 1 - Authorization 
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

headers = {"Authorization": "Bearer " + token}

#url = "https://api.spotify.com/v1/search?q=Zac%20Brown&type=track&limit=1"

songs = open(r"C:\Users\Cornucopia\PycharmProjects\LyricsToneSci\Lyrics\X.txt", "r", encoding="utf8").read()
#info_file = open("Documents/random/randoms/WebScraping/real/X_info.txt", "a")
song_list = songs.split("#####")
song_list.pop(0)
title_list = [list(filter((str("")).__ne__, song.split("\n")))[:2] for song in song_list]
for title in title_list:
    title_string = title[1] + " " + title[0]
    print(title_string)


'''	url = "https://api.spotify.com/v1/search?q=" + title_string.replace(" ", "%20") + "&type=track"
	r = requests.get(url, headers=headers)
	song_dict = {}
	try:
		song_dict = json.loads(r.text)
	except:
		print(title_string + " ERROR" + "\n")
	if song_dict["tracks"]["items"] != []:
		count = 0
		for item in song_dict["tracks"]["items"]:
			count += 1
			artist = re.sub('[^A-Za-z0-9 ]+', '', item["artists"][0]["name"])
			song = re.sub('[^A-Za-z0-9 ]+', '', item["name"])
			if artist.upper() == title[1].upper() and song.upper() == title[0].upper():
				url = "https://api.spotify.com/v1/audio-analysis/" + item["id"]
				r = requests.get(url, headers=headers)
				song_dict = json.loads(r.text)
				info_file.write("#####" + "\n" + title[0] + "\n" + title[1] + "\n" + str(song_dict) +  "\n")
				print(item["artists"][0]["name"])
				print(item["name"])
				print(song_dict)
				print("\n")
				break
			elif count == len(song_dict["tracks"]["items"]):
				print("\n" + title_string + " NO RESULTS" + "\n")
	else:
		print("\n" + title_string + " NO RESULTS" + "\n")'''
