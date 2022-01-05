from app import app as p
import time

START = time.time()

def client():
    app = p.test_client
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield clien

def test_login(p):
    p = p.test_client()

    print("Testing Login GET response...")
    
    res = p.get(f"/auth")

    assert res.status_code == 405

    print("Success")

    print("Testing Login POST response...")

    res = p.post(f"/auth", json={
        'username':"Haramillo",
        'password':"password"
        })
    
    assert res.status_code == 201

    print("Success")

    p.get('/logout')

def test_logout(p):
    p = p.test_client()
    
    print("Testing Logout without Login...")

    res = p.get("/logout")

    assert res.status_code == 400

    print("Success")

    print("Testing Logout with Login...")

    p.post(f"/auth", json={
        'username':"Haramillo",
        'password':"password"
        })

    res = p.get("/logout")

    print("Success")

    assert res.status_code == 200

def test_list_images(p):
    p = p.test_client()

    print("Testing List of all images without Login...")

    res = p.get("/images")

    assert res.status_code == 403

    print("Success")

    print("Testing List of all images with Login...")

    p.post(f"/auth", json={
        'username':"Haramillo",
        'password':"password"
        })

    res = p.get("/images")

    assert res.status_code == 200

    print("Success")

    print("Testing number of images recieved...")

    assert len(res.json) > 0

    print("Success")


test_login(p)
test_logout(p)
test_list_images(p)

END = time.time()


print(f"Test run time: {END-START:.2f} s")