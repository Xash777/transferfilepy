import socket as s
import sys
flag = b'EOF'

def close_everything():
    con.close()
    f.close()
    exit()

# Modulating the whole as a func so can be used later ?!?!?!
def send_file():
    # Creating a connection
    try:
        con = s.socket(s.AF_INET, s.SOCK_STREAM)
        print("Created connection successfully")
    except:
        print("Error creating connection")
        close_everything()

    # Defining ports 
    ip = str(sys.argv[2]); port = 7070

    # Opening the file and adding flag to it
    filename = str(sys.argv[3])
    try:
        f = open(filename, "rb+")
        f.seek(0, 2)
        filesize = int(f.tell())
        f.seek(0)
    except:
        print("Error opening the file (File does not exist or wrong name)")
        close_everything()

    # Connecting
    try:
        con.connect((ip, 7070))
        print("Connected successfully")
    except:
        print("Error connecting")
        close_everything()

    # Sending the file information
    con.send(filename.encode())
    resp = con.recv(64)
    if resp == b'filename recv':
        print("Filename sent Successfully")
    else:
        close_everything()

    # Send the chunks of data
    buffer = b'' # DEBUGGING PURPOSES???!!!
    try:
        while chunk := f.read(4096):
            con.sendall(chunk)
            buffer += chunk
        con.send(flag)
        print(size(buffer))
        con.shutdown(s.SHUT_WR)
        print("Data sent successsfully")
    except:
        print("Error sending the file, try again")
    finally:
        con.shutdown(s.SHUT_WR)
        f.close()
