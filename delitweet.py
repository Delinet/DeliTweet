#!/usr/bin/env python
#
# Copyright 2013 Antonio Candela
#
# Author: Antonio Candela <candela.antonio@gmail.com>
# AKA: Delinet <twitter.com/delinet>
# Web Site: www.snacktech.it
# License: GNU
# Created: 04.28.2013
"""
   DeliTweet Library
   ver 0.1
   A class definition to use Twitter API 
"""

import urllib

class DeliTweet():
   def __init__(self):
      """
      init function: set default istance variables
      """
      pass

   def percent_encode(self,parToEncode):
      """
      percent_encode: class module to encode [parToEncode]
      in percent coding
      """
      valueEncoded = parToEncode.encode('utf8') #unicode encode
      valueEncoded = urllib.quote(valueEncoded, '')
      return valueEncoded

def main():
   dt = DeliTweet()
   value = 'tnnArxj06cWHq44gCs1OSKk/jLY='
   print dt.percent_encode(value)
   

if __name__ == '__main__':
   main()
