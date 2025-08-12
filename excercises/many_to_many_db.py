import json
import sqlite3
from importlib.resources import files


def doDataManipulation():
    conn = sqlite3.connect("mdb.sqlite")
    cur = conn.cursor()
    """
    we always drop tables first just in case
    """
    cur.executescript("""
    
       DROP TABLE IF EXISTS User;
       DROP TABLE IF EXISTS Member;
       DROP TABLE IF EXISTS Course 
    """)

    cur.executescript("""
    CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
    );

    CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
    );

    CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
    )
    """)
    print("logic")
    with files("excercises").joinpath("roster_data.json").open("r") as f:
        contents = json.load(f)
        id_user = 1
        id_course = 1
        for content in contents:
            user = content[0]
            course = content[1]
            role = content[2]
            cur.execute(
                """
            SELECT id FROM User WHERE name = (?)
            """,
                (user,),
            )
            uid = cur.fetchone()
            if uid is None:
                id_user += 1
                uid = id_user
            else:
                uid = uid[0]
            cur.execute(
                """
            INSERT OR IGNORE INTO User(id,name) VALUES (?,?)
            """,
                (uid, user),
            )
            cur.execute(
                """
            SELECT id FROM Course WHERE title = (?)
            """,
                (course,),
            )
            cid = cur.fetchone()
            if cid is None:
                id_course += 1
                cid = id_course
            else:
                cid = cid[0]

            cur.execute(
                """
            INSERT OR IGNORE INTO Course (id,title) VALUES (?,?)
            """,
                (cid, course),
            )
            cur.execute(
                """
            INSERT INTO Member (user_id,course_id,role) VALUES (?,?,?)
            """,
                (uid, cid, role),
            )
            conn.commit()

        """
        doing some data retrieval
        """
        cur.execute("""
        SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
        """)
        cur.execute("""
                SELECT User.name,Course.title, Member.role FROM 
            Member JOIN User JOIN Course 
            ON Member.user_id = User.id AND Member.course_id = Course.id
            ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
                """)
        res = cur.fetchmany(2)
        for r in res:
            print(f"{r[0]}|{r[1]}|{r[2]}")
        """
        final query
        """
        cur.execute("""
        SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
        """)
        r = cur.fetchone()
        print(r)


if __name__ == "__main__":
    doDataManipulation()
