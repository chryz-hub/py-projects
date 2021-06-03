# import xml library into the python code
import xml.etree.ElementTree as ET

fname = input('Enter file name: ')

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# defined lookup
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

#parsing using the xml library
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if( lookup(entry, 'Track ID') is None ) : continue

# getting the output desired
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

#if any of the data lack one of these, ignore!
    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)
