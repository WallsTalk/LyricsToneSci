import lyricsgenius
import requests
import ast
from time import sleep

def incremention(link, count, artistList):
	while artistList[count] not in link:
		count+=1
	song = link.replace("https://genius.com/" + artistList[count] + "-", "")
	if "https://genius.com/" in song:
		count+=1
		incremention(link, count, artistList)
	return count

genius = lyricsgenius.Genius("fQRUAykcPQbNoKxRV0NY2GJPAuqX9sYlmUTYBfCUcSpnigkw-vjrpQuet0SmRa4w")
linksFile = open("Documents/random/randoms/WebScraping/real/linksO.txt", "r")
artistsFile = open("Documents/random/randoms/WebScraping/allartist.txt", "r")
songs = linksFile.readlines()
artists = artistsFile.readlines()


lyricsFile = open("Documents/random/randoms/WebScraping/real/O.txt", "a")
artistList = []
for link in artists:
	artistList.append(link.split("=")[2].rstrip("\n"))
	
count = 0

for link in songs:
	count = incremention(link, count, artistList)
	if artistList[count] in link:
		song = link.replace("https://genius.com/" + artistList[count] + "-", "")
		song = song.replace("-lyrics", "")
		#print(genius.search_song(song.replace("-", " ").title(), artistList[count].replace("-", " ").title()).lyrics)
		try:
			lyricsFile.write("#####" + "\n" + song.replace("-", " ").title() + "\n" + artistList[count].replace("-", " ").title() + "\n" + genius.search_song(song.replace("-", " ").title(), artistList[count].replace("-", " ").title()).lyrics + "\n")
		except KeyboardInterrupt:
			stored_exception=sys.exc_info()
		except:
			continue
	else:
		while artistList[count] not in link:
			count+=1	

lyricsFile.close() 
if stored_exception:
    raise(stored_exception[0], stored_exception[1], stored_exception[2])

sys.exit()
