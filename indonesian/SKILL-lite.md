---
name: anti-slop-writing-id-lite
description: Versi ringkas untuk platform dengan batas karakter ketat (ChatGPT Custom Instructions, dll). Tulis Bahasa Indonesia yang jelas dan sesuai suara yang diminta. Untuk aturan lengkap, pakai SKILL.md.
---

# Anti-Slop ID (Lite)

**Versi 4.0, 27 September 2026.** Berlaku lintas ChatGPT/OpenAI, Claude/Anthropic, Gemini/Google, dan Grok/xAI. Model dan tanggal rilis yang diverifikasi ada di [references/model-coverage.md](references/model-coverage.md); rollout dan ketersediaan bisa berbeda.

Tulis Bahasa Indonesia yang jelas, spesifik, dan sesuai konteks serta suara penulis.

## Pilih Tier Tone

Tentukan satu sebelum nulis. Default: **semi-formal**.

- **Formal**: makalah, laporan, dokumen kantor. Kata ganti: saya, Anda. Utamakan bentuk lengkap; partikel wacana biasanya dihindari kecuali sesuai konteks.
- **Semi-formal** (DEFAULT): blog, opini, newsletter, LinkedIn. Kata ganti: saya/aku, kamu. Kontraksi dan partikel wacana sesekali, bila alami.
- **Informal**: Twitter/X, Instagram, blog santai, TikTok. Kata ganti: aku/gw, kamu/lo. Kontraksi bebas. Partikel wacana natural.

Pilih satu register yang sesuai. Pergeseran hanya bila cocok dengan audiens dan tujuan.

## Dilarang Mutlak

1. **Tanda baca**: hindari em dash dan en dash pada prosa baru secara default. Pertahankan dalam kutipan atau bila format, gaya, atau instruksi memintanya.
2. **Pembuka temporal**: "Di era modern ini," "Seiring perkembangan zaman," "Dalam konteks X yang semakin Y." Mulai dengan fakta, angka, atau adegan.
3. **Kosakata puffery**: sangat krusial, fundamental (pujian samar), komprehensif, holistik, inovatif, dinamis, inklusif, transformasi digital, ekosistem, paradigma, sinergi, optimalisasi, lanskap.
4. **Kata kerja AI**: menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan, mengedepankan, menyelami (= "delve"), berkontribusi pada.
5. **Pasangan formulaik**: "tantangan dan peluang", "di satu sisi... di sisi lain", "tidak hanya X tetapi juga Y", "kelebihan dan kekurangan".
6. **Atribusi samar**: "para ahli", "penelitian menunjukkan", "banyak pihak", "studi menunjukkan" tanpa nama. Sebutkan sumber spesifik atau hapus.
7. **Penutup AI**: "Sebagai kesimpulan,", "Dapat disimpulkan bahwa", "Secara keseluruhan,", "Pada akhirnya,".
8. **Klausa partisipatif tempelan**: ", yang menyoroti pentingnya...", ", menggarisbawahi signifikansi...", ", mencerminkan tren yang lebih luas...". Jadikan kalimat sendiri atau hapus.

## Pegangan Menulis

1. **Variasi kalimat secukupnya**: ubah panjang atau struktur jika membantu alur. Jangan memaksakan fragmen atau pola pendek-panjang.
2. **Daftar**: pilih jumlah butir sesuai isi, bukan pola tertentu.
3. **Spesifisitas yang akurat**: sebutkan nama, angka, atau waktu hanya jika tersedia dan dapat diverifikasi. Jangan mengarang pengalaman atau data.
4. **Periksa rantai "yang"**: susun ulang bila kalimat menjadi sulit dibaca.
5. **Pilih bentuk aktif/pasif** sesuai fokus kalimat; hindari "oleh" bila pelakunya tidak perlu disebut.
6. **Kurangi "adalah"**: bahasa Indonesia sering nggak butuh kopula. "Indonesia negara kepulauan" cukup.
7. **Pro-drop**: kalau subjek udah jelas, hilangkan. Jangan ulang "dia, dia, dia" atau "saya, saya, saya".
8. **Hindari "di mana" sebagai klausa relatif** bila "yang" atau susunan ulang terdengar lebih alami.
9. **Lebih suka kata kerja daripada nominalisasi**: "melatih" bukan "pelaksanaan pelatihan".
10. **Partikel wacana di tier 2/3**: sih, kan, kok, deh, lho, nih, tuh. Pakai bila alami, tanpa kuota.
11. Hapus scaffolding chat dan uraian proses yang bukan bagian dari hasil yang diminta.
12. Buang reassurance, promosi, atau gaya edgy yang tidak diminta. Pertahankan fakta, sumber, kutipan, dan ketidakpastian.
13. Ikuti format serta register yang diminta. Jangan menyisipkan kesalahan atau pengalaman pribadi rekaan demi kesan autentik.

## Checklist Cepat

Setelah draft selesai:
1. Tinjau tanda baca dan pastikan mendukung makna serta register.
2. Cari pembuka "Di era" / "Seiring" / "Dalam konteks" → tulis ulang dengan fakta spesifik.
3. Cari "merupakan" dan "tidak hanya...tetapi juga" → susun ulang.
4. Hitung "yang" dalam kalimat terpanjang → kurangi kalau >2.
5. Cek variasi panjang kalimat → ubah hanya jika ritmenya terasa monoton.
6. Cek tier konsistensi → apakah "Anda" cocok? Atau "kamu"? Atau "lo/gw"?
7. Baca keras-keras → periksa kelancaran, makna, dan kesesuaian suara.
