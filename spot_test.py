import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import PATH_TO_LYRICS as PATH

auth_manager = SpotifyClientCredentials("1e42620b2b034f63bd21a1ff5b8526c1", "c587be0ae31d44f387f80d40aec3d3a7")
sp = spotipy.Spotify(auth_manager=auth_manager)

artist = 'spotify:artist:54NqjhP2rT524Mi2GicG4K'

results = sp.artist_albums(artist)
albums = results['items']
while results['next']:
	results = sp.next(results)
	albums += results['items']

print(len(albums))
'''for item in albums:
	print(item['name'], item['total_tracks'], item['uri'])'''
tracks = []
for album in albums:
	results = sp.album_tracks(album['uri'])
	tracks += results['items']
	while results['next']:
		results = sp.next(results)
		tracks += results['items']

print(len(tracks))
TRACKS = []
URI = []
for item in tracks:
	TRACKS.append(item['name'])
	URI.append(item['uri'])
print(len(list(set(TRACKS))))
print(len(list(set(URI))))


'''x_file = open('X_tracks.txt', 'a')
for item in tracks:
	x_file.write(item['name'] + "," + item['uri'] + '\n')
x_file.close()'''



'''results = sp.search(q='artist:' + 'Angel', type='artist', limit=50)
temp = results['artists']['items']
artists = []
artists += temp
count = 1
check = False
answer = None
while len(temp) == 50 or check == True:
	print(len(artists))
	results = sp.search(q='artist:' + 'Angel', type='artist', limit=50, offset=50*count)
	temp = results['artists']['items']
	artists += temp
	for item in temp:
		artist = re.sub('[^A-Za-z0-9 ]+', '', item['name'])
		if artist.upper() == 'Angel'.upper():
			answer = item['id']
			check = True
		
print(answer)'''
