import json
import os.path
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

song = {}
isSongAdded = False

def DisplayMenu():
    print("Select operation.")
    print("add – Add a new song to the database")
    print("list – List the songs in the database")
    print("save – Save the songs to the database")
    print("total – Get total number of songs in the database")
    print("info – Get the information about a particular song in the database")
    print("help – Display a menu explaining the commands to the users")
    print("exit – Exit the program")


    
def AddSong():
    global isSongAdded
    isSongAdded = True
    global song
    song_title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    album = input("Enter Album: ")
    track_number = int(input("Enter the Track_number: "))
    released_year = int(input("Enter the Released_year: "))
    genre = input("Enter Genre: ")
   
    # create a song record
    song = dict(Song_title = song_title, Artist = artist, Album = album, Track_number = track_number, Released_year = released_year, Genre = genre) 

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
  if(os.path.exists('Song_DB.json')):
    songs_list = json.load(open('Song_DB.json'))
    print("The list of Songs are: " , songs_list)
  else:
    print("Song database doesn't exist")

def SongSave():
  global song
  global isSongAdded
  #json.dump(song, fp=open('Song_DB.json','w'), indent=4)
  if(isSongAdded):
    # Create a blank array to store the songs by first getting from file and then appending new song
    songArr = []
    #Check if File exist before opening and loading the data

    if(os.path.exists('Song_DB.json')):
      with open('Song_DB.json') as f:
        # Load the existing songs from file
        data = json.load(f)
        # Add those songs to the song Array
        for songdata in data:
          songArr.append(songdata)  

    # Now add the new song to the existing songs in the song array
    songArr.append(song)

    with open('Song_DB.json', 'w') as f:
      json.dump(songArr, f)
  
    song = {}
  else:
    print("Please add a song first")
  
  isSongAdded = False

def Help():
  DisplayMenu()

def GetTotalSongs():
  if(os.path.exists('Song_DB.json')):
    songs_list = json.load(open('Song_DB.json'))
    print("Total songs in database::",len(songs_list))
  else:
    print("Song database doesn't exist")
 
def GetSongInformation(songNumber):
  if(songNumber > 8 or songNumber < 1):
    print("Enter a correct Song Number to get the information")
  else:  
    if(os.path.exists('Song_DB.json')):
      songs_list = json.load(open('Song_DB.json'))
      print(songs_list[songNumber-1])
    else:
      print("Song database doesn't exist")