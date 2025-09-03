import socket as s
import os

# Global flags
file_buffer = b''
flag = b'EOF'
CHUNK_SIZE = 512

def recv_file():
    try:
        con = s.socket(s.AF_INET, s.SOCK_STREAM)
        print("Socket made successfully")
    except:
        print("Error making the connection")

    # Binding and listening
    try:
        con.bind(("0.0.0.0", 7070))
        con.listen(1)
        cln, addr = con.accept()
        print(f"Receiving a file from {str(addr)}")
    except:
        print("Failed deploying the connection on port")

    # Receiving file name and opening it
    resp = b'filename recv'
    filename = cln.recv(CHUNK_SIZE); filename = filename.decode()
    cln.send(resp)
    if not os.path.exists(f"./{filename}"):
        os.system(f"touch {filename}")
    f = open(f"./{filename}", "rb+")

    # Receiving the data
    try:
        while chunk := cln.recv(CHUNK_SIZE):
            if flag in chunk:
                f.write(chunk[:-3])
                break
            else:
                f.write(chunk)

        f.seek(0, 2)
        
        print("Data received successfully")
    except:
        print("Error getting the data")
    finally:
        con.shutdown(s.SHUT_WR)
        cln.close()
        f.close()
