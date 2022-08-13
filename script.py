#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
from utils import getPage
from constants import *


class Federica:
    def __init__(self):
        self.session = requests.Session()
    
    def login(self, user, pwd):
        pass
    
    def loginCookie(self):
        pass
    
    # Get all lectures id (and urls) for selected course
    def getCourse(self, course_url):
        page = getPage(course_url, self.session)
        lectures_url = re.findall(LECTURES_REGEX, page)
        return lectures_url

    # Get all chapters from lecture selected
    def getChapters(self, lecture_url, lecture_id):
        page = getPage(lecture_url, self.session)
        
        soup = BeautifulSoup(page, PARSER)
        
        chapters_url = [CHAPTER_BASE_URL.format(lecture_id, x['href']) for x in soup.select(CHAPTERS_SELECTOR)]
        return chapters_url

    def parseChapter(self, chapter_url):
        page = getPage(chapter_url, self.session)
        
        videoSrc = re.findall(PLAYER_REGEX, page)
        
        # No video
        if len(videoSrc) > 0:
            return (videoSrc[0], True) # True -> there is video, False -> no video
        else:
            soup = BeautifulSoup(page, PARSER)
            return (str(soup.select("div.book_content")[0]), False)

