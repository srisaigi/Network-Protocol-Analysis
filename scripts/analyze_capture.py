#!/usr/bin/env python3
"""Summarize a .pcap/.pcapng capture using Wireshark's tshark command."""

import csv
import shutil
import subprocess
import sys
from pathlib import Path


def tshark_fields(capture: Path, fields: list[tuple[str, str]]) -> list[list[str]]:
    tshark = shutil.which("tshark")
    if not tshark:
        raise RuntimeError("tshark was not found. Install Wireshark and ensure tshark is on PATH.")

    command = [tshark, "-n", "-r", str(capture), "-T", "fields"]
    for field_name, _ in fields:
        command.extend(["-e", field_name])

    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return [line.split("\t") for line in result.stdout.splitlines() if line.strip()]


def protocol_summary(capture: Path) -> None:
    rows = tshark_fields(capture, [("_ws.col.Protocol", "protocol")])
    counts: dict[str, int] = {}
    for row in rows:
        name = row[0].strip() if row else "Unknown"
        counts[name] = counts.get(name, 0) + 1

    print("\nProtocol summary")
    print("----------------")
    for name, count in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:15]:
        print(f"{name:<24} {count}")


def dns_summary(capture: Path) -> None:
    rows = tshark_fields(capture, [("dns.qry.name", "dns_name"), ("dns.a", "dns_address")])
    print("\nDNS observations")
    print("----------------")
    if not rows:
        print("No DNS packets found.")
        return
    for row in rows[:20]:
        name = row[0] if len(row) > 0 else "-"
        address = row[1] if len(row) > 1 else "-"
        print(f"Query: {name:<35} Response: {address}")


def retransmission_summary(capture: Path) -> None:
    rows = tshark_fields(capture, [("tcp.analysis.retransmission", "retransmission")])
    print("\nTCP retransmissions")
    print("-------------------")
    print(len([row for row in rows if row and row[0] == "1"]))


def endpoint_summary(capture: Path) -> None:
    rows = tshark_fields(capture, [("ip.src", "source"), ("ip.dst", "destination")])
    endpoints: dict[str, int] = {}
    for row in rows:
        for endpoint in row:
            if endpoint:
                endpoints[endpoint] = endpoints.get(endpoint, 0) + 1

    print("\nTop endpoints")
    print("-------------")
    for endpoint, count in sorted(endpoints.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{endpoint:<24} {count}")


def write_csv_report(capture: Path, output: Path) -> None:
    rows = tshark_fields(capture, [
        ("frame.time", "time"), ("ip.src", "source"), ("ip.dst", "destination"),
        ("_ws.col.Protocol", "protocol"), ("tcp.analysis.retransmission", "retransmission")
    ])
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Timestamp", "Source", "Destination", "Protocol", "Retransmission"])
        for row in rows:
            padded = (row + [""] * 5)[:5]
            writer.writerow(padded)
    print(f"\nCSV report written to {output}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/analyze_capture.py capture/file.pcapng")
        return 2

    capture = Path(sys.argv[1]).resolve()
    if not capture.is_file():
        print(f"Capture not found: {capture}")
        return 2

    try:
        print(f"Analyzing: {capture}")
        protocol_summary(capture)
        dns_summary(capture)
        retransmission_summary(capture)
        endpoint_summary(capture)
        write_csv_report(capture, capture.with_suffix("-summary.csv"))
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
