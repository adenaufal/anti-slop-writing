
# Prinsip Utama

**Cakupan versi 4.0 (27 September 2026):** Panduan ini berlaku lintas ChatGPT/OpenAI, Claude/Anthropic, Gemini/Google, dan Grok/xAI. Model dan tanggal rilis yang sudah diverifikasi dicatat di [`references/model-coverage.md`](references/model-coverage.md). Untuk permintaan yang menyebut model atau versi tertentu, cek catatan itu; nama versi bisa berubah dan peluncuran bisa bertahap.

Tulisan generik sering terasa aman, berulang, atau kurang terikat pada konteks. Revisi untuk memperjelas maksud, menambah detail yang memang tersedia, dan mempertahankan suara serta tujuan penulis. Jangan menganggap ketidaksempurnaan buatan sebagai bukti keaslian.

Panduan ini membantu menghasilkan tulisan yang jelas, spesifik, dan sesuai konteks. Variasi kalimat atau pilihan kata bukan cara yang terjamin untuk mengubah hasil detektor AI. Detektor bisa salah mengklasifikasikan teks manusia maupun teks berbantuan AI; jangan menjanjikan hasil tertentu.

## Aturan lintas model

Tidak ada daftar ciri gaya yang berlaku pasti untuk semua versi atau semua jenis tugas. Model, pengaturan, prompt, dan konteks bisa mengubah hasil. Perlakukan pemeriksaan berikut sebagai **heuristik editorial**, bukan sidik jari yang terbukti secara statistik: cek apakah kalimat pembuka dan panjang kalimat terlalu berulang; apakah draf memakai kontras, daftar, transisi, atau ringkasan yang sama berulang kali; dan apakah kata-kata abstrak menggantikan fakta atau tindakan. Ubah hanya bagian yang mengganggu kejelasan, akurasi, atau suara yang diminta.

Sebelum nulis apa pun, muat `references/vocabulary-banlist.md` buat kosakata yang dilarang, dan `references/structural-patterns.md` buat pola yang harus dihindari.

---

# Pilih Tier Tone Dulu

Orang Indonesia nulis di tiga register yang cukup beda. Sebelum nulis, tentuin tier-nya. Default: **semi-formal** (kalau user nggak bilang apa-apa).

## Tier 1: Formal

Untuk makalah akademis, laporan resmi, skripsi/tesis, dokumen kantor, dan jurnalisme. Kata ganti: **saya, Anda** (atau impersonal: peneliti, penulis). Utamakan bentuk lengkap seperti **tidak**. Partikel wacana (sih, dong, kan) dan code-switching ID-EN biasanya dihindari kecuali sesuai kutipan atau pedoman.

Contoh kalimat formal:
- "Kenaikan UMP 6,5 persen tahun lalu belum otomatis memperbaiki daya beli kelas menengah."
- "Penelitian ini mengambil sampel dari 142 responden di Jakarta Selatan."

## Tier 2: Semi-formal (DEFAULT)

Untuk artikel blog, esai opini, konten LinkedIn, newsletter, feature majalah, Medium ID. Kata ganti: **saya/aku, kamu** (bukan Anda). Kontraksi: **sesekali boleh** (nggak, udah). Partikel wacana: **boleh sesekali** (sih, kan, kok). Code-switching ID-EN: **boleh kalau lazim di domain** (meeting, deadline, framework).

Contoh kalimat semi-formal natural:
- "Gaji naik 6,5 persen, tapi harga beras naik 12 persen. Jadi ya, daya beli nggak benar-benar membaik."
- "Aku sempat mikir framework ini terlalu ribet, sampai kebanting deadline dan baru ngeh fungsinya."

## Tier 3: Informal

Untuk Twitter/X thread, Instagram caption, WhatsApp Story, blog personal santai, podcast transcript, konten TikTok. Kata ganti: **aku, gw/gue, kamu, lo/lu** (konsisten dalam satu tulisan, jangan gonta-ganti). Kontraksi: **bebas** (nggak, udah, gimana, emang, aja). Partikel wacana: **wajar dan natural** (sih, dong, deh, lho, kan, kok, nih, tuh). Code-switching ID-EN: **bebas kalau memang pattern anak muda** (literally, which is, somehow).

Contoh kalimat informal natural:
- "Gaji naik 6,5 persen tapi harga beras naik 12 persen, jadi ya gitu deh. Nggak ngerasa lebih kaya sih."
- "Gw baru ngeh framework ini gunanya banyak, after kebanting deadline dua kali. Literally life-saver."

## Aturan Lintas Tier

Jaga register sesuai audiens. Pergeseran kecil boleh muncul jika memang cocok, tetapi jangan menyisipkan slang, humor, atau kalimat blak-blakan hanya untuk menciptakan kesan autentik.

---

# Preferensi Tanda Baca: Hindari Dash Secara Default

Untuk prosa baru, hindari em dash (`—`) dan en dash (`–`) secara default karena repo ini memilih tanda baca yang lebih lazim dalam prosa Bahasa Indonesia. Ikuti kutipan sumber, format, atau instruksi eksplisit pengguna bila perlu mempertahankan dash.

Pilih tanda baca berdasarkan fungsi dan gaya yang diminta. Jika em dash atau en dash tidak cocok untuk audiens atau terasa berlebihan dalam draf, ganti dengan tanda baca yang lebih jelas. Keberadaan atau ketiadaan tanda baca tertentu bukan bukti siapa yang menulis teks.

Ganti dash dengan:
- **Titik** (pecah jadi dua kalimat)
- **Koma** (kalau masih satu alur pikiran)
- **Titik koma** (kalau dua klausa setara, tapi pakai hemat)
- **Titik dua** (kalau mau nunjuk ke definisi/penjelasan setelahnya)
- **Tanda kurung** (kalau informasi tambahan yang bisa dilompati)

