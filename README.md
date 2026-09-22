# Python Port Scanner

A simple Python-based TCP port scanner designed to scan a specified range of ports on an IPv4 address or hostname.

## Features

* Accepts an IPv4 address or hostname as the target
* Allows the user to specify a starting and ending port
* Scans ports using TCP sockets
* Displays a progress bar using `tqdm`
* Identifies common services associated with open ports
* Displays the total number of ports scanned
* Displays the number of open ports found
* Measures the total scan time
* Uses coloured terminal output for readability

## Usage

Run the program with:

```bash
python portscanner.py
```

The program will prompt the user to input the following:

1. Target IPv4 address or hostname
2. Starting port
3. Ending port

Example:

```text
Please enter target IP address or Hostname: 192.168.1.1
Enter start port: 1
Enter end port: 1000
```

## Example Output

```text
================================
       Port Scanner Tool
================================

Please enter target IP address or Hostname: 192.168.1.1
Enter start port: 1
Enter end port: 1000

Resolved Target: 192.168.1.1 -> 192.168.1.1
Scanning 1000 ports on 192.168.1.1...

Open Ports:
  Port 22: SSH
  Port 80: HTTP
  Port 443: HTTPS

Scan Summary:
  Total Ports Scanned: 1000
  Open Ports Found: 3
  Time Elapsed: 12.45 seconds
```

## Purpose

This was a personal project that I created after seeing similar projects made by others online and figured I'd give it a shot. This project was overall created to develop my experience with Python networking, TCP connections, and basic network reconnaissance through a hands on activity.

## Disclaimer

Please only scan systems and networks that you own or have explicit permission to test. Unauthorised port scanning may violate organisational policies or applicable laws.

