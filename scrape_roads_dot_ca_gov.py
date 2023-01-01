import urllib.request
import urllib.parse
import sys

start = "<p><em>This highway information"
end = "<hr />"


def scrape_roadnumber(roadnumber):
    url = "https://roads.dot.ca.gov/"
    data = {"roadnumber": str(roadnumber), "submit": "Search"}

    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(req) as response:
        html = response.read()

    html = html.decode("utf-8")
    html = html.split(start)[1].split(end)[0]
    return (start + html).strip()


if __name__ == "__main__":
    number = sys.argv[-1]
    assert number.isdigit(), "Should be called with a road number, e.g. 92"
    print(scrape_roadnumber(number))
