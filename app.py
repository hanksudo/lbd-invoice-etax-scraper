# encoding=utf-8
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def main():
    url = "http://invoice.etax.nat.gov.tw/"

    try:
        headers = {
            "Accept": "text/html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22"
        }
        request = Request(url, headers=headers)
        response = urlopen(request).read()
    except (HTTPError, URLError) as e:
        print(e)
        exit(1)

    soup = BeautifulSoup(response, "html.parser")
    for row in soup.find(id="area1").find("table").find_all("tr"):
        cols = row.find_all("td")
        if not cols:
            continue
        
        numbers_col = cols[1].find("span", {"class": "t18Red"})
        if not numbers_col:
            continue
            
        print(cols[0].text)
        for number in numbers_col.text.split("、"):
            print("\t{}".format(number))


if __name__ == "__main__":
    main()
