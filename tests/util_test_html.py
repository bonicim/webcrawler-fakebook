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
FLAG_HTML = r'''<p>foobar</p>
<h2 class="secret flag" style="color:red">FLAG: FB494811FFA433A2C36BFFEB3242C955113D38E95FA3101FE41A9EA586A4BF74</h2'''
MEMBER_LANDING_YES_FLAG_HTML = MEMBER_LANDING_HTML + FLAG_HTML
FAKEBOOK_LOGIN_YES_FLAG_HTML = FAKEBOOK_LOGIN_HTML + FLAG_HTML
FAKEBOOK_LOGIN_YES_3_FLAG_HTML = FAKEBOOK_LOGIN_HTML + FLAG_HTML + FLAG_HTML + FLAG_HTML
