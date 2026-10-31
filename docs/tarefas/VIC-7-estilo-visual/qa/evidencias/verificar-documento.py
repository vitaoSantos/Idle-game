# Verificação mecânica do documento do VIC-7 (qa-analista, 2026-10-31).
# Uso: python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md
# Confere: (1) tags de fonte usadas x definidas; (2) contagem das marcas de confiança;
# (3) URLs e hosts; (4) recálculo das somas, da sensibilidade e das contas de memória e escala.
import re, sys, collections

txt = open(sys.argv[1], encoding="utf-8").read()
body, src = txt.split("## 9. Fontes")

used = set(re.findall(r"\[([MPCXG]\d{1,2})\]", body))
defined = set(re.findall(r"^- \[([MPCXG]\d{1,2})\]", src, flags=re.M))
print("tags usadas no corpo:", len(used), "| definidas na seção 9:", len(defined))
print("usadas e NÃO definidas:", sorted(used - defined))
print("definidas e NÃO usadas no corpo:", sorted(defined - used))

marks = collections.Counter()
for m in re.findall(r"\[(F fraca|F \+ I|F \+ cálculo|F|I|N|I, a validar[^\]]*|cálculo[^\]]*|N:[^\]]*)\]", body):
    marks[m.split(",")[0].split(":")[0]] += 1
total = sum(marks.values())
fraco = marks["F fraca"] + marks["I"] + marks["N"]
print("marcas de confiança (corpo):", dict(marks), "| total:", total,
      "| F fraca + I + N:", fraco, f"({100*fraco/total:.0f}%)")

urls = re.findall(r"https?://[^\s)\]>,]+", txt)
hosts = collections.Counter(re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls)
print("URLs:", len(urls), "| hosts distintos:", len(hosts))
for h, c in sorted(hosts.items(), key=lambda x: -x[1])[:8]:
    print("  ", h, c)

pix = [3, 3, 4, 3, 3, 5, 4]; car = [4, 4, 3, 3, 3, 3, 4]
def pesos(w): return sum(a*b for a, b in zip(pix, w)), sum(a*b for a, b in zip(car, w))
print("soma simples (pixel, cartoon):", pesos([1]*7), "(documento: 25 e 24)")
print("peso 2 nos critérios 1 e 2:", pesos([2, 2, 1, 1, 1, 1, 1]), "(documento: 31 e 32)")
print("peso 2 nos critérios 3 e 6:", pesos([1, 1, 2, 1, 1, 2, 1]), "(documento: 34 e 30)")
print("30 quadros 64x64 =", 30*64*64, "px; atlas 256x512 =", 256*512, "px =", 256*512*4/2**20, "MiB; 30 classes =", 30*256*512*4/2**20, "MiB")
print("atlas 1024x1024 =", 1024*1024*4/2**20, "MiB; 30 classes =", 30*4, "MiB")
print("1080x2400: /3 =", (1080/3, 2400/3), "/4 =", (1080/4, 2400/4), "| 1440x3200 /4 =", (1440/4, 3200/4))
print("pilha confortável de pixel: 20 + 65 =", 20 + 65)
