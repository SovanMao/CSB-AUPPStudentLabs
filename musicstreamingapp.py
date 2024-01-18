"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process


class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

class MusicLibrary:
    # Dictionary to store songs with titles as keys for quick title-based retrieval
    def __init__(self):
        self.songs = {}

    def add_song(self, song):
        if song.title not in self.songs:
            self.songs[song.title] = song

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs.values() if song.artist == artist]

    def get_songs_by_album(self, album):
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        return self.songs.get(title, None)

class Playlist:
    def __init__(self, name):
        # Basic list to store songs, suitable for maintaining the order of songs in a playlist
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def reorder_songs(self, new_order):
        self.songs = [self.songs[i] for i in new_order]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        print("---------------------------")
        print("Title | Artist")
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")

# Example usage:
# Song: title, artist, album, genre, length
moonlight = Song("Moonlight Dance", "Harmony Haven", "Starry Nights", "Instrumental", "4:20")
cascade = Song("Cascade", "Rhythmic Rapture", "Euphonic Echoes", "Electronic", "5:15")
serenade = Song("Serenade", "Fools Garden", "Harmony Haven", "Pop", "3:45")
pulse = Song("Pulse", "Digital_Dreams", "Synthwave Symphony", "Synthpop", "4:30")
reflections = Song("Reflections", "Harmony Haven", "Euphonic Echoes", "Chillout", "3:58")
kaleidoscope = Song("Kaleidoscope", "Celestial Sounds", "Abstract Artistry", "Ambient", "6:02")
whisper = Song("Whisper", "Fools Garden", "Melodic Moments", "Indie", "3:28")
aurora = Song("Aurora", "Celestial Sounds", "Starry Nights", "Orchestral", "4:50")
reverie = Song("Reverie", "Rhythmic Rapture", "Dreamy Delights", "Electronic", "3:55")
solstice = Song("Solstice", "Celestial Sounds", "Abstract Artistry", "Ambient", "5:12")
daydream = Song("Daydream", "Harmony Haven", "Euphonic Echoes", "Chillout", "4:10")
mirage = Song("Mirage", "Digital_Dreams", "Synthwave Symphony", "Synthpop", "3:45")
mystic = Song("Mystic", "Fools Garden", "Melodic Moments", "Indie", "3:22")
cosmic = Song("Cosmic", "Rhythmic Rapture", "Dreamy Delights", "Electronic", "4:25")
lullaby = Song("Lullaby", "Harmony Haven", "Starry Nights", "Orchestral", "3:40")
ethereal = Song("Ethereal", "Celestial Sounds", "Abstract Artistry", "Ambient", "5:30")
journey = Song("Journey", "Rhythmic Rapture", "Dreamy Delights", "Electronic", "4:18")
echoes = Song("Echoes", "Digital_Dreams", "Synthwave Symphony", "Synthpop", "3:58")
tranquility = Song("Tranquility", "Harmony Haven", "Euphonic Echoes", "Chillout", "4:45")
resonance = Song("Resonance", "Celestial Sounds", "Starry Nights", "Orchestral", "5:05")


# Create a list of all songs
all_songs = [
    moonlight, cascade, serenade, pulse, reflections, kaleidoscope, 
    whisper, aurora, reverie, solstice, daydream, mirage, mystic, 
    cosmic, lullaby, ethereal, journey, echoes, tranquility, resonance
]

library = MusicLibrary()
# Add each song to the library
for song in all_songs:
    library.add_song(song)


playlist1 = Playlist("My Playlist 1")
# Add song into My playlist 1
playlist1.add_song(moonlight)
playlist1.add_song(serenade)
playlist1.add_song(lullaby)

playlist1.display_playlist()


print("\n")
print("---------------------------")
songs_by_artist1 = library.get_songs_by_artist("Rhythmic Rapture")
print(f"Songs by artist 'Rhythmic Rapture': ")
print("---------------------------")
print("Title | Album")
for song in songs_by_artist1:
    print(f"{song.title} - {song.album}")
print("---------------------------")
print("\n")


print("---------------------------")
get_songs_by_album = library.get_songs_by_album("Starry Nights")
print(f"Songs by album 'Starry Nights': ")
print("---------------------------")
print("Title | Artist")
for song in get_songs_by_album:
    print(f"{song.title} - {song.artist}")
print("---------------------------")
print("\n")


print("---------------------------")
get_songs_by_genre = library.get_songs_by_genre("Chillout")
print(f"Songs by genre 'Chillout': ")
print("---------------------------")
print("Title | Album")
for song in get_songs_by_genre:
    print(f"{song.title} - {song.album}")
print("---------------------------")


# Output: 

# Playlist: My Playlist 1
# ---------------------------
# Title | Artist
# 1. Moonlight Dance - Harmony Haven
# 2. Serenade - Fools Garden
# 3. Lullaby - Harmony Haven


# ---------------------------
# Songs by artist 'Rhythmic Rapture': 
# ---------------------------
# Title | Album
# Cascade - Euphonic Echoes
# Reverie - Dreamy Delights
# Cosmic - Dreamy Delights
# Journey - Dreamy Delights
# ---------------------------


# ---------------------------
# Songs by album 'Starry Nights':
# ---------------------------
# Title | Artist
# Moonlight Dance - Harmony Haven
# Aurora - Celestial Sounds
# Lullaby - Harmony Haven
# Resonance - Celestial Sounds
# ---------------------------


# ---------------------------
# Songs by genre 'Chillout':
# ---------------------------
# Title | Album
# Reflections - Euphonic Echoes
# Daydream - Euphonic Echoes
# Tranquility - Euphonic Echoes
# ---------------------------
