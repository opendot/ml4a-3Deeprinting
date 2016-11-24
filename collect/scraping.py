from lxml import html
import requests

# starts here
if __name__ == '__main__':

    queries = [
        'vase',
        'vases',
        'pot',
    ]
    pages = 10

    for q in queries:
        for p in range(pages):
            searchUrl  = 'http://www.thingiverse.com/search/page:' + str(p) + '?sort=makes&q=' + q + '&type=things'

            searchPage = requests.get(searchUrl)
            tree = html.fromstring(searchPage.content)

            print searchUrl, tree.xpath('//div[@title="buyer-name"]/text()')
            exit()