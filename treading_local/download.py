import gc
import urllib.request
import xml.etree.ElementTree as ET
from io import StringIO

CLEANUP_INTERVAL = 1000
url = "https://www.studioatrium.pl/files/murator.xml"
username = "murator"
password = "murator.2019;"

def main():
    print("start")
    p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)

    auth_handler = urllib.request.HTTPBasicAuthHandler(p)

    opener = urllib.request.build_opener(auth_handler)

    urllib.request.install_opener(opener)

    try:
        result = opener.open(url)
        content = result.read()
        print(content)
    except IOError as e:
        print(e)

    iterator(content)
    print("the end")


def iterator(xml):
    events = ("start",)
    xml = xml.decode("utf-8")
    for i, (event, elem) in enumerate(ET.iterparse(StringIO(xml), events=events)):
        if elem.tag == "projekt":
            print(elem.tag)
        elem.clear()
        if i % CLEANUP_INTERVAL == 0:
            gc.collect()

if __name__ == "__main__":  # pragma: no cover
    main()
