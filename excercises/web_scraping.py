import sys
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def scrape():
    target = "http://py4e-data.dr-chuck.net/comments_2164355.html"
    try:
        req = Request(target, None, method="GET")
        with urlopen(req) as res:
            soup = BeautifulSoup(res.read().decode("utf-8"), "html.parser")
            spans = soup("span")
            count = 0
            for span in spans:
                count += int(span.contents[0])
            print(count)
    except Exception as e:
        print("there is an error", e)


def scrape_link(args):
    print("triggering link scraping")
    target = "http://py4e-data.dr-chuck.net/known_by_Jabin.html"
    try:
        req = Request(target, None, method="GET")
        count = int(args[0])
        posn = int(args[1])
        with urlopen(req) as res:
            soup = BeautifulSoup(res.read().decode("utf-8"), "html.parser")
            print("Retrieving:", target)
            anchors = soup("a")
            out_loop = 1
            for anchor in anchors:
                if out_loop < posn:
                    out_loop += 1
                    continue
                elif out_loop == posn:
                    anchor_p = anchor.get("href")
                    for inner_lop in range(0, count):
                        print("Retrieving:", anchor_p)
                        req_inner = Request(anchor_p, None, method="GET")
                        with urlopen(req_inner) as res_inner:
                            soup = BeautifulSoup(
                                res_inner.read().decode("utf-8"), "html.parser"
                            )
                            anchors_inner = soup("a")
                            in_posn = 1
                            # for anchor_inner in anchors_inner:

                            anchor_p = giveTarget(posn, anchors_inner)

                            """for anchor_inner in anchors_inner:
                                if in_posn != posn:
                                    in_posn +=1
                                    continue
                                else:
                                    anchor_p = anchor_inner.get('href')
                                    break"""
                    out_loop += 1
                else:
                    break

    except Exception as e:
        print("there is an error:", e)


def giveTarget(posn, links):
    loop = 1
    target_link = ""
    for inner_link in links:
        if loop != posn:
            loop += 1
            continue
        else:
            target_link = inner_link.get("href")
            break
    return target_link


if __name__ == "__main__":
    scrape()
    args = sys.argv
    args_con = args[1:]
    scrape_link(args_con)
