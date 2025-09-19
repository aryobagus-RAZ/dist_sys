# Praktikum ZMQ
## Perintah yang akan dijalankan :

### 1 jalankan Perintah
docker compose -f compose/zmq.yml up -d
### untuk build docker pada pengujian ZMQ
![alt text](img/image1.png)
### 2. Sebelum melakukan pengujian jalankan 
ip a
### untuk mencari bridge interface yang digunakan container untuk melakukan packet capturing
![alt text](img/image4.png)
### 3. Sebelum melakukan pengujian jalankan 
sudo tcpdump -nvi br-(sesuaikan) -w (namafile).pcap
![alt text](img/image5.png)
### 4. jalankan Perintah
docker compose -f compose/zmq.yml exec zmq-req python clientzmq.py
### untuk menjalankan server pada file clinetzmq.py
![alt text](img/image2.png)
### 5. jalankan Perintah
docker compose -f compose/zmq.yml exec zmq-sub python subzmq.py
![alt text](img/image3.png)
### 5. jalankan Perintah
docker compose -f compose/zmq.yml exec zmq-pull python pullzmq.py
### untuk menjalankan client pada file client.py
![alt text](img/image6.png)

### 6. pada bagian client masukkan pesan pesan yang nantinya akan diterima di server
![alt text](img/image7.png)
### 7. Setelah itu anda dapat memonitor pada file .pcap
![alt text](img/image8.png)
![alt text](img/image9.png)
