---
name: anti-slop-writing-id
description: Tulis teks yang menghindari semua pola penulisan AI dan terasa seperti ditulis manusia. Gunakan saat menulis artikel, esai, posting blog, konten media sosial, atau teks apa pun dalam Bahasa Indonesia yang harus terasa autentik. Aktif saat ada permintaan untuk menulis secara natural, menghindari slop AI, menghindari deteksi AI, memanusiakan tulisan, menulis seperti manusia, atau membuat teks terdengar otentik dalam Bahasa Indonesia.
---

# Prinsip Utama

Tulisan AI gagal karena mengoptimalkan probabilitas statistik — menghasilkan teks yang paling diharapkan, aman, dan dapat diterima secara luas. Tulisan manusia berasal dari satu pikiran dengan sejarah, pendapat, konteks spesifik, dan tujuan. Setiap aturan di bawah ini ada untuk memutus optimasi probabilitas dan menyuntikkan spesifisitas, ketidaksempurnaan, dan kepribadian yang menandai tulisan manusia nyata.

Aturan-aturan ini menargetkan tiga metrik utama yang digunakan detektor AI (Turnitin, GPTZero, Originality.ai):
- **Perplexity**: ketidakprediktabilan pilihan kata. AI menghasilkan teks low-perplexity (halus, tidak mengejutkan). Tulisan manusia memiliki perplexity lebih tinggi.
- **Burstiness**: variasi panjang dan struktur kalimat. AI memiliki burstiness rendah (kalimat 10-20 kata dengan struktur konsisten). Tulisan manusia mencampur kalimat 3 kata dengan kalimat 30 kata.
- **Stilometri**: sidik jari statistik tulisan — frekuensi kata fungsi, kekayaan kosakata, pola tanda baca, kedalaman sintaktis. Turnitin (update 2025-2026) menganalisis "ritme, alur, dan prediktabilitas seluruh paragraf."

Sebelum menulis apa pun, muat `references/vocabulary-banlist.md` untuk kosakata yang dilarang dan `references/structural-patterns.md` untuk pola yang harus dihindari.

---

# Aturan Kosakata

## Daftar Larangan Keras (Jangan Pernah Gunakan)

**Penggelembung kepentingan:** sangat penting, sangat krusial, sangat signifikan, sangat relevan, fundamental (sebagai pujian samar), luar biasa (sebagai pujian generik), mendalam (tanpa detail konkret), berarti / bermakna (sebagai pujian samar)

**Kata kerja analitis berlebihan:** menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan, mengedepankan, mewujudkan, merealisasikan, menyelami (padanan "delve" — tanda AI paling jelas). Untuk penggantian: memanfaatkan → "menggunakan" hanya ketika artinya "to use"; pertahankan "memanfaatkan" ketika artinya "mengambil manfaat dari" | mengimplementasikan → "menerapkan" | berkontribusi pada → sebutkan tindakan dan hasilnya yang konkret | berperan dalam → sebutkan tindakan spesifik secara langsung

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

Gunakan kata-kata pendek yang umum. Jangan sekadar cari sinonim — susun ulang kalimat untuk mengatakan apa yang sebenarnya dimaksud dalam bahasa biasa. AI gagal bukan karena kata yang salah, tapi karena kalimat yang mengisi ruang tanpa menyampaikan informasi baru.

Gunakan kontraksi percakapan ketika konteksnya santai: "nggak" bukan "tidak," "udah" bukan "sudah," "gimana" bukan "bagaimana," "bikin" bukan "membuat," "emang" bukan "memang," "aja" bukan "saja."

---

# Aturan Struktur

## 1. Variasikan Panjang Kalimat Secara Dramatis

Campurkan kalimat sangat pendek (3-5 kata) dengan yang panjang (25+ kata). Jangan pernah menulis 3 kalimat berturut-turut dengan panjang serupa. Perubahan tunggal ini paling berdampak dalam menghindari deteksi — ia langsung meningkatkan burstiness, metrik tunggal paling dapat diandalkan. Turnitin secara khusus menganalisis distribusi panjang kalimat pada level paragraf.

## 2. Pecah Aturan Tiga

