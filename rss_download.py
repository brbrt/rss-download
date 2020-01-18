import os
import re
import shutil
import urllib.request, urllib.parse
import xml.etree.ElementTree as ET


feed_url = os.environ['RSS_DOWNLOAD_FEED_URL']
target_directory = os.environ['RSS_DOWNLOAD_TARGET_DIR']


def download_feed(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return data.decode('utf-8')

def extract_links(feed):
    result = []
    for elem in ET.fromstring(feed).findall(".//item//link"):
        result.append(elem.text)
    return result

def extract_file_name(url):
    url_parts = urllib.parse.urlsplit(url)
    filename = url_parts.path.split("/")[-1]
    unquoted = urllib.parse.unquote(filename)
    return re.sub(r"(\[.*\])(\[.*\])*", "", unquoted) # Remove []

def download_file(url, target_path):
    local_filename, headers = urllib.request.urlretrieve(url, target_path)


feed = download_feed(feed_url)

links = extract_links(feed)
print('Link count:', len(links))

for link in links:
    print('Processing link:', link)
    file_name = extract_file_name(link)

    target_path = os.path.join(target_directory, file_name)
    download_file(link, target_path)

    print('Sucessfully downloaded link to:', target_path)
