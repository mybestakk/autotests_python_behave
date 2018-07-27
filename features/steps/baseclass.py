# file:features/steps/page.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import sys, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass(object):
	"""docstring for BaseClass"""
	def __init__(self):
		self.browser = webdriver.Chrome("D:/chromedriver.exe")

	def addLine(self):
		print("------------------------------------------------------------------------------------------------------------------")
	
	def goToLink(self, link):
		# print(link)
		self.browser.get(link)

	def waitTime(self, number):
		WebDriverWait(self.browser, number)

	def checkTitle(self, title):
		self.browser.title == title

	def includeText(self, text):
		self.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

	def searchItem(self, text):
		WebDriverWait(self.browser, 5).until(
		EC.element_to_be_clickable((By.ID, 'q'))
		)
		self.browser.find_element_by_id('q').send_keys(text)
		self.browser.find_element_by_id('find').click()

	def openSignInPage(self):
		self.browser.find_element_by_link_text('Зарегистрироваться').click()
		element = self.browser.find_element_by_id('page-title').text
		assert "Регистрация" in element

	def signIn(self, log, pas):
		self.browser.find_element_by_class_name('auth-btn').click()
		self.browser.find_element_by_name('login').send_keys(log)
		self.browser.find_element_by_name('password').send_keys(pas)
		self.browser.find_element_by_class_name('button').click()
		element = self.browser.find_element_by_class_name('username').text
		assert "User_83446" in element

	def openBasket(self):
		self.browser.find_element_by_id('basket').click()
		element = self.browser.find_element_by_class_name('header').text
		assert "Ваша корзина" in element

	def signUp(self, email, pas):
		self.browser.find_element_by_id('email').send_keys(email)
		self.browser.find_element_by_id('password').send_keys(pas)
		self.browser.find_element_by_id('do-registration').click()
		element = self.browser.find_element_by_class_name('elmir-notice').text
		print(element)
		assert "Поздравляем! Регистрация успешно завершена! Теперь Вы можете заполнить данные о себе." in element

	# def clearCache(self):
	#     """Clear the cookies and cache for the Chromebrowser instance."""
	#     self.browser.get('chrome://settings/clearBrowserData')
	#     WebDriverWait(self.browser, 20)
	#     self.browser.find_element_by_id('clearBrowsingDataConfirm').click()
	#     BaseClass.waitTime(self, 100)

	def closeChrome(self):
		self.baseclass.browser.close()
