try:
    import socket
    import concurrent.futures
    import os
except Exception as e:
    input(e)

ip = input("Enter the IP address to scan: ")

try:
    def PortScanner(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }
        def scan_port(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        protocol = port_protocol_map.get(port, "Unknown")
                        print(f"Port {port} is open ({protocol})")
                        Indentify_Port(ip, port)
            except Exception as e:
                pass

        def Indentify_Port(ip, port):
            try:
                if port in port_protocol_map
                    protocol = port_protocol_map[port]
                    return(f"Identified service on port {port}: {protocol}")
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(0.1)
                        sock.connect((ip, port))
                        sock.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
                        response = sock.recv(1024).decode('utf-8', errors='ignore')
                        if "HTTP" in response:
                            print(f"Port {port} is running HTTP service")
                            sock.send(b"\r\n")
                            response = sock.recv(1024).decode('utf-8', errors='ignore')
                        elif "SSH" in response:
                            print(f"Port {port} is running SSH service")
                            return "SSH"
                        elif "FTP" in response:
                            print(f"Port {port} is running FTP service")
                            sock.send(b"\r\n")
                            response = sock.recv(1024).decode('utf-8', errors='ignore')
                        elif "SMTP" in response:
                            print(f"Port {port} is running SMTP service")
                        else:
                            print(f"Port {port} is open but service is unknown")
                            return
                except Exception as e:
                    input(e)

            except Exception as e:
                pass


        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: scan_port(ip, port), range(1, 65536))


except Exception as e:
    input(e)
    socket.inet_aton(ip)