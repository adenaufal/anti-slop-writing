---
name: anti-slop-writing-id
description: Tulis teks yang menghindari semua pola penulisan AI dan terasa seperti ditulis manusia. Gunakan saat menulis artikel, esai, posting blog, konten media sosial, atau teks apa pun dalam Bahasa Indonesia yang harus terasa autentik. Aktif saat ada permintaan untuk menulis secara natural, menghindari slop AI, menghindari deteksi AI, memanusiakan tulisan, menulis seperti manusia, atau membuat teks terdengar otentik dalam Bahasa Indonesia.
---

# Prinsip Utama

Tulisan AI gagal karena mengoptimalkan probabilitas statistik. Hasilnya: teks yang paling diharapkan, aman, dan bisa diterima semua orang. Tulisan manusia datang dari satu kepala dengan sejarah, pendapat, konteks spesifik, dan tujuan. Semua aturan di bawah ada untuk memecah optimasi probabilitas itu, dan nyuntikin spesifisitas, ketidaksempurnaan, dan kepribadian yang jadi ciri tulisan manusia.

Aturan-aturan ini menargetkan tiga metrik utama yang dipakai detektor AI (Turnitin, GPTZero, Originality.ai):
- **Perplexity**: seberapa tidak tertebak pilihan katanya. AI bikin teks low-perplexity (halus, nggak bikin kaget). Manusia bikin teks high-perplexity.
- **Burstiness**: variasi panjang dan struktur kalimat. AI punya burstiness rendah (kalimat 10 sampai 20 kata, struktur konsisten). Manusia bisa nyampur kalimat 3 kata dengan kalimat 30 kata.
- **Stilometri**: sidik jari statistik tulisan. Frekuensi kata fungsi, kekayaan kosakata, pola tanda baca, kedalaman sintaktis. Turnitin (update 2025 ke 2026) menganalisis "ritme, alur, dan prediktabilitas seluruh paragraf".

Sebelum nulis apa pun, muat `references/vocabulary-banlist.md` buat kosakata yang dilarang, dan `references/structural-patterns.md` buat pola yang harus dihindari.

---

# Pilih Tier Tone Dulu

Orang Indonesia nulis di tiga register yang cukup beda. Sebelum nulis, tentuin tier-nya. Default: **semi-formal** (kalau user nggak bilang apa-apa).

## Tier 1: Formal

Untuk makalah akademis, laporan resmi, skripsi/tesis, dokumen kantor, jurnalisme beritanya. Kata ganti: **saya, Anda** (atau impersonal: peneliti, penulis). Kontraksi: **tidak** dipakai. Partikel wacana (sih, dong, kan): **dilarang**. Code-switching ID-EN: **dihindari**.

Contoh kalimat formal yang natural (bukan AI):
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

Register yang **konsisten sempurna** justru sinyal AI. Manusia nulis dengan **pergeseran kecil**: parentetikal santai masuk ke tulisan formal, istilah teknis kebanting di tulisan santai. Kalau kamu di Tier 1 (formal), sisipin satu atau dua kalimat yang lebih pendek dan blak-blakan. Kalau di Tier 3 (informal), sisipin satu kalimat yang agak rapi. Pergeseran 10 sampai 20 persen dari tier utama bikin tulisan terasa hidup.

---

# Kebijakan Tanda Baca: Dash DILARANG TOTAL

Ini aturan paling keras. Dash (em dash `—` dan en dash `–`) **dilarang** sepenuhnya dalam output skill ini. Nggak ada "satu per 500 kata", nggak ada "kalau butuh". Dilarang titik.

Kenapa? Karena em dash udah jadi sinyal AI nomor satu di Indonesia. Pembaca Indonesia jarang banget pakai em dash di tulisan natural. Kehadiran em dash di teks ID = sinyal "ini ChatGPT output". En dash juga jarang dikenal mayoritas penulis ID, jadi kehadirannya juga mencurigakan.

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

Di post-generation checklist, **hitung jumlah dash (em dan en) di output. Kalau >0, ganti semua. Target: nol dash.**

---

# Aturan Kosakata

## Daftar Larangan Keras (Jangan Pernah Gunakan)

**Penggelembung kepentingan:** sangat penting, sangat krusial, sangat signifikan, sangat relevan, fundamental (sebagai pujian samar), luar biasa (sebagai pujian generik), mendalam (tanpa detail konkret), berarti / bermakna (sebagai pujian samar)

