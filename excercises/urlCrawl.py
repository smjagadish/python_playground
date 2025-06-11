from urllib.request import urlopen, Request


def docrawl():
    print("This code will do bare-bones HTTP GET")
    url = "http://localhost:8989/default"

    # Create a Request object with a User-Agent header
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="GET")

    try:
        with urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except Exception as e:
        print(f"An error occurred: {e}")


def dosend():
    print("This code will do a bare-bones HTTP POST")
    url = "http://localhost:8989/validate"
    data = "v1.local.cC2bSa6nhE-PBlqh8EBnF7WdjvZi6Y3TzhK_sF-j4jiSq9R6ua1WV6Rp88dvBxgvEYKRDZH9RBZb8x8h2OygpvDU-VHTcwWD5TFDJ42ZzOq0oxVmKTELJvvr5Pr1"
    data_bytes = data.encode("utf-8")
    req = Request(url, data_bytes, method="POST")
    req.add_header(
        "Content-Type", "text/plain"
    )  # this is critical . set as text/plain or application/json , else the spring rest controller screws up on the parsing
    try:
        with urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except Exception as e:
        print(f"an error occured:{e}")


def getpublickey():
    print("This code will get a public key")
    url = "http://localhost:8989/publickey"
    req = Request(url, None, method="GET")  #
    try:
        with urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except Exception as e:
        print(f"an error occurred:{e}")


if __name__ == "__main__":
    docrawl()
    dosend()
    getpublickey()
