from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
	
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
	
		#She is invited to do a to-do item straight away
	
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		
		#She types 'Buy peacock features' into a text box
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do list item did not appear in row"
		
		)
	
	
		#When she hits enter, the pages updates and now the page lists the to-do

		#There is still a box inviting her to add another item 

	
		self.fail('Finish the test!')
		
		
 
	
	
	#When she hits enter, the pages updates and now the page lists the to-do

	#There is still a box inviting her to add another item 

	#The page updates again and now shows both items on her list

	#Edith wonders whether the site will remember her list. The she sees that the site has generated a unique URL for her

	#Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')