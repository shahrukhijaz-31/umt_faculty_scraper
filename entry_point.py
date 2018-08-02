from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'umt_scraper', '-o', 'umt_scraper.json'])
#execute(['scrapy', 'crawl', 'umt_scraper'])
# execute(['scrapy', 'shell', 'https://www.sheego.de/'])