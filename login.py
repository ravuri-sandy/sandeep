# sandeep script for login
def is_valid(username,password):
   
    return username == 'username' and password == 'password'

if is_valid(_username,_password):
    Session().username = _username
    print "Hello %s <br>" %_username
    
else:
    print "Sorry, you are not allowed to access this page"
