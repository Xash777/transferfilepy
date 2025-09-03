from utils import client as ct
from utils import server as sv
import sys
import os

if sys.argv[1] == 'send':
    ct.send_file()
elif sys.argv[1] == 'receive' or sys.argv[1] == 'recv':
    sv.recv_file()
