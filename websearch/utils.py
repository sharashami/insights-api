from abc import ABC, abstractmethod

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
        return_limit (int): The max number of links to be returned.

    Raises:
        ValueError: If search_for is None or empty.

    Returns:
        An empty dictionary or a dictionary sized up to return_limit

    """
    def search(self, search_for, return_limit):
        return []

#one can add more searchers below

class PageInsight:

    def __init__(self, page_link):
        self.page_link = page_link
        
    def most_revelant_information(self):
        return None
        
    def extra_information(self):
        return None