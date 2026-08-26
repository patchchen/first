import tkinter as tk
from tkinter import messagebox

try:
    from first.tcp_initial import tcp_init
    from first.tcp_read_write import tcp_read, tcp_write
    from first.tcp_release import tcp_release
except ModuleNotFoundError:
    from tcp_initial import tcp_init
    from tcp_read_write import tcp_read, tcp_write
    from tcp_release import tcp_release


TCP_PORT = 8888
TCP_TIMEOUT = 10


class TcpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TCP Instrument Communication")
        self.root.resizable(False, False)
        self.tcp_socket = None

        tk.Label(root, text="Instrument IP:").grid(
            row=0, column=0, padx=10, pady=(10, 5), sticky="w"
        )
        self.ip_entry = tk.Entry(root, width=30)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=(10, 5))
        self.ip_entry.insert(0, "172.16.8.104")

        self.connect_button = tk.Button(
            root, text="Connect", width=12, command=self.connect
        )
        self.connect_button.grid(row=0, column=2, padx=10, pady=(10, 5))

        tk.Label(root, text="Command:").grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.command_entry = tk.Entry(root, width=30)
        self.command_entry.grid(row=1, column=1, padx=10, pady=5)

        self.send_button = tk.Button(
            root, text="Send", width=12, command=self.send, state=tk.DISABLED
        )
        self.send_button.grid(row=1, column=2, padx=10, pady=5)

        self.send_setting_button = tk.Button(
            root, text="Send Setting", width=12,
            command=self.send_setting, state=tk.DISABLED
        )
        self.send_setting_button.grid(row=2, column=2, padx=10, pady=5)

        tk.Label(root, text="Log:").grid(
            row=3, column=0, padx=10, pady=5, sticky="nw"
        )
        self.log_text = tk.Text(root, width=60, height=12, state=tk.DISABLED)
        self.log_text.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        self.stop_button = tk.Button(
            root, text="Stop", width=12, command=self.stop
        )
        self.stop_button.grid(row=4, column=2, padx=10, pady=(5, 10))

        self.root.protocol("WM_DELETE_WINDOW", self.stop)

    def write_log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def connect(self):
        if self.tcp_socket:
            self.write_log("Already connected.")
            return

        ip = self.ip_entry.get().strip()
        if not ip:
            messagebox.showwarning("Input required", "Please enter the instrument IP.")
            return

        self.write_log("Connecting to {0}:{1}...".format(ip, TCP_PORT))
        self.tcp_socket = tcp_init(ip, TCP_PORT, timeout=TCP_TIMEOUT)

        if self.tcp_socket:
            self.write_log("Connected to instrument.")
            self.connect_button.config(state=tk.DISABLED)
            self.send_button.config(state=tk.NORMAL)
            self.send_setting_button.config(state=tk.NORMAL)
        else:
            self.write_log("Failed to connect to instrument.")

    def send(self):
        command = self.command_entry.get()
        if not command:
            messagebox.showwarning("Input required", "Please enter a command.")
            return

        if not self.tcp_socket:
            self.write_log("Please connect to the instrument first.")
            return

        if tcp_write(self.tcp_socket, command):
            self.write_log("Sent: {0}".format(command))
            response = tcp_read(self.tcp_socket)
            if response is None:
                self.write_log("No response received.")
            else:
                self.write_log("Received: {0}".format(response))
        else:
            self.write_log("Failed to send command.")

    def send_setting(self):
        command = self.command_entry.get()
        if not command:
            messagebox.showwarning("Input required", "Please enter a command.")
            return

        if not self.tcp_socket:
            self.write_log("Please connect to the instrument first.")
            return

        if tcp_write(self.tcp_socket, command):
            self.write_log("Setting sent: {0}".format(command))
        else:
            self.write_log("Failed to send setting command.")

    def stop(self):
        if self.tcp_socket:
            tcp_release(self.tcp_socket)
            self.tcp_socket = None
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TcpApp(root)
    root.mainloop()
