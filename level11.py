# 이미지 분리

from PIL import Image

with Image.open("./data/cave.jpg") as img :
    odd_img = Image.new("RGB",img.size)
    even_img = Image.new("RGB",img.size)
    for y in range(img.height) :
        for x in range(img.width) :
            if((x+y)%2==0) :
                even_img.putpixel((x,y),img.getpixel((x,y)))                
            else :
                odd_img.putpixel((x,y),img.getpixel((x,y)))

    odd_img.save("./data/odd_image.png")
    even_img.save("./data/even_image.png")

# ans = evil