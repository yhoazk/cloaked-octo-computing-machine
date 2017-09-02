#!/usr/bin/python -tt
"""
now the king is dead

sweet baby jesus
cats are eating my baby
turtles have boners
"""

from mechanize import Browser
browser = Browser()
browser.set_handle_robots(False)
response = browser.open('http://www.google.com')
print response.code
