# Panduan: kerjakan di Theia Lab

Proyek sudah disiapkan di folder `final_project` di komputer Anda. **API Watson** (`sn-watson-emotion.labs.skills.network`) hanya bisa diakses dari **Skills Network Theia Lab**, tidak dari jaringan rumah/kantor biasa.

## Yang sudah selesai di lokal

| Task | Status |
|------|--------|
| 1 | Repo di-clone; `README.md` berisi teks **Final project** |
| 2–3 | `emotion_detection.py` — Watson API + format output + handling HTTP 400 |
| 4 | Paket `EmotionDetection/` + `__init__.py` |
| 5 | `test_emotion_detection.py` (5 unit test) |
| 6–7 | `server.py` — Flask `/`, `/emotionDetector`, pesan error blank |
| 8 | `pylint server.py` → **10.00/10** (lihat `deliverables/8b_static_code_analysis.txt`) |

**Tidak ada push ke Git** (sesuai permintaan Anda).

## Langkah di Theia Lab

1. Salin folder `final_project` ke lab (upload zip, atau fork/clone repo Anda sendiri lalu salin file-file ini).
2. Di terminal lab:
   ```bash
   cd final_project
   pip install -r requirements.txt
   ```
3. **Task 2b / 3b / 4b / 5b** — jalankan tes API & unit test:
   ```bash
   python3
   >>> from emotion_detection import emotion_detector
   >>> emotion_detector("I love this new technology.")
   >>> emotion_detector("I am so happy I am doing this.")
   ```
   ```bash
   python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I hate working long hours.'))"
   python3 test_emotion_detection.py
   ```
   Simpan output terminal ke file di `deliverables/` (2b, 3b, 4b, 5b).
4. **Task 6** — jalankan server dan screenshot:
   ```bash
   python3 server.py
   ```
   Buka `http://localhost:5000`, uji kalimat **"I think I am having fun"** → screenshot `6b_deployment_test.png`.
5. **Task 7c** — submit kosong, klik Run → harus muncul **Invalid text! Please try again!** → screenshot `7c_error_handling_interface.png`.
6. **Task 1 & 4 (URL GitHub)** — hanya jika Anda fork ke GitHub publik dan push sendiri (opsional untuk tugas; Anda memilih tidak push dari sini).

File teks untuk Option 1 (AI grader) sudah disiapkan di folder `deliverables/`.
