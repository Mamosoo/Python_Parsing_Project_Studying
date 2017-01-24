# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

try:
    response = urllib2.urlopen("http://www.mamosoo.tistory.com") # 가져올 주소
    page = response.read().decode('cp949','ignore') # 인코딩 변환
    response.close()

except urllib2.HTTPError, e:
    print e.reason.args[1]

except urllib2.URLError, e:
    print e.reason.args[1]

    soup = BeautifulSoup(page)
