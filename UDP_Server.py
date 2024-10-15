import socket
import cv2
import numpy as np

BUFFER_SIZE = 65536  # Maksimal ukuran paket UDP
SAVE_PATH = 'received_video.mp4'  # Lokasi penyimpanan video

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))
print("Server siap menerima file video...")

# Menyimpan data video yang diterima
file_data = b''

while True:
    # Menerima data paket dari client
    packet, addr = server_socket.recvfrom(BUFFER_SIZE)

    # Jika menerima "DONE", hentikan penerimaan
    if packet == b'DONE':
        print("Penerimaan file selesai.")
        break

    # Menggabungkan paket ke file_data
    file_data += packet
    print(f"Received {len(packet)} bytes...")

# Menyimpan data video ke file
with open(SAVE_PATH, 'wb') as f:
    f.write(file_data)

print(f"File video berhasil disimpan sebagai {SAVE_PATH}")

# Menutup socket
server_socket.close()