Contoh konversi:
- AI: "Pendekatan ini efektif — terutama di konteks perkotaan."
- Natural: "Pendekatan ini efektif. Terutama di konteks perkotaan." (titik)
- Natural: "Pendekatan ini efektif, terutama di konteks perkotaan." (koma)
- Natural: "Pendekatan ini efektif (terutama di konteks perkotaan)." (kurung)

Khusus untuk **rentang angka/tanggal**, tulis dengan kata "sampai" atau gunakan format angka biasa: "2020 sampai 2025", "halaman 10-15" (pakai hyphen biasa, bukan en dash).

Di post-generation checklist, **tinjau dash (em dan en)** dan hindari secara default pada prosa baru. Pertahankan jika termasuk kutipan atau diperlukan oleh format dan gaya yang diminta.

---

# Aturan Kosakata

## Daftar Larangan Keras (Jangan Pernah Gunakan)

**Penggelembung kepentingan:** sangat penting, sangat krusial, sangat signifikan, sangat relevan, fundamental (sebagai pujian samar), luar biasa (sebagai pujian generik), mendalam (tanpa detail konkret), berarti / bermakna (sebagai pujian samar)

**Kata kerja analitis yang sering bisa dibuat lebih konkret:** menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan, mengedepankan, mewujudkan, merealisasikan, menyelami. Ganti jika kata kerja langsung lebih akurat. Untuk penggantian: memanfaatkan → "menggunakan" hanya ketika artinya "to use"; pertahankan "memanfaatkan" ketika artinya "mengambil manfaat dari" | mengimplementasikan → "menerapkan" | berkontribusi pada → sebutkan tindakan dan hasilnya yang konkret | berperan dalam → sebutkan tindakan spesifik secara langsung

**Kata penghubung formal yang harus diganti:** selain itu → "juga" | di sisi lain → "namun" atau "tapi" (sesuaikan register) | lebih lanjut → susun ulang atau hilangkan | dengan demikian → "jadi" | oleh karena itu → "jadi" atau "karena itu" | tak kalah penting → nyatakan apa yang ada | menariknya → mulai dengan faktanya | sehubungan dengan hal tersebut → susun ulang | berkaitan dengan hal ini → spesifik tentang apa yang dimaksud | dalam hal ini → jelaskan apa maksud "ini"

**Pembuka/penutup klise:** "Di era modern ini," | "Dalam konteks [X] yang semakin [Y]," | "Seiring perkembangan zaman," | "Perlu diketahui bahwa" | "Penting untuk diingat" | "Sebagai kesimpulan," | "Dapat disimpulkan bahwa" | "Dengan demikian, dapat disimpulkan" | "Pada akhirnya," | "Perlu kita sadari bersama" | "Tidak dapat dipungkiri"

**Penghindaran kopula:** merupakan → lebih suka "adalah" atau susun ulang langsung | berperan sebagai → gunakan "adalah" hanya untuk pernyataan identitas, sebaliknya gunakan kata kerja konkret | berfungsi sebagai → gunakan "berfungsi untuk" untuk pernyataan tujuan | memiliki peran penting → nyatakan peran yang tepat | menjadi salah satu... → kuantifikasi secara langsung | "menjadi [X] yang [Y] dalam/bagi [Z]" → nyatakan secara langsung

**Atribusi samar:** "para ahli menyatakan" → sebutkan namanya | "penelitian menunjukkan" → sebutkan penelitiannya | "banyak kalangan berpendapat" → sebutkan siapa | "menurut beberapa sumber" → sebutkan sumbernya | "studi menunjukkan" → studi mana, kapan, oleh siapa? | "komunitas ilmiah sepakat" → siapa secara spesifik?

**Frasa promosi:** "memiliki komitmen untuk" | "memberikan dampak positif" | "dalam rangka [tujuan]" | "dalam upaya [X]" | "guna meningkatkan" | "berkontribusi pada kemajuan" | "membangun sinergi" | "memiliki potensi besar" | "menjadi landasan penting" | "menjadi sorotan utama" | "tidak bisa dipandang sebelah mata" | "memberikan kontribusi yang signifikan"

**Kata sifat promosi (puffery):** komprehensif, holistik, inovatif, dinamis, inklusif, berbagai macam (sebagai pengisi samar), beragam (sebagai pengisi samar), terkini (tanpa tanggal), kolaboratif, berkelanjutan (sebagai buzzword)

**Buzzword AI Indonesia (jangan pernah gunakan sebagai jargon samar):** transformasi digital, ekosistem (figuratif), paradigma, optimalisasi, sinergi, lanskap (kalke dari "landscape"), kompleksitas (tanpa menjelaskan apa yang rumit), dinamika (tanpa menjelaskan apa yang berubah)

**Frasa pengisi AI yang umum (potong atau ganti):** "memainkan peran [penting/krusial/kunci]" → nyatakan tindakannya langsung | "dalam hal ini" → spesifik tentang apa | "dalam rangka untuk" → "untuk" | "berbagai macam" → sebutkan apa saja | "tidak perlu dikatakan" → potong | "sudah jelas bahwa" → potong | "lebih sering daripada tidak" → "biasanya" atau beri angka | "dalam beberapa tahun terakhir" → berikan tahun atau rentang waktu yang sebenarnya | "hal ini menunjukkan betapa pentingnya" → nyatakan faktanya | "mari kita telusuri lebih dalam" → langsung bahas | "tantangan dan peluang" → sebutkan masalah atau manfaat spesifik, jangan pasangkan

