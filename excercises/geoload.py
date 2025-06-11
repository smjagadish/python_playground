from urllib import parse
import json
import importlib.resources
import sqlite3
from urllib.request import Request, urlopen

serviceurl = "https://py4e-data.dr-chuck.net/opengeo?"


def doDataPrep():
    conn = sqlite3.connect("geodata.sqlite")
    cur = conn.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS Locations;
    CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
    """)


def doDataFetch():
    print("fetching data")
    conn = sqlite3.connect("geodata.sqlite")
    cur = conn.cursor()
    with importlib.resources.files("excercises").joinpath("where.data").open("r") as f:
        for line in f:
            data1 = line.strip()

            data_mem = memoryview(data1.encode())
            cur.execute("SELECT * FROM Locations WHERE address= (?)", (data_mem,))
            res = cur.fetchone()
            if res is not None:
                print(
                    f"{res[0].decode()} is present in db already , will not query the api"
                )
                continue
            else:
                enc_loc = parse.urlencode([("q", data1)])
                url = f"{serviceurl}{enc_loc}"
                print(url)
                req = Request(url, None, method="GET")
                with urlopen(req) as res:
                    data = res.read().decode()
                    data = data[0] + data[28:]
                    data_clean = data.replace("\n", "")
                    js = None
                    try:
                        js = json.loads(data_clean)

                    except Exception as e:
                        print(f"there is an error{e} and skipping to next")
                        print(f"downloaded data is:{data_clean}")
                        continue
                    if js is not None or "features" not in js:
                        print("partial data, skipping to next ")
                        continue
                    else:
                        print(f"fetching{data1} from api")
                        print(data_clean)
                        cur.execute(
                            """
                        INSERT INTO Locations(address,geodata) VALUES (?,?)
                        """,
                            (data_mem, memoryview(data_clean.encode())),
                        )
        conn.commit()
        cur.close()


if __name__ == "__main__":
    # doDataPrep()
    doDataFetch()
