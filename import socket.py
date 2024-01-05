import socket
import concurrent.futures

# Function to scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Main function that uses multithreading to scan ports
def main(ip, start_port, end_port):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter IP address for scanning: ")
    start_port = int(input("Enter start port for scanning: "))
    end_port = int(input("Enter end port for scanning: "))
    main(target_ip, start_port, end_port)
