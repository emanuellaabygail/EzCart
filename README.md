# EzCart
## Tautan deploy: 
emanuella-abygail-ezcart.pbp.cs.ui.ac.id

# Tugas 2
## Pertanyaan:
### I. Cara Pengimplementasian checklist
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

### II. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![image](https://github.com/user-attachments/assets/5bab8580-aa5f-4a6d-9a3b-81173b279372)
Pertama-tama, Client mengirimkan request ke browser. Django akan memeriksa urls.py untuk menemukan rute yang cocok dengan permintaan URL dan mengarahkan ke fungsi views.py. Fungsi views akan mengolah request dan kode di dalam views.py akan dijalankan dan mengambil data yang diperlukan. Jika ada, view akan mengumpulkan data dari models.py. Setelah data sudah ada, view akan memilih template HTML untuk merender halaman yang akan ditampilkan, yaitu pada main.html. Template ini menggunakan data dari view untuk menghasilkan HTML. Halaman web yang sudah dirender akan dikirim kembali ke browser pengguna sebagai respons.

### III. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah alat yang digunakan untuk pengelolaan versi dalam pengembangan perangkat lunak. Git dapat melacak semua perubahan yang dilakukan pada kode sehingga memudahkan kita untuk melihat riwayat perubahan dan mengembalikan ke versi sebelumnya jika memang diperlukan. Misalnya kita sedang mencoba suatu logic tetapi logic tersebut tidak benar dan merusak fungsionalitas kode. Dengan git, kita dapat mengembalikan kode ke versi sebelum logic yang merusak ditambahkan. 

Git juga berguna untuk pengembangan yang memerlukan kolaborasi dengan orang lain. Git memiliki fitur branching sehingga seseorang dapat mekerjakan suatu bagian code di branch terpisah tanpa mempengaruhi kode utama. Untuk menyatukan perubahan-perubahan pada branch, dilakukan merge. Saat merge, ada kemungkinan terjadinya konflik antarcabang. Git dapat membantu mendeteksi konflik tersebut sehingga dapat segera diselesaikan.

Git juga menyimpan seluruh riwayat kode secara lokal di repo lokal dan online di repo utama. Oleh karena itu, git dapat berfungsi sebagai back-up sehingga jika terjadi masalah pada repo lokal, pemulihan kode dapat dilakukan dengan mudah.

### IV. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih menjadi framework awal untuk pembelajaran pengembangan perangkat lunak karena Django punya struktur proyek yang jelas dan terorganisir sehingga lebih mudah untuk dipahami oleh pemula. Django adalah framework yang sudah memiliki berbagai fitur penting yang tersedia secara default. Dengan begitu, kita dapat fokus belajar konsep dasar tanpa perlu memikirkan penginstallan segala tambahan. Django memakai bahasa Python yang merupakan bahasa sederhana dan high-level serta sebagai mahasiswa Fasilkom UI, kita sudah mempelajarinya di mata kuliah DDP 1 sehingga kita sudah familiar dengan bahasa tersebut. Dokumentasi Django pun lengkap dan jelas. Django juga mengikuti pola arsitektur Model-View-Controller atau MVC yang sering digunakan di dunia industri sehingga cocok untuk dipelajari.

### V. Mengapa model pada Django disebut sebagai ORM?
Model di Django disebut sebagai ORM atau Object Relational Mapping karena fungsinya untuk menghubungkan antara kode Python dan database relasional. ORM memungkinkan kita untuk bekerja dengan data dalam bentuk object di Python tanpa menulis query SQL secara langsung. Dengan ORM, kita dapat berinteraksi dengan lebih mudah dan aman karena tidak perlu khawatir tentang sintaks SQL atau perbedaan antardatabase. ORM juga menjaga konsistensi dan integritas data secara otomatis sehingga dapat mengurangi risiko kesalahan.

<br>
<br>

# Tugas 3
## Pertanyaan:
### I. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam mengimplementasikan sebuah platform, data delivery sangat penting untuk memastikan aliran data yang efisien antara pengguna dan server serta antara berbagai komponen dalam aplikasi. Data delivery dibutuhkan agar interaksi antara pengguna dengan platform bisa berjalan dengan lancar dan konsisten. Data delivery memungkinkan pengiriman data secara cepat dan aman, baik data itu merupakan request, pembaruan, ataupun informasi penting lainnya. Tanpa adanya data delivery, aplikasi tidak akan berfungsi dengan baik dan optimal karena data yang diperlukan bisa saja rusak ataupun hilang sehingga tidak bisa dikirim dan diterima dengan baik.

