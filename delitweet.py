#!/usr/bin/env python
#
# Copyright 2013 Antonio Candela
# Author: Antonio Candela
# AKA: Delinet <twitter.com/delinet>
# Web Site: www.snacktech.it
# License: MIT License
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# Created: 04.28.2013
"""
   DeliTweet Library
   ver 0.1
   A class definition to use Twitter API 
"""
import re
import random # use it to generate main random key(s)
import base64 # use it to generate Nonce
import time # use it to generate timestamp and random key(s)
import urllib # use it to make request

class DeliTweet():
   def __init__(self):
      """
      init function: set default istance variables
      DST variable: conteiner for the header string
      """
      self.oauth_consumer_key = ""
      self.oauth_nonce = ""
      self.oauth_signature = ""
      self.oauth_signature_method = "HMAC-SHA1"
      self.oauth_timestamp = ""
      self.oauth_token = ""
      self.oauth_version = "1.0"
   
      self.bss = "" # base signature string - parameters collection
      self.dst = "" # header string   
   
   def setOauthConsumerKey(self,oauth_consumer_key):
      """
      setOauthConsumerKey: set default istance variables oauth_consumer_key
      parameter type: string
      """
      self.oauth_consumer_key = oauth_consumer_key
      
   def setOauthConsumerSecret(self,oauth_consumer_secret):
      """
      setOauthConsumerSecret: set default istance variables oauth_consumer_secret
      parameter type: string
      """
      self.oauth_consumer_secret = oauth_consumer_secret   

   def getOauthTimestamp(self):
      """
      setOauthTimestamp: set and get value of the istance variable oauth_timestamp
      at the valid value for the request
      """
      self.oauth_timestamp = str(int(time.time()))
      return self.oauth_timestamp
   
   def setRequestParameters(self,include_entities_value,parameters_to_set):
      """
      setRequestParameters: set parameters string to use with request API + method of the
      request -> Get or Post
      parameters_to_set: a dictionary (key,value) link to the specific API. 
      Example: https://api.twitter.com/1.1/statuses/user_timeline.json
      parameter_to_set => user_id: value, count: value and so on
      """
      ps = {} # base parameters dictionary 
      ps['include_entities'] = include_entities_value
      ps['oauth_consumer_key'] = self.percent_encode(self.oauth_consumer_key)
      ps['oauth_nonce'] = self.percent_encode(self.oauth_nonce)
      ps['oauth_signature_method'] = self.oauth_signature_method
      ps['oauth_timestamp'] = self.percent_encode(self.oauth_timestamp)
      ps['oauth_toke'] = self.percent_encode(self.oauth_token)
      ps['oauth_versione'] = self.oauth_version
      
      # start - read parameters_to_set. Percent encode key,value and add value(s) to the ps dict
      for key,value in parameters_to_set:
         ps[key] = value
      
      # start - sort and read ps dict. Create the bss string 
      for key in sorted(ps.iterkeys()):
         self.bss += key
         self.bss += ps[key]
         self.bss += '&'
      
      self.bss = self.bss[-1]
      
   def setSignatureBaseString(self,method,apiurl_request,request_parameters):
      sbs = '' #signature base string
      method = method.upper()
      sbs += method
      sbs += '&'
      apiurl_request = self.percent_encode(apiurl_request)
      sbs += apiurl_request
      sbs += '&'
      
   
   def getNonce(self):
      """
      getRandomKeySignture: get a valid signature value for the API request
      LI_BRS: Lorem Ipsum base string to generate a random string
      rks: aka Rnadom Key Signature variable
      """
      LI_BRS = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
      LI_BRS.encode('utf8')
      LI_BRS_splitted = re.findall(r"[\w']+", LI_BRS)
      LI_BRS_splitted = random.sample(LI_BRS_splitted,10)
      rks = ""
      for s in LI_BRS_splitted:
         rks += s
      rks += str(int(time.time()))
      self.oauth_nonce = base64.b64encode(rks) 
      return self.oauth_nonce
   
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
   dt.setOauthConsumerKey('')
   dt.setOauthConsumerSecret('')
   
   
   
   value = 'tnnArxj06cWHq44gCs1OSKk/jLY='
   print dt.percent_encode(value)
   print dt.getNonce()

if __name__ == '__main__':
   main()
