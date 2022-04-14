# install pillow

from PIL import Image

print("Welcome to WaterMarker")
print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

Gonogo=input()

while Gonogo=="n":
    print("Have you saved the file to be watermarked to the WaterMarker folder (/opt/WaterMarker/src/images) with filename image.png?(y/n)")
    Gonogo=input()  

if Gonogo=="y":
    words=Image.open('/opt/WaterMarker/images/image.png')
    hmat,wmat = words.size
    mask=Image.open('/opt/WaterMarker/src/watermark.png')
    mask.putalpha(150)
    complete=mask.resize((hmat,wmat))
    complete.paste(words,(0,0),mask=words)
    complete.save("/opt/WaterMarker/images/watermarkedimage.png")
    print("Your watermarked file has been saved to /opt/WaterMarker/images/watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")
