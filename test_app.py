from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert 'Hello from Flask with CI/CD!' in response.get_data(as_text=True)

def test_about():
    tester = app.test_client()
    response = tester.get('/about')
    assert response.status_code == 200
    assert 'Этот сайт сделан с использованием Flask и CI/CD' in response.get_data(as_text=True)

def test_contact_get():
    tester = app.test_client()
    response = tester.get('/contact')
    assert response.status_code == 200
    # Заменим на то, что точно есть в шаблоне
    assert 'Контакты' in response.get_data(as_text=True)

def test_contact_post():
    tester = app.test_client()
    response = tester.post('/contact', data=dict(
        name="Test",
        email="test@example.com",
        message="Привет от теста!"
    ), follow_redirects=True)

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Мы получили' in html
    assert 'Привет от теста!' in html
