
import requests



def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://wlxy.hotwind.net/do.win?go=mytrainingprogram")
#req = urllib.request.urlopen("http://www.baidu.com")

# urllib.request.urlretrieve("http://cn.bing.com/","E:\\bing.html")

#print(req.read())

print(html)
