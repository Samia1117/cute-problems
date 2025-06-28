from concurrent import futures

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    const_prefix = "http://"

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        same_hostname = lambda x, y: x.split('/')[2] == y.split('/')[2]
        seen = set([startUrl])

        with futures.ThreadPoolExecutor(max_workers = 10) as executor:
            futures_q = deque([executor.submit(htmlParser.getUrls, startUrl)])

            while futures_q:
                for url in futures_q.popleft().result():
                    # print(f"found url = {url}")
                    if url not in seen and same_hostname(startUrl, url):
                        seen.add(url)
                        futures_q.append(executor.submit(htmlParser.getUrls, url))
        return list(seen)



        


        
