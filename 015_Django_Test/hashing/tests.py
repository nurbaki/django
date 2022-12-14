from selenium import webdriver
from django.test import TestCase

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000/")


class FunctionalTestCase(TestCase):


    def setUp(self):
        self.browser = webdriver.Chrome()


    def test_there_is_homepage(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn('Enter hash here:',self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id("id_text")
        text.send_keys("hello")
        self.browser.find_element_by_name("submit").click()
        self.assertInHTML("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", self.browser.page_source)