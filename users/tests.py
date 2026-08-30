from django.contrib.auth.models import User
from django.test import TestCase

class RegisterTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post('/users/register', data={
            'username':'dave', 
            'first_name':'Dave', 
            'last_name': 'Zoirov', 
            'email': 'davlatbekzoirov08@gmail.com',
            'password': 'dave'
        })

        user = User.objects.get(username='dave')
        self.assertEqual(user.first_name, 'Dave')
        self.assertEqual(user.last_name, 'Zoirov')
        self.assertEqual(user.email, 'davlatbekzoirov08@gmail.com')
        self.assertNotEqual(user.password, 'dave')
        self.assertTrue(user.check_password('dave'))