from tkinter.messagebox import NO
import scrapy


class CellphoneS(scrapy.Spider):
    name = "cellphones"

    start_urls = [
        'https://cellphones.com.vn/',
    ]

    def parse(self, response):
        # yield scrapy.Request('https://cellphones.com.vn/mobile/apple.html', callback=self.parseSmallList)
        for i in response.css('li.item-menu'):
            linkTo = i.css('a::attr(href)').get()
            if "https://cellphones.com.vn" not in linkTo: continue
            # yield {
            #     'link': demo
            # }
            yield scrapy.Request(linkTo, callback=self.parseSmallList)
            
    def parseSmallList(self, response):
        for i in response.css('div.item-product__box-img'):
            linkTo = i.css('a::attr(href)').get()
            yield scrapy.Request(linkTo, callback=self.parseProduct)
    def parseProduct(self, response):
        
        name = response.css('title::text').get()
        
        x = response.css('div.list-linked a strong::text').getall()
        y = response.css('div.list-linked a span::text').getall()
        
        # print(2,x,y)
        
        i = 0
        lenX = min(len(x),len(y))
        
        while i < lenX:
            yield {
                'Name': name,
                'No Name': x[i],
                'Price': y[i],
            }
            i += 1