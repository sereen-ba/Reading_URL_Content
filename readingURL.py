import urllib.request
import ssl
url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
file = urllib.request.urlopen(url) ##to read a text file from a URL
for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)
##to read an image from an url use 'urlretrieve'
