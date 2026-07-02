# Dokumentasi Tugas UAS Teknik Kompilasi
## Simulasi Tahapan Kompilasi pada Konstruksi If-Else

### Identitas Mahasiswa
- Nama : Heri Purnomo
- NIM : 231011400127
- Kelas : 06TPLE003
- Mata Kuliah : Teknik Kompilasi

---

# 1. Pendahuluan

Compiler merupakan program yang berfungsi untuk menerjemahkan source code ke dalam bahasa yang dapat dipahami oleh komputer. Dalam prosesnya, compiler memiliki beberapa tahapan, yaitu analisis leksikal, analisis sintaksis, analisis semantik, dan generasi kode.

Pada tugas ini dipilih konstruksi **If-Else** untuk mensimulasikan tahapan kompilasi tersebut menggunakan bahasa pemrograman Python.

---

# 2. Konstruksi yang Dipilih

Source code yang digunakan:

```text
if ( x > 5 ) {
    y = 1
}
else {
    y = 0
}
```

---

# 3. Pattern (BNF)

Grammar yang digunakan adalah:

```bnf
<if_stmt> ::= "if" "(" <condition> ")" "{" <statement> "}" "else" "{" <statement> "}"

<condition> ::= <identifier> <operator> <number>

<statement> ::= <identifier> "=" <number>
```

Keterangan:
- `<if_stmt>` : struktur percabangan if-else.
- `<condition>` : kondisi yang akan diperiksa.
- `<statement>` : perintah yang akan dijalankan.

---

# 4. Analisis Leksikal (Lexical Analysis)

Tahap ini bertujuan memecah source code menjadi token.

Contoh token yang dihasilkan:

| Lexeme | Token |
|--------|--------|
| if | KEYWORD |
| x | IDENTIFIER |
| > | OPERATOR |
| 5 | NUMBER |
| else | KEYWORD |
| y | IDENTIFIER |
| = | OPERATOR |
| 1 | NUMBER |
| 0 | NUMBER |

Hasil dari tahap ini akan digunakan pada tahap sintaksis.

---

# 5. Analisis Sintaksis (Syntax Analysis)

Tahap sintaksis bertujuan untuk memeriksa apakah susunan token sesuai dengan grammar yang telah ditentukan.

Program akan memeriksa:
- keberadaan keyword `if`
- keberadaan keyword `else`
- keseimbangan tanda kurung `()`
- keseimbangan tanda kurung kurawal `{}`

Jika terjadi kesalahan, program akan menghasilkan pesan error.

---

# 6. Abstract Syntax Tree (AST)

AST yang terbentuk:

```text
IfElseStatement
├── Condition
│   ├── x
│   ├── >
│   └── 5
├── IfBody
│   └── y = 1
└── ElseBody
    └── y = 0
```

AST digunakan untuk merepresentasikan struktur program secara sederhana dan menjadi dasar dalam pembangkitan kode antara.

---

# 7. Analisis Semantik (Semantic Analysis)

Tahap semantik melakukan pengecekan:

1. Variabel yang digunakan telah dideklarasikan.
2. Nilai pembanding bertipe angka.
3. Struktur kondisi sesuai dengan aturan yang berlaku.

Contoh kesalahan:

```text
if ( x > lima )
```

akan menghasilkan:

```text
Semantic Error:
Nilai pembanding harus berupa angka.
```

---

# 8. Three Address Code (TAC)

Hasil generasi TAC:

```text
ifFalse x > 5 goto L1
y = 1
goto L2
L1:
y = 0
L2:
```

Penjelasan:

- `ifFalse` digunakan untuk mengecek kondisi.
- `goto` digunakan untuk berpindah ke label tertentu.
- `L1` dan `L2` merupakan label yang mewakili percabangan program.

---

# 9. Cara Menjalankan Program

Buka terminal pada folder project kemudian jalankan:

```bash
python mini_compiler_ifelse.py
```

atau

```bash
python3 mini_compiler_ifelse.py
```

---

# 10. Kesimpulan

Program berhasil mensimulasikan tahapan utama pada proses kompilasi, yaitu analisis leksikal, analisis sintaksis, analisis semantik, dan generasi kode antara berupa Three Address Code (TAC) pada konstruksi If-Else. Dengan simulasi ini, proses kerja compiler menjadi lebih mudah dipahami.

---

**Heri Purnomo**  
**231011400127**  
**06TPLE003**
