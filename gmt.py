# GMT check and push to the forum

import re
import requests

#channel = "https://www.youtube.com/user/benoistrousseauandli"
channel = "https://www.youtube.com/@BenoistRousseau/streams"
html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

print(info)
print(url)