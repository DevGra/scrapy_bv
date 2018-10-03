
import requests

url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

print "downloading with requests"
r = requests.get(url)
# with open("code3.zip", "wb") as code:
#     code.write(r.content)

