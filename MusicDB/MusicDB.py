
#import json

#book1 = dict(title = "Learning Python", author = "Mark Lutz", PubDate = 2013 )
#book2 = dict(title = "As I Lay Dying", author = "William Faulkner", PubDate = 930 )

#tempTitle = input("Enter Title: ")
#tempAuthor = input("Enter author: ")
#tempPubDate = int(input("Enter Publication Year: "))

#books = [book1, book2]

#book3 = dict(title = tempTitle, author = tempAuthor, PubDate = tempPubDate )
#books.append(book3)

#json.dump(books, fp=open('myFile.txt','w'), indent=4)

#newBook = json.load(open('myFile.txt'))
#print(newBook)
#print(len(newBook))

#for book in newBook:
 #   print(book["title"])
###

import json
#from enum import Enum
#class genre (Enum)
	#  Blues = 1
   # Country = 2
	 # Electronic = 3
	 # Folk = 4
	 # HipHop = 5
	 # Jazz = 6
	 # Latin = 7
	 # Pop = 8

songs = {}
songs['song'] = []

def DisplayMenu():
    print("Select operation.")
    print("add – Add a new song to the database")
    print("list – List the songs in the database")
    print("save – Save the songs to the database")
    print("help – Display a menu explaining the commands to the users")
    print("exit – Exit the program")


    
def AddSong():
    
    song_title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    album = input("Enter Album: ")
    track_number = int(input("Enter the Track_number: "))
    released_year = int(input("Enter the Released_year: "))
    genre = input("Enter Genre: ")
    # create a song record
    song = dict(Song_title = song_title, Artist = artist, Album = album, Track_number = track_number, Released_year = released_year, Genre = genre) 

    # add it to the list
    songs['song'].append(song)  


#def GetSongNumber(number):  
   # try:
    #     int(number)
    #except:
    #     return None
    #if(number <1):
   #     return None
   # if((number // 1) > songs.count):
    #   return None
    #else:
    #    return songs[(number // 1)-1]


#song GetSongByTitle(string title)
#{
#   // Do something to get the song by tit


def SongList():
    songs_list = json.load(open('Song_DB.txt'))
    print("The list of Songs are: " , songs_list)

def SongSave():
 # json.dump(songs, fp=open('Song_DB.txt','w'), indent=4)
 
  with open('Song_DB.txt','w+') as f:
    try: 
         data = json.load(f)
    except ValueError: 
         data = {}    
  data.update(songs)

  with open('Song_DB.txt', 'w') as f:
    json.dump(data, f)

def Help():
  DisplayMenu()

#def GetTotalSongs(int):
 
#def GetSongInformation();   