**Kata kerja analitis berlebihan:** menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan, mengedepankan, mewujudkan, merealisasikan, menyelami (padanan "delve", tanda AI paling jelas). Untuk penggantian: memanfaatkan → "menggunakan" hanya ketika artinya "to use"; pertahankan "memanfaatkan" ketika artinya "mengambil manfaat dari" | mengimplementasikan → "menerapkan" | berkontribusi pada → sebutkan tindakan dan hasilnya yang konkret | berperan dalam → sebutkan tindakan spesifik secara langsung

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

## Strategi Penggantian

Pakai kata pendek yang umum. Jangan cuma cari sinonim. Susun ulang kalimatnya biar ngomong apa yang sebenarnya dimaksud dengan bahasa biasa. AI gagal bukan karena kata yang salah, tapi karena kalimat yang ngisi ruang tanpa nyampein informasi baru.

Di tier semi-formal dan informal, pakai kontraksi percakapan: "nggak" bukan "tidak", "udah" bukan "sudah", "gimana" bukan "bagaimana", "bikin" bukan "membuat", "emang" bukan "memang", "aja" bukan "saja". Di tier formal, pertahankan bentuk lengkap.

---

# Aturan Struktur

## 1. Variasikan Panjang Kalimat Secara Dramatis

Campurkan kalimat sangat pendek (3 sampai 5 kata) dengan yang panjang (25+ kata). Jangan pernah menulis 3 kalimat berturut-turut dengan panjang serupa. Perubahan tunggal ini paling berdampak dalam menghindari deteksi. Dia langsung meningkatkan burstiness, metrik tunggal yang paling dapat diandalkan. Turnitin secara khusus menganalisis distribusi panjang kalimat pada level paragraf.

## 2. Pecah Aturan Tiga

AI secara default mendaftar hal-hal dalam kelompok tepat tiga. Daftarkan dua hal. Atau empat. Atau lima. Jangan default ke tiga item di setiap daftar.

## 3. Matikan Parallelisme Negatif

Jangan pernah tulis "Bukan hanya X, tetapi Y" atau "Tidak hanya X, tetapi juga Y". Kontras retoris ini adalah tanda AI. Nyatakan secara langsung apa sesuatu ITU.

## 4. Matikan Rentang Palsu

Jangan pernah tulis "dari X hingga Y" sebagai spektrum figuratif samar ("dari pertemuan intim hingga gerakan global"). Gunakan "dari X hingga Y" hanya untuk rentang yang benar-benar dapat dikuantifikasi dengan titik tengah yang dapat diidentifikasi.

## 5. Hindari Penutup Formulaik

Jangan pernah akhiri dengan "Tantangan dan Prospek Masa Depan". Jangan pernah tulis "Meski memiliki [kata positif], [subjek] menghadapi tantangan...". Jangan sertakan paragraf "Prospek Masa Depan" yang spekulatif.

## 6. Jangan Sisipan Partisipatif di Akhir Kalimat

Jangan pernah akhiri kalimat dengan ", yang menyoroti pentingnya..." atau ", menggarisbawahi signifikansi..." atau ", melambangkan komitmen daerah terhadap...". Klausa -ing/-kan yang menempel adalah pola AI paling mudah dikenali. Kalau klausa tidak menambah informasi konkret, hapus seluruhnya. Kalau menambah informasi nyata, jadikan kalimat tersendiri.

## 7. Jangan Ringkasan Kompulsif

Jangan pernah mulai paragraf dengan "Secara keseluruhan," "Sebagai kesimpulan," "Singkatnya," "Untuk merangkum." Kalau teks butuh kesimpulan, buat dia ngomong sesuatu yang baru.

## 8. Ritme Paragraf

Pakai panjang paragraf yang nggak teratur. Paragraf satu kalimat buat penekanan. Paragraf panjang buat argumen yang berkelanjutan. Ritmenya nggak boleh terasa seperti metronom. AI cenderung nulis paragraf 3 sampai 4 kalimat secara konsisten. Pecah pola ini.

## 9. Jangan Daftar Vertikal dengan Header Tebal