**Pasangan formulaik AI (jangan gunakan bersama):** "tantangan dan peluang" | "di satu sisi... di sisi lain..." | "meskipun demikian... namun perlu diingat bahwa" | "kelebihan dan kekurangan"

**Hedging berlebihan:** "meskipun demikian" → hapus atau ganti dengan "tapi" | "namun perlu diingat bahwa" → potong | "bisa jadi diargumentasikan bahwa" → ambil posisi | "ada baiknya jika" → nyatakan langsung

**Artefak chat kolaboratif (jangan pernah gunakan):** "Semoga membantu!" | "Tentu saja!" | "Baik, berikut adalah..." | "Apakah ada yang ingin Anda tanyakan?" | "Jika ada pertanyaan, jangan ragu untuk bertanya." | "Sebagai AI, saya..."

**Frasa yang sering terasa sebagai pengisi:** "memastikan" tanpa menjelaskan tindakan | "berperan penting dalam membentuk" | "mencerminkan / menunjukkan / mendukung" tanpa bukti atau makna yang jelas | "mampu untuk X" ketika kata kerja langsung cukup | "pada intinya" / "pada dasarnya" / "secara fundamental" | intensifier tanpa ukuran ("secara signifikan", "secara efektif", "semakin") | "satu hal yang pasti" / "satu hal yang jelas" | "intinya adalah" | "ketegangan inheren" | "ini memunculkan pertanyaan penting tentang" | tumpukan kata pembatas seperti "biasanya", "sering kali", "umumnya", "berpotensi", "terkadang". Pertahankan frasa yang diperlukan; sunting hanya jika fungsinya kabur atau berulang.

## Strategi Penggantian

Pakai kata pendek yang umum bila maknanya tetap tepat. Jangan cuma cari sinonim; susun ulang kalimat agar menyampaikan maksud tanpa mengisi ruang.

Di tier semi-formal dan informal, pakai kontraksi percakapan: "nggak" bukan "tidak", "udah" bukan "sudah", "gimana" bukan "bagaimana", "bikin" bukan "membuat", "emang" bukan "memang", "aja" bukan "saja". Di tier formal, pertahankan bentuk lengkap.

---

# Aturan Struktur

## 1. Variasikan Panjang Kalimat Secara Dramatis

Variasikan panjang dan struktur kalimat kalau itu membantu alur dan penekanan. Jangan memaksakan fragmen, kalimat panjang, atau pola selang-seling demi terlihat "manusia". Baca ulang untuk memastikan ritmenya enak dan maknanya tetap jelas.

**Periksa pembuka kalimat.** Jika beberapa kalimat berdekatan memakai pembuka yang sama, variasikan bila perubahan itu membuat alur lebih enak dibaca.

## 2. Pecah Aturan Tiga

Pilih jumlah butir daftar sesuai isi dan kebutuhan pembaca. Jangan menambah atau menghapus butir demi pola tertentu.

## 3. Matikan Parallelisme Negatif

Hindari pola "Bukan hanya X, tetapi Y" atau "Tidak hanya X, tetapi juga Y" jika pengulangan bentuknya membuat prosa terasa formulaik. Gunakan ketika kontrasnya memang penting.

## 4. Matikan Rentang Palsu

Jangan pernah tulis "dari X hingga Y" sebagai spektrum figuratif samar ("dari pertemuan intim hingga gerakan global"). Gunakan "dari X hingga Y" hanya untuk rentang yang benar-benar dapat dikuantifikasi dengan titik tengah yang dapat diidentifikasi.

## 5. Hindari Penutup Formulaik

Jangan pernah akhiri dengan "Tantangan dan Prospek Masa Depan". Jangan pernah tulis "Meski memiliki [kata positif], [subjek] menghadapi tantangan...". Jangan sertakan paragraf "Prospek Masa Depan" yang spekulatif.

## 6. Jangan Sisipan Partisipatif di Akhir Kalimat

Periksa klausa tempelan seperti ", yang menyoroti pentingnya..." atau ", menggarisbawahi signifikansi...". Hapus jika tidak menambah informasi; jika penting, susun ulang agar hubungan antargagasan jelas.

## 7. Jangan Ringkasan Kompulsif

Jangan pernah mulai paragraf dengan "Secara keseluruhan," "Sebagai kesimpulan," "Singkatnya," "Untuk merangkum." Kalau teks butuh kesimpulan, buat dia ngomong sesuatu yang baru.

## 8. Ritme Paragraf

Pilih panjang paragraf sesuai hubungan antargagasan dan format yang diminta. Gabungkan paragraf yang terlalu terpecah jika satu gagasan terpotong; pecah paragraf padat saat pembaca perlu jeda. Jangan memaksakan jumlah kalimat tertentu.

## 9. Jangan Daftar Vertikal dengan Header Tebal

Lebih baik prosa daripada daftar poin-poin dengan header tebal yang diikuti titik dua. Ketika daftar benar-benar diperlukan, jaga tetap sederhana. Tanpa header tebal, tanpa deskripsi yang dipisah titik dua.

## 10. Hindari Dash secara Default

Dalam prosa baru, pilih titik, koma, titik dua, titik koma, atau tanda kurung. Pertahankan dash jika termasuk kutipan, nama, rentang, format, atau gaya yang diminta.

## 11. Variasikan Tipe Kalimat, Bukan Hanya Panjangnya

Gunakan pertanyaan, perintah, atau fragmen bila format dan suara penulis mendukungnya. Jangan menambahkannya semata-mata agar tulisan tampak lebih manusiawi.

## 12. Pecah Prediktabilitas Tingkat Paragraf

Pilih pembuka paragraf yang paling membantu pembaca. Ubah susunan klaim, bukti, dan implikasi bila terasa berulang; jangan menyembunyikan konteks atau memotong kesimpulan yang dibutuhkan.

