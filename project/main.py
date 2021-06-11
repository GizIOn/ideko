import aiohttp
import asyncio
import socket
import json

class Port:
    def __init__(self, port, open):
        self.port=port
        self.open=open

    def __repr__(self):
        is_open=""
        if self.open: is_open="open"
        else: is_open="close"
        return json.JSONEncoder().encode(f"port: {self.port}, open: {is_open}")


def main_socket():
    global scan_port

    def scan_port(ip_to_check, port_to_check):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if client.connect_ex((ip_to_check, port_to_check)):
            return Port(port_to_check, False)
        else:
            return Port(port_to_check, True)

    def check_ports(operation, func, host_ip, first_port, last_port):
        ports=[]
        port_to_check = int(first_port)
        last_port = int(last_port)
        while port_to_check < last_port:
            port_info = scan_port(host_ip, port_to_check)
            print(port_info)
            ports.append(port_info)
            port_to_check += 1

        return ports


    operation, func, host_ip, first_port, last_port = input("Type needed operation \n"
        "(Needed format: GET /scan/178.213.207.117/25565/27015): ").split("/")
    result = check_ports(operation, func, host_ip, first_port, last_port)
    print(result)

# scannin ports, using socket module
main_socket()