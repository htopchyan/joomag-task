from lxml import html
import requests
import re


class WebScraper:
    def get_elements_by_xpath(self, url, xpath):
        url_validator = URLValidator()
        if url_validator.is_valid(url):
            result = requests.get(url)
            page_content = html.fromstring(result.content)
            elements = page_content.xpath(xpath)
            return elements
        else: raise Exception("The URL is invalid")


class URLValidator:
    def is_valid(self,url):
        regex = re.compile(
            r'^(?:http|ftp)s?://' 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
            r'localhost|' 
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
            r'(?::\d+)?' 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return (re.match(regex,url) is not None)


class ImageFormTagRetriever:
    def retrieve_tag_count(self, url):
        web_scraper = WebScraper()
        imgs = web_scraper.get_elements_by_xpath(url, '//img')
        forms = web_scraper.get_elements_by_xpath(url, '//form[@method="get"]')

        return {'image_count': len(imgs), 'form_count': len(forms)}


class ImageFormTagRetrieverTest:
    retrieve_tags = ImageFormTagRetriever()
    result = retrieve_tags.retrieve_tag_count("https://www.netflix.com/am/")
    print(result)
