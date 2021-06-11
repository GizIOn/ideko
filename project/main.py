import aiohttp
import asyncio
import socket



def main_socket():
    global scan_port

    def scan_port(ip_to_check, port_to_check):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if client.connect_ex((ip_to_check, port_to_check)): pass
        print(f"Port {port_to_check} is open")

    def check_ports(operation, func, host_ip, first_port, last_port):
        port_to_check = int(first_port)
        last_port = int(last_port)
        while port_to_check < last_port:
            scan_port(host_ip, port_to_check)
            port_to_check += 1


    operation, func, host_ip, first_port, last_port = input("Type needed operation \n"
        "(Needed format: * GET /scan/178.213.207.117/25565/27015): ").split("/")
    check_ports(operation, func, host_ip, first_port, last_port)


# scannin ports, using socket module
main_socket()