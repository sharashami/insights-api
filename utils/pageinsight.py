from abc import ABC, abstractmethod
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
        '''
        if search_for==None or (not search_for):
            raise ValueError("I can't query for nothing, sorry :(")

        session = HTMLSession()

        for link in pages_link:      

            try:
                r = session.get(link)
            except ConnectionError:
                raise ConnectionError('Sorry, connection error. No response.')

            

            links = r.html.find(f'#search .srg .g div.r > a:nth-child(1)')
            return [link.attrs['href'] for i,link in enumerate(links) if i < limit ]
        '''
        return None, None
        