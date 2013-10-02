from PIL import Image
im = Image.new("RGB", (1440,900), "white")


for j in xrange(0,900,30):
	for i in xrange(0,1440,48):
		for ii in xrange(0,48):
			for jj in xrange(0,30):
				im.putpixel((i+ii,j+jj),(255,0,0))
		im.save("t-test_"+str(j/30)+"_"+str(i/48)+".jpeg","jpeg")

