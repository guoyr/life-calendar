from PIL import Image
im = Image.new("RGB", (1440,900), "white")


year = 1
month = 1
for j in xrange(0,900,30):
	for i in xrange(0,1440,48):
		for ii in xrange(0,48):
			for jj in xrange(0,30):
				im.putpixel((i+ii,j+jj),(255,0,0))
		im.save("t-test_"+str(year)+"_"+str(month)+".jpeg","jpeg")
		month += 1
		if month > 12:
			month = 1
			year += 1