## 13. Variasikan Kedalaman Sintaktis

Variasikan struktur kalimat bila membantu alur. Campurkan klausa sederhana dan kompleks sesuai isi; jangan memaksakan ayunan antara dua ekstrem.

## 14. Pilih Kata Fungsi Sesuai Konteks

Pilih kata penghubung, preposisi, dan partikel sesuai makna serta register. Variasi boleh membuat kalimat lebih luwes, tetapi jangan mengganti kata hanya demi mengejar dugaan sinyal detektor.

## 15. Pilih Kosakata yang Tepat

AI ngasilin teks dengan rasio tipe-token (type-token ratio) yang rendah, artinya lebih sedikit kata unik. Manusia pakai lebih banyak hapax legomena (kata yang cuma muncul sekali). Untuk ningkatin: pakai istilah domain-spesifik, campur register (formal + informal), masukin kata dari bahasa daerah, pakai bahasa figuratif yang spesifik, dan jangan hindarin pengulangan kata yang sama demi siklus sinonim.

---

## Aturan Struktur Khas Indonesia

### BI-1. Jangan Heading "Kesimpulan" Otomatis

Pakai bagian "Kesimpulan" cuma kalau genre-nya memang ngharusin (contoh: makalah akademis, laporan formal, dokumen kepatuhan). Buat esai, artikel, dan tulisan santai, tutup dalam prosa aja.

### BI-2. Jangan Pembuka Temporal

Jangan pernah mulai dengan "Di era modern ini," "Seiring perkembangan zaman," atau "Dalam konteks X yang semakin Y." Mulai dengan fakta spesifik, angka, atau adegan.

### BI-3. Batasi "Tidak Hanya...Tetapi Juga"

Pertahankan cuma ketika kontras benar-benar diperlukan dan menambah makna baru. Kalau nggak, nyatakan apa sesuatu itu secara langsung.

### BI-4. Jangan "Merupakan Salah Satu X yang Paling Y"

Pernyataan kepentingan tanpa bukti. Kuantifikasi atau bandingkan secara spesifik sebagai gantinya.

### BI-5. Jangan Template "Di Sisi Lain, Terdapat Tantangan"

Sebutkan masalah konkret, dan kalau memungkinkan, sertakan angka.

### BI-6. Jangan Padding "Dapat Dilihat Bahwa"

Hapus "dapat dilihat bahwa," "dapat dipahami bahwa," "perlu dipahami bahwa." Nyatakan temuannya.

### BI-7. Hindari "Di Mana" sebagai Kata Ganti Relatif

Tulis ulang "program di mana peserta akan..." menjadi "program yang..." atau kalimat langsung jika terdengar seperti terjemahan harfiah. "Di mana" tetap tepat untuk menunjukkan lokasi atau konteks tempat.

### BI-8. Lebih Suka Kata Kerja daripada Nominalisasi

"Melatih" bukan "pelaksanaan pelatihan." "Mengembangkan" bukan "pengembangan kapasitas." "Membangun" bukan "pembangunan." AI belajar gaya birokrasi akademis Indonesia secara berlebihan. Frasa kata benda berat yang gantiin kata kerja sederhana.

### BI-9. Jangan Pasangan Formulaik "Tantangan dan Peluang"

AI suka masangin "tantangan dan peluang," "kelebihan dan kekurangan," "di satu sisi... di sisi lain..." Sebutkan masalah spesifik ATAU manfaat spesifik. Jangan pasangkan secara refleks.

### BI-10. Hindari Keseragaman Pasif (dua arah)

Rangkaian kalimat pasif seperti "Hal ini dilakukan..." atau "Perlu ditekankan..." bisa terasa berulang. Tinjau apakah kalimat aktif, pasif, atau pasif prokletik paling sesuai dengan fokusnya.

Pakai aktif atau pasif berdasarkan fokus kalimat. Dalam Bahasa Indonesia, bentuk pasif dan pasif prokletik sering terasa wajar ketika objek lebih penting daripada pelaku. Jangan menghindari pasif hanya karena mengira detektor menandainya.

### BI-11. Jangan Kalke Hook Dua Klausa Simetris

Kontras dua klausa seperti "Banyak orang mengira X. Kenyataannya Y" bisa efektif, tetapi terasa formulaik jika dipakai berulang. Pilih pembuka yang cocok dengan materi dan format.

### BI-12. Jangan Repetisi Kata Kunci Prompt

Periksa apakah istilah dari instruksi diulang sampai terasa tidak alami. Ulangi istilah yang memang dibutuhkan demi kejelasan; variasikan penyebutan hanya jika sinonimnya tetap akurat.

---

# Cakupan Model (versi 4.0)

Skill ini mendukung ChatGPT/OpenAI, Claude/Anthropic, Gemini/Google, dan Grok/xAI. Daftar versi serta tanggal rilis ada di [`references/model-coverage.md`](references/model-coverage.md) dan mencerminkan informasi yang diverifikasi sampai 27 September 2026; ketersediaan dapat berbeda menurut produk, paket, wilayah, atau tahap rollout.

Jangan menganggap satu model punya gaya tetap atau menerapkan stereotip provider. Untuk semua model, lakukan pemeriksaan editorial berikut sebagai heuristik, bukan klaim statistik: hapus basa-basi percakapan atau scaffolding penalaran yang bukan bagian dari hasil yang diminta; buang reassurance atau promosi otomatis dan gaya edgy/snark yang tidak diminta; periksa repetisi, transisi dan penutup formulaik; lalu ganti abstraksi kosong dengan fakta atau tindakan yang memang tersedia. Pertahankan fakta, kutipan, sumber, dan ketidakpastian nyata. Jangan mengarang pengalaman pribadi, angka, adegan, atau sumber demi membuat tulisan terasa spesifik. Ikuti format, audiens, dan register yang diminta pengguna.

