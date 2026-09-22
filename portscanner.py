import socket
import sys
import time
from datetime import datetime
from tqdm import tqdm


# colour codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

# reference table for common ports
common_ports = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    587: "SMTP",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    3306: "MySQL",
    3389: "RDP (Remote Desktop Protocol)",
    5432: "PostgreSQL",
    8080: "HTTP Alternate"
}

# decorative banner displayed at execution of tool
def print_banner():
    banner = f"""
{BOLD}{CYAN}================================{RESET}
{BOLD}{CYAN}       Port Scanner Tool        {RESET}
{BOLD}{CYAN}================================{RESET}
    """
    print(banner)

def resolve_target(target):
    try:
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror:
        print(f"{RED}Error: Unable to resolve target '{target}'. Please check the hostname or IP address.{RESET}")
        sys.exit(1)

def scan_port(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        return result == 0

def run_scan(ip, start_port, end_port):
    open_ports = []
    total_ports = end_port - start_port + 1

    print(f"{YELLOW}Scanning {total_ports} ports on {ip}...{RESET}")
    
    for port in tqdm(range(start_port, end_port + 1), desc="Scanning Ports", unit="port"):
        if scan_port(ip, port):
            open_ports.append(port)
    
    return open_ports

def print_results(ip, open_ports, time_elapsed, total_scanned):
    print(f"\n{BOLD}{CYAN}Scan Results for {ip}:{RESET}")

    if open_ports:
        print(f"{GREEN}Open Ports:{RESET}")
        for port in open_ports:
            service = common_ports.get(port, "Unknown Service")
            print(f"  Port {port}: {service}")
    else:
        print(f"{RED}No open ports found.{RESET}")

    print(f"\n{BOLD}{CYAN}Scan Summary:{RESET}")
    print(f"  Total Ports Scanned: {total_scanned}")
    print(f"  Open Ports Found: {len(open_ports)}")
    print(f"  Time Elapsed: {time_elapsed:.2f} seconds")

def main():
    print_banner()

    target = input("Please enter target IP address or Hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print(f"{RED}Error: Invalid port range. Please specify ports between 1 and 65535.{RESET}")
        sys.exit(1)

    ip = resolve_target(target)
    print(f"{CYAN}Resolved Target: {target} -> {ip}{RESET}")

    start_time = time.time()
    open_ports = run_scan(ip, start_port, end_port)
    end_time = time.time()

    time_elapsed = end_time - start_time
    total_scanned = end_port - start_port + 1

    print_results(ip, open_ports, time_elapsed, total_scanned)

if __name__ == "__main__":
    main()
