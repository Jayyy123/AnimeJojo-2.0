from optparse import Values
from turtle import title
from unittest import result
from django.shortcuts import redirect, render
from numpy import imag
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
from django.contrib.auth.decorators import login_required

def home(request):
        # r = requests.get('https://www.python.org')
        # url = "https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=148"
        # data = requests.get(url)
        # with open('topnewsfeed.xml', 'wb') as f:
        #     f.write(data.content)

        # tree = ET.parse(data)
        # root = tree.getroot()
        # ET.etree.ElementTree.dump(tree)
        # doc = minidom.parse('topnewsfeed.xml')
        # anime = doc.getElementsByTagName('report')[0]
        # item = anime.getElementByTagName('items')[0]
        # for i in item:
        #     print(i)
        # def pars():
        #     xmldoc = minidom.parse('topnewsfeed.xml')
        #     readbitlist = xmldoc.getElementsByTagName('item')
        #     b = readbitlist.getElementsByTagName('anime')
        #     values = []
        #     for s in b  :
        #         # x = s.attributes['anime'].value
        #         values.append(s)
        #     return values
            

        # def pars():
        #     xmldoc = minidom.parse('topnewsfeed.xml')
        #     root = xmldoc.getroot()
        #     elements = []
        #     for readbit in root.findall('item'):
        #         # get the attribute with value equal 'bit'
        #         bit = readbit.get('anime')
        #         elements.append(bit)
        #     return elements

        # values = pars()
    url = "https://jikan1.p.rapidapi.com/top/anime/1/upcoming"

    headers = {
        'x-rapidapi-host': "jikan1.p.rapidapi.com",
        'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
    }
    response = requests.request("GET", url, headers=headers)
    
    values = response.json()
    val = values["top"]
    title = []
    url = []
    image = []
    for i in val:
        title.append(i["title"])
        url.append(i["url"])
        image.append(i["image_url"])
    rang = range(0, len(title))
    ran = len(title) - 1
    # print(title)
    data = [{"title":title, "url":url, "image":image}]

    data1 = zip(title,image,url)
    
    print(len(title))

    title_set1 = title[:15]
    url_set1 = url[:15]
    image_set1 = image[:15]
    data2 = zip(title_set1,image_set1,url_set1)

    # Top anime

    url1 = "https://anime-release.p.rapidapi.com/anime"

    headers1 = {
    'x-rapidapi-host': "anime-release.p.rapidapi.com",
    'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
    }

    response1 = requests.request("GET", url1, headers=headers1)

    topValues = response1.json()
    top_title = []
    top_url = []
    top_source = []

    for n in topValues:

        top_title.append(n['title'])
        top_url.append(n['url'])
        top_source.append(n['source'])

    top_t = top_title[:10]
    top_u = top_url[:10]
    top_s = top_source[:10]

    data3 = zip(top_t,top_u,top_s)

    return render(request, 'base/home.html',{'d':data2, 'dd':data3})

login_required('loginPage')
def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def allAnime(request):
    # url = "https://hummingbirdv1.p.rapidapi.com/anime/steins-gate"

    # headers = {
    #     'x-rapidapi-host': "hummingbirdv1.p.rapidapi.com",
    #     'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
    #     }

    # response = requests.request("GET", url, headers=headers)
    # response.json

    a = pd.read_csv('AnimeList.csv')
    b = []
    b.append(a['title'])
    def loop():
        b =[]
        b.append(a['title'])
        count = 0
        result = []
        while count < 14477:
            count += 1
            for i in b:
                result.append(i[count])
        return result

    a = loop()



    # return render(request, 'parse.html', {'values': values})

    # print(data.content)


    return render(request, 'base/database.html', {'b':b,'rang': a})

def home1(request):


    url = "https://jikan1.p.rapidapi.com/top/anime/1/upcoming"

    headers = {
        'x-rapidapi-host': "jikan1.p.rapidapi.com",
        'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
    }
    response = requests.request("GET", url, headers=headers)
    
    values = response.json()
    val = values["top"]
    title = []
    url = []
    image = []
    for i in val:
        title.append(i["title"])
        url.append(i["url"])
        image.append(i["image_url"])
    rang = range(0, len(title))
    ran = len(title) - 1
    # print(title)
    data = [{"title":title, "url":url, "image":image}]

    data1 = zip(title,image,url)
    
    print(len(title))

    title_set1 = title[:15]
    url_set1 = url[:15]
    image_set1 = image[:15]
    data2 = zip(title_set1,image_set1,url_set1)

    # Top anime

    url1 = "https://anime-release.p.rapidapi.com/anime"

    headers1 = {
    'x-rapidapi-host': "anime-release.p.rapidapi.com",
    'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
    }

    response1 = requests.request("GET", url1, headers=headers1)

    topValues = response1.json()
    top_title = []
    top_url = []
    top_source = []

    for n in topValues:

        top_title.append(n['title'])
        top_url.append(n['url'])
        top_source.append(n['source'])

    top_t = top_title[:10]
    top_u = top_url[:10]
    top_s = top_source[:10]

    data3 = zip(top_t,top_u,top_s)

    # print(response1.text)


    if request.method == "POST":
        q = request.POST['search']
        print(q)
        
        url2 = "https://jikan1.p.rapidapi.com/search/anime"

        querystring = {"q":q}

        headers2 = {
            'x-rapidapi-host': "jikan1.p.rapidapi.com",
            'x-rapidapi-key': "c35ac8900cmsh5ca7846ec59e70dp144bafjsn316847f30361"
            }

        response2 = requests.request("GET", url2, headers=headers2, params=querystring)
        # print(response.text)
        print(response2.text)

    return render(request,'base/home1.html',  {'d':data2, 'dd':data3})

def slideshow(request):
    return render(request,'base/slideshow.html')