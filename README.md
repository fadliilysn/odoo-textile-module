
# Textile Management – Odoo ERP Custom Module

Custom ERP module berbasis **Odoo 19** yang dikembangkan untuk mendukung pengelolaan proses produksi pada industri tekstil.

Proyek ini berfokus pada pengembangan sistem **Production Order Management** untuk membantu pencatatan rencana produksi, pengelolaan informasi produk, penentuan jumlah produksi, penjadwalan, serta pemantauan tahapan proses produksi.

Proyek ini dikembangkan sebagai implementasi pembelajaran dan pengembangan mandiri dalam memahami ERP, business process, dan Odoo Development, khususnya pada industri manufaktur.

## Project Overview

Dalam proses manufaktur tekstil, perusahaan membutuhkan sistem untuk mengelola aktivitas produksi secara terstruktur. Informasi seperti produk yang akan diproduksi, jumlah produksi, tanggal produksi, deadline, dan penanggung jawab perlu dicatat agar proses produksi dapat dipantau dengan baik.

Melalui custom module ini, pengguna dapat membuat dan mengelola Production Order dengan alur kerja yang terstruktur, mulai dari tahap perencanaan hingga produksi selesai.

## Features

### 1. Production Order Management

- Membuat dan mengelola data Production Order.
- Memilih produk yang akan diproduksi melalui relasi dengan model produk bawaan Odoo (`product.product`).
- Mencatat jumlah produksi.
- Menentukan tanggal produksi dan deadline.
- Menentukan penanggung jawab produksi.

### 2. Automatic Production Order Number

- Nomor Production Order dibuat secara otomatis menggunakan fitur `ir.sequence` Odoo.
- Menggunakan format nomor produksi `PO/YYYY/00001`.
- Nomor produksi tidak dapat diubah secara manual melalui Form View.

### 3. Production Workflow Management

Modul menerapkan alur kerja produksi menggunakan field `Selection` dengan lima status:

| Status | Keterangan |
|---|---|
| Draft | Production Order baru dibuat dan masih dalam tahap perencanaan. |
| Confirmed | Production Order telah dikonfirmasi. |
| In Progress | Proses produksi sedang berlangsung. |
| Quality Check | Hasil produksi masuk ke tahap pemeriksaan kualitas. |
| Completed | Proses produksi telah selesai. |

Perubahan status dilakukan melalui tombol aksi pada Form View. Setiap tombol hanya tersedia sesuai dengan status saat ini untuk menjaga urutan proses bisnis.

### 4. Business Validation

Beberapa validasi diterapkan untuk menjaga konsistensi data:

- Jumlah produksi harus lebih besar dari 0.
- Deadline tidak boleh lebih awal daripada tanggal produksi.
- Data perencanaan hanya dapat diubah ketika Production Order masih berstatus Draft.
- Perubahan status harus mengikuti urutan workflow yang telah ditentukan.

### 5. User Interface

- **List View** untuk menampilkan daftar Production Order.
- **Form View** untuk membuat dan mengelola detail Production Order.
- **Statusbar** untuk memantau tahapan produksi.
- **Action Buttons** untuk menjalankan proses perubahan status.

## Application Preview

Screenshot berikut menampilkan implementasi custom module pada aplikasi Odoo.

### Production Order – List View

<!-- Tambahkan screenshot List View di sini -->
<!-- Contoh: ![Production Order List View](static/description/production_order_list.png) -->

### Production Order – Form View

<!-- Tambahkan screenshot Form View di sini -->
<!-- Contoh: ![Production Order Form View](static/description/production_order_form.png) -->

## Technology Stack

| Technology | Usage |
|---|---|
| Odoo 19 | ERP Framework |
| Python | Custom business logic dan model development |
| XML | View, menu, action, dan sequence configuration |
| PostgreSQL 15 | Database |
| Docker & Docker Compose | Application environment dan containerization |
| Git & GitHub | Version control dan project repository |

## Project Structure

```text
odoo-textile-module/
│
├── addons/
│   └── textile_management/
│       ├── __init__.py
│       ├── __manifest__.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── production_order.py
│       │
│       ├── views/
│       │   └── production_order_views.xml
│       │
│       ├── security/
│       │   └── ir.model.access.csv
│       │
│       └── data/
│           └── sequence.xml
│
├── .gitignore
└── docker-compose.yml
```

## Installation & Setup

### Prerequisites

- Docker Desktop
- Git
- Web browser

### Installation Steps

1. Clone repository:

   ```bash
   git clone <repository-url>
   cd odoo-textile-module
   ```

2. Jalankan container menggunakan Docker Compose:

   ```bash
   docker compose up -d
   ```

3. Buka aplikasi Odoo melalui browser:

   ```text
   http://localhost:8069
   ```

4. Buat atau gunakan database Odoo.

5. Aktifkan Developer Mode, kemudian buka menu Apps.

6. Perbarui daftar aplikasi melalui **Update Apps List**.

7. Cari modul **Textile Management**, kemudian klik Install.

## Skills Demonstrated

Melalui pengembangan modul ini, beberapa konsep dan keterampilan teknis yang dipraktikkan meliputi:

- Memahami konsep ERP dan business process pada industri manufaktur.
- Mengembangkan custom module pada Odoo.
- Membuat model dan field menggunakan Odoo ORM.
- Menggunakan relasi antar-model (`Many2one`).
- Mengimplementasikan automatic sequence menggunakan `ir.sequence`.
- Menerapkan business logic menggunakan Python.
- Membuat validasi data menggunakan `@api.constrains`.
- Mengimplementasikan workflow menggunakan `Selection` field dan object methods.
- Membuat tampilan menggunakan XML (List View dan Form View).
- Mengelola hak akses model melalui Access Control List.
- Menjalankan Odoo dan PostgreSQL menggunakan Docker Compose.
- Menggunakan Git dan GitHub untuk version control.

## Development Status

### Completed

- [x] Custom Odoo module setup.
- [x] Production Order model development.
- [x] Automatic Production Order numbering.
- [x] List View and Form View.
- [x] Production workflow implementation.
- [x] Business validation.
- [x] Basic access control configuration.

### Planned

- [ ] Production Log Management.
- [ ] Production performance monitoring.
- [ ] Additional manufacturing features.

Proyek ini masih dalam tahap pengembangan bertahap. Fitur berikutnya direncanakan untuk memperluas pencatatan aktivitas produksi dan pemantauan hasil produksi.

---

**Project Focus:** Odoo ERP Development | Manufacturing Process Management | Textile Industry
