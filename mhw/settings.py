BOT_NAME = 'mhw'

SPIDER_MODULES = ['mhw.spiders']
NEWSPIDER_MODULE = 'mhw.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
# 'scrapy.pipelines.images.ImagesPipeline': 1,
'mhw.pipelines.MyImagesPipeline': 1
}
