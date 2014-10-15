from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn ('To-Do', self.browser.title)
		self.fail('Finish the test!')
		
		
 
	#She is invited to do a to-do item straight away

	#She types 'Buy peacock features' into a text box

	#When she hits enter, the pages updates and now the page lists the to-do

	#There is still a box inviting her to add another item 

	#The page updates again and now shows both items on her list

	#Edith wonders whether the site will remember her list. The she sees that the site has generated a unique URL for her

	#Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')