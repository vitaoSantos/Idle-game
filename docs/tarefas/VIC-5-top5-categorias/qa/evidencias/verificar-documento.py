# Verificação mecânica do documento do VIC-5 (qa-analista, 2026-10-31).
# Uso: python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md
# Confere: (1) notas do ranking pela fórmula 0,4/0,3/0,3; (2) sensibilidade (pesos iguais e testes de robustez);
# (3) tags de fonte usadas x definidas; (4) marcas [secundária]/[antigo]/[sem data]; (5) contas derivadas citadas no texto.
import re, sys, collections

txt = open(sys.argv[1], encoding="utf-8").read()
body, src = txt.split("## 10. Fontes")

# (1) ranking: (C1, C2, C3, nota declarada)
cats = {
 "Puzzle": (5, 4, 5, 4.7), "Estratégia 4X casual": (3, 5, 5, 4.2), "Sandbox social/UGC": (3, 4, 4.5, 3.8),
 "Híbrido-casual": (5, 2, 3, 3.5), "Jogos web instantâneos": (3.5, 3, 3, 3.2), "Cassino/coin looter": (1.5, 4, 4, 3.0),
 "Shooter": (3, 2, 4, 3.0), "RPG (inclui idle RPG)": (1, 4, 3, 2.5), "Simulação casual": (2, 1.5, 2, 1.9)}
def nota(c1, c2, c3, w=(0.4, 0.3, 0.3)): return w[0]*c1 + w[1]*c2 + w[2]*c3
print("== (1) notas recalculadas (peso 0,4/0,3/0,3) ==")
for k, (a, b, c, decl) in cats.items():
    n = nota(a, b, c)
    flag = "OK" if abs(n - decl) < 0.051 else "DIVERGE"
    print(f"{k:28s} calculado={n:.3f} declarado={decl} {flag}")
print("\n== (2) sensibilidade ==")
eq = {k: nota(a, b, c, (1/3, 1/3, 1/3)) for k, (a, b, c, _) in cats.items()}
for k, v in sorted(eq.items(), key=lambda x: -x[1]): print(f"pesos iguais: {k:28s} {v:.2f}")
print("web x cassino com pesos iguais:", round(eq['Jogos web instantâneos'], 3), round(eq['Cassino/coin looter'], 3))
for c2 in (2, 3, 4):
    s = nota(3, c2, 4); w = nota(3.5, 3, 3)
    print(f"Shooter com C2={c2}: {s:.2f} (web = {w:.2f}) -> {'passa a web' if s > w + 1e-9 else 'não passa a web'}")
for c2 in (3, 4, 5):
    print(f"Cassino com C2={c2}: {nota(1.5, c2, 4):.2f}")
print("só crescimento (C1): ", sorted(((v[0], k) for k, v in cats.items()), reverse=True)[:6])

# (3) tags de fonte
used = set(re.findall(r"\[(\d{1,2}|B)\]", body))
defined = set(re.findall(r"^\| \[(\d{1,2}|B)\] \|", src, flags=re.M))
print("\n== (3) fontes ==")
print("tags usadas:", len(used), "| definidas:", len(defined))
print("usadas e NÃO definidas:", sorted(used - defined, key=lambda x: (x == 'B', int(x) if x != 'B' else 0)))
print("definidas e NÃO usadas:", sorted(defined - used, key=lambda x: (x == 'B', int(x) if x != 'B' else 0)))
urls = re.findall(r"https?://[^\s)\]|,]+", src)
hosts = collections.Counter(re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls)
print("URLs:", len(urls), "| hosts:", len(hosts), "| top:", hosts.most_common(6))
for h in ("sensortower.com", "x.com", "www.sec.gov"):
    print("  host", h, "->", sum(c for k, c in hosts.items() if h in k), "URLs")

# (4) marcas
print("\n== (4) marcas ==")
for m in ("[secundária", "[antigo]", "[sem data]", "estimativa", "reportado pela empresa", "pesquisa (amostra)"):
    print(f"{m:26s} {body.count(m)}")
