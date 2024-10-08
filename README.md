# EzCart
## Tautan deploy: 
emanuella-abygail-ezcart.pbp.cs.ui.ac.id

# Tugas 2
## Pertanyaan:
### I. Cara Pengimplementasian checklist
#### a. Membuat sebuah proyek Django baru
1. Saya membuat sebuah direktori kosong pada komputer saya dan menginisiasikan repositori dengan perintah "git init" untuk membuat repositori git kosong di direktori yang dibuat lalu konfigurasi repositori tersebut
2. Saya juga membuat sebuah repositori pada github yang akan menjadi tempat penyimpanan repo lokal di github, kemudian hubungkan repo lokal dan repo di git dengan perintah "git remote add origin <URL_REPO>". Add, commit, dan push file-file yang dibuat di repo lokal ke repo github sehingga tersimpan juga di repo github
3. Setelah repo telah terbuat, saya mengaktifkan virtual environment dan menginstall semua dependencies yang diperlukan untuk menjalankan django. Dependencies diinstall pada virtual environment agar tidak bertabrakan dengan dependencies lain yang sudah ada di komputer
4. Kemudian, saya menkonfigurasikan proyek dengan menambahkan "localhost", "127.0.0.1" ke ALLOWED_HOST pada file settings.py. Hal ini akan memberi izin akses dari host local. Untuk melihat proyek django yang sudah dibuat, jalankan perintah "python manage.py runserver" dan buka pada link http://localhost:8000

#### b. Membuat aplikasi dengan nama main pada proyek Django yang sudah dibuat
Untuk membuat aplikasi baru dengan nama main, saya menjalankan perintah "python manage.py startapp main" yang akan menyebabkan direktori baru dengan nama main terbuat. Direktori ini berisi struktur awal aplikasi Django

#### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Agar aplikasi main bisa dijalankan, perlu dilakukan routing. Routing dilakukan dengan cara membuka file settings.py lalu pada list INSTALLED_APPS, saya menambahkan "main".

#### d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description
Pada file models.py, saya membuat sebuah class baru yang bernama Product dan saya mengisi atributnya dengan name dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField. Setelah membuat model, saya membuat dan mengaplikasikan migrasi model agar Django dapat melacak perubahan pada model basis data saya.

#### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML 
Pada file views.py di dalam folder aplikasi main, saya menambahkan fungsi bernama show_main yang berisi dictionary context yang di dalamnya terdapat pasangan key dan value. Key akan dipanggil di dalam template HTML dan aplikasi Django akan menampilkan valuenya. 

#### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Di direktori aplikasi main, saya membuat file urls.py dan menambahkan kode:
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
dengan kode ini, urls.py akan mengatur rute URL yang terkait dengan aplikasi main. variable app_name diberikan untuk memberi nama unik pada pola URL dalam aplikasi.
2. Di direktori proyek, saya membuka file urls.py. Pada file tersebut, saya menambahkan fungsi include dari django.urls dan menambahkan rute URL path('', include('main.urls')) untuk mengarahkan proyek ke tampilan main

