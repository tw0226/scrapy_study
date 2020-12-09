import scrapy
import datetime

from scrapy.spiders import Spider
section_list = ['today_main_news', 'section_politics', 'section_economy', 'section_society',
                'section_life', 'section_world', 'section_it']
category = ['메인', '정치', '경제', '사회', '생활', '세계', 'IT']
class NaverNewsSpider(scrapy.Spider):
    name = 'naver_news'
    start_urls = ['https://news.naver.com/main/home.nhn']
    def parse(self, response):
        for index, data in enumerate(response.css("div#main_content div.main_component")):
            # 헤드라인
            if index == 0:
                titles = data.css("ul.hdline_article_list div.hdline_article_tit a.lnk_hdline_article::text").getall()
                for title in titles:
                    yield {
                        'time': datetime.datetime.today().strftime('%y-%m-%d %H:%M'),
                        'category': category[index],
                        'title': title.strip()
                    }

            # 헤드라인 외
            else:
                titles = data.css("ul.mlist2 a strong::text")
                for title in titles:
                    yield {
                        'time': datetime.datetime.today().strftime('%y-%m-%d %H:%M'),
                        'category': category[index],
                        'title': title.get()
                    }

