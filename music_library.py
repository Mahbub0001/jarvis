music={
    "blue eyes":"https://www.youtube.com/watch?v=NbyHNASFi6U",
    "blue eye":"https://www.youtube.com/watch?v=NbyHNASFi6U",
    "love dose":"https://www.youtube.com/watch?v=TvngY4unjn4",
    "adat":"https://www.youtube.com/watch?v=eK5gPcFjQps",
    "aadat":"https://www.youtube.com/watch?v=eK5gPcFjQps"
}

def music(song_name):
    songs = {
    "blue eyes":"https://www.youtube.com/watch?v=NbyHNASFi6U",
    "blue ice":"https://www.youtube.com/watch?v=NbyHNASFi6U",
    "blue eye":"https://www.youtube.com/watch?v=NbyHNASFi6U",
    "love dose":"https://www.youtube.com/watch?v=TvngY4unjn4",
    "adat":"https://www.youtube.com/watch?v=eK5gPcFjQps",
    "aadat":"https://www.youtube.com/watch?v=eK5gPcFjQps"
    }
    return songs.get(song_name, None)
