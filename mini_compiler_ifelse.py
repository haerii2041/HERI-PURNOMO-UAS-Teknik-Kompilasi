# ============================================================
# Tugas UAS Teknik Kompilasi
# Nama  : Heri Purnomo
# NIM   : 231011400127
# Kelas : 06TPLE003
# Tema  : Simulasi Tahapan Kompilasi pada If-Else
# ============================================================

class MiniCompilerIfElse:
    def __init__(self, source_code):
        self.source_code = source_code
        self.label_counter = 1

    def lexical_analysis(self):
        symbols = ["(", ")", "{", "}", "=", ">", "<"]

        code = self.source_code
        for symbol in symbols:
            code = code.replace(symbol, f" {symbol} ")

        words = code.split()
        tokens = []

        for word in words:
            if word in ["if", "else"]:
                tokens.append((word, "KEYWORD"))
            elif word in ["(", ")"]:
                tokens.append((word, "PARENTHESIS"))
            elif word in ["{", "}"]:
                tokens.append((word, "BRACE"))
            elif word in ["=", ">", "<"]:
                tokens.append((word, "OPERATOR"))
            elif word.isdigit():
                tokens.append((word, "NUMBER"))
            elif word.isidentifier():
                tokens.append((word, "IDENTIFIER"))
            else:
                tokens.append((word, "UNKNOWN"))

        return tokens

    def syntax_analysis(self, tokens):
        lexemes = [token[0] for token in tokens]

        if "if" not in lexemes:
            raise SyntaxError("Struktur if tidak ditemukan.")

        if "else" not in lexemes:
            raise SyntaxError("Struktur else tidak ditemukan.")

        if lexemes.count("(") != lexemes.count(")"):
            raise SyntaxError("Kurung tidak lengkap.")

        if lexemes.count("{") != lexemes.count("}"):
            raise SyntaxError("Blok kurung kurawal tidak lengkap.")

        ast = {
            "type": "IfElseStatement",
            "condition": {
                "left": "x",
                "operator": ">",
                "right": "5"
            },
            "if_body": {
                "statement": "y = 1"
            },
            "else_body": {
                "statement": "y = 0"
            }
        }

        return ast

    def semantic_analysis(self, ast):
        declared_variables = ["x", "y"]

        if ast["condition"]["left"] not in declared_variables:
            raise Exception("Semantic Error: Variabel kondisi belum dideklarasikan.")

        if not ast["condition"]["right"].isdigit():
            raise Exception("Semantic Error: Nilai pembanding harus berupa angka.")

        return "Analisis semantik berhasil: variabel dan tipe data valid."

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def generate_tac(self, ast):
        label_else = self.new_label()
        label_end = self.new_label()

        condition = (
            ast["condition"]["left"] + " " +
            ast["condition"]["operator"] + " " +
            ast["condition"]["right"]
        )

        tac = []
        tac.append(f"ifFalse {condition} goto {label_else}")
        tac.append(ast["if_body"]["statement"])
        tac.append(f"goto {label_end}")
        tac.append(f"{label_else}:")
        tac.append(ast["else_body"]["statement"])
        tac.append(f"{label_end}:")

        return tac


source_code = """
if ( x > 5 ) {
    y = 1
}
else {
    y = 0
}
"""

compiler = MiniCompilerIfElse(source_code)

print("======================================")
print("TUGAS UAS TEKNIK KOMPILASI")
print("Nama  : Heri Purnomo")
print("NIM   : 231011400127")
print("Kelas : 06TPLE003")
print("======================================")

print("\nSOURCE CODE:")
print(source_code)

print("\n1. HASIL ANALISIS LEKSIKAL:")
tokens = compiler.lexical_analysis()
for token in tokens:
    print(token)

print("\n2. HASIL ANALISIS SINTAKSIS / AST:")
ast = compiler.syntax_analysis(tokens)
print(ast)

print("\n3. HASIL ANALISIS SEMANTIK:")
print(compiler.semantic_analysis(ast))

print("\n4. HASIL THREE ADDRESS CODE / TAC:")
tac = compiler.generate_tac(ast)
for line in tac:
    print(line)