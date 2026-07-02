# Tugas UAS Teknik Kompilasi
## Simulasi Tahapan Kompilasi pada Konstruksi If-Else

### Identitas Mahasiswa
- **Nama** : Heri Purnomo
- **NIM** : 231011400127
- **Kelas** : 06TPLE003
- **Mata Kuliah** : Teknik Kompilasi

---

## Deskripsi Proyek
Proyek ini merupakan simulasi sederhana tahapan proses kompilasi pada konstruksi **If-Else** menggunakan bahasa **Python**.

Tahapan yang direpresentasikan:
1. Analisis Leksikal (*Lexical Analysis*)
2. Analisis Sintaksis (*Syntax Analysis*)
3. Analisis Semantik (*Semantic Analysis*)
4. Generasi Kode Antara (*Three Address Code / TAC*)

---

## Konstruksi yang Dipilih

```text
if ( x > 5 ) {
    y = 1
}
else {
    y = 0
}
```

---

## Pattern (BNF)

```bnf
<if_stmt> ::= "if" "(" <condition> ")" "{" <statement> "}" "else" "{" <statement> "}"

<condition> ::= <identifier> <operator> <number>

<statement> ::= <identifier> "=" <number>
```

---

## Tahapan Kompilasi

### 1. Analisis Leksikal
Memecah source code menjadi token seperti:
- KEYWORD
- IDENTIFIER
- NUMBER
- OPERATOR
- BRACE
- PARENTHESIS

### 2. Analisis Sintaksis
Memeriksa apakah struktur `if-else` sesuai dengan aturan grammar dan membentuk Abstract Syntax Tree (AST).

### 3. Analisis Semantik
Melakukan pengecekan:
- keberadaan variabel,
- validasi tipe data,
- kesesuaian nilai pada kondisi.

### 4. Three Address Code (TAC)

```text
ifFalse x > 5 goto L1
y = 1
goto L2
L1:
y = 0
L2:
```

---

## Struktur Project

```text
HERI PURNOMO-UAS-Teknik-Kompilasi/
│
├── mini_compiler_ifelse.py
├── dokumentasi.md
├── README.md
└── screenshot/
```

---

## Cara Menjalankan Program

```bash
python mini_compiler_ifelse.py
```

atau

```bash
python3 mini_compiler_ifelse.py
```

---

## Kesimpulan
Program berhasil mensimulasikan tahapan utama dalam proses kompilasi mulai dari analisis leksikal, sintaksis, semantik, hingga pembangkitan kode antara berupa Three Address Code (TAC) pada konstruksi `if-else`.

---