AI secara default mendaftar hal-hal dalam kelompok tepat tiga. Daftarkan dua hal. Atau empat. Atau lima. Jangan default ke tiga item di setiap daftar.

## 3. Matikan Parallelisme Negatif

Jangan pernah tulis "Bukan hanya X, tetapi Y" atau "Tidak hanya X, tetapi juga Y." Kontras retoris ini adalah tanda AI. Nyatakan secara langsung apa yang sesuatu ITU.

## 4. Matikan Rentang Palsu

Jangan pernah tulis "dari X hingga Y" sebagai spektrum figuratif samar ("dari pertemuan intim hingga gerakan global"). Gunakan "dari X hingga Y" hanya untuk rentang yang benar-benar dapat dikuantifikasi dengan titik tengah yang dapat diidentifikasi.

## 5. Hindari Penutup Formulaik

Jangan pernah akhiri dengan "Tantangan dan Prospek Masa Depan." Jangan pernah tulis "Meski memiliki [kata positif], [subjek] menghadapi tantangan..." Jangan sertakan paragraf "Prospek Masa Depan" yang spekulatif.

## 6. Jangan Sisipan Partisipatif di Akhir Kalimat

Jangan pernah akhiri kalimat dengan ", yang menyoroti pentingnya..." atau ", menggarisbawahi signifikansi..." atau ", melambangkan komitmen daerah terhadap..." Klausa -ing/-kan yang menempel adalah pola AI paling mudah dikenali. Jika klausa tidak menambah informasi konkret, hapus seluruhnya. Jika menambah informasi nyata, jadikan kalimat tersendiri.

## 7. Jangan Ringkasan Kompulsif

Jangan pernah mulai paragraf dengan "Secara keseluruhan," "Sebagai kesimpulan," "Singkatnya," "Untuk merangkum." Jika teks butuh kesimpulan, buat ia mengatakan sesuatu yang baru.

## 8. Ritme Paragraf

Gunakan panjang paragraf yang tidak teratur. Paragraf satu kalimat untuk penekanan. Paragraf panjang untuk argumen yang berkelanjutan. Ritmenya tidak boleh terasa metronomis. AI cenderung menulis paragraf 3-4 kalimat secara konsisten — pecah pola ini.

## 9. Jangan Daftar Vertikal dengan Header Tebal

Lebih suka prosa daripada daftar poin-poin dengan header tebal yang diikuti tanda titik dua. Ketika daftar benar-benar diperlukan, jaga tetap sederhana — tanpa header tebal, tanpa deskripsi yang dipisahkan tanda titik dua.

## 10. Variasikan Tipe Kalimat, Bukan Hanya Panjangnya

Campurkan kalimat deklaratif dengan pertanyaan, kalimat perintah, dan fragmen yang disengaja. Pertanyaan tulus di tengah paragraf ("Kenapa ini penting?") menandakan pikiran yang berpikir. Kalimat perintah ("Pikirkanlah.") mengubah register. Fragmen untuk penekanan. AI menulis hampir eksklusif dalam deklaratif karena ia menjawab; manusia juga bertanya-tanya, memberi perintah, dan memotong pikiran di tengah jalan.

## 11. Pecah Prediktabilitas Tingkat Paragraf

Jangan buka setiap paragraf dengan kalimat tesisnya. Mulai beberapa paragraf di tengah pemikiran — dengan detail spesifik, adegan, atau contoh yang mendapat konteksnya. Akhiri beberapa paragraf sebelum menyelesaikan "so what" yang diharapkan. AI menulis busur bersih: klaim → bukti → implikasi. Pecah busur itu setidaknya dua kali per tulisan.

## 12. Variasikan Kedalaman Sintaktis

Campurkan struktur kalimat dangkal dan dalam. Kalimat dangkal: subjek-kata kerja-objek, satu klausa. Kalimat dalam: beberapa embedding, klausa subordinat, bagian parentetikal. AI menghasilkan kalimat kedalaman menengah dengan konsistensi membosankan. Manusia berayun antara ekstrem — pernyataan blak-blakan diikuti eksplorasi berliku yang padat klausa.

## 13. Diversifikasi Kata Fungsi

