import scapy.all as scapy
import optparse
def options():
    opt = optparse.OptionParser()
    opt.add_option("-i","--ip",dest="ipadress",help="enter the ip adress")
    (value,key)=opt.parse_args()
    return value
def Scan(ipadress):
    arppacket = scapy.ARP(pdst=ipadress)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    mix = broadcast/arppacket
    (answered,unanswered) = scapy.srp(mix,timeout=1)
    print(answered.summary())
deg = options()
Scan(deg.ipadress)