#### g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet.
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
#### a. Membuat input form untuk menambahkan objek model pada app sebelumnya.
Pada direktori main, saya membuat file baru dengan nama forms.py. Di dalamnya, saya membuat struktur form yang akan menerima data product entry baru, yaitu class ProductEntryForm. Lalu, pada file views.py, saya membuat fungsi create_product_entry(request) yang akan menerima parameter request, melakukan validasi data, dan menghasilkan form yang akan menambahkan data Product Entry secara otomatis ketika form di-submit. Setelah itu, saya membuat file HTML baru yang berisi template untuk tampilan form.
#### b. Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Pada file views.py, import HttpResponse dari django.http dan serializers dari django.core. Pada file tersebut juga, saya membuat 4 fungsi views, yaitu show_xml(request), show_json(request), show_xml_by_id(request, id), dan show_json_by_id(request, id) yang masing-masing akan mengembalikan HttpResponse. Masing-masing fungsi memiliki atribut data yang berisi ProductEntry.objects.all() untuk show_xml dan show_json, serta ProductEntry.objects.filter(pk=id) untuk show_xml_by_id dan show_json_by_id.
#### c. Membuat routing URL untuk masing-masing views yang telah ditambahkan.
Pada file urls.py pada direktori main, saya menambahkan import keempat fungsi tersebut dan menambahkan path untuk masing-masing fungsi.

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![image](https://github.com/user-attachments/assets/9ced82f7-300d-4601-bf91-341ef907e519)
![Screenshot (2798)](https://github.com/user-attachments/assets/7ef8e64b-19f3-4d90-b586-8dd72a1a42c0)
![Screenshot (2800)](https://github.com/user-attachments/assets/3a7af467-358e-4634-8ba9-270063fb87a5)
![Screenshot (2799)](https://github.com/user-attachments/assets/9211534e-5bdf-4818-a194-b0992d69dc9e)

<br>
<br>

# Tugas 4
## Pertanyaan:
### I. Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect() dan redirect() pada Django memiliki fungsi yang sama, yaitu mengarahkan kembali pengguna ke URL lain yang ditentukan. Perbedaannya adalah pada HttpResponseRedirect(), argumen yang dapat diterima hanya berupa url, sedangkan pada redirect(), argumen dapat berupa model, view, ataupun url. Fungsi redirect() akan mengembalikan HttpResponseRedirect() dengan url yang sesuai dengan argumen yang dimasukkan ke fungsi redirect. Jadi, redirect akan menentukan terlebih dahulu url yang sesuai dengan argumen yang dimasukkan dan mengembalikan HttpResponseRedirect() ke url tersebut.

### II. Jelaskan cara kerja penghubungan model Product dengan User!
Pada proyek ini, model Product dihubungkan dengan User dengan menggunakan ForeignKey. Penggunaan ForeignKey dapat dilihat pada file models.py di mana class ProductEntry memiliki atribut user = models.ForeignKey(User, on_delete=models.CASCADE) yang menghubungkan satu product entry dengan satu user sehingga satu product pasti terasosiasi dengan satu user. Pada potongan kode product_entries = ProductEntry.objects.filter(user=request.user) di file views.py menyebabkan product yang ditunjukkan hanyalah product yang terasosiasi dengan user yang logged in pada session tersebut. Pada fungsi create_product_entry di file views.py, terdapat potongan kode product_entry.user = request.user sehingga saat product disimpan, atribut user pada model ProdyctEntry akan diisi dengan user yang sedang login (request.user). 

### III. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication adalah proses untuk memverifikasi identitas pengguna dengan memeriksa credentials yang dimasukkan oleh pengguna pada saat login. Sistem akan melihat apakah pengguna terdaftar di dalam database. Authorization adalah tahap lanjut dari authentification, yaitu proses pemberian akses dan izin kepada mengguna untuk menggunakan fitur-fitur tertentu yang ada di aplikasi. 
- Pada saat pengguna login, pengguna memasukkan username dan password lalu aplikasi akan memvalidasi apakah username dan password ada dalam database sebagai credential user yang valid. Jika valid, pengguna sudah terautentikasi sedangkan jika tidak valid pengguna akan diminta untuk memasukkan ulang. Setelah berhasil login, aplikasi akan menyimpan status login pengguna dalam sesi (menggunakan session management) sehingga pada permintaan berikutnya, aplikasi tahu bahwa pengguna tersebut sudah login.Cookie bisa disimpan di browser pengguna untuk mengingat login atau melacak waktu login terakhir.
- Django mengimplementasikan authentication dengan mengecek apakah pengguna sudah login melalui sistem login, logout, dan session management. Untuk authorization, Django memastikan pengguna yang sudah login hanya bisa mengakses halaman atau fitur tertentu menggunakan izin (permissions) dan dekorator seperti @login_required. Dengan begitu, setelah pengguna berhasil login, Django memutuskan apa yang boleh dan tidak boleh mereka lakukan berdasarkan aturan izin yang ada.

### IV. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Django mengingat pengguna yang telah login dengan menggunakan session yang disimpan di server dan dihubungkan dengan cookies yang disimpan di browser pengguna. Saat pengguna login, Django akan membuat session ID yang unik dan menyimpannya di cookie pada browser miliki pengguna. Setiap pengguna mengakses halaman aplikasi, cookie akan dikirim ke server sehingga Django dapat mengenali pengguna tersebut tanpa melakukan login ulang.
- Selain mengingat pengguna yang telah login, cookies juga berguna untuk penyimpanan preferensi pengguna seperti bahasa, theme dan tampilan aplikasi, dan berbagai pengaturan lainnya sehingga pengguna tidak perlu mengaturnya lagi setiap kali membuka suatu aplikasi. Cookies juga berguna untuk melacar aktivitas pengguna di situs web seperti halaman apa yang dikunjungi terlebih untuk keperluan analisis ataupun personalisasi iklan yang ditampilkan.
- Tentunya tidak semua cookies aman untuk digunakan. Cookies dapat rentan terhadap serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF) jika tidak dikonfigurasi dengan baik. Untuk meningkatkan keamanan, Django mendukung penggunaan secure cookies (hanya dikirim melalui HTTPS), HttpOnly cookies (tidak dapat diakses melalui JavaScript), dan CSRF protection untuk mencegah serangan berbahaya yang menargetkan sesi pengguna.

### V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
#### a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Untuk mengimplementasikan fungsi registrasi, saya membuat function register pada file views.py, fungsi ini akan menghasilkan formulir registrasi dan mengashilkan akun pengguna baru. Untuk memastikan fungsi ini bisa terlihat pada aplikasi, saya membuat file register.html yang berisi code yang akan mengasilkan form pada website. Lalu, saya membuat fungsi login dengan menambahkan function login_user pada views.py dan membuat file html baru bernama login html pada direktori main/templates. Setelah itu, saya membuat fungsi logout dengan menambahkan function logout pada views.py dan menambahkan button dan hyperlink pada main.html di direktori main/templates yang jika ditekan, akan mengarahkan user untuk keluar dari akunnya. Setelah membuat ketiga fungsi tersebut, saya melakukan routing dengan mengimport functions tersebut dan menambahkan path ke masing-masing function pada list urlpatterns yang terletak pada file urls.py pada aplikasi main. Agar halaman hanya bisa dibuka oleh pengguna yang sudah login, saya menambahkan dekorator @login_required(login_url='/login') di atas fungsi show_main pada views.py dengan tidak lupa untuk mengimport fungsi pendukungnya.

#### b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Saya menjalankan aplikasi dengan memanggil command 'python manage.py runserver' pada terminal dengan virtual environment yang sudah aktif. Lalu, saya membuka http://localhost:8000/ yang akan mengarahkan saya ke website saya yang dibuka secara lokal. Saya pun melakukan registrasi untuk 2 akun pengguna dan melakukan login dengan data yang saya registrasikan. Setelah login, saya menambahkan 3 dummy data untuk satu pengguna. Saya logout lalu login lagi dengan credentials pengguna satunya dan membuat 3 dummy data juga.

#### c. Menghubungkan model Product dengan User.
Untuk menghubungnkan model Product dengan User, pada models.py saya menambahkan import User dari django.contrib.auth.models dan menambahkan atribut user = models.ForeignKey(User, on_delete=models.CASCADE) pada class ProductEntry. Atribut ini menandakan bahwa setiap instance dari class ProductEntry terasosiasi dengan satu user. Pada file views.py, saya mengubah potongan kode pada function create_product_entry yaitu dengan menambahkan product_entry.user = request.user yang akan mengisi atribut product_entry.user dengan hasil return request.user yang akan mengembalikan user yang sedang login sehingga pada saat menambahkan product, user yang sedang login akan tersimpan di product tersebut. 

#### d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Untuk menampilkan informasi username yang sedang login, pada func show_main di file views.py, value dari 'name' pada dictionary context yang tadinya didefinisikan sebagai string statis, sekarang diubah menjadi request.user.username sehingga akan menampilkan username dari pengguna yang sedang login. Untuk menerapkan cookies last login pada halaman utama aplikasi, pada dictionary context juga ditambahkan keypair baru berupa 'last_login': request.COOKIES['last_login'] sehingga data last_login disimpan dan menambahkan <h5>Sesi terakhir login: {{ last_login }}</h5> pada main.html agar last_login bisa ditampilkan di halaman utama aplikasi.

<br>
<br>

# Tugas 5
## Pertanyaan:
### I. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika untuk suatu elemen HTML terdapat beberapa CSS selector, urutan prioritas pengambilan CSS selector tersebut dari yang tertinggi hingga yang terendah adalah sebagai berikut:
- !important: jika terdapat CSS selector ini, CSS selector lain akan diabaikan dan pasti CSS selector ini yang didahulukan.
- Inline styles: jika style langsung ditulis di atribut style pada elemen HTML, selector ini lah yang akan dijalankan. contoh: '<p style="color: red;">Teks berwarna merah</p>'
- ID selector: selector ini ditulis dengan menggunakan tanda pagar diikuti oleh id elemen HTML yang ingin dipilih. Contoh:
pada css:
'#judul {
  color: blue;
}'
pada html:
'<h1 id="judul">judul ini biru</h1>'
- Class, Pseudo-class, dan Attribute Selector: selector class ditandai dengan tanda titik (.), pseudo-class ditandai dengan titik dua (:), dan attribute ditandai dengan tanda kurung siku berisi atributnya ([atribut=""]). Contoh:
pada css:
'.teks-hijau {
  color: green;
}
p:hover {
  color: orange;
}'
pada html:
'<p class="teks-hijau">teks hijau jadi orange kalau hover</p>'
- Tag/element selector: Selector tag memiliki prioritas yang paling rendah. Selector ini mempengaruhi semua elemen dengan tag yang ditentukan (kecuali yang sudah diatur oleh selector lain). Contoh:
pada css:
'p{
    color: yellow;
}'
pada html:
'<p>p kuning</p>'