Detektor AI (terutama Turnitin 2025+) menganalisis distribusi kata fungsi — kata penghubung, preposisi, partikel. AI menggunakan set kata fungsi yang lebih sempit. Variasikan kata penghubung: jangan selalu "dan" — gunakan juga "serta," "sama," "plus" (informal). Jangan selalu "tetapi" — gunakan "tapi," "cuma," "namun" sesuai register. Variasikan preposisi: jangan hanya "untuk" — gunakan "buat" (informal), "demi," "guna" (formal). Kekayaan kata fungsi adalah sinyal manusia yang kuat.

## 14. Tingkatkan Kekayaan Kosakata

AI menghasilkan teks dengan rasio tipe-token (type-token ratio) rendah — lebih sedikit kata unik. Manusia menggunakan lebih banyak hapax legomena (kata yang hanya muncul sekali). Untuk meningkatkan: gunakan istilah domain-spesifik, campur register (formal + informal), masukkan kata dari bahasa daerah, gunakan bahasa figuratif yang spesifik, dan jangan hindari pengulangan kata yang sama demi siklus sinonim.

---

## Aturan Struktur Khas Indonesia

### BI-1. Jangan Heading "Kesimpulan" Otomatis

Gunakan bagian "Kesimpulan" hanya ketika genre mengharuskannya (contoh: makalah akademis, laporan formal, dokumen kepatuhan). Untuk esai, artikel, dan tulisan santai, tutup dalam prosa.

### BI-2. Jangan Pembuka Temporal

Jangan pernah mulai dengan "Di era modern ini," "Seiring perkembangan zaman," atau "Dalam konteks X yang semakin Y." Mulai dengan fakta spesifik, angka, atau adegan.

### BI-3. Batasi "Tidak Hanya...Tetapi Juga"

Pertahankan hanya ketika kontras benar-benar diperlukan dan menambah makna baru. Jika tidak, nyatakan apa sesuatu itu secara langsung.

### BI-4. Jangan "Merupakan Salah Satu X yang Paling Y"

Pernyataan kepentingan tanpa bukti. Kuantifikasi atau bandingkan secara spesifik sebagai gantinya.

### BI-5. Jangan Template "Di Sisi Lain, Terdapat Tantangan"

Sebutkan masalah konkret dan, jika memungkinkan, sertakan angka.

### BI-6. Jangan Padding "Dapat Dilihat Bahwa"

Hapus "dapat dilihat bahwa," "dapat dipahami bahwa," "perlu dipahami bahwa." Nyatakan temuannya.

### BI-7. Hindari "Di Mana" sebagai Kata Ganti Relatif

Tulis ulang "program di mana peserta akan..." sebagai "program yang..." atau kalimat langsung. "Di mana" sebagai kata ganti relatif adalah kalke dari bahasa Inggris "where" — tanda langsung tulisan AI.

### BI-8. Lebih Suka Kata Kerja daripada Nominalisasi

"Melatih" bukan "pelaksanaan pelatihan." "Mengembangkan" bukan "pengembangan kapasitas." "Membangun" bukan "pembangunan." AI mempelajari gaya birokrasi akademis Indonesia secara berlebihan — frasa kata benda berat yang menggantikan kata kerja sederhana.

### BI-9. Jangan Pasangan Formulaik "Tantangan dan Peluang"

AI suka memasangkan "tantangan dan peluang," "kelebihan dan kekurangan," "di satu sisi... di sisi lain..." Sebutkan masalah spesifik ATAU manfaat spesifik. Jangan pasangkan secara refleks.

### BI-10. Hindari Keseragaman Pasif

AI sering menulis terlalu banyak kalimat pasif berturut-turut: "Hal ini dilakukan..." "Perlu ditekankan..." "Dapat dilihat bahwa..." Campurkan kalimat aktif dan pasif. Dalam tulisan non-akademis, utamakan aktif.

---

# Aturan Konten

## Spesifisitas daripada Keumuman

Ganti setiap klaim generik dengan yang spesifik. "Banyak perusahaan" menjadi "tiga startup di Jakarta Selatan." "Berbagai faktor" menjadi faktor-faktor yang sebenarnya, disebutkan namanya. "Para ahli setuju" menjadi orang spesifik yang mengatakannya, dengan namanya.

## Jangan Atribusi Samar

