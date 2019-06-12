# -*- coding: utf-8 -*-
import scrapy
from sc01.items import Sc01Item

class Nksc01Spider(scrapy.Spider):
    name = 'nksc01'
    allowed_domains = ['db.netkeiba.com/race']
    start_urls = ['http://db.netkeiba.com/race/201905030211/']
    # start_urls = ['https://db.netkeiba.com/race/list/20190602/']
    # start_urls = ['http://127.0.0.1:5000/']

    def parse(self, response):
        item = Sc01Item()
        raceinfo = response.css('.race_head_inner')
        racenums = raceinfo.css('.race_num')
        item['raceid'] = racenums.css('li')[10].css('a::attr(href)').get().split('/')[2]
        mainrace_data = raceinfo.css('.mainrace_data')
        item['racetitle'] = mainrace_data.css('h1::text')
        for tr in response.css('[summary="レース結果"] tr:not(tr:first-of-type)'):
            item['place'] = tr.css('td')[0].css('::text').get()
            item['postnum'] = tr.css('td')[1].css('span::text').get()
            item['horsenum'] = tr.css('td')[2].css('::text').get()
            item['horsename'] = tr.css('td')[3].css('a::text').get()
            item['sex'] = tr.css('td')[4].css('::text').get()[0]
            item['age'] = tr.css('td')[4].css('::text').get()[1:]
            item['weight'] = tr.css('td')[5].css('::text').get()
            item['jockey'] = tr.css('td')[6].css('a::text').get()
            item['time'] = tr.css('td')[7].css('::text').get()
            margin = tr.css('td')[8].css('::text').get()
            item['margin'] = margin if margin is not None else '0'
            item['position'] = tr.css('td')[10].css('::text').get()
            item['last3f'] = tr.css('td')[11].css('::text').get()
            item['odds'] = tr.css('td')[12].css('::text').get()
            item['fav'] = tr.css('td')[13].css('::text').get()
            item['horseweight'] = tr.css('td')[14].css('::text').get().split('(')[0]
            item['horseweightdiff'] = tr.css('td')[14].css('::text').get().split('(')[1][:-1].replace('+', '')
            item['trainer'] = tr.css('td')[18].css('a::text').get()
            item['owner'] = tr.css('td')[19].css('a::text').get()
            addedmoney = tr.css('td')[20].css('::text').get()
            item['addedmoney'] = addedmoney if addedmoney is not None else '0'

            yield item
