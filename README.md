# lbd-invoice-etax-scraper

Learning by doing - 抓下台灣統一發票對獎號碼

## Usage

Run on local

```bash
pip install -r requirements.txt
python app.py
```

Run By docker

```bash
docker image build -t hanksudo/invoice-etax-scrapper .
docker run --rm hanksudo/invoice-etax-scrapper
```

## Output

```bash
特別獎
    59647042
特獎
    01260528
頭獎
    01616970
    69921388
    53451508
增開六獎
    710
    585
    633
```

## References

- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/) is a Python library for pulling data out of HTML and XML files.
- [統一發票](http://invoice.etax.nat.gov.tw/)
