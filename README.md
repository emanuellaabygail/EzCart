# EzCart
## Tautan deploy: 
## Pertanyaan:
### Cara Pengimplementasian checklist
#### A. Membuat sebuah proyek Django baru
1. Saya membuat sebuah direktori kosong pada komputer saya dan menginisiasikan repositori dengan perintah "git init" untuk membuat repositori git kosong di direktori yang dibuat lalu konfigurasi repositori tersebut
2. Saya juga membuat sebuah repositori pada github yang akan menjadi tempat penyimpanan repo lokal di github, kemudian hubungkan repo lokal dan repo di git dengan perintah "git remote add origin <URL_REPO>". Add, commit, dan push file-file yang dibuat di repo lokal ke repo github sehingga tersimpan juga di repo github
3. Setelah repo telah terbuat, saya mengaktifkan virtual environment dan menginstall semua dependencies yang diperlukan untuk menjalankan django. Dependencies diinstall pada virtual environment agar tidak bertabrakan dengan dependencies lain yang sudah ada di komputer
4. Kemudian, saya menkonfigurasikan proyek dengan menambahkan "localhost", "127.0.0.1" ke ALLOWED_HOST pada file settings.py. Hal ini akan memberi izin akses dari host local. Untuk melihat proyek django yang sudah dibuat, jalankan perintah "python manage.py runserver" dan buka pada link http://localhost:8000

#### B. Membuat aplikasi dengan nama main pada proyek Django yang sudah dibuat
Untuk membuat aplikasi baru dengan nama main, saya menjalankan perintah "python manage.py startapp main" yang akan menyebabkan direktori baru dengan nama main terbuat. Direktori ini berisi struktur awal aplikasi Django

#### C. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Agar aplikasi main bisa dijalankan, perlu dilakukan routing. Routing dilakukan dengan cara membuka file settings.py lalu pada list INSTALLED_APPS, saya menambahkan "main".

#### D. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description
Pada file models.py, saya membuat sebuah class baru yang bernama Product dan saya mengisi atributnya dengan name dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField. Setelah membuat model, saya membuat dan mengaplikasikan migrasi model agar Django dapat melacak perubahan pada model basis data saya.

#### E. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML 
Pada file views.py di dalam folder aplikasi main, saya menambahkan fungsi bernama show_main yang berisi dictionary context yang di dalamnya terdapat pasangan key dan value. Key akan dipanggil di dalam template HTML dan aplikasi Django akan menampilkan valuenya. 

#### F. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Di direktori aplikasi main, saya membuat file urls.py dan menambahkan kode:
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
dengan kode ini, urls.py akan mengatur rute URL yang terkait dengan aplikasi main. variable app_name diberikan untuk memberi nama unik pada pola URL dalam aplikasi.
2. Di direktori proyek, saya membuka file urls.py. Pada file tersebut, saya menambahkan fungsi include dari django.urls dan menambahkan rute URL path('', include('main.urls')) untuk mengarahkan proyek ke tampilan main

#### G. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet.
1. Saya log in pada website PWS dan membuat project baru dengan menekan "Create New Project". Di laman pembuatan proyek baru, saya memasukkan nama proyek saya, yaitu ezcart dan menekan tombol "Create New Project". Akan muncul info tentang project credentials dan project command. Saya meng-copy project credentialsnya karena diperlukan pada step-step berikutnya.
2. Sebelum menjalankannya, saya menambahkan URL deployment saya, yaitu emanuella-abygail-ezcart.pbp.cs.ui.ac.id, pada list ALLOWED_HOSTS di settings.py
3. git add, commit, dan push perubahan ke repo GitHub
4. Jalankan perintah pada Project Command dan web akan dijalankan