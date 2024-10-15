import socket

# Fungsi untuk menerima data dari client
def receive_data(connection, file_name, data_size):
    total_received = 0
    with open(file_name, 'wb') as f:
        while total_received < data_size:
            # Menerima data dari client
            data = connection.recv(1024)
            if not data:
                break
            # Menulis data ke file
            f.write(data)
            total_received += len(data)
    
    print(f"Data {total_received // 1024}KB berhasil diterima dan disimpan di '{file_name}'")

# Membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat IP lokal server
server_socket.bind(('192.168.2.236', 12345))  # Ganti dengan IP server

# Mendengarkan koneksi
server_socket.listen(5)
print("Server menunggu koneksi...")

# Menerima koneksi dari client
client_socket, addr = server_socket.accept()
print(f"Koneksi diterima dari {addr}")

# Menerima pesan dari client dengan ukuran spesifik
data_size = int(client_socket.recv(1024).decode())  # Mendapatkan ukuran data yang akan diterima
receive_data(client_socket, 'received_file.txt', data_size)

# Menutup koneksi
client_socket.close()
server_socket.close()
