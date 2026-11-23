# PacketTrace — Network Protocol Analysis Lab

A practical Wireshark and Linux networking project for learning packet-level troubleshooting across TCP/IP, DNS, DHCP, ARP, ICMP, TCP and UDP.

## Project contents

- `index.html` — interactive protocol analysis dashboard
- `assets/styles.css` — responsive dashboard styling
- `assets/app.js` — navigation, theme and filter interactions
- `docs/lab-guide.md` — capture and troubleshooting procedure
- `docs/wireshark-filters.md` — focused Wireshark display filters
- `scripts/analyze_capture.py` — summarizes a capture with `tshark`
- `capture/packet-summary-template.csv` — reporting template

## Run the dashboard

Open `index.html` directly in a browser, or serve the folder:

```powers
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Run packet analysis

Install Wireshark/tshark and place a capture under `capture/`.

```powers
python scripts/analyze_capture.py capture/live-traffic.pcapng
```

The script generates protocol, endpoint, DNS, retransmission and TCP summary fields in the terminal.

## Lab objective

Capture and analyze traffic to demonstrate:

1. DHCP address assignment
2. ARP address resolution
3. DNS name resolution
4. ICMP reachability
5. TCP three-way handshake
6. UDP and application traffic
7. Retransmissions and connection failures

## Resume-ready summary

> Captured and analyzed network traffic using Wireshark to investigate TCP/IP communication and troubleshoot connectivity issues across DNS, DHCP, ARP, ICMP, TCP and UDP. Examined address assignment, name resolution, MAC discovery, connection establishment, retransmissions and communication patterns using Wireshark filters and Linux networking commands.
