# paypal
# 이미지가 지퍼형태, 해당 페이지 주석의 zip확인
# channel.zip 입력
# README
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip

import re, zipfile

f = open("./data/channel/90052.txt", "r")
tmp = f.read() # 파일번호
f.close()
my_zip = zipfile.ZipFile("./data/channel.zip")
info = my_zip.getinfo("90052.txt")
tmp_z = info.comment.decode("UTF-8") # 설명창

while 1 :
    print(tmp_z, end="")
    num = re.findall("\d{1,}", tmp)[0]
    f = open(f"./data/channel/{num}.txt", "r")
    tmp = f.read()
    f.close()
    info = my_zip.getinfo(num+".txt")
    tmp_z = info.comment.decode("UTF-8")

# 46145
# Collect the comments.
# 설명을 수집하라

# zipfile모듈 사용하여 파일 설명창 확인
# ans? = hockey
# it's in the air. look at the letters.
# 공기 중에 있습니다. 글자를 봐.
# ans = oxygen