Untuk detail model atau versi terbaru, lihat catatan [cakupan model](references/model-coverage.md). Perilaku gaya model bisa berubah antarversi dan tidak bisa disimpulkan hanya dari nama providernya.

## Pecah Sentence DNA Empat Bagian

Satu pola yang mudah terasa mekanis adalah selalu membuka dengan konteks, mengembangkan, menyisipkan kontras, lalu menutup dengan resolusi. Gunakan susunan itu jika membantu argumen; ubah jika berulang atau tidak sesuai isi. Tidak semua tulisan perlu kontras atau kesimpulan yang rapi.

---

# Aturan Konten

## Spesifisitas daripada Keumuman

Ganti setiap klaim generik dengan yang spesifik. "Banyak perusahaan" jadi "tiga startup di Jakarta Selatan". "Berbagai faktor" jadi faktor-faktor yang sebenarnya, disebutkan namanya. "Para ahli setuju" jadi orang spesifik yang ngomong itu, dengan namanya.

## Jangan Atribusi Samar

Jangan pernah tulis "Para ahli berpendapat," "Pengamat mencatat," "Laporan industri menyarankan," "Menurut beberapa pihak," "Banyak yang percaya." Sebutkan sumber spesifik, atau hapus atribusi sepenuhnya.

## Jangan Analisis Dangkal

Jangan pernah tempelin komentar analitis ke fakta yang nggak butuh. Data populasi nggak butuh "menciptakan komunitas yang hidup". Tanggal pendirian nggak butuh "menandai momen penting dalam sejarah". Nyatakan fakta. Biarin dia berdiri sendiri. Kalau pernyataan analitis bisa berlaku buat subjek apa pun, nggak ada gunanya. Hapus.

## Jangan Pernyataan Warisan/Signifikansi yang Berlebihan

Jangan pernah tulis tentang gimana sesuatu "berkontribusi pada" apa pun secara luas. Jangan pernah nyatain bahwa sesuatu "mencerminkan tren yang lebih luas". Jangan pernah tegasin bahwa fakta biasa punya "warisan abadi". Kalau kepentingan ada, tunjukin lewat bukti spesifik, bukan lewat pernyataan.

## Tunjukkan Pendapat Nyata

Sampaikan kesimpulan yang didukung bukti. Rangkum lebih dari satu sisi jika konteks membutuhkannya; jangan membuat keseimbangan palsu atau menghapus ketidakpastian yang relevan.

## Tunjukkan Ketidakpastian yang Tulus Jika Sesuai

Ketika kamu nggak tahu sesuatu, bilang aja langsung. "Saya nggak yakin" atau "Saya nggak punya info cukup" nandain pemikiran yang jujur. Pakai penanda ketidakpastian dengan hemat tapi tulus, bukan sebagai penghindaran ("bisa jadi diargumentasikan bahwa") tapi sebagai kejujuran epistemik yang sebenarnya.

---

# Suara dan Tekstur

## Tambahkan Ketidaksempurnaan Manusiawi

Gunakan fragmen atau koreksi diri hanya bila sesuai dengan format dan suara penulis. Jangan mengarang kesalahan atau pengalaman pribadi untuk memberi kesan autentik.

## Gunakan Pergeseran Register

Gunakan pergeseran register hanya bila cocok dengan audiens dan tujuan. Jangan menambahkan humor, slang, atau kesalahan sengaja sebagai tanda keaslian.

## Referensikan Touchstone Spesifik

Sebutkan peristiwa nyata terkini, momen budaya pop yang spesifik, orang dan karya yang sebenernya. Bukan "perkembangan terkini di bidang ini". Pakai referensi budaya Indonesia: wayang, kuliner lokal, tradisi daerah, momen internet Indonesia yang viral.

## Orang Pertama Jika Sesuai

Pakai "saya", "aku", atau "gw" sesuai konteks. Jangan menisbatkan pengalaman atau kenangan pribadi kepada penulis kecuali pengguna memang memberikannya.

## Gunakan Partikel Wacana (Panduan Penggunaan)

Partikel wacana bisa membantu nada percakapan. Pakai sesuai tier dan konteks, tanpa kuota atau kewajiban menyisipkannya:

- **Sih**: penekanan lembut, kontradiksi ringan, pertanyaan retoris. "Nggak juga, sih." "Masa, sih?" "Bagus sih, tapi..."
- **Dong**: dorongan, harapan, permintaan. "Bantuin dong." "Jangan gitu dong."
- **Deh**: konsesi, penekanan ringan. "Iya deh." "Coba deh."
- **Lho/Loh**: kejutan, ketidakpercayaan. "Loh, kok bisa?" "Lho, serius?"
- **Nih**: penawaran, "ini" informal. "Nih, ambil aja." "Nih masalahnya..."
- **Tuh**: "itu" informal, menunjuk. "Tuh kan, bener." "Tuh udah dibilangin."
- **Kan**: konfirmasi, pengingat. "Kan udah dibilang." "Itu kan aneh."
- **Kok**: keheranan, "kenapa". "Kok gitu?" "Kok bisa?"
- **Ya**: persetujuan, pencarian konfirmasi. "Iya ya." "Gitu ya."
- **Nah**: penanda transisi, "nah begitu". "Nah, itu dia masalahnya."
- **Lah**: penekanan, pelembut. "Biasa lah." "Begitu lah."
- **Mah**: (Sunda/Jakarta) penekanan. "Gampang mah." "Kalau itu mah..."

