from PIL import Image

baseimage=Image.open('/home/path/filename.png')

baseimage.putalpha(100)

hmat,wmat = baseimage.size

watermark=Image.open('/home/path/filename.png')

complete=watermark.resize((hmat,wmat))

complete.paste(baseimage,box=(0,0),watermark=baseimage)

complete.save("/home/path/watermarkedfile.png")