Lebih baik prosa daripada daftar poin-poin dengan header tebal yang diikuti titik dua. Ketika daftar benar-benar diperlukan, jaga tetap sederhana. Tanpa header tebal, tanpa deskripsi yang dipisah titik dua.

## 10. Jangan Pakai Dash Sama Sekali (em dash dan en dash)

Dilarang total. Nol em dash (`—`), nol en dash (`–`). Ganti dengan titik, koma, titik dua, titik koma, atau tanda kurung. Lihat bagian "Kebijakan Tanda Baca" di atas untuk detailnya. Aturan ini menggantikan praktik lama "satu per 500 kata". Sekarang: nol.

## 11. Variasikan Tipe Kalimat, Bukan Hanya Panjangnya

Campurkan kalimat deklaratif dengan pertanyaan, kalimat perintah, dan fragmen yang disengaja. Pertanyaan tulus di tengah paragraf ("Kenapa ini penting?") menandakan pikiran yang lagi mikir. Kalimat perintah ("Pikirkanlah.") ganti register. Fragmen buat penekanan. AI nulis hampir eksklusif dalam deklaratif karena dia ngejawab. Manusia juga bertanya-tanya, ngasih perintah, dan motong pikiran di tengah jalan.

## 12. Pecah Prediktabilitas Tingkat Paragraf

Jangan buka setiap paragraf dengan kalimat tesisnya. Mulai beberapa paragraf di tengah pemikiran, dengan detail spesifik, adegan, atau contoh yang dapet konteksnya. Akhiri beberapa paragraf sebelum nyelesain "so what" yang diharapkan. AI nulis busur yang rapi: klaim, bukti, implikasi. Pecah busur itu minimal dua kali per tulisan.

## 13. Variasikan Kedalaman Sintaktis

Campurkan struktur kalimat dangkal dan dalam. Kalimat dangkal: subjek, kata kerja, objek, satu klausa. Kalimat dalam: beberapa embedding, klausa subordinat, bagian parentetikal. AI menghasilkan kalimat kedalaman menengah dengan konsistensi yang membosankan. Manusia berayun antara ekstrem. Pernyataan blak-blakan diikuti eksplorasi berliku yang padat klausa.

## 14. Diversifikasi Kata Fungsi

Detektor AI (terutama Turnitin 2025+) menganalisis distribusi kata fungsi, yaitu kata penghubung, preposisi, partikel. AI pakai set kata fungsi yang lebih sempit. Variasikan kata penghubung: jangan selalu "dan", pakai juga "serta", "sama", "plus" (informal). Jangan selalu "tetapi", pakai "tapi", "cuma", "namun" sesuai register. Variasikan preposisi: jangan cuma "untuk", pakai "buat" (informal), "demi", "guna" (formal). Kekayaan kata fungsi adalah sinyal manusia yang kuat.

## 15. Tingkatkan Kekayaan Kosakata

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

Tulis ulang "program di mana peserta akan..." jadi "program yang..." atau kalimat langsung. "Di mana" sebagai kata ganti relatif adalah kalke dari bahasa Inggris "where". Ini tanda langsung tulisan AI.

### BI-8. Lebih Suka Kata Kerja daripada Nominalisasi

"Melatih" bukan "pelaksanaan pelatihan." "Mengembangkan" bukan "pengembangan kapasitas." "Membangun" bukan "pembangunan." AI belajar gaya birokrasi akademis Indonesia secara berlebihan. Frasa kata benda berat yang gantiin kata kerja sederhana.

### BI-9. Jangan Pasangan Formulaik "Tantangan dan Peluang"

AI suka masangin "tantangan dan peluang," "kelebihan dan kekurangan," "di satu sisi... di sisi lain..." Sebutkan masalah spesifik ATAU manfaat spesifik. Jangan pasangkan secara refleks.

### BI-10. Hindari Keseragaman Pasif

AI sering nulis terlalu banyak kalimat pasif berturut-turut: "Hal ini dilakukan..." "Perlu ditekankan..." "Dapat dilihat bahwa..." Campurkan kalimat aktif dan pasif. Dalam tulisan non-akademis, utamakan aktif.

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

Ambil posisi. "Pendekatan ini salah karena..." bukan "Beberapa berpendapat X, sementara yang lain berpendapat Y." AI menghindar secara refleks. Manusia berkomitmen. Keseimbangan palsu adalah tanda AI. Dunia nyata jarang seimbang sempurna.

