import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    #target_board = ['Gossiping', 'Gossiping']
    target_board = ['Gossiping']
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('PTTCrawler',board=board)
    
    process.start()
        
'''
在python中有隱含的元素__name__
當此元素在執行的主程式中固定為__main__
而在calling 的function中，則為function name
'''        
if __name__ == '__main__':
    main()
