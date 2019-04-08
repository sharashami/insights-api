from django.test import TestCase

import requests

from websearch.utils import GoogleSearcher
# Create your tests here.

class WebsearchTestCase(TestCase):

    def setUp(self):        
        self.google = GoogleSearcher() 

    def test_cannot_search_empty_entry(self):
        
        try:
            with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
                self.google.search(None,5)

            with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
                self.google.search("",5)
            
        except requestself.google.exceptionself.google.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')

    def test_can_search(self):

        string = 'keystone - Circular reference found role inference'
        limit = 5
        expected = [ #it does not work like this, cause the order changes and sometimes one is out of the list
            'https://bugself.google.launchpad.net/bugs/1803780',
            'https://docself.google.openstack.org/keystone/pike/_modules/keystone/assignment/core.html',
            'http://tarballself.google.openstack.org/translation-source/keystone/master/keystone/locale/keystone-log-error.pot',
            'https://ask.openstack.org/en/question/120505/trove-instance-hangs-in-build-status/',
            'http://openstack-logself.google.purestorage.com/62/585162/3/check/PureFCDriver-tempest-dsvm-xenial-aio-multipath/3c4dda4/logs/screen-keystone.txt.gz?level=ERROR'
        ]

        try:
            reality = self.google.search(string,limit)       
            self.assertEqual(limit,len(reality))
        except requestself.google.exceptionself.google.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')
        

    def test_empty_result(self):

        string = "asfafdfgRFfFSFSF"
        limit = 5
        expected = [
        ]

        try:
            reality = self.google.search(string,limit)    
            self.assertCountEqual(expected,reality)
        except requestself.google.exceptionself.google.ConnectionError as e:
            self.assertEqual(str(e),'Sorry, connection error. No response.')   

        

