import serial

def init_serial(port, baudrate=9600, timeout=1): # init_serial function to initialize the serial connection
    """
    Initialize serial connection.
    
    Args:
        port (str): COM port (e.g., 'COM1')
        baudrate (int): Baud rate
        timeout (float): Timeout in seconds
    
    Returns:
        serial.Serial or None: Serial object if successful, None otherwise
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        return ser
    except Exception as e:
        print(f"Error initializing serial: {e}")
        return None