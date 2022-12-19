# 카이사르 암호

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
st = ""

for i in range(26) :
    st += chr(ord("a")+i)
for i in range(26) :
    st += chr(ord("A")+i)

for i in a :
    if i != " " :
        t = ord(i)+2
        if t >= ord('a') and t <= ord('z') :
            print(chr(t), end="")
        else :
            print(chr(t-26), end="")
    else :
        print(" ", end="")

# i hope you didnt translate it by hand thats what computers are for doing it in by hand is inefficient and thats why this text is so long using stringmaketrans is recommended now apply on the url
# 컴퓨터가 손으로 번역하는 것은 비효율적이며 stringmaketrans를 사용하여 이 텍스트가 너무 긴 이유는 지금 URL에 적용하는 것이 좋습니다

# ans = map => ocr