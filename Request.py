from HttpsAdapter import requests, DESAdapter

class Request:
    @staticmethod
    def get_response(url:str):
        tmoval=10
        proxies={}
        hdr = {'Accept-Language':'ru-RU,zh;q=0.8,en-US;q=0.6,en;q=0.4', 'Cache-Control':'max-age=0', 'Connection':'keep-alive', 'Proxy-Connection':'keep-alive', #'Cache-Control':'no-cache', 'Connection':'close',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
                'Accept-Encoding':'gzip,deflate,sdch','Accept':'*/*'}
        ses = requests.session()
        ses.mount(url, DESAdapter())

        return ses.get(url, timeout=tmoval, headers = hdr, proxies=proxies)