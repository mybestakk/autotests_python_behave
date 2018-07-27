# -*- coding: utf-8 -*-
Feature: Checking search

	Scenario: Open sign in page
		Given we visit link "https://elmir.ua/"
		Then wait "5"
		Then it should have a title "Электронный мир"

	Scenario: Сheck Macbook in search results
		Given we visit link "https://elmir.ua/"
		When search item "Macbook"
		Then page include text "Apple MacBook Air SuperDrive"

	Scenario: Open Basket
		Given we visit link "https://elmir.ua/"
		Then we open basket

	Scenario: Sign In to the personal account
		Given we visit link "https://elmir.ua/"
		Then we sign in "remotework65@gmail.com" "qwertasdf"
		# Then clear cache

	Scenario: Sign Up to the Elmir
		Given we visit link "https://elmir.ua/"
		When we open sign up page
		Then we sign up "qqqq12qqqq@gmail.com" "qwertasdf"