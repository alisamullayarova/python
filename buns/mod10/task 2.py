import requests
import re

def get_html(url):
    response = requests.get(url)
    html = response.text
    subheadings = re.findall(r'<h3.*?>(.*?)</h3>', html)
    return subheadings

url = 'http://www.columbia.edu/~fdc/sample.html'
print(get_html(url))