def tcp_release(tcp_socket):
    """
    Release a TCP connection.

    Args:
        tcp_socket (socket.socket): Connected TCP socket.
    """
    if tcp_socket:
        try:
            tcp_socket.close()
            print("TCP connection released.")
        except Exception as e:
            print(f"Error releasing TCP connection: {e}")
