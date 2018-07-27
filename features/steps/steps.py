# -*- coding: utf-8 -*-
from behave import *

from baseclass import BaseClass


@given('line')
def step_impl(context):
	context.baseclass.addLine()

@given('we visit link "{link}"')
def step_impl(context,link):
	context.baseclass.goToLink(link)
	assert True is not False

@step('close Chrome')
def step_impl(context):
	context.baseclass.closeChrome()
	assert True is not False


@step('wait "{number}"')
def step_impl(context,number):
	context.baseclass.waitTime(number)
	assert True is not False

@step('it should have a title "{title}"')
def step_impl(context,title):
	context.baseclass.checkTitle(title)
	assert True is not False

@step('search item "{text}"')
def step_impl(context, text):
	context.baseclass.searchItem(text)
	assert True is not False

@step('page include text "{text}"')
def step_impl(context, text):
	context.baseclass.includeText(text)
	assert True is not False

@step('we open basket')
def step_impl(context):
	context.baseclass.openBasket()
	assert True is not False

@step('we open sign up page')
def step_impl(context):
	context.baseclass.openSignInPage()
	assert True is not False

@step('we sign in "{log}" "{pas}"')
def step_impl(context, log, pas):
	context.baseclass.signIn(log, pas)
	assert True is not False

@step('we sign up "{email}" "{pas}"')
def step_impl(context, email, pas):
	context.baseclass.signUp(email, pas)
	assert True is not False

@step('clear cache')
def step_impl(context):
	context.baseclass.clearCache()
	assert True is not False