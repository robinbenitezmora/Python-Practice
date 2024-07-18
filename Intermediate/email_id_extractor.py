import scrapy
import re
from scrapy_selenium import SeleniumRequest
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import Rule, CrawlSpider

def start_requests(self):
    yield SeleniumRequest(
        url='https://www.geeksforgeeks.org/',
        wait_time=3,
        screenshot=True,
        callback=self.parse,
        dont_filter=True
    )

def parse(self, response):
    links = LxmlLinkExtractor(allow=()).extract_links(response)
    
    Finallinks = [str(link.url) for link in links]

    links = []
    for link in Finallinks:
        if ('Contact' in link) or ('contact' in link) or ('About' in link) or ('about' in link):
            links.append(link)

    links.append(str(response.url))

    l = links[0]
    links.pop(0)

    yield SeleniumRequest(
        url=l,
        wait_time=3,
        screenshot=True,
        callback=self.parse_link,
        dont_filter=True,
        meta={
            'links': links
        }
    )

def parse_link(self, response):
    links = response.meta.get('links')
    flag = 0

    bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'linkedin']
    for word in bad_words:
        if word in str(response.url):
            flag = 1
            break

    if flag != 1:
        html_text = str(response.text)
        mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)

        mail_list = list(set(mail_list))
        if len(mail_list) != 0:
            for mail in mail_list:
                yield {
                    'Email': mail,
                    'Link': str(response.url)
                }

    if len(links) > 0:
        l = links[0]
        links.pop(0)
        yield SeleniumRequest(
            url=l,
            wait_time=3,
            screenshot=True,
            callback=self.parse_link,
            dont_filter=True,
            meta={
                'links': links
            }
        )
    else:
        yield SeleniumRequest(
            url = response.url,
            callback = self.parsed, 
            dont_filter = True
        )

def parsed(self, response):
    emails = list(self.unique_emails)
    finalemail = []

    for email in emails:
        if ('.in' in email) or ('.com' in email) or 'info' in email or 'org' in email:
            finalemail.append(email)

    finalemail = list(set(finalemail))
    yield {
        'Email': finalemail,
        'Link': str(response.url)
    }

    print('\n'*2)
    print('All the emails have been extracted')
    print('\n'*2)

   