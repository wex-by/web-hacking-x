from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from colorama import init, Fore
import os
import requests
import ftplib
from datetime import datetime
import time
class col:
			red = '\033[91m'
			gr = '\033[92m'
			bl = '\033[94m'
time.sleep(2)
print(f"""{col.gr}
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOookXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkccddkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkodkOOk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKKOxdxOOOOOkk0000KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkdddodxxkkO0OOO0OOOkxxxkOk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOoldxxkOO000OO000000000kxkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kddkOO00OO00000000OdlxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0ddkOOOOO000000kddx0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
OOKX0OKX0OKWMMMMMMMMMMMMWKOOXWMMMMNxoxkOOO000000OocdXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
:;oOo;dkc;oXMMMMMMMMMMMMNd;:kNMMMMKolxkOOkkkO000OxokXWWWMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMM
:,oOl;dk:;oXMMMMMWWWMMMMNd;:kNWWWNx:lddoodxxdxkOOOkxdooOWMMNkoxXMMMMMMMMMMMMMMMMMMMMMMMMXxlxXMMMMMMM
:,oOo;dk:;oXMMWKxdddddONNd;:dkdddkl,;:coOXNX0Okoclol:;;xNMMXo,lKMMMMMMMMMMMMMMMMMMMMMMMMKl,lKMMMMMMM
:;oOo;dk:,oXMWXx:colc;oKXd;;cooc;:lodxOXNNNNNNXOxdxxo;;xNMMXo,lKMMNOxxxk0NMMMMN0kxxxk0WMKl,cKWKkxk0N
c;okl;dx:;dXWKo;ckKKkc;oOd;,;dXKo;cOWMMMMMMMMMMMMMMWk:,lkOOxc,lKMMXxllc:cONMMNOc:clc:lONKl,c0Ko::lkN
kclo:;clcoKWKo;,;:cc:;,lOd;;dXWW0l;l0WMMMMMMMMMMMMMWk:,;cccc;,oKMMWXXXOl,c0WW0l:dKNKdcxXKl,cOx;:kNWM
0c;:odc;;dNWNk:,;oxxxxk0Kd;:kNWXx::xXMMMMMMMMMMMMMMWk:,oKXX0l,oKWNklllc;,c0W0o;oXWMWNXNWKl,;c::xXMMM
Kl,:k0o;;xNMMXkc:okkkkKWNd:cdxkxookXMMMMMMMMMMMMMMMWk:;xNMMXo,lKXk::dkd:,c0WXx:ckNWNOdkXKl,:dl;o0WMM
NkldKWOloKWMMMW0lcccclkNNkokdcclONWMMMMMMMMMMMMMMMMWk:;xNMMXo,lKXkc:oxdl::dXWNx::dxd::kNKl,l00l:lxkX
WNXXWMNXXWMMMMMNXKKKKKNWWNXNXKKXNMMMMMMMMMMMMMMMMMMWk:;xNMMXo,lKWNd;,,;oo;:OWWKo;,,,,oXWKl,lKNk:,,:k
        {col.bl}                     github : https://github.com/wex-by
                                         conex team
        {col.gr}

        1/ code HTML                2/ file server Directory
                    3/ port scanner
""")
num = float(input("$/ number test hacking ? "))
print("")
if num >= 1:
    if num == 1:
        os.system("clear")
        moz = input(f"{col.gr}$/address site ? ")
        r = requests.get(f"{moz}")
        print(r.text)
    else:
        os.system("clear")
        FTP_HOST = "ftp.ed.ac.uk"
        FTP_USER = "anonymous"
        FTP_PASS = ("")
# some utility functions that we gonna need
def get_size_format(n, suffix="B"):
    # converts bytes to scaled format (e.g KB, MB, etc.)
    for unit in ["", "K", "M", "G", "T", "P"]:
        if n < 1024:
            return f"{n:.2f}{unit}{suffix}"
        n /= 1024
def get_datetime_format(date_time):
    # convert to datetime object
    date_time = datetime.strptime(date_time, "%Y%m%d%H%M%S")
    # convert to human readable date time string
    return date_time.strftime("%Y/%m/%d %H:%M:%S")
# initialize FTP session
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"
# print the welcome message
print(ftp.getwelcome())
# change the current working directory to 'pub' folder and 'maps' subfolder
ftp.cwd("pub/maps")
# LIST a directory
print("*"*50, "LIST", "*"*50)
ftp.dir()
# NLST command
print("*"*50, "NLST", "*"*50)
print("{:20} {}".format("File Name", "File Size"))
for file_name in ftp.nlst():
    file_size = "N/A"
    try:
        ftp.cwd(file_name)
    except Exception as e:
        ftp.voidcmd("TYPE I")
        file_size = get_size_format(ftp.size(file_name))
    print(f"{file_name:20} {file_size}")
print("*"*50, "MLSD", "*"*50)
# using the MLSD command
print("{:30} {:19} {:6} {:5} {:4} {:4} {:4} {}".format("File Name", "Last Modified", "Size",
                                                    "Perm","Type", "GRP", "MODE", "OWNER"))
for file_data in ftp.mlsd():
    # extract returning data
    file_name, meta = file_data
    # i.e directory, file or link, etc
    file_type = meta.get("type")
    if file_type == "file":
        # if it is a file, change type of transfer data to IMAGE/binary
        ftp.voidcmd("TYPE I")
        # get the file size in bytes
        file_size = ftp.size(file_name)
        # convert it to human readable format (i.e in 'KB', 'MB', etc)
        file_size = get_size_format(file_size)
    else:
        # not a file, may be a directory or other types
        file_size = "N/A"
    # date of last modification of the file
    last_modified = get_datetime_format(meta.get("modify"))
    # file permissions
    permission = meta.get("perm")
    # get the file unique id
    unique_id = meta.get("unique")
    # user group
    unix_group = meta.get("unix.group")
    # file mode, unix permissions
    unix_mode = meta.get("unix.mode")
    # owner of the file
    unix_owner = meta.get("unix.owner")
    # print all
    print(f"{file_name:30} {last_modified:19} {file_size:7} {permission:5} {file_type:4} {unix_group:4} {unix_mode:4} {unix_owner}")
    ftp.quit()
else:
	# some colors
	init()
	GREEN = Fore.GREEN
	RESET = Fore.RESET
	GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, port):
    """
    determine whether `host` has the `port` open
    """
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        # return false
        return False
    else:
        # the connection was established, port is open!
        return True

# get the host from the user
host = input(f"{col.gr}$/ Enter the host ? ")
# iterate over ports, from 1 to 1024
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
