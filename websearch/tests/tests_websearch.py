from django.test import TestCase

from websearch.utils import GoogleSearcher
# Create your tests here.

class WebsearchTestCase(TestCase):

    def setUp(self):
        pass

    def test_cannot_search_empty_entry(self):

        s = GoogleSearcher() 
        
        with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
            s.search(None,5)

        with self.assertRaisesMessage(ValueError, "I can't query for nothing, sorry :("):
            s.search("",5)
            

    def test_can_search(self):
        s = GoogleSearcher() 
        string = 'keystone - Circular reference found role inference'
        limit = 5
        expected = [
            'https://bugs.launchpad.net/bugs/1803780',
            'https://docs.openstack.org/keystone/pike/_modules/keystone/assignment/core.html',
            'https://docs.openstack.org/keystone/pike/_modules/keystone/resource/core.html',
            'https://ask.openstack.org/en/question/120505/trove-instance-hangs-in-build-status/',
            'https://github.com/Vincit/objection.js/issues/787'
        ]

        reality = s.search(string,limit)       

        self.assertDictEqual(expected,reality)

    def test_empty_result(self):
        s = GoogleSearcher() 
        string = "asfafdfgRFfFSFSF"
        limit = 5
        expected = [
        ]
        reality = s.search(string,limit)       

        self.assertDictEqual(expected,reality)
