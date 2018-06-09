#-*-coding:utf-8-*-
from urllib import parse
from urllib import request
from html.parser import HTMLParser
import os
import time
import random

baseUrl = 'https://www.repettoelementary.org/'
#baseUrl = 'https://pythonprogramming.net/'
#baseUrl = 'http://www.csulb.edu/university-library'



projectName = 'spider2'

PATH = projectName
webQueue = os.path.join(PATH, 'webQueue.txt')
doneList = os.path.join(PATH, 'doneList.txt')
NUM = 0


def get_full_domain(url):
    try:
        result = get_sub_domain(url).split('.')
        return result[-2]+'.' + result[-1]
    except:
        return ''

def get_sub_domain(url):
    try:
        return parse.urlparse(url).netloc
    except:
        return ''
class linkFinder(HTMLParser):
    try:
        def __init__(self, baseUrl, projectPath, domainName):
            super().__init__()
            self.baseUrl = baseUrl
            self.links = set()
            self.photoLinks = set()
            self.projectPath = projectPath
            self.domainName = domainName
            print(self.projectPath)
        def handle_starttag(self, tag, attrs):
            global NUM

            #img
            if tag == 'img':
                for (attribute, value) in attrs:
                    #src
                    if attribute == 'src':
                        '''
                        if self.domainName not in value:
                            print("not in: ", value)
                            continue
                        '''
                        #slow down....
                        if NUM % 10 == 0 and NUM != 0:
                            sleepTime = random.randint(1, 5)/15
                            print("Rest for {0} second: ".format(sleepTime))
                            time.sleep(sleepTime)
                        #get the full url of that photo
                        itemurl = request.urljoin(self.baseUrl, value)
                        #global NUM
                        name = NUM
                        name = name + 1
                        NUM = name
                        photoName = str(name) + ".jpg"
                        photoPath = os.path.join(self.projectPath, photoName)
                        if os.path.exists(photoPath):
                            print("skipping...",str(name))
                            continue
                        #self.photoLinks.add(itemurl)
                        #when save the image link to file, they become unknown link.. don't know why, bc forgot write(data+'\n')
                        print("photos: ",name)
                        print(itemurl)
                        #download
                        request.urlretrieve(itemurl, photoPath)
            if tag == 'a':
                for(attribute, value) in attrs:
                    if attribute == 'href':
                        '''
                        if self.domainName not in value:
                            print("not in link: ",value)
                            continue
                        '''
                        if 'javascript' in value:
                            continue
                        url = parse.urljoin(self.baseUrl, value)
                        if len(self.links) > 20:
                            pass
                        self.links.add(url)
                        #print("The links: ", url)
        def get_links(self):
            return self.links

        def error(self, message):
            print("Link finder error! ")
    except Exception as e:
        print("Link finder error: ",str(e))





def workSpace(folderPath, baseUrl):
    if not os.path.exists(folderPath):
        print('Creating a folder: ', projectName)
        os.makedirs(projectName)

    if not os.path.exists(webQueue):
        print("Creating file: webQueue.txt")
        write_file(webQueue, baseUrl )
    if not os.path.exists(doneList):
        print("Creating file: doneList.txt")
        write_file(doneList,'')

def write_file(filePath,data):
    with open(filePath,'wt') as f:
        f.write(data + '\n')


def append_file(filePath, data):
    with open(filePath, 'a') as f:
        f.write(data + '\n')


def connect_link(finder, linkGiven):
    req = request.Request(linkGiven)
    req.add_header('User-Agent', 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    req = request.urlopen(req)
    resp = req.read().decode("utf-8")
    #print(resp)
    try:
        finder.feed(resp)
    except Exception as e:
        print("Feed error: ", str(e))


'''
#when save the image link to file, they become unknown link.. don't know why
for i in finder.photoLinks:
    append_file(webQueue, i)
'''

def main():
    #to start
    print("="*35)
    doneSet = set()
    linkTempSet = set()
    workSpace(PATH,baseUrl)
    doneSet = file_to_set(doneList)
    DOMAIN_NAME = get_full_domain(baseUrl)
    finder = linkFinder(baseUrl, PATH, DOMAIN_NAME)
    connect_link(finder, baseUrl)
    linkSet = finder.get_links()
    #set_to_file(linkSet, webQueue)
    print("#"*35)
    print("start as : ")
    print(len(linkSet))
    #nice cycle
    while True:
        remain = len(linkSet)
        for url in linkSet:
            print("-------------------Inside the for loop: ")
            print(url in doneSet)
            print(type(url))
            #print(url)
            #print(doneSet)
            #FIXME: something is wrong, the url is loop back and forth...
            '''
            if url in doneSet:
                print("already in doneset")
                print(url)
            continue
            '''
            finder2 = linkFinder(url, PATH, DOMAIN_NAME)
            connect_link(finder2, url)
            linkTempSet = finder.get_links()
            doneSet.add(url)
            remain -= 1
            print("-------------Remaining Links: ...", remain)
            alreadyNum = len(linkSet) - remain
            if len(doneSet) >= 2:
                set_to_file(doneSet, doneList)
                set_to_file(linkTempSet, webQueue)
        set_to_file(linkSet, doneList)
        set_to_file(linkTempSet,webQueue)
        set_to_file(doneSet,doneList)
        linkSet = file_to_set(webQueue)

def set_to_file(linkSet, filePath):
    for i in linkSet:
        if i not in filePath:
            append_file(filePath, i)

def file_to_set(filePath):
    result = set()
    with open(filePath, 'rt') as f:
        for line in f:
            result.add(line.replace('\n',''))
    return result

main()
