# encoding=utf-8
import urllib2
from bs4 import BeautifulSoup


def main():
    url = "http://invoice.etax.nat.gov.tw/"

    try:
        headers = {
            "Accept": "text/html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22"
        }
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request).read()
    except (urllib2.HTTPError, urllib2.URLError) as e:
        print e
        exit(1)

    soup = BeautifulSoup(response, "html.parser")
    # 我只需要這個月的，所以只取前四個Row
    for row in soup.findAll("span", {"class": "t18Red"})[:4]:
        print row.renderContents()


if __name__ == "__main__":
    main()
