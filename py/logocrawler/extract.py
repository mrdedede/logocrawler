import urllib.request as req
import threading

def get_html_body(url):
    """
    Given a URL, this function should return the body of the URL

    Args:
        url (str): The URL currently being analysed and fetched
    
    Retuns:
        str: the body of the request
    """
    hdr = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.0.3 Safari/537.36'
    }

    beginnings_list = ["https://www.", "http://www.", "http://", "https://"]
    results_list = []

    def request_url(full_url):
        """
        Given a full URL (path), this function will append the retrieved values to results_list

        Args:
            full_url (str): The full URL, including the http method and www
        """
        try:
            req_object = req.Request(full_url, headers=hdr)
            res = req.urlopen(req_object, timeout=60)
            results_list.append(res.read().decode())
        except Exception as e:
            #TODO: Deal with HTTP Errors in a better way, most of them are just 403 forbidden
            results_list.append(e)
    
    for index in range(0, len(beginnings_list) - 1, 2):
        request_1 = threading.Thread(target=request_url, args=((beginnings_list[index]+url),))
        request_2 = threading.Thread(target=request_url, args=((beginnings_list[index+1]+url),))

        request_1.start()
        request_2.start()

        request_1.join()
        request_2.join()

        final_results = [res for res in results_list if not isinstance(res, Exception)]

        if len(final_results) > 0:
            return final_results[0]

    return "UNREACHABLE"

def get_urls(urls):
    """
    Given a list of URLs, this function returns a iterable that would generate the result of the HTTP request
    one at a time

    Args:
        url (list): A list of https URLs to be requested

    Yields:
        str: The body of a URL
    """
    for url in urls:
        body = get_html_body(url)
        yield body
