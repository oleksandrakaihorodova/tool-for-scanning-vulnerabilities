import socket
import threading
import concurrent.futures

# Функція для сканування одного порту
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Порт {port} відкритий")
            else:
                print(f"Порт {port} закритий")
    except Exception as e:
        print(f"Помилка при скануванні порту {port}: {e}")

# Головна функція, яка використовує багатопоточність для сканування портів
def main(ip, start_port, end_port):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

# Приклад використання
if __name__ == "__main__":
    target_ip = input("Введіть IP адресу для сканування: ")
    start_port = int(input("Введіть початковий порт для сканування: "))
    end_port = int(input("Введіть кінцевий порт для сканування: "))
    main(target_ip, start_port, end_port)