print("'Não encontrei' no corpo:", len(re.findall(r"Não encontrei|não encontrei", body)))
print("'Ficaram sem levantamento' (seção 9):", "Ficaram sem levantamento" in body)

# (5) contas derivadas citadas
print("\n== (5) contas derivadas ==")
print("H1 2026 IAP: 39,8 / 40,6 =", f"{(39.8/40.6-1)*100:.2f}%", "(documento: -2%)")
print("AppMagic puzzle: 6,3 -> 7,6 =", f"{(7.6/6.3-1)*100:.1f}%", "(documento: ~+20%)")
print("Sensor Tower: estratégia 9,3 - puzzle 8,1 =", round(9.3-8.1, 2), "(documento: 1,2)")
print("RPG: 11,6 / 13,7 =", f"{(11.6/13.7-1)*100:.2f}%", "(documento: -15,4%; diferença de arredondamento das entradas)")
print("Roblox 2025: bookings 6,8 (+55%) -> base 2024 =", round(6.8/1.55, 2), "| receita 4,9 (+36%) -> base 2024 =", round(4.9/1.36, 2))
print("Roblox 4T25: 2,22 (+63%) -> base =", round(2.22/1.63, 2), "| DAU 144 (+69%) -> base =", round(144/1.69, 1))
print("D7 meta 8% / mediana 3,4–3,9% =", f"{8/3.9:.1f}x a {8/3.4:.1f}x", "(documento: ~2x)")
print("temporada 6–8 semanas em 2–3 meses (8,7–13 semanas):", f"{8.7/8:.1f} a {13/6:.1f} ciclos")

# (6) fontes por linha das tabelas de sinais (o documento diz que os números principais foram cruzados em 2+ fontes)
print("\n== (6) fontes por linha de sinal (tabelas com coluna Fonte) ==")
um, dois_ou_mais, total_linhas = [], 0, 0
for linha in body.splitlines():
    if not linha.startswith("|"): continue
    cel = [c.strip() for c in linha.strip().strip("|").split("|")]
    if len(cel) < 5: continue
    if not re.fullmatch(r"(\[\d+\])+", cel[-1]): continue
    n = len(set(re.findall(r"\[(\d+)\]", cel[-1])))
    total_linhas += 1
    if n >= 2: dois_ou_mais += 1
    else: um.append(cel[0][:60])
print(f"linhas de sinais: {total_linhas} | com 2+ fontes: {dois_ou_mais} | com 1 fonte: {len(um)}")
print("linhas com 1 só fonte:", um)

# (7) todas as linhas de sinais têm tag de fonte? e números de mercado soltos na prosa (heurística)
print("\n== (7) sinais sem fonte e números soltos na prosa ==")
total = com_tag = 0
for l in body.splitlines():
    if not l.startswith("|") or set(l.replace("|", "").strip()) <= set("-: "): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) != 5 or c[0] in ("Sinal", "Indicador", "Pilar do briefing [B]"): continue
    if not c[3].startswith(("estimativa", "reportado", "pesquisa", "relatório", "rastread", "análise")): continue
    total += 1
    com_tag += bool(re.search(r"\[\d+\]", c[4]))
print(f"linhas de sinais: {total} | com tag de fonte: {com_tag}")
print("linhas de prosa com número de mercado e sem tag [n] ou [B]:")
n = 0
for i, l in enumerate(body.splitlines(), 1):
    if l.startswith("|") or l.startswith("```"): continue
    if re.search(r"(US\$|R\$|\d+(?:[.,]\d+)?\s*%|\d+(?:[.,]\d+)?\s*(bi|mi)\b)", l) and not re.search(r"\[(\d+|B)\]", l):
        n += 1
        print(f"  L{i}: {l.strip()[:110]}")
print("total sinalizadas:", n, "(revisadas à mão: método do ranking, leitura que resume a tabela, itens da pesquisa da Poki com fonte na linha de abertura e meta que remete à seção 7)")
