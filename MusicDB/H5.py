import MusicDB

MusicDB.DisplayMenu()
while(True):

    choice = input("Enter your choice: ")
    if choice == 'add':
         MusicDB.AddSong()
         continue
    elif choice == 'list':  
         MusicDB.SongList()
         continue
    elif choice == 'save':   
         MusicDB.SongSave() 
         continue
    elif choice == 'help':
         MusicDB.Help()
    elif choice == 'exit':
         break
    else:
        print("Invalid Choice")