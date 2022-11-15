import random
import threading
from time import sleep

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1, send

def sendTcp(imei,ip,port,host):
    seq = random.randint(10000, 20000)
    sport = random.randint(12000, 30000)
    pkg_1 = IP(dst=ip) / TCP(sport=sport, dport=port, flags='S', seq=seq)
    reply = sr1(pkg_1, timeout=5, verbose=False)
    seq = reply[TCP].ack
    ack = reply[TCP].seq + 1
    pkg_2 = IP(dst=ip) / TCP(sport=sport, dport=port, flags='A', seq=seq, ack=ack)
    sr1(pkg_2, timeout=3, verbose=False)
    v = host.encode().hex()
    a = bytes.fromhex("15002f0f"+v+"63dd02")
    print("15002f0f"+v+"63dd02")
    reply = send(IP(dst=ip) / TCP(sport=sport, dport=port, flags='PA', seq=seq, ack=ack) / a,verbose=False)
    v = imei.encode().hex()
    a = bytes.fromhex("{:02X}".format(len(imei)+2).lower()+"00"+"{:02X}".format(len(imei)).lower()+v)
    print("{:02X}".format(len(imei)+2).lower()+"00"+"{:02X}".format(len(imei)).lower()+v)
    reply = sr1(IP(dst=ip) / TCP(sport=sport, dport=port, flags='PA', seq=seq + 22, ack=ack) / a,verbose=False)
    print('Send TCP To Server Successful')
def random_(number):
    CHAT_ = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    c = ''
    for i in range(0,number):
        c += CHAT_[random.randint(0,len(CHAT_)-1)]
    return c
if __name__ == '__main__':
    for i in range(0,7):
        USERNAME = "think_"+random_(5)
        threading.Thread(target=sendTcp,args=(USERNAME,'192.168.114.128',25565,'192.168.114.128')).start()
        sleep(0.7)
    # sendTcp('thinkJSP','192.168.114.128',25565,'192.168.114.128')