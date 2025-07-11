from scapy.all import ARP ,Ether, srp

# Cambia se la tua rete non è 192.168.1.0/24
rete = "192.168.1.0/24"
arp= ARP(pdst=rete)
eth= Ether(dst="ff:ff:ff:ff:ff:ff")
pacchetti = srp(eth/arp, timeout=2, verbose=0)[0]

print("IP\t\tMAC")
for _, r in pacchetti:
    print(r.psrc + "\t" + r.hwsrc)
