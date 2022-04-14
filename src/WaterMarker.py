# install pillow

from PIL import Image

print("Welcome to WaterMarker")
print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

Gonogo=input()

while Gonogo=="n":
    print("Have you saved the file to be watermarked to the WaterMarker folder (/opt/WaterMarker/src/images) with filename image.png?(y/n)")
    Gonogo=input()  

if Gonogo=="y":
    words=Image.open('/opt/WaterMarker/images/image.jpg')
    words.save("/opt/WaterMarker/images/temp.png")
    words2=Image.open("/opt/WaterMarker/images/temp.png")
    words2.putalpha(150)
    hmat,wmat = words2.size
    mask=Image.open('/opt/WaterMarker/src/watermark.png')
    # need to remove the grid from the mask
    mask.putalpha(255)
    complete=mask.resize((hmat,wmat))
    complete.paste(words2,box=(0,0),mask=words2)
    complete.save("/opt/WaterMarker/images/watermarkedimage.jpg")
    # delete the temp file
    print("Your watermarked file has been saved to /opt/WaterMarker/images/watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")
