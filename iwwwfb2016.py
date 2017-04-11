# coding = UTF-8
import urllib2
import re
import os
import time

# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def getFile(url):
    file_name = url.split('_')[-1]
    try:
        u = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.reason
    else:
        print "Web is OK"
        
    f = open(file_name, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    u.close()
    print "Sucessful to download" + " " + file_name 

raw_url = 'http://www.iwwwfb.org/Workshops/31.htm'

root_url = 'http://iwwwfb2017.dlut.edu.cn'

html = getHtml(raw_url)
url_lst = getUrl(html)

#os.mkdir('iwwwfb2016_download')
os.chdir(os.path.join(os.getcwd(), 'iwwwfb2016_download'))

for url in url_lst[:]:
    #url = root_url + url
    print url
    time.sleep(1.5) 
    getFile(url)
