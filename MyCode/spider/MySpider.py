import urllib.parse
import urllib.request

def GetHtml(url,values):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    headers = {'User-Agent',user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html

#获取数据
def requestCnblogs(index):
    print('请求数据')
    # url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
    url = 'http://news.baidu.com/'
    value= {
         'CategoryId':808,
         'CategoryType' : 'SiteHome',
         'ItemListActionName' :'PostList',
         'PageIndex' : index,
         'ParentCategoryId' : 0,
        'TotalPostCount' : 4000
    }
    result = GetHtml(url,value)
    return result

if __name__ == '__main__':
    requestCnblogs(1) 