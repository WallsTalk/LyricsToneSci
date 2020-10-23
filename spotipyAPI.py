import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import PATH_TO_LYRICS as PATH
import unidecode
import time



auth_manager = SpotifyClientCredentials("1e42620b2b034f63bd21a1ff5b8526c1", "c587be0ae31d44f387f80d40aec3d3a7")
sp = spotipy.Spotify(auth_manager=auth_manager)


songs = open(PATH.LYRICS_FOLDER_PATH + "X.txt", "r", encoding="utf8").read()
song_list = songs.split("#####\n")
song_list.pop(0)
song_title_list = []
print(len(song_list))
for song in song_list:
    song_title_list.append(song.split('\n'))

artist_dict = {}
first_row_val = 0
for title in song_title_list:
    if title[2] in artist_dict.keys():
        artist_dict[title[2]].append([title[0], '\n'.join(title[3:])])
    else:
        artist_dict[title[2]] = []
        artist_dict[title[2]].append([title[0], '\n'.join(title[3:])])

artist_id_dict = {}
found = 0
not_found = 0
for name, songs in artist_dict.items():
    artist_found = False
    count = 0
    temp = None
    for song in songs:
        query_string = (song[0] + ' ' + name).lower()
        results = sp.search(q=query_string, type='track', limit=50)
        tracks = results['tracks']['items']
        for item in tracks:
            track_artist = re.sub('[^A-Za-z0-9 ]+', '', item['artists'][0]['name'])
            print(track_artist.lower(),  name.lower())

            if temp == track_artist:
                count += 1
            if count == 10:
                artist_id_dict[name] = item['artists'][0]['uri']
                found += 1
                print(track_artist)
                print(found, not_found)
                artist_found = True
                break
            temp = track_artist

            if track_artist.lower() == name.lower():
                found += 1
                print(track_artist)
                print(found, not_found)
                artist_id_dict[name] = item['artists'][0]['uri']
                artist_found = True
                break
        if artist_found:
            break
    if not artist_found:
        not_found += 1
        print("NOT FOUND : " + name)
        print(found, not_found)

artist_id = open('X_artist_id.txt', 'a')
print(len(artist_id_dict))
print(len(artist_dict))

'''for key, val in artist_id_dict.items():
    artist_id.write(key + "," + val + "\n")
artist_id.close()'''
