# Save Federica.EU
Small python tool for downloading lectures from MOOC federica.eu

## What
A tool for downloading both videos and written contents from courses hosted on federica.eu

## How
Open in your favourite browser the course page, login and get current cookies (MoodleSession is important)

## Requirements
 - Python 3
  - BeautifulSoup4, Requests
 - YT-DLP

## Todo
-[x] Detect and download video lectures (w/ yt-dlp)
-[x] Download html of lecture (only relevant parts - what you would see in focus mode)
-[x] Download each lecture materials in different directories
-[ ] Create a html template with basic navigation for easy content exploring (maybe adpating reveal.js, idk)
-[ ] Automatically retrive cookies from login (now they are hardcoded)
-[ ] Some mechanism to save already processed and downloaded courses
-[ ] Better error management
-[ ] Get Quiz pages (they are interactive, I don't how and if I'll do it)


