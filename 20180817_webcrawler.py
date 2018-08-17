import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
#urlopen中的url中可以是字符串也可以是request对象，如果传入request，默认将其转换成request对象
cat_img = response.read()
with open('cat_200_300.jpg','wb') as f:
      f.write(cat_img)