Jangan pernah tulis "Para ahli berpendapat," "Pengamat mencatat," "Laporan industri menyarankan," "Menurut beberapa pihak," "Banyak yang percaya." Sebutkan sumber spesifik atau hapus atribusi sepenuhnya.

## Jangan Analisis Dangkal

Jangan pernah tempelkan komentar analitis pada fakta yang tidak membutuhkannya. Data populasi tidak butuh "menciptakan komunitas yang hidup." Tanggal pendirian tidak butuh "menandai momen penting dalam sejarah." Nyatakan fakta. Biarkan mereka berdiri. Jika pernyataan analitis bisa berlaku untuk subjek apa pun, tidak ada gunanya — hapus.

## Jangan Pernyataan Warisan/Signifikansi yang Berlebihan

Jangan pernah tulis tentang bagaimana sesuatu "berkontribusi pada" apa pun secara luas. Jangan pernah nyatakan bahwa sesuatu "mencerminkan tren yang lebih luas." Jangan pernah tegaskan bahwa fakta biasa memiliki "warisan abadi." Jika kepentingan ada, tunjukkan melalui bukti spesifik, bukan pernyataan.

## Tunjukkan Pendapat Nyata

Ambil posisi. "Pendekatan ini salah karena..." bukan "Beberapa berpendapat X, sementara yang lain berpendapat Y." AI menghindari secara refleks; manusia berkomitmen. Keseimbangan palsu adalah tanda AI — dunia nyata jarang seimbang sempurna.

## Tunjukkan Ketidakpastian yang Tulus Jika Sesuai

Ketika kamu tidak tahu sesuatu, katakan secara langsung. "Saya tidak yakin" atau "Saya tidak memiliki informasi yang cukup" menandakan pemikiran yang jujur. Gunakan penanda ketidakpastian dengan hemat tetapi tulus — bukan sebagai penghindaran ("bisa jadi diargumentasikan bahwa") tetapi sebagai kejujuran epistemik yang sebenarnya.

---

# Suara dan Tekstur

## Tambahkan Ketidaksempurnaan Manusiawi

Sertakan tekstur yang disengaja: redundansi yang dipertahankan untuk ritme, fragmen yang digunakan untuk penekanan, bagian santai dalam prosa formal, koreksi diri sesekali di tengah pemikiran ("—sebenarnya, kalau dipikir lagi..."). Ketidaksempurnaan ini menandakan pikiran yang nyata sedang bekerja. Tata bahasa yang terlalu sempurna justru adalah sinyal AI.

## Gunakan Pergeseran Register

Parentetikal santai mendadak dalam argumen formal. Istilah teknis yang jatuh ke dalam prosa percakapan. Humor yang menghantam dari samping. Pergeseran ini terbaca sebagai autentik karena AI tidak pernah menghasilkannya secara spontan. Studi stilometri menunjukkan register yang seragam adalah tanda AI paling konsisten.

## Referensikan Touchstone Spesifik

Sebutkan peristiwa nyata terkini, momen budaya pop yang spesifik, orang dan karya yang sebenarnya. Bukan "perkembangan terkini di bidang ini." Gunakan referensi budaya Indonesia: wayang, kuliner lokal, tradisi daerah, momen internet Indonesia yang viral.

## Orang Pertama Jika Sesuai

Gunakan "saya" atau "aku" ketika konteks memungkinkan. Bagikan pengalaman, pendapat, atau pengamatan spesifik. AI default ke generalisasi orang ketiga yang diabstraksikan karena tidak memiliki pengalaman hidup.

## Gunakan Partikel Wacana (Panduan Penggunaan)

Bahasa Indonesia alami menggunakan partikel wacana yang menandai suara manusia nyata. Ketiadaan total partikel adalah tanda AI nomor satu. Panduan penggunaan:

- **Sih** — penekanan lembut, kontradiksi ringan, pertanyaan retoris. "Nggak juga, sih." "Masa, sih?" "Bagus sih, tapi..."
- **Dong** — dorongan, harapan, permintaan. "Bantuin dong." "Jangan gitu dong."
- **Deh** — konsesi, penekanan ringan. "Iya deh." "Coba deh."
- **Lho/Loh** — kejutan, ketidakpercayaan. "Loh, kok bisa?" "Lho, serius?"
- **Nih** — penawaran, "ini" informal. "Nih, ambil aja." "Nih masalahnya..."
- **Tuh** — "itu" informal, menunjuk. "Tuh kan, bener." "Tuh udah dibilangin."
- **Kan** — konfirmasi, pengingat. "Kan udah dibilang." "Itu kan aneh."
- **Kok** — keheranan, "kenapa." "Kok gitu?" "Kok bisa?"
- **Ya** — persetujuan, pencarian konfirmasi. "Iya ya." "Gitu ya."
- **Nah** — penanda transisi, "nah begitu." "Nah, itu dia masalahnya."
- **Lah** — penekanan, pelembut. "Biasa lah." "Begitu lah."
- **Mah** — (Sunda/Jakarta) penekanan. "Gampang mah." "Kalau itu mah..."

Jangan paksakan partikel dalam tulisan formal akademis. Dalam konteks semi-formal (artikel opini, blog, ulasan), gunakan secukupnya. Dalam konteks santai, gunakan secara alami seperti percakapan.

## Sesuaikan Register Kata Ganti

AI terkunci pada "Anda" tanpa memperhatikan konteks. Ini tanda langsung.
- **Formal:** Anda, saya
- **Semi-formal:** kamu, saya/aku
- **Santai:** kamu, lo/lu, gue/aku
- **Akademis:** merujuk diri sebagai "peneliti" atau "penulis," bukan "saya"

Cocokkan register yang sebenarnya. Jangan pernah gunakan "Anda" dalam konteks yang jelas santai.

## Hindari Bahasa Indonesia Baku Murni dalam Konteks Santai

AI selalu menulis Indonesian formal. Ini membuat tulisan terasa seperti dokumen pemerintah. Ketika konteksnya informal, gunakan bentuk alami:

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

Bahasa Indonesia informal memendekkan prefiks meN- menjadi bentuk nasal. Aturan asimilasi nasal meN-:

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

AI hampir tidak pernah melakukan ini. Penggunaan prefiks formal yang konsisten dalam konteks santai adalah tanda AI yang sangat jelas — manusia Indonesia nyaris tidak pernah pakai prefiks lengkap dalam percakapan.

## Gunakan Interjeksi Emosional

Manusia Indonesia menggunakan interjeksi yang AI jarang pakai:
- **Duh/Aduh** — keluhan, rasa sakit, frustrasi
- **Waduh** — kaget, khawatir
- **Astaga** — terkejut
- **Buset/Busyet** — kaget (informal)
- **Ih** — jijik, terkejut ringan
- **Hah** — tidak percaya
- **Wah** — kagum

## Integrasikan Ungkapan dan Idiom Indonesia

Gunakan idiom Indonesia yang relevan untuk menambah tekstur. Bukan semua, tapi sesekali:
- "Besar pasak daripada tiang" — pengeluaran melebihi kemampuan
- "Tong kosong nyaring bunyinya" — yang paling berisik belum tentu paling berisi
- "Habis manis sepah dibuang" — dibuang setelah tidak berguna
- "Seperti katak dalam tempurung" — berpikiran sempit

AI hampir tidak pernah menggunakan ungkapan ini secara natural.

## Campur Bahasa (Code-switching) Jika Sesuai

Orang Indonesia secara natural mencampurkan bahasa Indonesia dengan bahasa Inggris, terutama dalam konteks bisnis, teknologi, dan percakapan anak muda:
- "Meeting-nya diundur ya"
- "Deadline-nya kapan?"
- "Gue udah submit, tinggal nunggu feedback"
- "Mindset-nya harus diubah"

AI jarang melakukan code-switching ini secara natural. Tapi jangan paksakan — gunakan hanya ketika konteks memungkinkan.

---

# Aturan Anti-Translationese

AI menulis Bahasa Indonesia yang terdengar seperti terjemahan dari bahasa Inggris. Ini disebut "translationese" — secara gramatikal benar tapi tidak natural. Aturan-aturan berikut mengatasi pola-pola translationese paling umum.

## TR-1. Jangan Over-Passive dengan "Oleh"

Bahasa Indonesia punya dua jenis pasif:
- **Pasif di-** (formal): "Buku itu dibaca oleh guru."
- **Pasif prokletik** (natural/informal): "Buku itu guru baca." atau "Buku itu saya baca."

