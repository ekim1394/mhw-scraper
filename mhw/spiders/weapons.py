# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from mhw.items import ImageItem

class WeaponsSpider(scrapy.Spider):
    name = 'weapons'
    allowed_domains = ['monsterhunterworld.wiki.fextralife.com']
    start_urls = ['http://monsterhunterworld.wiki.fextralife.com/Weapons']
    custom_settings = {
        "IMAGES_STORE": 'images/weapons'
    }
    def parse(self, response):
        LINK_SELECTOR = '.wiki_link'
        img_url_list = []        
        for weapon in response.css(LINK_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            IMG_SELECTOR = 'img ::attr(data-original)'
            name = weapon.css(NAME_SELECTOR).extract_first()
            img_url = urljoin(response.url, weapon.css(IMG_SELECTOR).extract_first())
            if name is not None and img_url is not None and img_url.strip()[-4:] == '.png':
                img_url_list.append(img_url)
                yield {
                    'name': name,
                    'image_urls': img_url
                }
        yield ImageItem(image_urls=img_url_list)                