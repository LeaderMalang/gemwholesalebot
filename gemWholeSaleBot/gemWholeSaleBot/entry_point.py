from spiders.gemwholesale import GemwholesaleSpider
from scrapy.cmdline import execute
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)
task = LoopingCall(lambda: runner.crawl(GemwholesaleSpider)
                   )
task.start(100 * 10)
reactor.run()

# execute(['scrapy', 'crawl', 'gemwholesale'])