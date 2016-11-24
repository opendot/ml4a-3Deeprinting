from lxml import html
import requests
import wget
import time

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

            print 'Query', q, 'page', p

            searchUrl  = 'http://www.thingiverse.com/search/page:' + str(p) + '?sort=makes&q=' + q + '&type=things'

            searchPage = requests.get(searchUrl)
            tree = html.fromstring(searchPage.content)

            # get item links
            objectURLs = tree.xpath('//a[@class="thing-img-wrapper"]/@href')

            for objectURL in objectURLs:
                fullObjectUrl = 'http://www.thingiverse.com' + objectURL

                objPage = requests.get(fullObjectUrl)
                objTree = html.fromstring(objPage.content)

                #print objPage.text
                print '\t\t Page', fullObjectUrl
                downloadURL = objTree.xpath('//a[@class="track thing-file-download-link"]/@href')
                if len(downloadURL) > 0:
                    downloadURL     = downloadURL[0]    # only first (they are ordered by downloads)
                    fullDownloadURL = 'http://www.thingiverse.com/' + downloadURL
                    print '\t\t Download', fullDownloadURL

                    wget.download(fullDownloadURL, 'data/' + downloadURL + '_' + str(time.time()) )