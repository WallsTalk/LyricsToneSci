import sqlite3

conn = sqlite3.connect('songs.db')
c = conn.cursor()
answer = c.execute('''SELECT * FROM artists_X;''')
print(answer.fetchall())
conn.close()

songs = open(r"C:\Users\Cornucopia\PycharmProjects\LyricsToneSci\Lyrics\X.txt", "r", encoding="utf8").read()
song_list = songs.split("#####\n")
song_list.pop(0)
song_title_list = []
print(len(song_list))
for song in song_list:
    song_title_list.append(song.split('\n'))
  # ([(song.partition('\n')[0]).partition('\n')[0], song.partition('\n')[2]])

song_list_main = []
first_row_val = 0
for title in song_title_list:
    song_list_main.append([title[2], title[0], '\n'.join(title[3:])])


'''counter2 = 0
for item in song_list_main:
    ##if item[0][0] != 'X':
    if item[2].count('\n') == 6:
        print(item)
        counter2 += 1

print(counter2)'''
print(len(song_list_main))
artist_list = list(set([item[0] for item in song_list_main]))
#for item in artist_list:

'''for title in song_title_list:
    if title[0] != "":
        if title[2] != "":
            print(title[0], title[2])
    else:
        if title[1] != "":
            if title
            print(title[1], title[2])
        else:
            if title[2] != "":
                print(title[2])
            else:
                if title[3] != "":
                    print(title[3])
'''


