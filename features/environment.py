from steps  import baseclass

def before_scenario(context, scenario):
	context.baseclass = baseclass.BaseClass()
	context.baseclass.browser
	context.baseclass.browser.maximize_window()

def after_scenario(context, scenario):
	context.baseclass.browser.close()
