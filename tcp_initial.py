import socket


def tcp_init(host, port, timeout=1):
    """
    Initialize a TCP client connection.

    Args:
        host (str): Server hostname or IP address.
        port (int): Server TCP port.
        timeout (float): Socket timeout in seconds.

    Returns:
        socket.socket or None: Connected socket if successful, None otherwise.
    """
    try:
        tcp_socket = socket.create_connection((host, port), timeout=timeout)
        tcp_socket.settimeout(timeout)
        return tcp_socket
    except Exception as e:
        print(f"Error initializing TCP connection: {e}")
        return None
