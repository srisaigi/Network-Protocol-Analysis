# Wireshark Display Filters

## Address and protocol

```text
ip
ipv6
eth
arp
icmp || icmpv6
udp
tcp
```

## Capture flows

```text
ip.addr == 192.168.1.20
ip.src == 192.168.1.20
ip.dst == 10.0.0.12
tcp.port == 443
udp.port == 53
```

## DHCP and DNS

```text
dhcp or bootp
bootp.option.dhcp == 1
dns
dns.flags.response == 0
dns.flags.response == 1
```

## TCP handshake and failures

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.flags.syn == 1 && tcp.flags.ack == 1
tcp.flags.reset == 1
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.lost_segment
tcp.analysis.zero_window
tcp.analysis.window_full
```

## HTTP/TLS

```text
http
http.request
http.response
tls.handshake
```

## Linux commands

```bash
ip address
ip route
ip neighbour
ss -tunap
ping -c 4 example.com
nslookup example.com
sudo tcpdump -ni eth0
```