### II. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
XML dan JSON memiliki keuntungannya masing-masing. XML lebih baik digunakan saat memiliki struktur data yang kompleks, sedangkan JSON lebih baik digunakan dalam platform yang membutuhkan pertukaran data yang ringan dan efisien. Menurut saya, secara umum, JSON lebih baik dibandingkan XML karena penggunaan JSON yang lebih ringan, sederhana, dan mudah dibaca oleh manusia dan juga mesin. JSON memiliki sintaks yang lebih ringkas dengan lebih sedikit tags dibandingkan XML sehingga JSON lebih efisien dalam hal ukuran data dan kecepatan transmisi. JSON lebih populer daripada XML karena lebih ringkas, kompatibel dengan JavaScript, lebih mudah untuk dibaca dan juga ditulis, serta lebih mudah dan cepat untuk di-parsing menggunakan 'JSON.parse()'.

### III. Jelaskan fungsi dari method 'is_valid()' pada form Django dan mengapa kita membutuhkan method tersebut?
Method 'is_valid()' pada form Django berfungsi untuk melakukan validasi data yang diisi pada form. Method ini akan memeriksa apakah semua field pada form terisi dengan benar sesuai dengan ketentuan yang sudah dibuat. Jika data yang diisi sudah sesuai, method 'is_valid()' akan mengembalikan True dan akan diproses lebih lanjut. Sebaliknya, jika data tidak sesuai dengan ketentuan, method 'is_valid()' akan mengembalikan False dan menyebabkan error sehingga data tidak dapat diproses lebih lanjut. Kita membutuhkan method ini untuk memastikan data yang diproses sudah aman dan sesuai dengan ketentuan sehingga keamanan aplikasi dan integritas data terjaga.

### IV. Mengapa kita membutuhkan 'csrf_token' saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan 'csrf_token' pada form Django? Bagaimana hal tersebut
csrf_token diperlukan untuk melindungi aplikasi kita dari serangan cross-site request forgery yang merupakan jenis serangan di mana penyerang dapat membuat pengguna tanpa sadar mengirimkan permintaan yang tidak sah ke server. Tanpa csrf_token, aplikasi rentan terhadap serangan ini, yang bisa mengakibatkan perubahan data atau tindakan tak sah dari akun pengguna. Django menggunakan token ini untuk memastikan bahwa permintaan form berasal dari sumber yang sah, sehingga menjaga keamanan aplikasi dan melindungi pengguna.

### V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
#### A. Membuat input form untuk menambahkan objek model pada app sebelumnya.
Pada direktori main, saya membuat file baru dengan nama forms.py. Di dalamnya, saya membuat struktur form yang akan menerima data product entry baru, yaitu class ProductEntryForm. Lalu, pada file views.py, saya membuat fungsi create_product_entry(request) yang akan menerima parameter request, melakukan validasi data, dan menghasilkan form yang akan menambahkan data Product Entry secara otomatis ketika form di-submit. Setelah itu, saya membuat file HTML baru yang berisi template untuk tampilan form.
#### B. Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Pada file views.py, import HttpResponse dari django.http dan serializers dari django.core. Pada file tersebut juga, saya membuat 4 fungsi views, yaitu show_xml(request), show_json(request), show_xml_by_id(request, id), dan show_json_by_id(request, id) yang masing-masing akan mengembalikan HttpResponse. Masing-masing fungsi memiliki atribut data yang berisi ProductEntry.objects.all() untuk show_xml dan show_json, serta ProductEntry.objects.filter(pk=id) untuk show_xml_by_id dan show_json_by_id.
#### C. Membuat routing URL untuk masing-masing views yang telah ditambahkan.
Pada file urls.py pada direktori main, saya menambahkan import keempat fungsi tersebut dan menambahkan path untuk masing-masing fungsi.

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![image](https://github.com/user-attachments/assets/9ced82f7-300d-4601-bf91-341ef907e519)
![Screenshot (2798)](https://github.com/user-attachments/assets/7ef8e64b-19f3-4d90-b586-8dd72a1a42c0)
![Screenshot (2800)](https://github.com/user-attachments/assets/3a7af467-358e-4634-8ba9-270063fb87a5)
![Screenshot (2799)](https://github.com/user-attachments/assets/9211534e-5bdf-4818-a194-b0992d69dc9e)
