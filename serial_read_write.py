def serial_read(ser):
    """
    Read data from serial port.
    
    Args:
        ser (serial.Serial): Serial object
    
    Returns:
        str or None: Read data as string, None if error
    """
    if ser and ser.is_open:
        try:
            data = ser.readline()
            return data.decode('utf-8').strip()
        except Exception as e:
            print(f"Error reading data: {e}")
            return None
    return None

def serial_write(ser, command):
    """
    Write command to serial port.
    
    Args:
        ser (serial.Serial): Serial object
        command (str): Command to write
    """
    if ser and ser.is_open:
        try:
            ser.write(command.encode('utf-8'))
        except Exception as e:
            print(f"Error writing data: {e}")