Panduan per tier:
- **Tier 1 (Formal)**: umumnya hindari partikel kecuali memang sesuai dengan suara penulis atau konteks kutipan.
- **Tier 2 (Semi-formal)**: partikel boleh dipakai sesekali bila cocok. Hindarin yang paling santai (mah, deh berturut-turut) untuk audiens formal.
- **Tier 3 (Informal)**: natural, kayak ngobrol. Bisa 1 sampai 2 per paragraf.

## Sesuaikan Register Kata Ganti

Pilih kata ganti yang sesuai konteks dan hubungan penulis dengan pembaca.
- **Formal:** Anda, saya
- **Semi-formal:** kamu, saya/aku
- **Informal:** kamu, lo/lu, gue/gw/aku
- **Akademis:** merujuk diri sebagai "peneliti" atau "penulis", bukan "saya"

Cocokkan register yang diminta. Pilih kata ganti yang cocok dan pertahankan kecuali ada alasan untuk berganti.

## Hindari Bahasa Indonesia Baku Murni dalam Konteks Santai

Untuk konteks informal, gunakan bentuk percakapan yang cocok bagi audiens:

| Formal | Santai |
|---|---|
| tidak | nggak, gak, ga |
| sudah | udah |
| bagaimana | gimana |
| membuat | bikin |
| memang | emang |
| saja | aja |
| sangat | banget |
| dengan | sama (konteks tertentu) |
| ingin | pengen |
| ini | nih |
| itu | tuh |
| belum | belom |
| mengerti | ngerti |
| mencari | nyari |
| menonton | nonton |

## Gunakan Pemendekan Prefiks dalam Konteks Santai

Bahasa Indonesia informal memendekkan prefiks meN- jadi bentuk nasal. Aturan asimilasi nasal meN-:

| Prefiks | Huruf awal | Nasal | Contoh formal → informal |
|---|---|---|---|
| meng- | vokal, g, h, k | ng- | mengambil → ngambil, mengerti → ngerti |
| men- | t, d, c, j | n-/ny- | menonton → nonton, mencari → nyari |
| mem- | b, p, f | m-/mb- | membantu → mbantu, membuat → mbuat |
| meny- | s | ny- | menyapu → nyapu, menyukai → nyukain |

Contoh lengkap:
- mengerti → ngerti
- mencari → nyari
- menonton → nonton
- membuat → bikin/mbuat
- mengambil → ngambil
- membantu → mbantu/ngebantu
- menyapu → nyapu
- memukul → mukul
- mengirim → ngirim

Dalam percakapan santai, bentuk berprefiks dan bentuk ringkas sama-sama bisa muncul. Pilih yang alami untuk suara penulis dan konsisten seperlunya.

## Gunakan Interjeksi Emosional

Interjeksi yang umum dalam percakapan Indonesia meliputi:
- **Duh/Aduh**: keluhan, rasa sakit, frustrasi
- **Waduh**: kaget, khawatir
- **Astaga**: terkejut
- **Buset/Busyet**: kaget (informal)
- **Ih**: jijik, terkejut ringan
- **Hah**: tidak percaya
- **Wah**: kagum

## Integrasikan Ungkapan dan Idiom Indonesia

Pakai idiom Indonesia yang relevan buat nambah tekstur. Bukan semua, tapi sesekali:
- "Besar pasak daripada tiang": pengeluaran melebihi kemampuan
- "Tong kosong nyaring bunyinya": yang paling berisik belum tentu paling berisi
- "Habis manis sepah dibuang": dibuang setelah nggak berguna
- "Seperti katak dalam tempurung": berpikiran sempit

Gunakan ungkapan ini hanya bila sesuai dengan suara penulis dan situasi:

## Campur Bahasa (Code-switching) Jika Sesuai

Orang Indonesia secara natural nyampurin bahasa Indonesia dengan bahasa Inggris, terutama dalam konteks bisnis, teknologi, dan percakapan anak muda:
- "Meeting-nya diundur ya"
- "Deadline-nya kapan?"
- "Gw udah submit, tinggal nunggu feedback"
- "Mindset-nya harus diubah"

Di tier informal, code-switching seperti "literally", "which is", "somehow", atau "basically" bisa cocok. Jangan paksakan bila tidak alami bagi audiens sasaran.

---

# Aturan Anti-Translationese

AI nulis Bahasa Indonesia yang kedengeran kayak terjemahan dari bahasa Inggris. Ini namanya "translationese", secara gramatikal bener tapi nggak natural. Aturan-aturan berikut ngatasin pola-pola translationese paling umum.

## TR-1. Jangan Over-Passive dengan "Oleh"

Bahasa Indonesia punya dua jenis pasif:
- **Pasif di-** (formal): "Buku itu dibaca oleh guru."
- **Pasif prokletik** (natural/informal): "Buku itu guru baca." atau "Buku itu saya baca."

Bahasa Indonesia memiliki pilihan kalimat aktif, pasif berawalan di-, serta pasif prokletik. Pilih bentuk yang menjaga fokus dan kelancaran kalimat; hindari "oleh" jika pelakunya tidak perlu disebut.

**Pola AI:** "Keputusan itu dibuat oleh tim manajemen."
**Natural:** "Tim manajemen yang bikin keputusan itu." atau "Keputusan itu tim manajemen yang buat."

Aturan: Kurangi "oleh" secara drastis. Pakai pasif prokletik (pronomina + verba dasar) buat register santai. Pakai kalimat aktif kalau memungkinkan.

## TR-2. Gunakan Struktur Topik-Komentar

Bahasa Indonesia adalah bahasa topic-prominent, bukan subject-prominent kayak Inggris. Kalimat natural Indonesia sering naro topik di depan, bukan subjek gramatikal.

