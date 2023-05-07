from tornado.web import authenticated

from .auth import AuthHandler
from cryptography.fernet import Fernet


class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        key = b'fwgrUjVnHNo3mIt_fhCJT3vU1yzELbEEMlQrmJZqCLg='
        #f = Fernet(Key)

        self.set_status(200)
        self.response['email'] = self.current_user['email']
        self.response['password'] = f.encrypt(self.current_user['password']).decode() 
        self.response['fullName'] = f.encrypt(self.current_user['full_name']).decode() 
        self.response['address'] = f.encrypt(self.current_user['address']).decode()
        self.response['dateOfBirth'] = f.encrypt(self.current_user['date_of_birth']).decode()
        self.response['phoneNumber'] = f.encrypt(self.current_user['phone_number']).decode()
        self.response['disabilities'] = f.encrypt(self.current_user['disabilities']).decode()
        self.response['displayName'] = f.encrypt(self.current_user['display_name']).decode()
        self.write_json()