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
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.htm)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def getUrl2(html2):
    reg2 = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re2 = re.compile(reg2)
    url_lst2 = re.findall(url_re2,html2)
    return(url_lst2)

def getFile(url):
    file_name = url.split('_')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name 

raw_url = 'http://www.iwwwfb.org'
root_url = 'http://www.iwwwfb.org/'

html = getHtml(raw_url)
url_lst = getUrl(html)

os.mkdir('ldf10_download')
os.chdir(os.path.join(os.getcwd(), 'ldf10_download'))

for url in url_lst[:]:
    
    number1=url.split('/')[-1]
    number2=number1.split('.')[0]
    #print number1
    if number2.isdigit() and int(number2)<32: 
        print url
    else:
        continue
    ulr=root_url+url
    print ulr
    html2=getHtml(ulr)
    url_lst2=getUrl2(html2)
    for url2 in url_lst2[:]:
        print url2
        time.sleep(0.5) 
        getFile(url2)
