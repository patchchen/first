def serial_release(ser):
    """
    Release serial connection.
    
    Args:
        ser (serial.Serial): Serial object
    """
    if ser and ser.is_open:
        try:
            ser.close()
            print("Serial connection released.")
        except Exception as e:
            print(f"Error releasing serial: {e}")