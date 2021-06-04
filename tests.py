from app import app
with app.test_client() as c:
    response = c.get('/')
    assert response.status_code == 200
    response = c.get('/about')
    assert response.status_code == 200
    response = c.get('/contact')
    assert response.status_code == 200
    response = c.get('/search')
    assert response.status_code == 200
    response = c.get('/login')
    assert response.status_code == 200
    response = c.get('/register')
    assert response.status_code == 200
    