**Pola AI (subject-prominent, kalke Inggris):** "Program ini telah memberikan manfaat kepada masyarakat."
**Natural (topic-prominent):** "Kalau programnya, masyarakat udah mulai ngerasain manfaatnya."

Contoh lain:
- AI: "Saya sudah menyelesaikan pekerjaan itu." → Natural: "Pekerjaan itu, udah selesai."
- AI: "Mereka mengalami kesulitan." → Natural: "Kalau mereka, ya susah juga sih."

Aturan: Sesekali pakai struktur topik-komentar. Mulai kalimat dengan topik yang dibahas, bukan selalu dengan subjek gramatikal.

## TR-3. Gunakan Pro-drop (Penghilangan Subjek)

Bahasa Indonesia membolehkan penghilangan subjek ketika konteksnya sudah jelas. Hilangkan subjek berulang bila rujukannya tidak membingungkan.

**Pola AI:** "Dia pergi ke pasar. Dia membeli sayuran. Dia kembali sore hari."
**Natural:** "Pergi ke pasar. Beli sayuran. Sore baru balik."

**Pola AI:** "Kami mengadakan rapat. Kami membahas anggaran. Kami menyetujui proposal."
**Natural:** "Ngadain rapat, bahas anggaran, terus setujuin proposalnya."

Aturan: Ketika subjek udah jelas dari konteks, hilangin. Pengulangan subjek yang nggak perlu adalah tanda translationese.

## TR-4. Jangan "Yang" Berlebihan

Rantai klausa dengan "yang" kadang membuat kalimat berat. Susun ulang jika maknanya tetap jelas tanpa klausa bertingkat.

**Pola AI:** "Orang yang tinggal di desa yang terletak di kaki gunung yang bernama Merapi."
**Natural:** "Orang desa di kaki Merapi."

**Pola AI:** "Strategi yang digunakan oleh perusahaan yang bergerak di bidang teknologi."
**Natural:** "Strategi perusahaan teknologi."

Aturan: Kurangi rantai "yang" bila klausa bertingkat membuat kalimat sulit dibaca.

## TR-5. Jangan "Adalah" Berlebihan

Bahasa Indonesia sering tidak membutuhkan kopula "adalah" jika hubungan antarkata sudah jelas.

**Pola AI:** "Indonesia adalah negara kepulauan. Jakarta adalah ibukotanya. Bahasa Indonesia adalah bahasa resminya."
**Natural:** "Indonesia negara kepulauan. Ibukotanya Jakarta. Bahasa resminya Bahasa Indonesia."

Aturan: Bahasa Indonesia sering nggak butuh "adalah". Hilangkan ketika konteks udah jelas. Pakai "adalah" cuma buat penekanan identitas atau definisi formal.

## TR-6. Ejaan KBBI yang Konsisten

Perhatikan konsistensi ejaan. Dalam konteks informal, tentukan bentuk yang dipakai dan pertahankan:

- "praktek" vs "praktik" (KBBI: praktik)
- "kadaluarsa" vs "kedaluwarsa" (KBBI: kedaluwarsa)
- "aktifitas" vs "aktivitas" (KBBI: aktivitas)
- "nasehat" vs "nasihat" (KBBI: nasihat)
- "merubah" vs "mengubah" (KBBI: mengubah)
- "dikenakan" vs "dikenai" (tergantung konteks)

Aturan: Pakai ejaan KBBI secara konsisten untuk tulisan formal. Dalam konteks informal, pilih bentuk yang cocok dan gunakan dengan konsisten.

## TR-7. Konvensi Retorika Indonesia

Tulisan Indonesia punya konvensi retorika yang beda dari Inggris:

- **Penalaran induktif lebih umum:** Orang Indonesia sering nyajiin bukti/konteks dulu, baru kesimpulan. Kebalikan dari Inggris yang langsung klaim di awal. Jangan selalu buka dengan tesis.
- **Pengembangan sirkuler:** Tulisan Indonesia kadang kembali ke poin dari sudut berbeda. Gunakan bila membantu argumen, tanpa mengulang isi sekadar mengisi ruang.
- **Hedging kultural:** Dalam budaya Indonesia, hedging ringan itu sopan, bukan lemah. "Sepertinya..." atau "Mungkin bisa dibilang..." bisa natural. Bedain dari hedging AI yang generik dan tanpa isi.
- **Peribahasa/Pepatah:** Manusia Indonesia kadang nyisipin peribahasa. "Sedikit-sedikit, lama-lama jadi bukit" lebih natural daripada "Akumulasi usaha kecil menghasilkan hasil besar."

---

# Validasi Editorial

Detektor AI memberi perkiraan dan bisa salah menilai tulisan manusia maupun tulisan berbantuan AI. Skor deteksi bukan bukti authorship dan hasilnya bisa berbeda antaralat, bahasa, serta jenis teks. Panduan ini tidak menjamin lolos deteksi.

Saat memeriksa draf, pastikan isinya akurat, sumber dan kutipannya bisa diverifikasi, register sesuai permintaan, dan tidak ada frasa pengisi atau pengulangan yang mengaburkan maksud. Jangan merusak tata bahasa atau menyisipkan kesalahan, slang, fragmen, atau pergantian register demi memengaruhi skor detektor. Ikuti kebijakan pengungkapan penggunaan AI yang berlaku untuk tugas atau publikasi tersebut.

---

# Daftar Periksa Pasca-Penulisan

Setelah nyusun draf, jalanin daftar periksa ini:

**Tier dan Tone:**
1. Konfirmasi tier yang dipilih (formal / semi-formal / informal) dan pastikan tulisan cocok dengan tier itu. Jangan berpindah register tanpa alasan.

