# Praktikum SOAP
## Perintah yang akan dijalankan :

### 1 jalankan Perintah
docker compose -f compose/soap.yml up -d
### untuk build docker pada pengujian SOAP
![alt text](img/image1.png)
### 2. jalankan Perintah
docker compose -f compose/soap.yml exec soap-server python server.py
### untuk menjalankan server pada file server.py
![alt text](img/image2.png)
### 3. jalankan Perintah
docker compose -f compose/soap.yml exec soap-client python client.py
### untuk menjalankan client pada file client.py
![alt text](img/image3.png)
### 4. Sebelum melakukan pengujian jalankan 
ip a
### untuk mencari bridge interface yang digunakan container untuk melakukan packet capturing
![alt text](img/image4.png)
### 5. Sebelum melakukan pengujian jalankan 
sudo tcpdump -nvi br-(sesuaikan) -w (namafile).pcap
![alt text](img/image5.png)
### 6. pada bagian client masukkan pesan pesan yang nantinya akan diterima di server
![alt text](img/image6.png)
### 7. Setelah itu anda dapat memonitor pada file .pcap
![alt text](img/image7.png)
![alt text](img/image8.png)
