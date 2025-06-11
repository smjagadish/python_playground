import sqlite3
import json
import codecs


def doDataPrep():
    conn = sqlite3.connect("geodata.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Locations")
    res = cur.fetchmany(300)
    fhand = codecs.open("where.js", "w", "utf-8")
    fhand.write("myData = [\n")
    count = 0
    for row in res:
        data = str(row[1].decode())

        try:
            js = json.loads(str(data))
        except:
            continue

        if len(js["features"]) == 0:
            continue

        try:
            lat = js["features"][0]["geometry"]["coordinates"][1]
            lng = js["features"][0]["geometry"]["coordinates"][0]
            where = js["features"][0]["properties"]["display_name"]
            where = where.replace("'", "")
        except:
            print("Unexpected format")
            print(js)

        try:
            print(where, lat, lng)

            count = count + 1
            if count > 1:
                fhand.write(",\n")
            output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
            fhand.write(output)
        except:
            continue
    fhand.write("\n];\n")
    cur.close()
    fhand.close()
    print(count, "records written to where.js")
    print("Open where.html to view the data in a browser")


if __name__ == "__main__":
    doDataPrep()
