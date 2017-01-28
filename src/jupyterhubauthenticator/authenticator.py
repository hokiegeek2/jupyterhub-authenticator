from jupyterhub.auth import Authenticator
from tornado import gen
import os
from pyanaconda.regexes import USERNAME_VALID

class BasicAuthenticator(Authenticator):
    
    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']
        return username

class KeyValueFileAuthenticator(Authenticator):
    def _getLoginDictionary(self):
        logins = {}
        with open(os.environ("LOGIN_FILE")) as f:
            for line in f:
                (key,val) = line.split(":")
                logins[key] = val.rstrip('\n')
        return logins
    
    def _getPassword(self,username):
        logins = self._getLoginDictionary()
        return logins.get(username)
    
    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']
        system_password = self._getPassword(username)
        
        if (password == system_password):
            return username
        else:
            return None