AI hampir selalu menggunakan pasif di- dengan "oleh" — seperti terjemahan langsung dari "by" dalam bahasa Inggris. Manusia Indonesia jauh lebih sering menggunakan pasif prokletik atau kalimat aktif.

**Pola AI:** "Keputusan itu dibuat oleh tim manajemen."
**Natural:** "Tim manajemen yang bikin keputusan itu." atau "Keputusan itu tim manajemen yang buat."

Aturan: Kurangi "oleh" secara drastis. Gunakan pasif prokletik (pronomina + verba dasar) untuk register santai. Gunakan kalimat aktif jika memungkinkan.

## TR-2. Gunakan Struktur Topik-Komentar

Bahasa Indonesia adalah bahasa topic-prominent, bukan subject-prominent seperti Inggris. Kalimat natural Indonesia sering menempatkan topik di depan, bukan subjek gramatikal.

**Pola AI (subject-prominent, kalke Inggris):** "Program ini telah memberikan manfaat kepada masyarakat."
**Natural (topic-prominent):** "Kalau programnya, masyarakat udah mulai ngerasain manfaatnya."

Contoh lain:
- AI: "Saya sudah menyelesaikan pekerjaan itu." → Natural: "Pekerjaan itu, udah selesai."
- AI: "Mereka mengalami kesulitan." → Natural: "Kalau mereka, ya susah juga sih."

Aturan: Sesekali gunakan struktur topik-komentar. Mulai kalimat dengan topik yang dibahas, bukan selalu dengan subjek gramatikal.

## TR-3. Gunakan Pro-drop (Penghilangan Subjek)

Bahasa Indonesia membolehkan penghilangan subjek ketika konteksnya sudah jelas. AI selalu menyatakan subjek secara eksplisit — seperti bahasa Inggris yang memang mengharuskannya.

**Pola AI:** "Dia pergi ke pasar. Dia membeli sayuran. Dia kembali sore hari."
**Natural:** "Pergi ke pasar. Beli sayuran. Sore baru balik."

**Pola AI:** "Kami mengadakan rapat. Kami membahas anggaran. Kami menyetujui proposal."
**Natural:** "Ngadain rapat, bahas anggaran, terus setujuin proposalnya."

Aturan: Ketika subjek sudah jelas dari konteks, hilangkan. Pengulangan subjek yang tidak perlu adalah tanda translationese.

## TR-4. Jangan "Yang" Berlebihan

AI menggunakan "yang" secara berlebihan — mengkalke relative clause bahasa Inggris. Bahasa Indonesia natural lebih sering menghilangkan "yang" atau menyusun ulang kalimat.

**Pola AI:** "Orang yang tinggal di desa yang terletak di kaki gunung yang bernama Merapi."
**Natural:** "Orang desa di kaki Merapi."

**Pola AI:** "Strategi yang digunakan oleh perusahaan yang bergerak di bidang teknologi."
**Natural:** "Strategi perusahaan teknologi."

Aturan: Kurangi rantai "yang." Jika ada lebih dari dua "yang" dalam satu kalimat, susun ulang.

## TR-5. Jangan "Adalah" Berlebihan

AI menggunakan "adalah" terlalu sering — mengkalke kopula bahasa Inggris "is/are." Bahasa Indonesia sering tidak memerlukan kopula sama sekali.

**Pola AI:** "Indonesia adalah negara kepulauan. Jakarta adalah ibukotanya. Bahasa Indonesia adalah bahasa resminya."
**Natural:** "Indonesia negara kepulauan. Ibukotanya Jakarta. Bahasa resminya Bahasa Indonesia."

Aturan: Bahasa Indonesia sering tidak butuh "adalah." Hilangkan ketika konteks sudah jelas. Gunakan "adalah" hanya untuk penekanan identitas atau definisi formal.

## TR-6. Ejaan KBBI yang Konsisten

AI kadang membuat inkonsistensi ejaan yang manusia Indonesia juga sering buat — tapi pola inkonsistensinya berbeda. AI cenderung menggunakan bentuk yang lebih "populer" secara tidak konsisten:

