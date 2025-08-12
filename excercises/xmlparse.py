import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen


def parse_xml(url):
    print(f"parsing the target - {url}")
    try:
        req = Request(url, None, method="GET")
        with urlopen(req) as res:
            data = res.read().decode("utf-8")
            tree = ET.fromstring(data)
            lst_comments = tree.find(
                "comments"
            )  # only 1 comments element , so return it direct
            tval = 0
            for elem in lst_comments.findall(
                "comment"
            ):  # multiple comment under 1 comments, so get them and loop over them
                cval = elem.find("count").text
                tval += int(cval)
            print(tval)
    except Exception as e:
        print(f"there is an error:{e}")


def simple_parse_xml(url):
    """this snippet will leverage the xspath direct selection of the 'count' attr - all occurrences when using findall
    note that if i know the parent-child relationship i can go with / after //(refer simple_parse_xml_deps)
    else i can use // only to fetch the exact element regardless of the relationship
    the // signifies all descendents
    """
    try:
        req = Request(url, None, method="GET")
        total_count = 0
        with urlopen(url) as res:
            counts = ET.fromstring(res.read().decode("utf-8")).findall(".//count")
            for count in counts:
                total_count += int(count.text)
        print("the simple parse result is:", total_count)
    except Exception as e:
        print(f"there is an error:{e}")


def simple_parse_xml_deps(url):
    """using knowledge of the parent-child relationship to use xspath"""
    try:
        req = Request(url, None, method="GET")
        total_count = 0
        with urlopen(req) as res:
            counts = ET.fromstring(res.read().decode("utf-8")).findall(
                ".//comment/count"
            )
            for count in counts:
                total_count += int(count.text)
            print("the simple parse with deps result is:", total_count)
    except Exception as e:
        print(f"there is an error:{e}")


if __name__ == "__main__":
    target = input("enter the url for scraping")
    target = target.strip()
    parse_xml(target)
    simple_parse_xml(target)
    simple_parse_xml_deps(target)
