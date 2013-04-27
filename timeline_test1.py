#!/usr/bin/env python
#
# Copyright 2013 Antonio Candela
#
# Author: Antonio Candela <candela.antonio@gmail.com>
# AKA: Delinet <twitter.com/delinet>
# Web Site: www.snacktech.it
#

import urllib2
user_nick = 'Delinet'
response = urllib2.urlopen('http://www.example.com/')
timeline = response.read()
print timeline