# Praktikum ZMQ
ZeroMQ (ZMQ/ØMQ) adalah library messaging high-performance untuk distributed system.

Tidak seperti socket TCP biasa, ZeroMQ menyediakan messaging patterns siap pakai.

Beberapa pola populer:

- REQ–REP (Request–Reply) → client request, server reply.

- PUB–SUB (Publish–Subscribe) → publisher broadcast, subscriber pilih topik.

- PUSH–PULL (Pipeline) → push distribusi pekerjaan ke worker pull.
## Perintah yang akan dijalankan :

### 1 jalankan Perintah
`docker compose -f compose/zmq.yml up -d`
### untuk build docker pada pengujian ZMQ
![alt text](img/image1.png)
### 2. Sebelum melakukan pengujian jalankan 
`ip a`
### untuk mencari bridge interface yang digunakan container untuk melakukan packet capturing
![alt text](img/image4.png)
### 3. Sebelum melakukan pengujian jalankan 
`sudo tcpdump -nvi br-(sesuaikan) -w (namafile).pcap`
![alt text](img/image5.png)
### 4. jalankan Perintah
`docker compose -f compose/zmq.yml exec zmq-req python clientzmq.py`
### untuk menjalankan file clinetzmq.py
![alt text](img/image2.png)

Client buat socket `REQ` -> Connect ke server REP di `zmq-rep:5555` -> Kirim `"Hello"` → tunggu balasan.

### 5. jalankan Perintah
`docker compose -f compose/zmq.yml exec zmq-sub python subzmq.py`
<br>

![alt text](img/image3.png)

Client buat socket SUB -> Connect ke publisher di `zmq-pub:12345` -> SUBSCRIBE "WAKTU" artinya hanya terima pesan dengan prefix topik "WAKTU" -> Loop terus menerima pesan → cocok untuk broadcast real-time (misalnya harga saham, notifikasi waktu). 

### 6. jalankan Perintah
`docker compose -f compose/zmq.yml exec zmq-pull python pullzmq.py`
### untuk menjalankan  file pullzmq.py
![alt text](img/image6.png)

Worker pakai PULL -> Connect ke `zmq-push:9999 `-> Tunggu pekerjaan (job) dalam bentuk serialized object (pakai pickle) -> Setelah terima job (misalnya angka 2), worker sleep selama 2 detik → simulasi kerja.

### 7. pada bagian client masukkan pesan pesan yang nantinya akan diterima di server
![alt text](img/image7.png)
### 8. Setelah itu anda dapat memonitor pada file .pcap
![alt text](img/image8.png)
![alt text](img/image9.png)
