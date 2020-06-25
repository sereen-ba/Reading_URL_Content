###READING A URL COINTENT USING HTTP REQUEST
##Try this URL 'http://dustyfeet.com'
## Urthur: SEREEN BAHDAD

import requests as req
from requests.exceptions import HTTPError #To handel any exception

import cv2  #To display the image you just uploaded it

import numpy as np

URL = input('Enter the URL here: ')
r = req.get(URL)

#print(r.status_code)       ##The status code 200 means a successful execution of request
#print(r.content)           ## To print response bytes

if r:
    print('we are ready now:\n\n\n')
    print(r.text)          #To print the URL content as HTML file
else:
    
    print('sorry I can\'t print read the URL')   

                                          

headers = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}

r = req.get("http://dustyfeet.com", headers=headers)     # modify request headers

print()             ##TO ADD A NEW LINE
print(r.headers)                                # print response headers

#print(r.headers.get('Content-Type()'))         # output: application/json; charset=utf-8  and it will give knowen if you uncomment it

print() 

## To read and download an image from URL
##                                                                   $$$ I USED OPENCV TO SHOW THE IMAGE $$$

# First the user will enter the URL try this 'https://imgs.xkcd.com/comics/making_progress.png'

image_URL=input('Enter the image URL:')


pic =req.get(image_URL)   ##Simmular to the text file the get command is used to read the content of the URL

with open(r'image5.png','wb') as f:   
    
    f.write(pic.content)                                           ## This comand download the image on your machine you may find it on cv2.so file



##now we need to display the image to make sure that the process went well
    
pic = cv2.imread("image5.png",0)

cv2.imshow('pic',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()



 