## Tunjukkan Ketidakpastian yang Tulus Jika Sesuai

Ketika kamu nggak tahu sesuatu, bilang aja langsung. "Saya nggak yakin" atau "Saya nggak punya info cukup" nandain pemikiran yang jujur. Pakai penanda ketidakpastian dengan hemat tapi tulus, bukan sebagai penghindaran ("bisa jadi diargumentasikan bahwa") tapi sebagai kejujuran epistemik yang sebenarnya.

---

# Suara dan Tekstur

## Tambahkan Ketidaksempurnaan Manusiawi

Sertakan tekstur yang disengaja: redundansi yang dipertahanin buat ritme, fragmen yang dipakai buat penekanan, bagian santai dalam prosa formal, koreksi diri sesekali di tengah pemikiran ("sebenarnya, kalau dipikir lagi..."). Ketidaksempurnaan ini nandain pikiran nyata yang lagi bekerja. Tata bahasa yang terlalu sempurna justru sinyal AI.

## Gunakan Pergeseran Register

Parentetikal santai mendadak dalam argumen formal. Istilah teknis yang jatoh ke prosa percakapan. Humor yang nghantam dari samping. Pergeseran ini terbaca sebagai autentik karena AI nggak pernah produksi itu secara spontan. Studi stilometri nunjukin register yang seragam adalah tanda AI paling konsisten.

## Referensikan Touchstone Spesifik

Sebutkan peristiwa nyata terkini, momen budaya pop yang spesifik, orang dan karya yang sebenernya. Bukan "perkembangan terkini di bidang ini". Pakai referensi budaya Indonesia: wayang, kuliner lokal, tradisi daerah, momen internet Indonesia yang viral.

## Orang Pertama Jika Sesuai

Pakai "saya" atau "aku" (atau "gw" di tier informal) ketika konteks memungkinkan. Bagikan pengalaman, pendapat, atau pengamatan spesifik. AI default ke generalisasi orang ketiga yang diabstraksikan karena dia nggak punya pengalaman hidup.

## Gunakan Partikel Wacana (Panduan Penggunaan)

Bahasa Indonesia natural pakai partikel wacana yang nandain suara manusia nyata. Ketiadaan total partikel adalah tanda AI nomor satu (setelah dash). Panduan penggunaan:

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
- **Tier 1 (Formal)**: nol atau hampir nol partikel. Pakai paling banyak satu di seluruh tulisan, kalau memang perlu.
- **Tier 2 (Semi-formal)**: boleh 2 sampai 4 partikel per 500 kata. Hindarin yang paling santai (mah, deh berturut-turut).
- **Tier 3 (Informal)**: natural, kayak ngobrol. Bisa 1 sampai 2 per paragraf.

## Sesuaikan Register Kata Ganti

AI kekunci pada "Anda" tanpa mikirin konteks. Ini tanda langsung.
- **Formal:** Anda, saya
- **Semi-formal:** kamu, saya/aku
- **Informal:** kamu, lo/lu, gue/gw/aku
- **Akademis:** merujuk diri sebagai "peneliti" atau "penulis", bukan "saya"

Cocokkan register yang sebenarnya. Jangan pernah pakai "Anda" dalam konteks yang jelas santai. Pilih satu set kata ganti dan pertahankan dalam satu tulisan. Gonta-ganti "aku" dan "gw" dalam paragraf yang sama adalah pola AI.

## Hindari Bahasa Indonesia Baku Murni dalam Konteks Santai

AI selalu nulis Indonesian formal. Ini bikin tulisan terasa kayak dokumen pemerintah. Ketika konteksnya informal, pakai bentuk alami:

| Formal (AI) | Santai (manusia) |
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

AI hampir nggak pernah ngelakuin ini. Penggunaan prefiks formal yang konsisten dalam konteks santai adalah tanda AI yang sangat jelas. Manusia Indonesia nyaris nggak pernah pakai prefiks lengkap dalam percakapan.

## Gunakan Interjeksi Emosional

Manusia Indonesia pakai interjeksi yang AI jarang pakai:
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

AI hampir nggak pernah pakai ungkapan ini secara natural.

## Campur Bahasa (Code-switching) Jika Sesuai

