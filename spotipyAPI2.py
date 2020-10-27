import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import PATH_TO_LYRICS as PATH
import sqlite3
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
    results = sp.search(q='artist:' + name, type='artist', limit=50)
    artists = results['artists']['items']
    while results['artists']['next']:
        try:
            results = sp.next(results['artists'])
            artists += results['artists']['items']
        except:
            break
    for item in artists:
        artist = re.sub('[^A-Za-z0-9 ]+', '', item['name'])
        if artist.lower() == name.lower():
            found += 1
            print(name)
            print(found, not_found)
            artist_id_dict[name] = [item['uri'], songs]
            artist_found = True
            break
    if not artist_found:
        count = 0
        temp = None
        for song in songs:
            query_string = (song[0] + ' ' + name).lower()
            results = sp.search(q=query_string, type='track', limit=50)
            tracks = results['tracks']['items']
            for item in tracks:
                track_artist = re.sub('[^A-Za-z0-9 ]+', '', item['artists'][0]['name'])
                print(track_artist.replace(" ", "").lower(), name.replace(" ", "").lower())

                if track_artist.replace(" ", "").lower() == name.replace(" ", "").lower():
                    found += 1
                    print(track_artist)
                    print(found, not_found)
                    artist_id_dict[name] = [item['artists'][0]['uri'], songs]
                    artist_found = True
                    break
            if artist_found:
                break
        if not artist_found:
            not_found += 1
            print("NOT FOUND : " + name)
            print(found, not_found)

print(len(artist_id_dict))
print(len(artist_dict))

conn = sqlite3.connect('songs.db')
c = conn.cursor()
for artist, values in artist_id_dict.items():
    if c.execute('''SELECT id FROM artists WHERE name = ?;''', (artist,)).fetchone() is None:
        c.execute('''INSERT INTO artists (name, tune_bat_id, date_added) VALUES(?,?,?);''', (artist, values[0], time.time()))
        conn.commit()
    print(time.time())
    artist_id = c.execute('''SELECT id FROM artists WHERE name = ?;''', (artist,)).fetchone()[0]
    for song in values[1]:
        c.execute('''INSERT INTO  songs (song, artist_id, lyrics, date_added) VALUES(?,?,?,?);''', (song[0], artist_id, song[1], time.time()))
        conn.commit()
conn.close()
    #artists_found.write(str(key) + ":" + str(val) + "\n")
'''artists_found = open('found.txt', 'a')
artists_found.write("#####\n")
for key, val in artist_id_dict.items():
    for 
    artists_found.write(str(key) + ":" + str(val) + "\n")
artists_found.close()'''



artist_dict_not_found = {}
for key, val in artist_dict.items():
    if key not in artist_id_dict.keys():
        artist_dict_not_found[key] = val


artists_not_found = open('not_found.txt', 'a')
artists_not_found.write("#####\n")
for key, val in artist_dict_not_found.items():
    artists_not_found.write(str(key) + ":" + str(val) + "\n")
artists_not_found.close()
