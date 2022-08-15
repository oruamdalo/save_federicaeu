from script import Federica
import coloredlogs, logging
from constants import *
from time import sleep
import os
from utils import saveFile
import re

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

# EXAMPLE OF USAGE - NOT OPTIMIZED
scraper = Federica()
scraper.loginCookie()

lectures = scraper.getCourse("https://lms.federica.eu/course/view.php?id=216")

logger.info("Found {} lectures".format(len(lectures)))

for lecture in lectures:
    
    chapters = scraper.getChapters(lecture[0], lecture[1])
    chapters += [lecture[0]] # without &chapterid=ID means first page (usually contains videolecture)
    
    folderName = "YOUR_PATH/LECTURE_{}".format(lecture[1])
    os.makedirs(folderName, exist_ok=True)
    
    
    logger.info("Found {} chapters for lecture {}".format(len(chapters), lecture[1]))
    for chapter in reversed(chapters):
        
        logger.debug("chapter_url: {}".format(chapter))
        try:
            chapterid = re.findall(r"chapterid=(\d+)", chapter)[0]

            logger.info("Scraping chapter {}".format(chapterid))
        except:
            logger.info("Found page without chapterid. Probably it's a video")
            pass
        
        content = scraper.parseChapter(chapter)
        logger.debug("content: {}".format(content))
        if not content[1]:
            try:
                filename = "{}_{}.html".format(lecture[1], chapterid)
                saveFile(folderName + filename, content[0])
            except:
                continue
        else:
            cmd = YTDLP_COMMAND.format(folderName, chapter, content[0])
            logger.debug("ytdlp command: {}".format(cmd))
            os.system(cmd)
            
        sleep(1.5) # Prevent banning (429 or 503)
