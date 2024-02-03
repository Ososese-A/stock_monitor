import socket

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False
    
print(test_connection())