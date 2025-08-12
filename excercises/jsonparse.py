import json
from urllib import parse
from urllib.request import Request, urlopen


def querydata(url_data, qs):
    print("querying an endpoint that returns json data")
    query_string = [("q", qs)]
    query_string = parse.urlencode(query_string)
    url = f"{url_data}?{query_string}"
    req = Request(url, None, method="GET")
    try:
        with urlopen(req) as res:
            output = json.loads(res.read().decode("utf-8"))
            fs = output["features"]

            for f in fs:
                for k, v in f.items():
                    if k != "properties":
                        continue
                    else:
                        print(v["plus_code"])

            # print(output)
    except Exception as e:
        print(f"there is an error:{e}")


if __name__ == "__main__":
    url_data = input("enter the url")
    qs = input("enter the query string")
    querydata(url_data.strip(), qs.lstrip())