### II. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena konsep ini memungkinkan website ataupun aplikasi yang dikembangkan dapat diakses melalui berbagai aplikasi tanpa mengganggu tampilan ataupun fungsionalitasnya. Responsive design memastikan bahwa pengguna bisa melihat tampilan yang optimal dari segi layout ataupun aksesibilitas tanpa harus membuat versi terpisah untuk setiap perangkat. Contoh aplikasi website yang menerapkan responsive design adalah [Canva](https://www.canva.com/) dan [YouTube](https://www.youtube.com/). Contoh aplikasi website yang belum menerapkan responsive design adalah [siasisten](https://siasisten.cs.ui.ac.id/) 

### III. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding adalah 3 elemen yang digunakan untuk mengatur jarak dan tata letak elemen-elemen HTML pada suatu web. 
- Margin adalah ruang di luar elemen, yaitu ruang antara suatu elemen dengan elemen lain di sekitarnya; margin mengatur jarak antarelemen. Margin tidak dapat terlihat di web. Untuk pengimplementasiannya, kita dapat mengatur ketebalan per sisinya. 
- Border adalah garis pembatas yang mengelilingi elemen dan berada di antara margin & padding. Border dapat terlihat secara visual dan mempengaruhi ukuran elemen. Untuk pengimplementasiannya, kita dapat mengatur lebar, jenis, dan warnanya.
- Padding adalah ruang di dalam elemen, antara isi dari elemen dan border. Padding memberikan jarak antara isi dan border elemen. Padding tidak terlihat, tetapi mempengaruhi ukuran dari elemen. Untuk pengimplementasiannya, kita dapat mengatur ketebalan per sisinya.

