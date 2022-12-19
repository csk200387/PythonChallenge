# follow the chin

import re, requests

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"

nextlink = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
req = requests.get(link)
nothing = None
while 1 :
    try :
        nothing = re.findall("\d{1,}",req.text)[0]
        print(req.text)
        req = requests.get(nextlink+nothing)
    except :
        break

# 16044 devide
# You've been misleaded to here. Go to previous one and check.
# 여기까지 오셨습니다. 이전 항목으로 이동하여 확인하십시오.
# There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579
# 63579 넣고 다시 진행
# ans = peak.html