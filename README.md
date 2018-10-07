# Project Name
Yahoo Auction JP Product Information Crawler
This project includes following tools:

1. Crawler written with scrapy
2. csv_fix.py to remove abundant blank lines when use in Windows
3. csv_cplit.py to divide the result CSV file into 300-line CSV files

## Installation
Install python 3

## Usage
Run these commands in terminal or cmd:

```
scrapy crawl products -a author_url="https://auctions.yahoo.co.jp/seller/verifymarche"
py csv_fix.py (in windows only)
py csv_split.py
```

## License
MIT License
