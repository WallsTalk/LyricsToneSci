import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials("1e42620b2b034f63bd21a1ff5b8526c1", "c587be0ae31d44f387f80d40aec3d3a7")
sp = spotipy.Spotify(auth_manager=auth_manager)

'''
title_list = [list(filter((str("")).__ne__, song.split("\n")))[:2] for song in song_list]
big_list = list(set([item[1] for item in title_list]))
big_list2 = []'''

songs = open(r"C:\Users\Cornucopia\PycharmProjects\LyricsToneSci\Lyrics\X.txt", "r", encoding="utf8").read()
song_list = songs.split("#####\n")
song_list.pop(0)
song_title_list = []
print(len(song_list))
for song in song_list:
    song_title_list.append(song.split('\n'))

song_list_main = []
first_row_val = 0
for title in song_title_list:
    song_list_main.append([title[2], title[0], '\n'.join(title[3:])])

print(len(song_list_main))
artist_list = list(set([item[0] for item in song_list_main]))
print(len(artist_list))

artist_dict = {}
minilist = {}
for name in artist_list:
    results = sp.search(q='artist:' + name, type='artist', limit=50)
    artists = results['artists']['items']
    for item in artists:
        artist = re.sub('[^A-Za-z0-9 ]+', '', item['name'])
        if artist.upper() == name.upper():
            artist_dict[name] = [item['id'], len(artists)]
            break
    minilist[name] = len(artists)

print(len(artist_dict))
print([[item, minilist[item]] for item in artist_list if item not in artist_dict.keys()])


'''counter2 = 0
for item in song_list_main:
    ##if item[0][0] != 'X':
    if item[2].count('\n') == 6:
        print(item)
        counter2 += 1

print(counter2)'''
'''print(len(song_list_main))
artist_list = list(set([item[0] for item in song_list_main]))
#for item in artist_list:
for title in big_list:
    results = sp.search(q='artist:' + title, type='artist', limit=50)
    artists = results['artists']['items']
    for item in artists:
        artist = re.sub('[^A-Za-z0-9 ]+', '', item['name'])
        if artist.upper() == title.upper() and artist not in big_list2:
            big_list2.append(artist)
print(len(big_list), len(big_list2))
print(big_list)
print(big_list2)
notfound = [item for item in big_list if item not in big_list2]
print(len(notfound), notfound)'''
