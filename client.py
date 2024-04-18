import socket
import json
import time
import commons.config as config
from commons.utils import build_package, calculate_checksum
import tkinter as tk
from tkinter import messagebox
import os


class Client:
    def __init__(self, filename):
        self.filename = filename
        self.ids_to_recover = []
        self.received_data = []
        self.window = None
        self.user_response = None

    def establish_socket_connection(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if not host or not port:
            messagebox.showerror("Error", "Host and port must be filled")
            return

        self.server_address = (host, port)
        self.user_response.set("connected")
        print(self.user_response)

    def main(self):
        self.window = tk.Tk()
        self.window.geometry("600x700")
        self.window['padx'] = 10
        self.window['pady'] = 100
        self.user_response = tk.StringVar()
        tk.Label(self.window, text="Host:").pack(anchor='center', padx=2, pady=2)
        host = tk.Entry(self.window)
        host.pack(anchor='center', padx=2, pady=2)

        tk.Label(self.window, text="Port:").pack(anchor='center', padx=2, pady=2)
        port = tk.Entry(self.window)
        port.pack(anchor='center', padx=2, pady=2)

        tk.Button(self.window, text="Connect", command=lambda: self.establish_socket_connection(host.get(), port.get())).pack(anchor='center', padx=2, pady=2)
        tk.Button(self.window, text="Use Default", command=lambda: self.establish_socket_connection(config.HOST, config.PORT)).pack(anchor='center', padx=2, pady=2)
        self.window.wait_variable(self.user_response)
        self.clear()

        label = tk.Label(self.window, text="Enter the file name:")
        label.pack(anchor='center', padx=2, pady=2)

        entry = tk.Entry(self.window)
        entry.pack(padx=5, pady=5)

        button = tk.Button(self.window, text="Submit", command=lambda: self.handle_button_click(entry))
        button.pack()

        self.window.mainloop()

    def handle_button_click(self, entry):
        self.filename = entry.get()
        self.clear()

        try:
            self.request()
        except TypeError:
            messagebox.showerror("Error", "Invalid Port or Host address: "+str(self.server_address))
        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.window.destroy()

    def request(self):
        self.user_response = tk.StringVar()
        while True:
            self.sock.sendto(build_package(0, self.get_file_name(), config.SUCCESS_CODE, config.FETCH), self.server_address)
            self.listen()

            for data in self.received_data:
                if data['package_id'] in self.ids_to_recover and data['checksum'] == calculate_checksum(data['data'].encode()):
                    self.ids_to_recover.remove(data['package_id'])

            if not self.ids_to_recover:
                message = "All data received successfully, do you want to generate and open the output file?"
                tk.Label(self.window, text=message).pack(anchor='center', padx=2, pady=2)
                tk.Button(self.window, text="Y", command=lambda: self.write_output()).pack()
                tk.Button(self.window, text="N", command=lambda: self.leave()).pack()
                self.window.wait_variable(self.user_response)
                break

        self.sock.close()

    def get_file_name(self):
        if not self.ids_to_recover:
            return self.filename.encode()

        return (self.filename + ' ' + (' '.join(map(str, self.ids_to_recover)))).encode()

    def listen(self):
        while True:
            data, addr = self.sock.recvfrom(config.BUFFER_SIZE)
            data = json.loads(data.decode())
            if data['status_code'] == config.SUCCESS_CODE:
                break
            if data['status_code'] == config.ERROR_CODE:
                messagebox.showerror("Error", data['data'])
                self.sock.close()
                exit(1)

            self.ask_user(data)

    def destroy(self, data):
        if data['package_id'] not in self.ids_to_recover:
            self.ids_to_recover.append(data['package_id'])
        self.user_response.set('Yes')

    def keep(self, data):
        self.received_data.insert(data['package_id'], data)
        self.user_response.set('No')

    def ask_user(self, data):
        self.user_response = tk.StringVar()

        label = tk.Label(self.window, text="Do you want to destroy package " + str(data['package_id']) + "?")
        label.pack(anchor='center', padx=2, pady=2)
        tk.Button(self.window, text="Y", command=lambda: self.destroy(data)).pack()
        tk.Button(self.window, text="N", command=lambda: self.keep(data)).pack()

        self.window.wait_variable(self.user_response)
        self.clear()

    def write_output(self):
        print("Writing output file")
        sorted_data = sorted(self.received_data, key=lambda x: x['package_id'])
        with open('received_' + self.filename, 'wb') as file:
            for data in sorted_data:
                file.write(data['data'].encode())

        file.close()
        
        os.system('xdg-open received_' + self.filename)
        self.leave()

    def leave(self):
        self.user_response.set('Yes')

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()


client = Client("")
client.main()
