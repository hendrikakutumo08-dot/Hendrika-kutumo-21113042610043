def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

print(make_album('tulus', 'manusia'))
print(make_album('sheila on 7', 'kisah klasik'))
print(make_album('noah', 'keterkaitan keterikatan', 9))