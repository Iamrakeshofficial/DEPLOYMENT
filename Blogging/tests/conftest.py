import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def user_data():
    return {'first_name':'username','username':'Rakesh','email':'s@gmail.com','password':'user_pass@123'}

@pytest.fixture
def signup_user_data():
    return {'first_name':'username','username':'Rakesh','email':'s@gmail.com','password1':'user_pass@123','password2':'user_pass@123'}

@pytest.fixture
def create_test_user(user_data):
    user_model= get_user_model()
    test_user=user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user