### IV. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid Layout adalah dua metode dalam CSS untuk mengatur tata letak elemen di halaman web. Flexbox cocok untuk menyusun elemen dalam satu dimensi, baik baris atau kolom, seperti menu navigasi atau daftar gambar. Sedangkan Grid Layout lebih cocok untuk tata letak yang lebih kompleks karena bisa mengatur elemen dalam dua dimensi (baris dan kolom), misalnya untuk layout halaman web dengan banyak bagian.

Secara sederhana, Flexbox dipakai kalau dibutuhkan fleksibilitas dalam menyusun elemen secara horizontal atau vertikal, sedangkan Grid lebih cocok kalau dibutuhkan kontrol penuh dalam menempatkan elemen di tempat spesifik dalam tata letak yang lebih besar.

### V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### a. Implementasikan fungsi untuk menghapus dan mengedit product.
Untuk mengimplementasikan kedua fungsi tersebut, saya membuat 2 fungsi baru di views.py pada subdirektori main, yaitu fungsi edit_product dan delete_product. Saya mengimport kedua fungsi tersebut pada file urls.py pada direktori main lalu menambahkan path url pada list urlpatterns. Saya juga menambahkan tombol untuk masing-masing fungsi tersebut pada main.html saya.

#### b. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya
Pertama-tama saya membuat base.html pada direktori root yang akan diextend oleh semua pages di website saya.
- Kustomisasi halaman login, register, dan tambah product: saya mengkustomisasi masing-masing halaman website saya dengan menggunakan tailwing agar lebih menarik. Pada semua halaman, saya meng-extend base.html dan meng-include navbar.html
- Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card.: Saya menggunakan conditional pada main.html sehingga dapat memenuhi kriteria tersebut. Saya menambahkan sebuah gambar kucing yang akan ditampilkan jika belum ada product yang dimasukkan. Untuk kondisi di mana sudah ada product yang dimasukkan, saya melakukan loop terhadap list product_entries sehingga untuk masing-masing product_entry pada product_entries, terdapat card yang menampilkan informasi product tersebut. Saya juga membuat card_product.html yang menjadi tampilan card tersebut.
- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!: saya menambahkan 2 button, yaitu 1 untuk mengedit dan 1 untuk menghapus product saya. Button ini mengandung hyperlink yang jika ditekan akan mengarahkan pengguna ke halaman edit dan delete product.
- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.: Saya membuat navbar dengan menggunakan tailwind, lalu meng-include navbar saya pada semua halaman website saya.

