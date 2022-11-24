import socket


def get_ip_by_hostname():
    hostname = input('пожалуйста, введите URL-адрес веб-сайта: ')

    try:
        return f'Hostname: {hostname}\nIp адресс: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Неверный хост - {error}'



def main():
    print(get_ip_by_hostname())


if __name__ == '__main__':
    main()
