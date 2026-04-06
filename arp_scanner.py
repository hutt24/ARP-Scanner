from scapy.all import ARP, Ether, srp

# 你的网段（根据 ipconfig 结果填写）
ip_range = "172.20.10.0/28"

arp = ARP(pdst=ip_range)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

# verbose=1 可以看到发送过程
result = srp(packet, timeout=2, verbose=1)[0]

print(f"发现 {len(result)} 个设备：")
for sent, received in result:
    print(received.psrc, received.hwsrc)
