import ipaddress
import subprocess
import platform
import socket
import time


def ping_host(ip, timeout=1):
    """Проверяет доступность хоста с помощью ping"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-w', str(timeout), str(ip)]
    try:
        response = subprocess.call(command,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
        return response == 0
    except:
        return False


def get_hostname(ip):
    """Пытается получить имя хоста"""
    try:
        return socket.gethostbyaddr(str(ip))[0]
    except:
        return "Неизвестно"


def scan_network_with_delay(delay_sec=0.1):
    """Сканирует сеть с задержкой между запросами"""
    network = ipaddress.ip_network('192.168.1.0/24')
    active_hosts = []

    print(f"Начинаю сканирование сети {network} с задержкой {delay_sec} сек...")
    print("Это может занять некоторое время...\n")

    for i, ip in enumerate(network.hosts(), 1):
        start_time = time.time()

        if ping_host(ip):
            hostname = get_hostname(ip)
            print(f"[{i}] {ip} - {hostname} [ONLINE]")
            active_hosts.append(ip)
        else:
            print(f"[{i}] {ip} - проверка...", end='\r')

        # Вычисляем оставшееся время задержки
        elapsed = time.time() - start_time
        remaining_delay = max(0, delay_sec - elapsed)
        time.sleep(remaining_delay)

    print("\n\nСканирование завершено.")
    print(f"Найдено активных устройств: {len(active_hosts)}")
    print("Список доступных хостов:")
    for host in sorted(active_hosts, key=lambda x: int(x.partition('.')[-1])):
        print(f"• {host}")


if __name__ == "__main__":
    # Настройки
    SCAN_DELAY = 0.2  # Задержка между ping-запросами в секундах

    start_time = time.time()
    scan_network_with_delay(SCAN_DELAY)
    print(f"\nОбщее время сканирования: {time.time() - start_time:.2f} секунд")