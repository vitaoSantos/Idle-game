# Verificação mecânica do documento do VIC-6 (qa-analista, 2026-10-31).
# Uso: python3 -I docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py docs/pesquisa/idle-rpg-referencias.md
# Confere: (1) tags de fonte por família usadas x definidas; (2) campos por jogo comparável (idle, social, monetização);
# (3) fontes por reclamação; (4) marcas de confiança e ressalvas; (5) hosts; (6) contagens de seções; (7) contas citadas.
import re, sys, collections

txt = open(sys.argv[1], encoding="utf-8").read()
body, src = txt.split("## 6. Fontes")

print("== (1) tags de fonte ==")
fam = {"M": 38, "C": 97, "P": 21, "T": 23, "L": 25, "R": 5}
used = set(re.findall(r"\[([MCPTLR]\d{1,2})\]", body))
defined = set(re.findall(r"^\| ([MCPTLR]\d{1,2}) \|", src, flags=re.M))
for f, n in fam.items():
    u = {t for t in used if t[0] == f}; d = {t for t in defined if t[0] == f}
    print(f"família {f}: esperadas {n} | definidas {len(d)} | usadas {len(u)}")
print("usadas e NÃO definidas:", sorted(used - defined))
print("definidas e NÃO usadas:", sorted(defined - used, key=lambda x: (x[0], int(x[1:]))))
print("total definidas:", len(defined))

print("\n== (2) campos por jogo comparável (seções 2.2 a 2.10) ==")
partes = re.split(r"\n### (2\.\d+) ", body)
for i in range(1, len(partes), 2):
    num, corpo = partes[i], partes[i + 1]
    if num in ("2.11",): continue
    titulo = corpo.split("\n")[0]
    tem = {k: (f"**{k}" in corpo) for k in ("Farm idle e offline", "Social", "Monetização", "Reclamações")}
    social = re.search(r"\*\*Social:\*\*(.*)", corpo)
    nd = bool(social and re.search(r"não detalh|nenhum", social.group(1), flags=re.I))
    print(f"{num} {titulo[:42]:42s} campos={sum(tem.values())}/4 social_sem_detalhe_ou_inexistente={nd}")

print("\n== (3) fontes por reclamação (seção 4) ==")
sec4 = body.split("## 4. Reclamações comuns dos jogadores")[1].split("## 5.")[0]
for linha in sec4.splitlines():
    m = re.match(r"\| (\d+) \| (.*?) \|", linha)
    if m:
        tags = set(re.findall(r"\[([A-Z]\d+)\]", linha))
        print(f"#{m.group(1):>2} fontes={len(tags):2d}  {m.group(2)[:60]}")

print("\n== (4) marcas de confiança e ressalvas ==")
for chave in ("confiança baixa", "Confiança", "| Alta |", "| Média |", "| Baixa |", "não verificado", "não confirmad", "atribuição provável",
              "cálculo nosso", "Cálculo nosso", "Não encontramos", "não encontramos", "não detalhad"):
    print(f"{chave:22s} {body.count(chave)}")

print("\n== (5) hosts ==")
urls = re.findall(r"https?://[^\s)\]>,|]+", src)
hosts = collections.Counter(re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls)
print("URLs:", len(urls), "| hosts:", len(hosts))
for h in ("apps.apple.com", "play.google.com", "reddit.com", "sensortower.com", "toucharcade.com", "supercheats.com", "support.google.com", "developer.apple.com"):
    print("  ", h, sum(c for k, c in hosts.items() if h in k))

print("\n== (6) contagens ==")
tab21 = body.split("### 2.1 Tabela comparativa")[1].split("### 2.2")[0]
print("jogos na tabela 2.1:", len([l for l in tab21.splitlines() if l.startswith("| ") and not l.startswith("| Jogo ") and not l.startswith("|---")]))
print("oportunidades (5.1):", len(re.findall(r"^\| \d+ \| (?!\*\*)", body.split('### 5.1 Oportunidades')[1].split('### 5.2')[0], flags=re.M)))
print("riscos (5.2):", len(re.findall(r"^\| \d+ \| \*\*", body.split('### 5.2 Riscos')[1].split('### 5.3')[0], flags=re.M)))
print("hipóteses (5.3):", len(re.findall(r"^\| H\d \|", body, flags=re.M)), "| perguntas (5.4):", len(re.findall(r"^\d+\. \*\*", body.split('### 5.4')[1].split('---')[0], flags=re.M)))

print("\n== (7) contas citadas ==")
print("pontos de habilidade: 20 x 10 min =", 20*10, "min =", divmod(20*10, 60), "| VIP 4 (40):", divmod(40*10, 60))
print("8 h fora: gera", 8*60//10, "| perde", 8*60//10 - 20, f"({100*(8*60//10 - 20)/(8*60//10):.0f}%)")
for dia, usd in ((30, 0.99), (150, 4.99), (300, 9.99), (600, 19.99), (3000, 99.99)):
    print(f"  {dia} diamantes por US$ {usd}: {dia/usd:.2f} por dólar")
print("lendário: 15.000 / 30 =", 15000/30, "dólares | por soul stone (80):", 15000/80, "diamantes")
print("Nexon KFTC: ₩ 11,6 bi ~ US$ 8,9 mi => câmbio implícito", round(11.6e9/8.9e6), "₩/US$")
print("ECA Digital: 17/03/2026 cai numa", ["segunda","terça","quarta","quinta","sexta","sábado","domingo"][__import__('datetime').date(2026,3,17).weekday()], "(fontes: 'terça-feira, 17')")
