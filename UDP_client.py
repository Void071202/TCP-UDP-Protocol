import socket

BUFFER_SIZE = 65536  # Maksimal ukuran paket UDP
MAX_FILE_SIZE = 500 * 1024  # Maksimal ukuran file (500KB)
VIDEO_PATH = 'video.mp4'  # Lokasi file video

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP dan port server
server_ip = '192.168.2.198'  # Ganti dengan IP address server
server_port = 12345

# Membaca file video
with open(VIDEO_PATH, 'rb') as f:
    video_data = f.read()

# Mengecek apakah ukuran file melebihi 500KB
if len(video_data) > MAX_FILE_SIZE:
    print(f"File terlalu besar: {len(video_data) / 1024:.2f}KB. Maksimal ukuran file adalah 500KB.")
else:
    # Mengirimkan file dalam paket-paket kecil
    for i in range(0, len(video_data), BUFFER_SIZE):
        packet = video_data[i:i + BUFFER_SIZE]
        client_socket.sendto(packet, (server_ip, server_port))
        print(f"Sent {len(packet)} bytes...")

    # Mengirim sinyal "DONE" untuk memberitahukan server bahwa file sudah selesai dikirim
    client_socket.sendto(b'DONE', (server_ip, server_port))
    print("File video berhasil dikirim.")

# Menutup socket
client_socket.close()
