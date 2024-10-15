import socket

# Fungsi untuk membuat data dummy dengan ukuran tertentu
def generate_data(size_in_kb):
    return b'fufufafa' * (size_in_kb * 1024)  # Membuat data dengan isi karakter 'a'

# Fungsi untuk mengirim data ke server
def send_data(connection, data):
    connection.sendall(data)
    print(f"Data sebesar {len(data) // 1024}KB berhasil dikirim.")

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Terhubung ke server
client_socket.connect(('192.168.2.198', 12345))  # Ganti dengan IP server

# Pilih ukuran data yang ingin dikirim: 10KB, 100KB, atau 1000KB
data_size_kb = 100  # Ubah ini menjadi 10, 100, atau 1000 untuk ukuran yang berbeda
data = generate_data(data_size_kb)

# Mengirim ukuran data terlebih dahulu
client_socket.send(str(len(data)).encode())

# Mengirim data ke server
send_data(client_socket, data)

# Menutup koneksi
client_socket.close()
