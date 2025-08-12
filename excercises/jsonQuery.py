import json
from urllib.request import Request, urlopen


def fetchdata(url):
    print("will invoke endpoint that returns json data")
    req = Request(url, None, method="GET")
    try:
        with urlopen(req) as res:
            ind_count = 0
            data = res.read().decode()
            json_d = json.loads(data)
            comments = json_d["comments"]
            for comment in comments:
                ind_count += comment["count"]
            print(f"sum is:{ind_count}")
    except Exception as e:
        print(f"there is an error:{e}")


if __name__ == "__main__":
    data = input("Enter the url to query data")
    fetchdata(data.strip())