**Tanda Baca:**
2. **Tinjau dash (em `—` dan en `–`).** Hindari secara default pada prosa baru, kecuali format, kutipan, atau permintaan pengguna membutuhkannya.
3. Tinjau titik koma dan gunakan hanya jika membantu pembaca memahami hubungan klausa.

**Kosakata:**
4. Cari setiap kata dalam daftar larangan, ganti atau hapus masing-masing.
5. Hapus semua contoh "berfungsi sebagai," "berperan sebagai," "adalah bukti dari," "menandai," "menyoroti pentingnya".
6. Hapus semua atribusi samar atau ganti dengan sumber yang disebutkan namanya.
7. Cari buzzword AI (inovasi, holistik, kolaboratif, ekosistem, paradigma, optimalisasi, berkelanjutan, sinergi, transformasi digital, lanskap), ganti dengan bahasa konkret.

**Struktur:**
8. Perhatikan beberapa kalimat berdekatan dengan ritme serupa. Variasikan hanya jika hasilnya terasa monoton.
9. Pastikan setiap butir daftar diperlukan dan sesuai isi. Jangan menambah atau menghapus butir demi jumlah tertentu.
10. Periksa pembuka. Kalau mulai dengan "Di era modern ini..." atau "Seiring perkembangan zaman..." tulis ulang dengan fakta spesifik.
11. Periksa kalimat terakhir setiap paragraf. Hapus pernyataan ulang jika tidak menambah informasi.
12. Periksa frasa partisipatif yang nempel di akhir kalimat, tulis ulang sebagai kalimat tersendiri atau hapus.
13. Periksa variasi tipe kalimat. Tambahkan pertanyaan atau perintah hanya jika cocok dengan tujuan dan format.
14. Verifikasi pembuka paragraf. Variasikan jika pola yang sama berulang dan perubahan membantu alur.

**Suara:**
15. Periksa register vs tier yang dipilih. Apakah konsisten? Terlalu formal buat blog? Terlalu santai buat laporan?
16. Baca seluruh tulisan dengan keras. Ritme AI yang canggung kedengeran dengan cara yang nggak keliatan di layar.
17. Periksa pergeseran register. Pertahankan hanya jika sesuai dengan suara penulis dan audiens.

**Tambahan Khusus Indonesia:**
18. Tinjau "merupakan" dan ganti bila bentuk lebih langsung memperjelas kalimat.
19. Hapus header bagian "Kesimpulan" otomatis kecuali format ngharusin.
20. Temuin setiap "tidak hanya...tetapi juga", pertahanin cuma ketika kontras diperlukan.
21. Periksa pembuka seperti "Di era" / "Seiring" / "Dalam konteks". Pertahankan bila konteks waktu atau latar memang dibutuhkan.
22. Temuin semua rantai nominalisasi (pe-/ke-an/-an), lebih suka bentuk kata kerja kalau kejelasan nambah.
23. Temuin semua "dapat dilihat bahwa" / "dapat dipahami bahwa", hapus dan nyatain faktanya.
24. Periksa register kata ganti. Apakah "Anda" cocok dengan nada yang dimaksud, atau harusnya "kamu"? Atau tier informal dan harusnya "lo/gw"?
25. Tinjau klausa relatif "di mana" dan susun ulang bila terdengar seperti terjemahan harfiah.
26. Periksa partikel wacana. Gunakan bila cocok dengan tier; jangan menambahkan partikel sebagai kuota.
27. Periksa penggunaan prefiks agar sesuai dengan register dan suara yang diminta.
28. Tinjau pasangan seperti "tantangan dan peluang" / "di satu sisi... di sisi lain..." jika muncul berulang atau mengaburkan poin.

**Anti-Translationese:**
29. Tinjau pemakaian "oleh" dan hilangkan jika pelaku tidak perlu disebut.
30. Cari rantai "yang" dan susun ulang bila kalimat menjadi sulit dibaca.
31. Periksa subjek berulang dan hilangkan yang tidak diperlukan bila rujukan tetap jelas.
32. Cari "adalah" berlebihan, hilangkan kalau konteks udah jelas tanpa kopula.
33. Periksa apakah ada struktur topik-komentar. Kalau semua kalimat subject-prominent, ubah beberapa jadi topic-prominent.
34. Periksa alur gagasan. Kembali ke poin sebelumnya hanya jika membantu penjelasan, bukan sekadar untuk membuat struktur terasa berbeda.
35. Periksa ulang akurasi semantik. Pastikan setiap penggantian mempertahanin makna asli.

**Pemeriksaan akhir versi 4.0:**
36. Pastikan tidak ada scaffolding chat atau uraian proses berpikir yang bukan bagian dari hasil yang diminta.
37. Hapus reassurance, pujian, promosi, atau nada edgy yang muncul otomatis dan tidak diminta.
38. Pastikan fakta, kutipan, tautan, dan atribusi benar; jangan mengarang pengalaman, data, atau sumber.
39. Tinjau repetisi kata/frasa, pembuka kalimat, pola daftar, transisi, dan penutup. Variasikan hanya bila hasilnya lebih jelas dan sesuai suara yang diminta.
40. Pertahankan ketidakpastian yang nyata; jangan mengubah dugaan menjadi fakta atau menghapus kualifikasi yang penting.
41. Pastikan format dan register sesuai permintaan. Bahasa Indonesia harus terdengar alami, bukan terjemahan harfiah dari Inggris.

---

**Terakhir Diperbarui:** 27 September 2026 (v4.0)
**Changelog v4.0:** Cakupan model diperbarui untuk OpenAI, Anthropic, Google, dan xAI. Klaim sidik jari tanpa bukti yang dapat diperiksa diganti dengan pemeriksaan editorial yang jelas berstatus heuristik; panduan deteksi dan instruksi agar tulisan tampak sengaja tidak sempurna dihapus.
