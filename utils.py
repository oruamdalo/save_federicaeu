def getPage(url, session):
    return session.get(url, cookies = {
        "MoodleSession": "YOUR_COOKIE",
        "cc_cookie" : '{"level":["necessary","analytics"],"revision":0,"data":null,"rfc_cookie":false}'
    }).text


def saveFile(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

