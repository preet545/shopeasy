import requests

base_url = 'http://localhost:5000'

def test_register():
    url = f'{base_url}/register'
    payload = {
        'email': 'test@example.com',
        'password': 'test123'
    }
    response = requests.post(url, json=payload)
    print('Register:', response.json())

def test_login():
    url = f'{base_url}/login'
    payload = {
        'email': 'test@example.com',
        'password': 'test123'
    }
    response = requests.post(url, json=payload)
    print('Login:', response.json())

def test_reset_password():
    url = f'{base_url}/reset_password'
    payload = {
        'email': 'test@example.com'
    }
    response = requests.post(url, json=payload)
    print('Reset Password:', response.json())

if __name__ == '__main__':
    test_register()
    test_login()
    test_reset_password()
