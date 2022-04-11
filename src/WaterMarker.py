# install pillow

from Pillow import Image

print("Welcome to WaterMarker")
print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

Gonogo=input()

while Gonogo=="n":
    print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")
    Gonogo=input()  

if Gonogo=="y":
    baseimage=Image.open('/home/WaterMarker/image.png')
    baseimage.putalpha(100)
    hmat,wmat = baseimage.size
    watermark=Image.open('/opt/WaterMarker/src/watermark.png')
    complete=watermark.resize((hmat,wmat))
    complete.paste(baseimage,box=(0,0),watermark=baseimage)
    complete.save("/home/WaterMarker/watermarkedimage.png")
    print("Your watermarked file has been saved to your desktop with filename watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")