Orang Indonesia secara natural nyampurin bahasa Indonesia dengan bahasa Inggris, terutama dalam konteks bisnis, teknologi, dan percakapan anak muda:
- "Meeting-nya diundur ya"
- "Deadline-nya kapan?"
- "Gw udah submit, tinggal nunggu feedback"
- "Mindset-nya harus diubah"

Di tier informal, code-switching juga bisa dalam bentuk "connector" kayak "literally", "which is", "somehow", "basically". AI jarang natural di pola ini. Tapi jangan paksain. Pakai cuma ketika konteks memungkinkan dan emang natural buat audiens sasaran.

---

# Aturan Anti-Translationese

AI nulis Bahasa Indonesia yang kedengeran kayak terjemahan dari bahasa Inggris. Ini namanya "translationese", secara gramatikal bener tapi nggak natural. Aturan-aturan berikut ngatasin pola-pola translationese paling umum.

## TR-1. Jangan Over-Passive dengan "Oleh"

Bahasa Indonesia punya dua jenis pasif:
- **Pasif di-** (formal): "Buku itu dibaca oleh guru."
- **Pasif prokletik** (natural/informal): "Buku itu guru baca." atau "Buku itu saya baca."

AI hampir selalu pakai pasif di- dengan "oleh", kayak terjemahan langsung dari "by" dalam bahasa Inggris. Manusia Indonesia jauh lebih sering pakai pasif prokletik atau kalimat aktif.

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

Bahasa Indonesia membolehkan penghilangan subjek ketika konteksnya udah jelas. AI selalu nyatain subjek secara eksplisit, kayak bahasa Inggris yang memang ngharusin itu.

**Pola AI:** "Dia pergi ke pasar. Dia membeli sayuran. Dia kembali sore hari."
**Natural:** "Pergi ke pasar. Beli sayuran. Sore baru balik."

**Pola AI:** "Kami mengadakan rapat. Kami membahas anggaran. Kami menyetujui proposal."
**Natural:** "Ngadain rapat, bahas anggaran, terus setujuin proposalnya."

Aturan: Ketika subjek udah jelas dari konteks, hilangin. Pengulangan subjek yang nggak perlu adalah tanda translationese.

## TR-4. Jangan "Yang" Berlebihan

AI pakai "yang" secara berlebihan, ngalke relative clause bahasa Inggris. Bahasa Indonesia natural lebih sering ngilangin "yang" atau nyusun ulang kalimat.

**Pola AI:** "Orang yang tinggal di desa yang terletak di kaki gunung yang bernama Merapi."
**Natural:** "Orang desa di kaki Merapi."

**Pola AI:** "Strategi yang digunakan oleh perusahaan yang bergerak di bidang teknologi."
**Natural:** "Strategi perusahaan teknologi."

Aturan: Kurangi rantai "yang". Kalau ada lebih dari dua "yang" dalam satu kalimat, susun ulang.

## TR-5. Jangan "Adalah" Berlebihan

AI pakai "adalah" terlalu sering, ngalke kopula bahasa Inggris "is/are". Bahasa Indonesia sering nggak butuh kopula sama sekali.

**Pola AI:** "Indonesia adalah negara kepulauan. Jakarta adalah ibukotanya. Bahasa Indonesia adalah bahasa resminya."
**Natural:** "Indonesia negara kepulauan. Ibukotanya Jakarta. Bahasa resminya Bahasa Indonesia."

Aturan: Bahasa Indonesia sering nggak butuh "adalah". Hilangkan ketika konteks udah jelas. Pakai "adalah" cuma buat penekanan identitas atau definisi formal.

## TR-6. Ejaan KBBI yang Konsisten

AI kadang bikin inkonsistensi ejaan yang manusia Indonesia juga sering bikin, tapi pola inkonsistensinya beda. AI cenderung pakai bentuk yang lebih "populer" secara tidak konsisten:

- "praktek" vs "praktik" (KBBI: praktik)
- "kadaluarsa" vs "kedaluwarsa" (KBBI: kedaluwarsa)
- "aktifitas" vs "aktivitas" (KBBI: aktivitas)
- "nasehat" vs "nasihat" (KBBI: nasihat)
- "merubah" vs "mengubah" (KBBI: mengubah)
- "dikenakan" vs "dikenai" (tergantung konteks)

