MEMBER_LANDING_HTML = r'''<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1>Welcome to Fakebook</h1><p>Get started by browsing some random people's profiles!</p><ul><li><a href="/fakebook/190909169/">Zulirecate Zbomann</a></li><li><a href="/fakebook/191050166/">Refegisono Truslow</a></li><li><a href="/fakebook/192028748/">Hyman Arildsen</a></li><li><a href="/fakebook/192317376/">Tedohazi Whelan</a></li><li><a href="/fakebook/192441938/">Gudeduve Plamip</a></li><li><a href="/fakebook/193263645/">Carey Rubinoff</a></li><li><a href="/fakebook/193535714/">Reinaldo Rapp</a></li><li><a href="/fakebook/194184118/">Buserapu Dostoevsky</a></li><li><a href="/fakebook/194190215/">Celestina Kinds</a></li><li><a href="/fakebook/194756826/">Ludmilla Vacat</a></li></ul><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>'''
FAKEBOOK_LOGIN_HTML = r'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>Fakebook</title>
</head>

<body>
    <div id="header">
        
	<a href="/">Home</a> | 

	
	<a href="/accounts/login/">Log in</a>
	
	<hr />
        
    </div>

    <div id="content">
        
<form method="post" action=".">
  <p><label for="id_username">Username:</label> <input id="id_username" type="text" name="username" maxlength="30" /></p>
<p><label for="id_password">Password:</label> <input id="id_password" type="password" name="password" maxlength="4096" /></p>
<div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='475065a754a4239b456db028883d9856' /></div>
  <input type="submit" value="Log in" />
  <input type="hidden" name="next" value="/fakebook/" />
</form>

<p>Forgot password? <a href="/accounts/password/reset/">Reset it</a>!</p>
<p>Not member? <a href="/accounts/register/">Register</a>!</p>

    </div>

    <div id="footer">
        
        <hr />
        
    </div>
</body>

</html>
'''
FRIEND_LANDING_HTML = '''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1><a href="/fakebook/996350946/">Pube Bregel</a></h1><h2>Basic Information</h2><ul><li>Sex: Female</li><li>Hometown: Woburn</li></ul><h2>Personal Information</h2><ul></ul><h2>Friends</h2><p><a href="/fakebook/996350946/friends/1/">View Pube Bregel's friends</a></p><h2>Wall</h2><p>
Pube Bregel has not received any Wall posts.
</p><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
FRIEND_VIEWING_FRIENDS_HTML = '''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1>Viewing <a href="/fakebook/996350946/">Pube Bregel</a>'s Friends</h1><ul><li><a href="/fakebook/8185551/">Zop Joxell</a></li><li><a href="/fakebook/70552327/">Jimavuzote Jotet</a></li><li><a href="/fakebook/79437786/">Junzo Trout</a></li><li><a href="/fakebook/89081356/">Rob Hegler</a></li><li><a href="/fakebook/152068235/">Nixegoco Sosed</a></li><li><a href="/fakebook/182325757/">Nivosi Xexep</a></li><li><a href="/fakebook/194756826/">Ludmilla Vacat</a></li><li><a href="/fakebook/216285855/">Malcom Burdi</a></li><li><a href="/fakebook/224009282/">Doranna Xivann</a></li><li><a href="/fakebook/299346627/">Giuseppe Waller</a></li><li><a href="/fakebook/306053677/">Nak Treloll</a></li><li><a href="/fakebook/316039351/">Mal Plevac</a></li><li><a href="/fakebook/320286626/">Hiliha Zbenenn</a></li><li><a href="/fakebook/320298083/">Hime Psehod</a></li><li><a href="/fakebook/322403147/">Jeaniene Brabil</a></li><li><a href="/fakebook/331516212/">Gavin Tupot</a></li><li><a href="/fakebook/414226914/">Tarah Mentkowski</a></li><li><a href="/fakebook/451340070/">Nenababonu Justiss</a></li><li><a href="/fakebook/464413390/">Dibume Bertin</a></li><li><a href="/fakebook/517450351/">Jeremias Plupet</a></li></ul><p>Page 1 of 2
<ul id="pagelist"><li>
1 

</li><li><a href="/fakebook/996350946/friends/2/">2</a></li><li><a href="/fakebook/996350946/friends/2/">next</a></li><li><a href="/fakebook/996350946/friends/2/">last</a></li></ul></p><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML = '''
<html><head><title>Fakebook</title><style TYPE="text/css"><!--
#pagelist li { display: inline; padding-right: 10px; }
--></style></head><body><h1>Fakebook</h1><p><a href="/fakebook/">Home</a></p><hr/><h1>Viewing <a href="/fakebook/996350946/">Pube Bregel</a>'s Friends</h1><ul><li><a href="/fakebook/517522361/">Patrina Losano</a></li><li><a href="/fakebook/535559461/">Vivetoxe Mukherjee</a></li><li><a href="/fakebook/569454833/">Duzo Frankel</a></li><li><a href="/fakebook/571162886/">Christian Luft</a></li><li><a href="/fakebook/571902974/">Bryon Bergo</a></li><li><a href="/fakebook/613597456/">Chinua Ard</a></li><li><a href="/fakebook/682737904/">Nak Treloll</a></li><li><a href="/fakebook/784265252/">Stefanie Vifoll</a></li><li><a href="/fakebook/841125873/">Zapopu Weis</a></li><li><a href="/fakebook/842182455/">Lojevojaja Brelap</a></li><li><a href="/fakebook/862994592/">Rae Creegan</a></li><li><a href="/fakebook/863084153/">Rurucotota Gebic</a></li><li><a href="/fakebook/885069463/">Dazudamo Litek</a></li><li><a href="/fakebook/911033743/">Jinoxu Pluhiss</a></li></ul><p>Page 2 of 2
<ul id="pagelist"><li><a href="/fakebook/996350946/friends/1/">first</a></li><li><a href="/fakebook/996350946/friends/1/">prev</a></li><li><a href="/fakebook/996350946/friends/1/">1</a></li><li>
2 

</li></ul></p><h6>Fakebook is run by <a href="http://www.ccs.neu.edu/home/choffnes/">David Choffnes</a> at                        
<a href="http://www.northeastern.edu">NEU</a>. It is meant for educational purposes only.                       
For questions, contact <a href="mailto:choffnes@ccs.neu.edu">David Choffnes</a></h6></body></html>
'''
FLAG_HTML = r'''<p>foobar</p>
<h2 class="secret flag" style="color:red">FLAG: FB494811FFA433A2C36BFFEB3242C955113D38E95FA3101FE41A9EA586A4BF74</h2'''
MEMBER_LANDING_YES_FLAG_HTML = MEMBER_LANDING_HTML + FLAG_HTML
FAKEBOOK_LOGIN_YES_FLAG_HTML = FAKEBOOK_LOGIN_HTML + FLAG_HTML
FAKEBOOK_LOGIN_YES_3_FLAG_HTML = FAKEBOOK_LOGIN_HTML + FLAG_HTML + FLAG_HTML + FLAG_HTML
FAKEBOOK_LOGIN_YES_4_FLAG_HTML = FAKEBOOK_LOGIN_YES_3_FLAG_HTML + FLAG_HTML
