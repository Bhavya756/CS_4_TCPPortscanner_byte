# TCP Port Scanner

A Python-based TCP Port Scanner developed as part of the **Arithmatrix Cyber Security Internship**.

The tool scans a specified range of TCP ports on an authorized target and determines whether each port is **open** or **closed**. The scan results are automatically saved in both **CSV** and **JSON** formats.

## Features

* Scans a configurable range of TCP ports
* Accepts a target hostname or IP address
* Resolves the target hostname to an IP address
* Checks TCP port availability using Python sockets
* Displays scan results in the terminal
* Saves results in CSV format
* Saves results in JSON format
* Designed for authorized and educational security testing

## Technologies Used

* Python 3
* Python Socket Library
* CSV
* JSON

## Requirements

* Python 3.x
* No external libraries are required

## Project Structure

```text
CS_4_TCPPortscanner_byte/
│
├── port_scanner.py
├── scan_results.csv
├── scan_results.json
└── README.md
```

## How to Run

Open Command Prompt or Terminal in the project directory.

Run the following command:

```bash
python port_scanner.py
```

The program will display the target, resolved IP address, port range, and the status of each scanned port.

## Sample Execution

The scanner was tested using the local host `127.0.0.1` with ports `1-100`.

```text
=======================================================
        TCP PORT SCANNER
        Authorized Targets Only
=======================================================

Target: 127.0.0.1
Resolved IP: 127.0.0.1
Port Range: 1-100
---------------------------------------------
Port 1     -> closed
Port 2     -> closed
Port 3     -> closed
...
Port 80    -> closed
...
Port 100   -> closed

[+] JSON results saved to scan_results.json
[+] CSV results saved to scan_results.csv

[+] Scan completed.
```

## Output Files

### scan_results.csv

Stores the scanned port numbers and their corresponding status in CSV format.

Example:

```text
port,status
1,closed
2,closed
3,closed
```

### scan_results.json

Stores the scan results in structured JSON format.

Example:

```json
[
    {
        "port": 1,
        "status": "closed"
    },
    {
        "port": 2,
        "status": "closed"
    }
]
```

## Demonstration Target

For demonstration and testing, the scanner was executed against:

```text
127.0.0.1
```

`127.0.0.1` is the loopback address of the local computer and is used here for safe, authorized testing.

## Ethical and Legal Notice

This project is intended for **educational purposes and authorized security testing only**.

Do not scan systems, servers, networks, or devices without explicit permission from the owner or authorized administrator.

Unauthorized port scanning may violate organizational policies and applicable laws. The developer is not responsible for any misuse of this tool.

## Learning Objectives

This project demonstrates basic concepts of:

* TCP networking
* Port scanning
* Python socket programming
* IP address and hostname resolution
* Network security fundamentals
* CSV and JSON data handling

## Internship Information

**Internship:** Arithmatrix Cyber Security Internship
**Task:** Task 4 — TCP Port Scanner
**Language:** Python
**Testing Environment:** Localhost (`127.0.0.1`)