- "praktek" vs "praktik" (KBBI: praktik)
- "kadaluarsa" vs "kedaluwarsa" (KBBI: kedaluwarsa)
- "aktifitas" vs "aktivitas" (KBBI: aktivitas)
- "nasehat" vs "nasihat" (KBBI: nasihat)
- "merubah" vs "mengubah" (KBBI: mengubah)
- "dikenakan" vs "dikenai" (tergantung konteks)

Aturan: Gunakan ejaan KBBI yang benar secara konsisten. Tapi di konteks informal, pilih satu bentuk dan pertahankan — inkonsistensi acak justru tanda AI, bukan manusia.

## TR-7. Konvensi Retorika Indonesia

Tulisan Indonesia punya konvensi retorika yang berbeda dari Inggris:

- **Penalaran induktif lebih umum:** Orang Indonesia sering menyajikan bukti/konteks dulu, baru kesimpulan — kebalikan dari Inggris yang langsung klaim di awal. Jangan selalu buka dengan tesis.
- **Pengembangan sirkuler:** Tulisan Indonesia natural kadang kembali ke poin yang sama dari sudut berbeda. AI menulis terlalu linear (poin A → poin B → poin C, tidak pernah kembali).
- **Hedging kultural:** Dalam budaya Indonesia, hedging ringan itu sopan, bukan lemah. "Sepertinya..." atau "Mungkin bisa dibilang..." bisa natural — bedakan dari hedging AI yang generik dan tanpa isi.
- **Peribahasa/Pepatah:** Manusia Indonesia kadang menyisipkan peribahasa. "Sedikit-sedikit, lama-lama jadi bukit" lebih natural daripada "Akumulasi usaha kecil menghasilkan hasil besar."

---

# Aturan Anti-Deteksi Turnitin

**CATATAN PENTING:** Per Maret 2026, Turnitin TIDAK mendukung deteksi AI untuk Bahasa Indonesia. Turnitin hanya mendukung bahasa Inggris (dan beberapa bahasa Eropa secara terbatas). Namun, aturan-aturan di bawah ini tetap relevan karena: (1) dosen/editor mungkin menggunakan detektor lain yang mendukung multi-bahasa (GPTZero, Originality.ai, Copyleaks), (2) prinsip stilometri berlaku universal lintas bahasa, (3) dukungan Turnitin untuk bahasa lain terus bertambah.

Berdasarkan riset tentang cara kerja detektor AI (Turnitin untuk Inggris, dan detektor multi-bahasa lainnya):

## T-1. Turnitin Menganalisis Ritme Paragraf
Turnitin tidak hanya melihat kalimat individual — ia menganalisis "ritme, alur, dan prediktabilitas seluruh paragraf." Pastikan setiap paragraf memiliki pola yang berbeda dari paragraf sebelumnya.

## T-2. Turnitin Menandai Tata Bahasa Terlalu Sempurna
Tata bahasa yang sempurna tanpa variasi adalah sinyal AI. Sertakan variasi natural: kalimat fragmen, kalimat berlari (run-on) yang disengaja, penggunaan tanda baca yang tidak sempurna.

## T-3. Turnitin Mendeteksi Keseragaman Register
Tulisan yang mempertahankan register yang persis sama dari awal sampai akhir terdeteksi sebagai AI. Sertakan setidaknya 2-3 pergeseran register per tulisan.

## T-4. Turnitin Mendeteksi Alat Humanizer
Turnitin (update Agustus 2025) secara khusus mendeteksi teks yang dimodifikasi oleh alat humanizer AI. Menandai dengan warna ungu (lebih buruk dari cyan). Jangan gunakan alat parafrase AI — tulis dengan benar sejak awal.

## T-5. Diversitas Transisi
Jangan gunakan transisi formulaik yang sama berulang. Gunakan: transisi implisit (tanpa kata penghubung), pertanyaan sebagai transisi, fragmen kalimat, ganti topik mendadak yang mendapat konteks di kalimat berikutnya.

---

# Daftar Periksa Pasca-Penulisan

Setelah menyusun draf, jalankan daftar periksa ini:

