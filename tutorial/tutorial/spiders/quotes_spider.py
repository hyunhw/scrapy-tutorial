import scrapy

class QuotesSpider (scrapy.Spider):
    # identify the spider
    #  must be unique within a project
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # start_requests can be replaced by defining start_urls
    """
    def start_requests(self):
        """Return an iterable of Requests"""
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """

    def parse(self, response):
        """method that handles response downloaded for each request"""
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

