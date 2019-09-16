import socket

def main_udp():
    # 1. 初始化socket
    udp_skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # 2. 绑定本地ip和端口
    ip_address = socket.gethostname()
    print(ip_address)
    udp_skt.bind((ip_address, 6789))

    # 3. 接收/发送消息
    client_msg, client_addr = udp_skt.recvfrom(1024)
    print('收到了客户端的数据:', client_msg.decode())

    # 发送消息
    print(client_addr, '========')
    udp_skt.sendto('我是udp的服务端'.encode(), client_addr)

    # 4. 关闭
    udp_skt.close()
def main_tcp():
    tcp_skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    tcp_skt.bind((socket.gethostname(),6789))

    tcp_skt.listen()
    print("等待连接...")
    while True:
        skt_client, addr = tcp_skt.accept()
        print("接收消息:{}".format(addr))
        msg = skt_client.recv(1024)
        print(msg.decode() + '\n')
        skt_client.send('哈哈哈，已收到你的消息'.encode('utf-8'))
        skt_client.close()

if __name__ == "__main__":

    main_udp()
