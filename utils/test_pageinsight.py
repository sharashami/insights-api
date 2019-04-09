from unittest import TestCase
from contextlib import contextmanager
import requests

from simpletest import SimpleTest
from pageinsight import PageInsight

class PageInsightTestCase(SimpleTest):    
   
    def test_invalid_url(self):

        try:
            with self.assertRaisesMessage(ValueError, "Please, provide valid URL(s)."):
                PageInsight().most_revelant_information(pages_link=['http://www.google.com','fdfsgsd'], search_for="keystone - Circular reference found role inference")
                   
        except requests.exceptions.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')
            
    def test_empty_pages_link(self):

        try:
            with self.assertRaisesMessage(ValueError, "Please, provide the link page(s)."):
                PageInsight().most_revelant_information(pages_link=None, search_for="keystone - Circular reference found role inference")
            
            with self.assertRaisesMessage(ValueError, "Please, provide the link page(s)."):
                PageInsight().most_revelant_information(pages_link=[], search_for="keystone - Circular reference found role inference")
                            
        except requests.exceptions.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')
            

    def test_cannot_search_empty_entry(self):

        try:
            with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
                PageInsight().most_revelant_information(pages_link=["http://www.google.com"], #site that hardly ever is down
                                        search_for="")
                                        
            with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
                PageInsight().most_revelant_information(pages_link=["http://www.google.com"], #site that hardly ever is down
                                    search_for=None)
 
        except requests.exceptions.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')
            
    def test_returns_any_information(self):
        
        try:
            key_words, insights = PageInsight().most_revelant_information(pages_link=["https://bugs.launchpad.net/bugs/1803780"], 
                               search_for="keystone - Circular reference found role inference")
            
            self.assertIsNotNone(key_words)
            self.assertTrue(len(key_words))

            self.assertIsNotNone(insights)
            self.assertTrue(len(insights))

            expected_keys = ['link', 'most_relevant', 'extra', 'status']

            for dicts in insights: self.assertDictEqual(expected_keys, dicts.keys())

        except requests.exceptions.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')

if __name__ == "__main__":
    unittest.main()