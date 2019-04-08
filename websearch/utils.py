from abc import ABC, abstractmethod
from requests_html import HTML, HTMLSession
from requests.exceptions import ConnectionError

class WebSearcher(ABC):
    search_url = None

    @abstractmethod
    def search(self, search_for, return_limit):
        pass

class GoogleSearcher(WebSearcher):
    
    def __init__(self):
        self.search_url = "https://www.google.com/search?q="


    """Return the top 5 google link results.
    
    Args:
        search_for (str): The string to search for.
        limit (int): The max number of links to be returned.

    Raises:
        ValueError: If search_for is None or empty.

    Returns:
        An empty list or a list sized up to limit

    """
    def search(self, search_for, limit=5):
        if search_for==None or (not search_for):
            raise ValueError("I can't query for nothing, sorry :(")

        session = HTMLSession()
        try:
            r = session.get(f'{self.search_url}{search_for}')
        except ConnectionError:
            raise ConnectionError('Sorry, connection error. No response.')

        links = r.html.find(f'#search .srg .g div.r > a:nth-child(1)')
        return [link.attrs['href'] for i,link in enumerate(links) if i < limit ]

#one can add more searchers below

class PageInsight:
    
    """ Returns the most relevant information related to searching_for in each link in pages_link and optionally extra info.
    
    Args:
        pages_link (list): List of pages urls.
        searching_for (string): The entry used to detect the key words and find the most relevant content.

    Raises:
        ValueError: If pages_link or searching_for is empty/None or invalid URLs.
        ConnectionError: If no response.

    Returns:
        key_words : A list of strings representing the key words from searching_for.
        insights: A list of dictionaries with keys: link_page, most_revelant and extra. 

    """ 
    def most_revelant_information(self,pages_link, searching_for):

        return None, None
        