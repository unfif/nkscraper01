# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sc01.items import Sc01Item

class NkdailySpider(CrawlSpider):
    name = 'nkdaily'
    allowed_domains = ['db.netkeiba.com']
    start_urls = ['http://db.netkeiba.com/race/list/20190602/']

    rules = (
        Rule(LinkExtractor(
            allow = ['db.netkeiba.com/race/'],
            deny = ['db.netkeiba.com/race/movie'],
            restrict_css = '.race_kaisai_info'
        ),
            callback = 'parse_races', follow = False
        ),
    )

    def parse_races(self, response):
        item = Sc01Item()
        raceinfo = response.css('.race_head_inner')
        raceplaceurl = raceinfo.css('ul.race_place a.active::attr(href)').get()
        # raceplaceurl = response.request.url
        item['id'] = raceplaceurl.split('/')[2]
        item['place'] = raceinfo.css('ul.race_place a.active::text').get()
        item['racenum'] = raceinfo.css('div.race_num a.active::text').get().split('R')[0]
        item['title'] = raceinfo.css('dl.racedata h1::text').get().strip()
        # datadetail = raceinfo.css('div.data_intro p.smalltxt')
        racedetails = raceinfo.css('dl.racedata + p.smalltxt::text').get()
        racedatejp = racedetails.split()[0]
        raceyear = racedatejp.split('年')[0]
        racemonth = racedatejp.split('年')[1].split('月')[0].zfill(2)
        raceday = racedatejp.split('月')[1].split('日')[0].zfill(2)
        item['date'] = raceyear + '-' + racemonth + '-' + raceday
        item['schedule'] = racedetails.split()[1]
        item['classification'] = racedetails.split()[2]
        item['category'] = racedetails.split()[3]

        for tr in response.css('[summary="レース結果"] tr:not(tr:first-of-type)'):
            item['placenum'] = tr.css('td')[0].css('::text').get()
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
            # print(item)

            yield item
