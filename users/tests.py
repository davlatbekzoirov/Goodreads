from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class RegisterTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse('users:register'), data={
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

    def test_required_fields(self):
        response = self.client.post(reverse('users:register'), data={
            'first_name':'Dave', 
            'email': 'davlatbekzoirov08@gmail.com',
        })

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        form = response.context['form']
        self.assertFormError(form, 'username', 'This field is required.')
        self.assertFormError(form, 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(reverse('users:register'), data={
            'username':'dave', 
            'first_name':'Dave', 
            'last_name': 'Zoirov', 
            'email': 'davlatbekzoirov08',
            'password': 'dave'
        })

        user_count = User.objects.count()
        
        self.assertEqual(user_count, 0)
        form = response.context['form']
        self.assertFormError(form, 'email', 'Enter a valid email address.')