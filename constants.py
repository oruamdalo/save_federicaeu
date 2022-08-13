LECTURES_REGEX = r"(https:\/\/lms\.federica\.eu\/mod\/book\/view\.php\?id=(\d+))"
CHAPTERS_SELECTOR = ".book_toc >* a"
CHAPTER_BASE_URL = "https://lms.federica.eu/mod/book/view.php?id={}&chapterid={}"
PARSER = 'html.parser'
PLAYER_REGEX = r'<iframe title="" src="(.*?)"'
YTDLP_COMMAND = 'yt-dlp -o "{}%(title)s.%(ext)s" --add-header "Referer: {}" "{}"'