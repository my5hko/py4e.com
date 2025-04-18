import sqlite3

# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()

with sqlite3.connect('trackdb.sqlite') as conn:
    cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);
                  
CREATE TABLE Genre (
    id  INTEGER PRIMARY KEY,
    genre    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER,
    genre_id INTEGER    
);
''')

handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip();
    pieces = line.split(',')
    if len(pieces) < 7 : continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # print(name, artist, album, count, rating, length, genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (genre) 
    VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE genre = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

genres = ['Rock', 'Metal']
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.genre
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id
    WHERE Genre.genre IN (?, ?) ORDER BY Genre.genre ASC, Artist.name ASC''', genres)
genre_songs = cur.fetchall()
track_width = max(len(song[0]) for song in genre_songs) + 5
print(f"Number of {', '.join(genres)} songs: {len(genre_songs)}")
print(f"{'Track':<{track_width}}| {'Artist':<{20}}| {'Album':<{20}}| {'Genre':<{20}}")
print('=' * 100)
for song in genre_songs:
    print(f"{song[0]:<{track_width}}| {song[1]:<{20}}| {song[2]:<{20}}| {song[3]:<{20}}")
