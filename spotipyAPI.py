import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials("1e42620b2b034f63bd21a1ff5b8526c1", "c587be0ae31d44f387f80d40aec3d3a7")
sp = spotipy.Spotify(auth_manager=auth_manager)

songs = open(r"C:\Users\Cornucopia\PycharmProjects\LyricsToneSci\Lyrics\X.txt", "r", encoding="utf8").read()
#info_file = open("Documents/random/randoms/WebScraping/real/X_info.txt", "a")
song_list = songs.split("#####")
song_list.pop(0)
title_list = [list(filter((str("")).__ne__, song.split("\n")))[:2] for song in song_list]
big_list = list(set([item[1] for item in title_list]))
big_list2 = []

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
print(len(notfound), notfound)
