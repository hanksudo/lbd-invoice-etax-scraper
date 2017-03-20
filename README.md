# lbd-receipt-scraper

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

```
68789003
53077074
69796177、76868760、14952048
000、059、478、569
```

## References

- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/bs4/) Screen-scraping library
- [統一發票](http://invoice.etax.nat.gov.tw/)