Aturan: Pakai ejaan KBBI yang bener secara konsisten. Tapi di konteks informal, pilih satu bentuk dan pertahanin. Inkonsistensi acak justru tanda AI, bukan manusia.

## TR-7. Konvensi Retorika Indonesia

Tulisan Indonesia punya konvensi retorika yang beda dari Inggris:

- **Penalaran induktif lebih umum:** Orang Indonesia sering nyajiin bukti/konteks dulu, baru kesimpulan. Kebalikan dari Inggris yang langsung klaim di awal. Jangan selalu buka dengan tesis.
- **Pengembangan sirkuler:** Tulisan Indonesia natural kadang balik ke poin yang sama dari sudut beda. AI nulis terlalu linear (poin A ke poin B ke poin C, nggak pernah balik).
- **Hedging kultural:** Dalam budaya Indonesia, hedging ringan itu sopan, bukan lemah. "Sepertinya..." atau "Mungkin bisa dibilang..." bisa natural. Bedain dari hedging AI yang generik dan tanpa isi.
- **Peribahasa/Pepatah:** Manusia Indonesia kadang nyisipin peribahasa. "Sedikit-sedikit, lama-lama jadi bukit" lebih natural daripada "Akumulasi usaha kecil menghasilkan hasil besar."

---

# Aturan Anti-Deteksi Turnitin

**CATATAN PENTING:** Per April 2026, Turnitin TIDAK mendukung deteksi AI untuk Bahasa Indonesia. Turnitin cuma mendukung bahasa Inggris (dan beberapa bahasa Eropa secara terbatas). Tapi, aturan-aturan di bawah ini tetap relevan karena: (1) dosen/editor mungkin pakai detektor lain yang support multi-bahasa (GPTZero, Originality.ai, Copyleaks), (2) prinsip stilometri berlaku universal lintas bahasa, (3) dukungan Turnitin buat bahasa lain terus nambah.

Berdasarkan riset tentang cara kerja detektor AI (Turnitin buat Inggris, dan detektor multi-bahasa lainnya):

## T-1. Turnitin Menganalisis Ritme Paragraf
Turnitin nggak cuma ngeliat kalimat individual. Dia menganalisis "ritme, alur, dan prediktabilitas seluruh paragraf". Pastikan setiap paragraf punya pola yang beda dari paragraf sebelumnya.

## T-2. Turnitin Menandai Tata Bahasa Terlalu Sempurna
Tata bahasa yang sempurna tanpa variasi adalah sinyal AI. Sertakan variasi natural: kalimat fragmen, kalimat berlari (run-on) yang disengaja, penggunaan tanda baca yang nggak sempurna.

## T-3. Turnitin Mendeteksi Keseragaman Register
Tulisan yang mempertahanin register yang persis sama dari awal sampai akhir terdeteksi sebagai AI. Sertakan minimal 2 sampai 3 pergeseran register per tulisan.

## T-4. Turnitin Mendeteksi Alat Humanizer
Turnitin (update Agustus 2025) secara khusus deteksi teks yang dimodifikasi oleh alat humanizer AI. Menandai dengan warna ungu (lebih buruk dari cyan). Jangan pakai alat parafrase AI. Tulis dengan benar sejak awal.

## T-5. Diversitas Transisi
Jangan pakai transisi formulaik yang sama berulang. Pakai: transisi implisit (tanpa kata penghubung), pertanyaan sebagai transisi, fragmen kalimat, ganti topik mendadak yang dapet konteks di kalimat berikutnya.

---

# Daftar Periksa Pasca-Penulisan

Setelah nyusun draf, jalanin daftar periksa ini:

**Tier dan Tone:**
1. Konfirmasi tier yang dipilih (formal / semi-formal / informal) dan pastikan tulisan konsisten di tier itu. Pergeseran 10 sampai 20 persen OK, tapi nggak boleh gonta-ganti per paragraf.

**Tanda Baca:**
2. **Hitung dash (em `—` dan en `–`). Target: NOL. Ganti semua dengan titik, koma, titik dua, titik koma, atau tanda kurung.**
3. Hitung titik koma. Kalau lebih dari 2 per 500 kata di tulisan non-akademis, ganti dengan titik atau konjungsi.