# Tugas 6
## Pertanyaan:
### I. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Dalam pengembangan aplikasi web, penggunaan JavaScript memberikan beberapa manfaat, beberapa di antaranya adalah interaktivitas, peningkatan kualitas pengalaman pengguna, dan pengolahan data di sisi klien.
1. Interaktivitas yang dinamis: Javascript memungkinkan pembuatan halaman web yang interaktif dan juga responsif. Contohnya adalah pengguna dapat berinteraksi dengan elemen-elemen di web tanpa melakukan refresh setiap kalinya. Dengan menggunakan fitur AJAX, data dapat diperbarui secara asinkron
2. Pengalaman pengguna yang lebih baik: Javascript memungkinkan berbagai fitur untuk ditambahkan ke web kita, misalnua fitur validasi form langsung di browser, animasi, ataupun notifikasi secara real-time yang akan meningkatkan kualitas pengalaman pengguna.
3. Pengolahan data di sisi klien: JavaScript memungkinkan pengolahan data di sisi klien, sehingga bisa mengurangi beban server dan mempercepat respons, karena banyak operasi dilakukan di browser pengguna tanpa harus selalu berkomunikasi dengan server.

### II. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi await saat menggunakan fetch() adalah untuk menunggu hasil dari operasi asynchronous, seperti pengambilan data dari server, sebelum melanjutkan eksekusi kode. fetch() sendiri mengembalikan sebuah Promise, yang artinya hasilnya tidak langsung tersedia. Dengan await, JavaScript akan menunggu sampai Promise tersebut terselesaikan (resolved) dan mendapatkan hasilnya yang dapat berupa data ataupun error.

