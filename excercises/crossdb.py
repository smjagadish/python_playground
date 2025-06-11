import sqlite3
from importlib.resources import files


def doDataManipulation():
    conn = sqlite3.connect("joindb.sqlite")
    cur = conn.cursor()
    """
     DDL operations done always - so that we cleanup and start
    """
    cur.execute("DROP TABLE IF EXISTS Artist")
    cur.execute("DROP TABLE IF EXISTS Genre ")
    cur.execute("DROP TABLE IF EXISTS Album")
    cur.execute("DROP TABLE IF EXISTS Track")

    """
    DDL operations done always - create the needed tables
    """
    cur.execute("""
    CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name TEXT )
    """)

    cur.execute("""
    CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name TEXT )
    """)

    cur.execute("""
    CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT )
    """)

    cur.execute("""
    CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT ,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER , rating INTEGER , count INTEGER)
    """)

    with files("excercises").joinpath("tracks.csv").open("r") as file:
        for entry in file:
            contents = entry.split(",")
            track = contents[0]
            artist = contents[1]
            if artist == "0":
                artist = "no artist"
            album = contents[2]
            if album == "0":
                album = "no name album"
            len = contents[3]
            rating = contents[4]
            count = contents[5]
            genre = contents[6]
            if genre == "0":
                genre = "no genre"
            cur.execute(
                """
           INSERT INTO Artist (name) VALUES (?)
           """,
                (artist,),
            )

            cur.execute(
                """
           INSERT INTO Genre (name) VALUES (?)
           """,
                (genre,),
            )

            cur.execute(
                """
           SELECT id from Artist WHERE name = (?)
           """,
                (artist,),
            )
            artist_id = cur.fetchone()[0]

            cur.execute(
                """
           INSERT INTO Album (artist_id , title) VALUES (?,?)
           """,
                (artist_id, album),
            )

            cur.execute(
                """
           SELECT id from Album WHERE title = (?)
           """,
                (album,),
            )
            album_id = cur.fetchone()[0]

            cur.execute(
                """
           SELECT id from Genre WHERE name = (?)
           """,
                (genre,),
            )
            genre_id = cur.fetchone()[0]

            cur.execute(
                """
           INSERT INTO Track (title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)
           """,
                (track, album_id, genre_id, len, rating, count),
            )
    print("inserts over")
    conn.commit()
    print(" querying for the top hits")
    cur.execute("""
       SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.Id and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
       """)
    results = cur.fetchmany(3)
    for res in results:
        gen_res = (i for i in res)
        print(list(gen_res))


if __name__ == "__main__":
    doDataManipulation()
