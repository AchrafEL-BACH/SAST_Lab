# Python 3
import urllib.request

# Six
import six

def test_urlopen():
    # Python 3
    urllib.request.urlopen('file:///bin/ls')
    urllib.request.urlretrieve('file:///bin/ls', '/bin/ls2')
    opener = urllib.request.URLopener()
    opener.open('file:///bin/ls')
    opener.retrieve('file:///bin/ls')
    opener = urllib.request.FancyURLopener()
    opener.open('file:///bin/ls')
    opener.retrieve('file:///bin/ls')

    # Six
    six.moves.urllib.request.urlopen('file:///bin/ls')
    six.moves.urllib.request.urlretrieve('file:///bin/ls', '/bin/ls2')
    opener = six.moves.urllib.request.URLopener()
    opener.open('file:///bin/ls')
    opener.retrieve('file:///bin/ls')
    opener = six.moves.urllib.request.FancyURLopener()
    opener.open('file:///bin/ls')
    opener.retrieve('file:///bin/ls')
