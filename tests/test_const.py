import urllib.parse

USERNAME = 'bonicillo.m'
PASSWORD = 'toast'
REL_FRIEND_URL = '/fakebook/50644342'
FRIEND_HOME_URL = 'http://cs5700sp15.ccs.neu.edu/fakebook/50644342/'
FRIEND_VIEW_FRIENDS_URL = 'http://cs5700sp15.ccs.neu.edu/fakebook/50644342/friends/1/'
ARGV = ['webcrawler', USERNAME, PASSWORD]
FB_URL_PREFIX = 'http://cs5700sp15.ccs.neu.edu'
FB_LOGIN_URL = 'http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/'
LOGIN_DATA = urllib.parse.urlencode(
    {'username': USERNAME,
     'password': PASSWORD,
     'next': '/fakebook/',
     'csrfmiddlewaretoken': 'foobar'})
# My landing page html
MEMBER_LP_HTML = r'''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1>Welcome to Fakebook</h1><p>Get started by browsing some random people's profiles!</p><ul><li><a href="/fakebook/996350946/">Pube Bregel</a></li><li><a href="/fakebook/996460889/">Pugidotu Vuvot</a></li><li><a href="/fakebook/996604893/">Ali Transou</a></li><li><a href="/fakebook/996793509/">Edmundo Gresl</a></li><li><a href="/fakebook/997083323/">Hosea Gandarillia</a></li><li><a href="/fakebook/997892294/">Candie Bookmiller</a></li><li><a href="/fakebook/998156234/">Ezequiel Bossardet</a></li><li><a href="/fakebook/998192170/">Tia Linney</a></li><li><a href="/fakebook/998640929/">Jewell Latos</a></li><li><a href="/fakebook/999148512/">Rosamunde Crucass</a></li></ul><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
# Pollock's Landing page
FRIEND_LP_HTML = r'''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1><a href="/fakebook/26378739/">Riccardo Pollock</a></h1><h2>Basic Information</h2><ul><li>Sex: Female</li><li>Hometown: Belmont</li></ul><h2>Personal Information</h2><ul></ul><h2>Friends</h2><p><a href="/fakebook/26378739/friends/1/">View Riccardo Pollock's friends</a></p><h2>Wall</h2><p>
Riccardo Pollock has not received any Wall posts.
</p><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
# Bregel's first page of list of friends
VIEWING_FRIENDS_HTML = r'''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1>Viewing <a href="/fakebook/996350946/">Pube Bregel</a>'s Friends</h1><ul><li><a href="/fakebook/8185551/">Zop Joxell</a></li><li><a href="/fakebook/70552327/">Jimavuzote Jotet</a></li><li><a href="/fakebook/79437786/">Junzo Trout</a></li><li><a href="/fakebook/89081356/">Rob Hegler</a></li><li><a href="/fakebook/152068235/">Nixegoco Sosed</a></li><li><a href="/fakebook/182325757/">Nivosi Xexep</a></li><li><a href="/fakebook/194756826/">Ludmilla Vacat</a></li><li><a href="/fakebook/216285855/">Malcom Burdi</a></li><li><a href="/fakebook/224009282/">Doranna Xivann</a></li><li><a href="/fakebook/299346627/">Giuseppe Waller</a></li><li><a href="/fakebook/306053677/">Nak Treloll</a></li><li><a href="/fakebook/316039351/">Mal Plevac</a></li><li><a href="/fakebook/320286626/">Hiliha Zbenenn</a></li><li><a href="/fakebook/320298083/">Hime Psehod</a></li><li><a href="/fakebook/322403147/">Jeaniene Brabil</a></li><li><a href="/fakebook/331516212/">Gavin Tupot</a></li><li><a href="/fakebook/414226914/">Tarah Mentkowski</a></li><li><a href="/fakebook/451340070/">Nenababonu Justiss</a></li><li><a href="/fakebook/464413390/">Dibume Bertin</a></li><li><a href="/fakebook/517450351/">Jeremias Plupet</a></li></ul><p>Page 1 of 2
<ul id="pagelist"><li>
1 

</li><li><a href="/fakebook/996350946/friends/2/">2</a></li><li><a href="/fakebook/996350946/friends/2/">next</a></li><li><a href="/fakebook/996350946/friends/2/">last</a></li></ul></p><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
