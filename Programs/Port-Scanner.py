import socket
import concurrent.futures
from functools import partial
import sys

port_protocol_map = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
    80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
    443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
    1521: "Oracle DB", 3389: "RDP", 25565: "Minecraft", 27017: "MongoDB", 5000: "Flask",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 9000: "Webmin", 9200: "Elasticsearch", 11211: "Memcached",
    445: "SMB", 139: "NetBIOS", 135: "MSRPC"
}

def identify_service(sock, ip, port):
    try:
        sock.settimeout(0.5)
        try:
            banner = sock.recv(1024)
            if banner:
                banner_txt = banner.decode('utf-8', errors='ignore').strip()
                return banner_txt
        except socket.timeout:
            pass
        except Exception:
            pass
        if port in (80, 8080, 8000, 8888):
            try:
                sock.sendall(b"HEAD / HTTP/1.0\r\nHost: %b\r\n\r\n" % ip.encode())
                resp = sock.recv(1024).decode('utf-8', errors='ignore')
                return resp.strip()
            except Exception:
                pass

    except Exception:
        pass
    return None

def scan_port(ip, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            res = sock.connect_ex((ip, port))
            if res == 0:
                proto = port_protocol_map.get(port, "Unknown")
                print(f"\033[92m[+] {ip}:{port} OPEN ({proto})\033[0m")
                banner = identify_service(sock, ip, port)
                if banner:
                    banner_short = banner.replace("\r", " ").replace("\n", " ")[:200]
                    print(f"\033[92m[+] banner: {banner_short}\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error scanning {ip}:{port} -> {e}\033[0m", file=sys.stderr)

def port_scanner(ip, start_port=1, end_port=1024, max_workers=200, timeout=0.5):
    try:
        socket.gethostbyname(ip)
    except Exception as e:
        print(f"\033[91m[-] Invalid host/IP: {ip} ({e})\033[0m")
        return

    ports = range(start_port, end_port + 1)
    scan_partial = partial(scan_port, ip, timeout=timeout)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(scan_partial, ports)

if __name__ == "__main__":
    target = input("Enter the IP or hostname to scan: ").strip()
    port_scanner(target, start_port=1, end_port=1024, max_workers=200, timeout=0.3)
