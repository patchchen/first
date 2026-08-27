from tcp_initial import tcp_init
from tcp_read_write import tcp_read, tcp_write
from tcp_release import tcp_release

TCP_PORT = 8888
TCP_TIMEOUT = 10
TCP_SOCKET = None


def connect(ip):
    global TCP_SOCKET
    if TCP_SOCKET:
        return "Already connected."

    TCP_SOCKET = tcp_init(ip, TCP_PORT, timeout=TCP_TIMEOUT)
    if TCP_SOCKET:
        return "Connected to instrument."
    return "Failed to connect to instrument."


def send(command, buffer_size=1024, delay_time=200):
    global TCP_SOCKET
    if not TCP_SOCKET:
        return "Please connect to the instrument first."

    if not tcp_write(TCP_SOCKET, command):
        return "Failed to send command."

    response = tcp_read(TCP_SOCKET, buffer_size, delay_time)
    if response is None:
        return "No response received."
    return "Received: {0}".format(response)


def send_setting(command):
    global TCP_SOCKET
    if not TCP_SOCKET:
        return "Please connect to the instrument first."

    if tcp_write(TCP_SOCKET, command):
        return "Setting sent: {0}".format(command)
    return "Failed to send setting command."


def stop():
    global TCP_SOCKET
    if TCP_SOCKET:
        tcp_release(TCP_SOCKET)
        TCP_SOCKET = None
    return "TCP connection released."
