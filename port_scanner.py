import socket
import json
import csv
import argparse
from datetime import datetime


def scan_port(target, port, timeout=1):
    """
    Scan a single TCP port.
    Returns: open, closed, or filtered/timeout
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            status = "open"
        else:
            status = "closed"

    except socket.timeout:
        status = "filtered"

    except OSError:
        status = "filtered"

    finally:
        sock.close()

    return status


def scan_ports(target, start_port, end_port, timeout):
    results = []

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {target}")
        return []

    print(f"\nTarget: {target}")
    print(f"Resolved IP: {target_ip}")
    print(f"Port Range: {start_port}-{end_port}")
    print("-" * 45)

    for port in range(start_port, end_port + 1):

        status = scan_port(target_ip, port, timeout)

        result = {
            "port": port,
            "protocol": "TCP",
            "status": status
        }

        results.append(result)

        print(f"Port {port:<5} -> {status}")

    return results


def save_json(filename, target, start_port, end_port, results):
    data = {
        "scan_timestamp": datetime.now().isoformat(),
        "target": target,
        "start_port": start_port,
        "end_port": end_port,
        "protocol": "TCP",
        "results": results
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\n[+] JSON results saved to {filename}")


def save_csv(filename, target, results):
    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "target",
            "port",
            "protocol",
            "status"
        ])

        timestamp = datetime.now().isoformat()

        for result in results:
            writer.writerow([
                timestamp,
                target,
                result["port"],
                result["protocol"],
                result["status"]
            ])

    print(f"[+] CSV results saved to {filename}")


def main():

    parser = argparse.ArgumentParser(
        description="TCP Port Scanner - For authorized/local targets only"
    )

    parser.add_argument(
        "--target",
        default="127.0.0.1",
        help="Target hostname/IP. Default: 127.0.0.1"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting port"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=100,
        help="Ending port"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Connection timeout in seconds"
    )

    parser.add_argument(
        "--json",
        default="scan_results.json",
        help="JSON output filename"
    )

    parser.add_argument(
        "--csv",
        default="scan_results.csv",
        help="CSV output filename"
    )

    args = parser.parse_args()

    # Basic validation
    if not (1 <= args.start <= 65535):
        parser.error("Start port must be between 1 and 65535.")

    if not (1 <= args.end <= 65535):
        parser.error("End port must be between 1 and 65535.")

    if args.start > args.end:
        parser.error("Start port cannot be greater than end port.")

    if args.timeout <= 0:
        parser.error("Timeout must be greater than 0.")

    print("=" * 55)
    print("        TCP PORT SCANNER")
    print("        Authorized Targets Only")
    print("=" * 55)

    results = scan_ports(
        args.target,
        args.start,
        args.end,
        args.timeout
    )

    if results:
        save_json(
            args.json,
            args.target,
            args.start,
            args.end,
            results
        )

        save_csv(
            args.csv,
            args.target,
            results
        )

    print("\n[+] Scan completed.")


if __name__ == "__main__":
    main()