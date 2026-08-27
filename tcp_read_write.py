import time


def tcp_read(tcp_socket, buffer_size=4096, delay_time=0):
    """
    Read data from a TCP connection.

    Args:
        tcp_socket (socket.socket): Connected TCP socket.
        buffer_size (int): Maximum number of bytes to receive.
        delay_time (float): Delay in milliseconds before reading data.

    Returns:
        str or None: Read data as a string, or None if no data or an error occurs.
    """
    if tcp_socket:
        try:
            time.sleep(delay_time / 1000.0)
            data = tcp_socket.recv(buffer_size)
            if not data:
                return None
            return data.decode("utf-8").strip()
        except Exception as e:
            print(f"Error reading TCP data: {e}")
    return None


def tcp_write(tcp_socket, command):
    """
    Write a string to a TCP connection.

    Args:
        tcp_socket (socket.socket): Connected TCP socket.
        command (str): Command to write.

    Returns:
        bool: True if the data was sent, otherwise False.
    """
    if tcp_socket:
        try:
            tcp_socket.sendall(command.encode("utf-8"))
            return True
        except Exception as e:
            print(f"Error writing TCP data: {e}")
    return False
