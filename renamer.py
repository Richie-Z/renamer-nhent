from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import glob
import os

FOLDER = "D:/nsf/2d/Story/Nhentai/unprefix/"
PREFIX = ""
EXT = ".cbz"


def getTitle(id):
    URI = "https://nhentai.net/g/" + id
    req = Request(URI,
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    title = soup.find("span", "pretty").string
    return title


def getFile():
    FOLDER_NAME = FOLDER + "*" + EXT
    fixed = []
    path = []
    file = glob.glob(FOLDER_NAME)
    for item in file:
        fileName = os.path.basename(item)
        if PREFIX != "" and PREFIX in fileName:
            path.append(item)
            fixed.append(renameFile(fileName))
        if PREFIX == "" and len(fileName) <= 10:
            path.append(item)
            fixed.append(renameFile(fileName))
    return (fixed, path)


def renameFile(item):
    prefix = PREFIX[0] if PREFIX != "" else "."
    edited = item.split(prefix)
    return edited[0]


def fixedName(id, name):
    return os.path.join(FOLDER + id + " - " + validString(name) + EXT)


def validString(name):
    filename = "".join(i for i in name if i not in '\/:*?<>|"')
    return filename


def main():
    fixed, path = getFile()
    for k, item in enumerate(fixed):
        os.rename(path[k], fixedName(item, getTitle(item)))


def coba():
    fixed, path = getFile()
    for k, item in enumerate(fixed):
        print(k, item)


coba()
