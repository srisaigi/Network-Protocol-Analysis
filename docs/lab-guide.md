# Network Protocol Analysis Lab Guide

## 1. Setup

### Linux

```bash
sudo apt update
sudo apt install -y wireshark tshark dnsutils
```

Choose the primary interface and verify it:

```bash
ip address
ip route
ip neighbour
```

### Windows

Install Wireshark from the official installer. Open a Command Prompt or PowerShell terminal and confirm connectivity:

```powershell
ipconfig /all
route print
arp -a
```

## 2. Capture workflow

1. Start a capture on the active interface.
2. Open a terminal and release/renew DHCP only in an isolated lab if appropriate.
3. Resolve a public or internal name with `nslookup` or `dig`.
4. Test local and remote reachability with `ping`.
5. Visit a website or connect to a known service.
6. Stop capture after 1–2 minutes.
7. Save the capture as `.pcapng` inside `capture/`.

## 3. Analysis sequence

### DHCP

Filter `dhcp or bootp` and identify Discover, Offer, Request and Acknowledge messages.

Evidence to record:

- Client MAC address
- Offered IP address
- DHCP server address
- Lease duration

### ARP

Filter `arp`. Confirm Who Has and Is At exchanges.

Evidence to record:

- Queried IPv4 address
- Responder MAC address
- Whether the entry is present in `ip neighbour` or `arp -a`

### DNS

Filter `dns`. Compare DNS requests with responses.

Evidence to record:

- Query name
- Query type
- Response address
- Response time

### ICMP

Filter `icmp`. Separate successful replies from destination unreachable or time-exceeded messages.

### TCP

Filter `tcp.flags.syn == 1` to examine the handshake. Look for SYN, SYN/ACK and ACK.

Then filter:

- `tcp.analysis.retransmission`
- `tcp.analysis.lost_segment`
- `tcp.analysis.fast_retransmission`
- `tcp.reset`

### UDP

Filter `udp` and identify the source/destination ports and application protocol.

## 4. Common troubleshooting decisions

| Symptom | First checks |
|---|---|
| No IP address | DHCP packets; cable/Wi-Fi state; DHCP scope |
| IP works, domain names fail | DNS response; resolver configuration; UDP/TCP port 53 |
| Gateway cannot be reached | ARP entries; default route; subnet mask |
| Ping fails | ICMP policy; routing; firewall rules |
| TCP connects slowly | SYN retransmissions; RTT; firewall filtering |
| TCP stream resets | Application exit; security policy; timeout |

## 5. Recommended report structure

1. Scope and capture details
2. Network topology
3. Packet evidence
4. Observations by protocol
5. Issue reproduction
6. Root-cause conclusion
7. Recommended fix
8. Screenshots and filters used
