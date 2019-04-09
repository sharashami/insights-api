from abc import ABC, abstractmethod
import asyncio
import requests
from requests_html import HTML, HTMLSession
from requests.exceptions import ConnectionError

class PageInsight:
    
    """ Returns the most relevant information related to search_for in each link in pages_link and optionally extra info.
    
    Args:
        pages_link (list): List of pages urls.
        search_for (string): The entry used to detect the key words and find the most relevant content.

    Raises:
        ValueError: If pages_link or search_for is empty/None or invalid URLs.
        ConnectionError: If no response.

    Returns:
        key_words : A list of strings representing the key words from search_for.
        insights: A list of dictionaries with keys: link_page, most_revelant and extra. 

    """ 
    def most_revelant_information(self,pages_link, search_for):
        
        if search_for==None or (not search_for):
            raise ValueError("I can't query for nothing, sorry :(")

        session = HTMLSession()
        results = []
        for link in pages_link:
            try:
                r = session.get(link)
                results.append(r)
            except requests.exceptions.ConnectionError:
                results.append(link)
        
        for r in results:
            print(r.html.url)

        return None, None

if __name__ == "__main__":
      PageInsight().most_revelant_information(pages_link=[
            'https://ask.openstack.org/en/question/120505/trove-instance-hangs-in-build-status/',
            'http://openstack-logself.google.purestorage.com/62/585162/3/check/PureFCDriver-tempest-dsvm-xenial-aio-multipath/3c4dda4/logs/screen-keystone.txt.gz?level=ERROR'],
                                            search_for="keystone - Circular reference found role inference")