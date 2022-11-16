from django import urls
from django.contrib.auth import get_user_model
import pytest

@pytest.mark.parametrize('param', [('home'), ('signup'), ('login')])
def test_render_views(client,param):
    temp_url=urls.reverse(param)
    resp=client.get(temp_url)
    assert resp.status_code==200

@pytest.mark.django_db
def test_user_signup(client,signup_user_data):
    user_model=get_user_model()
    assert user_model.objects.count()==0
    signup_url=urls.reverse('signup')
    resp=client.post(signup_url,signup_user_data)
    assert user_model.objects.count()==1
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client,create_test_user,user_data):
    user_model=get_user_model()
    assert user_model.objects.count()==1
    login_url=urls.reverse('login')
    resp=client.post(login_url,user_data)
    assert resp.status_code == 302
    assert resp.url ==urls.reverse('pro')

