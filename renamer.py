from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import glob
import os

FOLDER = "D:/nsf/2d/Story/Nhentai/testing/"
PREFIX = "[cin.cin.pw]"


def getTitle(id):
    URI = "https://nhentai.net/g/" + id
    req = Request(URI,
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    title = soup.find("span", "pretty").string
    return title


def getFile():
    FOLDER_NAME = FOLDER + "*.cbz"
    fixed = []
    path = []
    file = glob.glob(FOLDER_NAME)
    for item in file:
        fileName = os.path.basename(item)
        if "-"+PREFIX in fileName:
            path.append(item)
            fixed.append(renameFile(fileName))
    return (fixed, path)


def renameFile(item):
    edited = item.split("-")
    return edited[0]


def fixedName(id, name):
    return os.path.join(FOLDER + id + " - " + name + ".cbz")


def main():
    fixed, path = getFile()
    for k, item in enumerate(fixed):
        os.rename(path[k], fixedName(item, getTitle(item)))


main()