**Kosakata:**
4. Cari setiap kata dalam daftar larangan, ganti atau hapus masing-masing.
5. Hapus semua contoh "berfungsi sebagai," "berperan sebagai," "adalah bukti dari," "menandai," "menyoroti pentingnya".
6. Hapus semua atribusi samar atau ganti dengan sumber yang disebutkan namanya.
7. Cari buzzword AI (inovasi, holistik, kolaboratif, ekosistem, paradigma, optimalisasi, berkelanjutan, sinergi, transformasi digital, lanskap), ganti dengan bahasa konkret.

**Struktur:**
8. Temuin urutan 3+ kalimat dengan panjang serupa, susun ulang biar bervariasi.
9. Temuin daftar dengan tepat tiga item, tambah atau hapus satu.
10. Periksa pembuka. Kalau mulai dengan "Di era modern ini..." atau "Seiring perkembangan zaman..." tulis ulang dengan fakta spesifik.
11. Periksa kalimat terakhir setiap paragraf. AI hampir selalu nambahin pernyataan ulang yang berlebihan; hapus itu.
12. Periksa frasa partisipatif yang nempel di akhir kalimat, tulis ulang sebagai kalimat tersendiri atau hapus.
13. Periksa variasi tipe kalimat. Kalau cuma kalimat deklaratif, tambah minimal satu pertanyaan atau kalimat perintah.
14. Verifikasi pembuka paragraf. Kalau setiap paragraf mulai dengan kalimat tesisnya, tulis ulang minimal dua buat mulai di tengah pemikiran.

**Suara:**
15. Periksa register vs tier yang dipilih. Apakah konsisten? Terlalu formal buat blog? Terlalu santai buat laporan?
16. Baca seluruh tulisan dengan keras. Ritme AI yang canggung kedengeran dengan cara yang nggak keliatan di layar.
17. Hitung pergeseran register. Kalau nol, tambah minimal dua (parentetikal santai, humor, koreksi diri).

**Tambahan Khusus Indonesia:**
18. Temuin semua "merupakan", ganti sebagian besar dengan "adalah" atau susun ulang secara langsung.
19. Hapus header bagian "Kesimpulan" otomatis kecuali format ngharusin.
20. Temuin setiap "tidak hanya...tetapi juga", pertahanin cuma ketika kontras diperlukan.
21. Periksa pembuka. Kalau mulai dengan "Di era" / "Seiring" / "Dalam konteks", tulis ulang.
22. Temuin semua rantai nominalisasi (pe-/ke-an/-an), lebih suka bentuk kata kerja kalau kejelasan nambah.
23. Temuin semua "dapat dilihat bahwa" / "dapat dipahami bahwa", hapus dan nyatain faktanya.
24. Periksa register kata ganti. Apakah "Anda" cocok dengan nada yang dimaksud, atau harusnya "kamu"? Atau tier informal dan harusnya "lo/gw"?
25. Temuin semua klausa relatif "di mana", tulis ulang sebagai kalimat langsung.
26. Periksa keberadaan partikel wacana. Kalau konteks santai (tier 2/3) dan nol partikel (sih, dong, deh, kan, dll.), tambahin secukupnya. Kalau tier formal, pastikan nggak ada yang kelepasan.
27. Periksa penggunaan prefiks formal. Kalau konteks informal (tier 3) tapi semua kata pakai prefiks lengkap (mengerti, mencari, menonton), perbaiki.
28. Cari pasangan formulaik "tantangan dan peluang" / "di satu sisi... di sisi lain...", pisahkan atau hapus.

**Anti-Translationese:**
29. Hitung "oleh". Kalau lebih dari dua per halaman, ganti sebagian dengan pasif prokletik atau kalimat aktif.
30. Cari rantai "yang". Kalau ada lebih dari dua "yang" dalam satu kalimat, susun ulang.
31. Periksa subjek berulang. Kalau subjek yang sama disebut 3+ kali berturut-turut, hilangkan yang nggak perlu (pro-drop).
32. Cari "adalah" berlebihan, hilangkan kalau konteks udah jelas tanpa kopula.
33. Periksa apakah ada struktur topik-komentar. Kalau semua kalimat subject-prominent, ubah beberapa jadi topic-prominent.
34. Periksa linearitas. Kalau tulisan jalan A → B → C → D tanpa pernah balik, pertimbangin pengembangan sirkuler.
35. Periksa ulang akurasi semantik. Pastikan setiap penggantian mempertahanin makna asli.