Jika kita tidak menggunakan await, maka JavaScript tidak akan menunggu hasil dari fetch(). Sebaliknya, kode berikutnya akan langsung dieksekusi sebelum data dari server benar-benar diterima. Akibatnya, kita mungkin bekerja dengan data yang belum tersedia, atau mengakses response dari fetch() yang masih berupa Promise, yang bisa menyebabkan kesalahan atau hasil yang tidak diinginkan.

### III. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Penggunaan decorator @csrf_exempt pada view yang digunakan untuk AJAX POST penting karena memungkinkan kita untuk melewati pemeriksaan token CSRF yang biasanya diperlukan dalam permintaan POST. Ini memudahkan pengembangan aplikasi web, terutama saat melakukan pengujian dan integrasi dengan front-end. Walaupun telah menggunakan @csrf_exempt, tetap penting untuk memastikan keamanan view dengan cara lain, yaitu memvalidasi input dengan menggunakan autentikasi yang tepat.

### IV. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna dilakukan di backend untuk alasan keamanan, karena pengguna dapat mengubah script di frontend sehingga validasi di sisi klien tidak dapat diandalkan. Dengan melakukan pembersihan data di backend, kita memastikan bahwa semua data yang diterima aman sebelum diproses. Selain itu, pembersihan di backend menjaga konsistensi data dari berbagai sumber dan mencegah masalah kedepannya, seperti kesalahan saat menyimpan data.

### V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### a. AJAX GET
**Ubahlah kode cards data product agar dapat mendukung AJAX GET:** Untuk melakukan hal ini, saya menghapus block kondisional yang menampilkan card_product yang kosong ataupun tidak. Sebagai penggantinya, saya menambahkan fungsi asynchronous getProductEntries() dan refreshProductEntries() pada bagian script dan memanggil fungsi tersebut. 

**Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in:** Untuk melakukan hal ini, saya mengubah baris pertama pada fungsi show_json dan show_xml sehingga menjadi `data = MoodEntry.objects.filter(user=request.user)`. Fungsi `show_json` akan dipanggil pada fungsi asynchronous getMoodEntries() sehingga dapat dipastikan bahwa data yang diambil hanyalah data milik pengguna yang sedang log in
#### b. AJAX POST
**Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood:** Untuk melakukan hal ini, saya menambahkan bagian code yang akan menampilkan form untuk menambah product baru. Saya juga menambahkan tombol untuk menambahkan product pada main yang jika ditekan akan mengarah ke form pembuatan product baru. Jika sudah selesai memasukkan data product baru, pengguna dapat memilih untuk menyimpan ataupun meng-cancel penambahan product baru. Pada bagian script, saya menambahkan bagian untuk mengatur modal tersebut. 

**Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data:** Untuk melakukan hal ini, saya menambahkan fungsi `add_product_entry_ajax` yang akan menambahkan sebuah product baru berdasarkan data yang dimasukkan saat pemanggilan modal.

**Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat:** Di berkas urls.py, saya meng-import fungsi `add_product_entry_ajax` dari views.py. Lalu, pada list path yang ada pada urls.py, saya menambahkan path yang mengarahkan ke fungsi tersebut.

**Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/:** Pada bagian script main.html saya membuat fungsi addProductEntry() yang terhubung dengan path itu.

**Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan:** Saya membuat fungsi asynchronous refreshProductEntries() pada bagian script sehingga web akan refresh main page tanpa perlu dilakukan reload.