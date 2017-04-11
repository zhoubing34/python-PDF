# coding = UTF-8
import urllib2
import re
import os

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


root_url = 'http://iwwwfb2017.dlut.edu.cn'

raw_url = 'http://iwwwfb2017.dlut.edu.cn/meeting/list_en.asp?id=2612&nid=1078'

html = getHtml(raw_url)
url_lst = getUrl(html)

os.mkdir('ldf5_download')
os.chdir(os.path.join(os.getcwd(), 'ldf5_download'))

for url in url_lst[:]:
    url = root_url + url
    print url
    getFile(url)
