import requests
import  re

url = 'http://image.baidu.com/search/index?ct=201326592&cl=2&nc=1&lm=-1&st=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=%B1%ED%C7%E9%B0%FC&fr=wenku&ie=gbk'

url1 = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=&hd=&latest=&copyright=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=90&rn=30&gsm=5a&1584436500599='
url2 = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=&hd=&latest=&copyright=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=120&rn=30&gsm=78&1584436500680='


headers={'Referer': 'http://image.baidu.com/search/index?ct=201326592&cl=2&nc=1&lm=-1&st=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=%B1%ED%C7%E9%B0%FC&fr=wenku&ie=gbk'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

wabgzhi =[]
#获取图片的统一资源定位符
for i in range(30,91,30):
    img_li = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=&hd=&latest=&copyright=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=2&qc=&nc=1&fr=&expermode=&force=&pn='+str(i)+'&rn=30&gsm=5a&1584436500599='
    res = requests.get(img_li,headers=headers)
    html = res.text
    img_url = re.findall(r'"thumbURL":"(http://.*?)"',html)
    wabgzhi+=img_url

# print(wabgzhi)
#下载图片
for index,i in enumerate(wabgzhi):
    print(index)
    res =requests.get(i,headers=headers)
    img_tu = res.content
    print(img_tu)
    img_name = "img"+str(index)+".jpg"
    # with open(img_name,"wb") as f:
    #     f.write(img_tu)
print('好了')