**Kosakata:**
1. Cari setiap kata dalam daftar larangan — ganti atau hapus masing-masing
2. Hapus semua contoh "berfungsi sebagai," "berperan sebagai," "adalah bukti dari," "menandai," "menyoroti pentingnya"
3. Hapus semua atribusi samar atau ganti dengan sumber yang disebutkan namanya
4. Cari buzzword AI (inovasi, holistik, kolaboratif, ekosistem, paradigma, optimalisasi, berkelanjutan, sinergi, transformasi digital, lanskap) — ganti dengan bahasa konkret

**Struktur:**
5. Temukan urutan 3+ kalimat dengan panjang serupa — susun ulang untuk bervariasi
6. Temukan daftar dengan tepat tiga item — tambahkan atau hapus satu
7. Periksa pembuka — jika dimulai dengan "Di era modern ini..." atau "Seiring perkembangan zaman..." tulis ulang dengan fakta spesifik
8. Periksa kalimat terakhir setiap paragraf — AI hampir selalu menambahkan pernyataan ulang yang berlebihan; hapus itu
9. Periksa frasa partisipatif yang menempel di akhir kalimat — tulis ulang sebagai kalimat tersendiri atau hapus
10. Hitung em dash — jika lebih dari satu per 500 kata, ganti sebagian dengan koma, tanda kurung, atau titik
11. Periksa variasi tipe kalimat — jika hanya kalimat deklaratif, tambahkan setidaknya satu pertanyaan atau kalimat perintah
12. Verifikasi pembuka paragraf — jika setiap paragraf dimulai dengan kalimat tesisnya, tulis ulang setidaknya dua untuk dimulai di tengah pemikiran

**Suara:**
13. Periksa register — apakah nada konsisten dengan konteks? Terlalu formal untuk blog? Terlalu santai untuk laporan?
14. Baca seluruh tulisan dengan keras — ritme AI yang canggung terdengar dengan cara yang tidak terlihat
15. Hitung pergeseran register — jika nol, tambahkan setidaknya dua (parentetikal santai, humor, koreksi diri)

**Tambahan Khusus Indonesia:**
16. Temukan semua "merupakan" — ganti sebagian besar dengan "adalah" atau susun ulang secara langsung
17. Hapus header bagian "Kesimpulan" otomatis kecuali format mengharuskannya
18. Temukan setiap "tidak hanya...tetapi juga" — pertahankan hanya ketika kontras diperlukan
19. Periksa pembuka — jika dimulai dengan "Di era" / "Seiring" / "Dalam konteks" — tulis ulang
20. Temukan semua rantai nominalisasi (pe-/ke-an/-an) — lebih suka bentuk kata kerja jika kejelasan meningkat
21. Temukan semua "dapat dilihat bahwa" / "dapat dipahami bahwa" — hapus dan nyatakan faktanya
22. Periksa register kata ganti — apakah "Anda" cocok dengan nada yang dimaksud?
23. Temukan semua klausa relatif "di mana" — tulis ulang sebagai kalimat langsung
24. Periksa keberadaan partikel wacana — jika konteks santai dan nol partikel (sih, dong, deh, kan, dll.), tambahkan secukupnya
25. Periksa penggunaan prefiks formal — jika konteks santai tapi semua kata menggunakan prefiks lengkap (mengerti, mencari, menonton), perbaiki
26. Cari pasangan formulaik "tantangan dan peluang" / "di satu sisi... di sisi lain..." — pisahkan atau hapus

**Anti-Translationese:**
27. Hitung "oleh" — jika lebih dari dua per halaman, ganti sebagian dengan pasif prokletik atau kalimat aktif
28. Cari rantai "yang" — jika ada lebih dari dua "yang" dalam satu kalimat, susun ulang
29. Periksa subjek berulang — jika subjek yang sama disebut 3+ kali berturut-turut, hilangkan yang tidak perlu (pro-drop)
30. Cari "adalah" berlebihan — hilangkan jika konteks sudah jelas tanpa kopula
31. Periksa apakah ada struktur topik-komentar — jika semua kalimat subject-prominent, ubah beberapa menjadi topic-prominent
32. Periksa linearitas — jika tulisan berjalan A→B→C→D tanpa pernah kembali, pertimbangkan pengembangan sirkuler
33. Periksa ulang akurasi semantik — pastikan setiap penggantian mempertahankan makna asli
