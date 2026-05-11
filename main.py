import tkinter as tk
from initial import init_serial
from read_write import read_data, write_data
from release import release_serial

class SerialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Serial Communication")
        self.ser = None

        # COM port indicator (status)
        self.status_label = tk.Label(root, text="Not Connected")
        self.status_label.pack(pady=10)

        # COM port entry
        self.port_label = tk.Label(root, text="COM Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()
        self.port_entry.insert(0, "COM1")  # default

        # Connect button
        self.connect_button = tk.Button(root, text="Connect", command=self.connect)
        self.connect_button.pack(pady=10)

        # Read button
        self.read_button = tk.Button(root, text="Read", command=self.read)
        self.read_button.pack(pady=5)

        # Write entry and button
        self.write_label = tk.Label(root, text="Command to Write:")
        self.write_label.pack()
        self.write_entry = tk.Entry(root)
        self.write_entry.pack()
        self.write_button = tk.Button(root, text="Write", command=self.write)
        self.write_button.pack(pady=5)

        # Release button
        self.release_button = tk.Button(root, text="Release", command=self.release)
        self.release_button.pack(pady=10)

    def connect(self):
        if self.ser and self.ser.is_open:
            print("Already connected.")
            return
        port = self.port_entry.get()
        self.ser = init_serial(port)
        if self.ser:
            self.status_label.config(text="Connected")
            print("Connected to serial port.")
        else:
            self.status_label.config(text="Failed to Connect")
            print("Failed to connect.")

    def read(self):
        data = read_data(self.ser)
        if data:
            print(f"Read: {data}")
        else:
            print("No data read or error.")

    def write(self):
        command = self.write_entry.get()
        if command:
            write_data(self.ser, command)
            print(f"Written: {command}")
        else:
            print("No command to write.")

    def release(self):
        release_serial(self.ser)
        self.ser = None
        self.status_label.config(text="Not Connected")

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialApp(root)
    root.mainloop()