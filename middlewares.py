# -*- coding:UTF-8 -*-
import random
import base64

from testproxy.settings import PROXIES

#随机切换UserAgent
class RandomUserAgent(object):
    def __init__(self,agents):
        self.agents = agents
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self,request,spider):
        # print "***************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# 智能切换ip
class ProxyMiddleware(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        # request.meta['proxy'] = "http://182.254.139.66:3128"
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s"%proxy['ip_port']
            encode_uer_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encode_uer_pass
            # print "************ProxyMiddleware have pass***********" + proxy["ip_port"]
        else:
            print "************ProxyMiddleware not pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s"%proxy['ip_port']



        # request.meta['proxy'] = "http://119.29.234.174:3128"
        # encode_user_pass = base64.encodestring("longer:longer")
        # request.headers['Proxy-Authorization'] = 'Basic ' + encode_user_pass
        # print "************ProxyMiddleware have pass***********" + proxy["ip_port"]



#
#
# import random
# import base64
# from settings import PROXIES
# class RandomUserAgent(object):
#   """Randomly rotate user agents based on a list of predefined ones"""
#   def __init__(self, agents):
#     self.agents = agents
#   @classmethod
#   def from_crawler(cls, crawler):
#     return cls(crawler.settings.getlist('USER_AGENTS'))
#   def process_request(self, request, spider):
#     #print "**************************" + random.choice(self.agents)
#     request.headers.setdefault('User-Agent', random.choice(self.agents))
# class ProxyMiddleware(object):
#   def process_request(self, request, spider):
#     proxy = random.choice(PROXIES)
#     if proxy['user_pass'] is not None:
#       request.meta['proxy'] = "http://%s" % proxy['ip_port']
#       encoded_user_pass = base64.encodestring(proxy['user_pass'])
#       request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#       print "**************ProxyMiddleware have pass************" + proxy['ip_port']
#     else:
#       print "**************ProxyMiddleware no pass************" + proxy['ip_port']
#       request.meta['proxy'] = "http://%s" % proxy['ip_port']