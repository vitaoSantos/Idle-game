# Verificação mecânica do documento do VIC-5 (qa-analista).
# Ciclo 1: 2026-10-31, commit 562b2de. Ciclo 2: 2026-10-31, commit 5b51f26.
# O que mudou no ciclo 2: o bloco (1) e o (2) passaram a ler a tabela de notas e a tabela de sensibilidade do próprio documento;
# o bloco (3) lê a classe de cada fonte; o (4) confere "sem dado público" e o critério da marca [secundária] (4b);
# o (5) foi reescrito (a meta "D7 de 8%" mudou para mínimo de 10% e meta de 15%, e entraram D60 e D90); o (8) cruza com o briefing e o VIC-6.
# Uso (na raiz do repositório):
#   python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md [docs/gdd/briefing.md] [docs/pesquisa/idle-rpg-referencias.md]
import re, sys, hashlib, collections

def lê(p): return open(p, encoding="utf-8").read()
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
def num(s):
    m = re.search(r"\d+(?:[.,]\d+)?", s)
    return float(m.group(0).replace(",", ".")) if m else None
def chk(nome, calc, doc, tol=0.051):
    print(f"  {nome}: calculado={calc:.3f} documento={doc} {'OK' if abs(calc - doc) <= tol else 'DIVERGE'}")

doc = sys.argv[1]
briefing = sys.argv[2] if len(sys.argv) > 2 else "docs/gdd/briefing.md"
vic6 = sys.argv[3] if len(sys.argv) > 3 else "docs/pesquisa/idle-rpg-referencias.md"
txt = lê(doc)
body, src = txt.split("## 10. Fontes")
linhas = body.splitlines()
print("entradas (sha256 parcial):", doc, sha(doc), "|", briefing, sha(briefing), "|", vic6, sha(vic6))

# (1) ranking lido do documento (seção 2) e recalculado
print("\n== (1) notas do ranking: lidas do documento e recalculadas (peso 0,4/0,3/0,3) ==")
sec2 = body.split("## 2. Ranking")[1].split("## 3.")[0]
cats = {}
for l in sec2.splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if not l.startswith("|") or len(c) != 7 or not (c[0].isdigit() or c[0] == "—"): continue
    cats[c[1]] = (num(c[2]), num(c[3]), num(c[4]), num(c[5]))
def nota(c1, c2, c3, w=(0.4, 0.3, 0.3)): return w[0] * c1 + w[1] * c2 + w[2] * c3
for k, (a, b, c, decl) in cats.items():
    n = nota(a, b, c)
    print(f"{k[:36]:36s} calculado={n:.3f} declarado={decl} {'OK' if abs(n - decl) < 0.051 else 'DIVERGE'}")
print("categorias lidas:", len(cats), "(esperado 9)")

# (2) sensibilidade
print("\n== (2) sensibilidade ==")
key = lambda s: next(k for k in cats if s in k)
web, hib, shoot, cass, ugc = key("web"), key("Híbrido"), key("Shooter"), key("Cassino"), key("Sandbox")
base = {k: nota(*v[:3]) for k, v in cats.items()}
eq = {k: nota(a, b, c, (1/3, 1/3, 1/3)) for k, (a, b, c, _) in cats.items()}
for k, v in sorted(eq.items(), key=lambda x: -x[1]): print(f"pesos iguais: {k[:36]:36s} {v:.2f}")
print("web x cassino com pesos iguais:", round(eq[web], 3), round(eq[cass], 3), "(documento: empate em 5º, 3,2)")
ordem_base = [k for k, _ in sorted(base.items(), key=lambda x: -x[1])]
ordem_eq = [k for k, _ in sorted(eq.items(), key=lambda x: -x[1])]
print("quatro primeiras iguais com pesos iguais:", ordem_base[:4] == ordem_eq[:4])
def posicoes(over):
    g = dict(base); g.update(over)
    ordem = [k for k, _ in sorted(g.items(), key=lambda x: -x[1])]
    return g, {k: i + 1 for i, k in enumerate(ordem)}
print("\ntabela 'Sensibilidade às notas sem número' do documento, linha a linha:")
sens = sec2.split("Sensibilidade às notas sem número")[1].split("**Leitura.**")[0]
for l in sens.splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if not l.startswith("|") or len(c) != 4 or not c[0].startswith("C2 do"): continue
    alvo = shoot if "shooter" in c[0] else cass
    novo, decl, ef = num(c[1]), num(c[2]), c[3]
    calc = nota(cats[alvo][0], novo, cats[alvo][2])
    g, pos = posicoes({alvo: calc})
    ok_ef = True
    if ef.startswith("fica fora do top 5"): ok_ef = pos[alvo] > 5 and pos[web] <= 5
    elif "que sai do top 5" in ef: ok_ef = pos[alvo] <= 5 and pos[web] > 5 and g[alvo] > g[web] and abs(g[web] - 3.20) < 0.0051
    elif "em 4º" in ef: ok_ef = pos[alvo] == 4 and pos[hib] == 5 and pos[web] > 5 and abs(g[hib] - 3.50) < 0.0051
    print(f"  {c[0]:16s} valor={novo:g} -> nota {calc:.2f} (documento {decl:.2f}) {'OK' if abs(calc - decl) < 0.0051 else 'DIVERGE'}"
          f" | posição do alvo={pos[alvo]}, web={pos[web]}, híbrido={pos[hib]} | efeito citado: '{ef}' -> {'OK' if ok_ef else 'DIVERGE'}")
g, pos = posicoes({shoot: nota(cats[shoot][0], cats[shoot][1] + 1, cats[shoot][2])})
print(f"Resumo/Leitura: shooter com 1 ponto a mais de escala -> web na posição {pos[web]} (fora do top 5 se > 5)")
g, pos = posicoes({cass: nota(cats[cass][0], cats[cass][1] + 1, cats[cass][2])})
print(f"Resumo/Leitura: cassino com 1 ponto a mais de escala -> web na posição {pos[web]} (fora do top 5 se > 5)")
g, pos = posicoes({shoot: nota(cats[shoot][0], 5, cats[shoot][2])})
print(f"Shooter com C2=5: nota {g[shoot]:.2f} (documento: 3,90), posição {pos[shoot]}; UGC = {base[ugc]:.2f} (passa o UGC se > UGC)")
print("Shooter pela receita: 20,6 - 9,3 - 6,1 =", round(20.6 - 9.3 - 6.1, 2), "bi no semestre; x2 =", round(2 * (20.6 - 9.3 - 6.1), 1), "bi por ano (documento: abaixo de cerca de 10 bi)")
print("Cassino C2=5 exige US$ 15 bi/ano ou mais (escala da 1.3); só crescimento (C1):", sorted(((v[0], k[:20]) for k, v in cats.items()), reverse=True)[:6])

# (3) tags de fonte e classes
used = set(re.findall(r"\[(\d{1,2}|B)\]", body))
defined = set(re.findall(r"^\| \[(\d{1,2}|B)\] \|", src, flags=re.M))
cls = {}
for l in src.splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    m = re.fullmatch(r"\[(\d+)\]", c[0]) if l.startswith("|") and len(c) == 5 else None
    if m: cls[m.group(1)] = c[2]
print("\n== (3) fontes ==")
ordem = lambda x: (x == 'B', int(x) if x != 'B' else 0)
print("tags usadas:", len(used), "| definidas:", len(defined))
print("usadas e NÃO definidas:", sorted(used - defined, key=ordem))
print("definidas e NÃO usadas:", sorted(defined - used, key=ordem))
print("[7] e [25] aparecem no corpo ou na lista (esperado False, False, False, False):", '7' in used, '25' in used, '7' in defined, '25' in defined)
esperado = {str(i) for i in range(1, 100) if i not in (7, 25)} | {'B'}
print("IDs definidos = 1..99 menos 7 e 25, mais B:", defined == esperado)
print("classes das fontes:", dict(collections.Counter(cls.values())), "| sem classe:", sorted(set(defined) - set(cls) - {'B'}, key=ordem))
urls = re.findall(r"https?://[^\s)\]|,]+", src)
hosts = collections.Counter(re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls)
print("URLs:", len(urls), "| hosts:", len(hosts), "| top:", hosts.most_common(6))

# (4) marcas e lacunas
print("\n== (4) marcas e lacunas ==")
for m in ("[secundária]", "[antigo]", "[sem data]", "[hipótese]", "estimativa", "reportado pela empresa", "pesquisa (amostra)"):
    print(f"{m:26s} corpo={body.count(m)}")
print("'Não encontrei' no corpo (esperado 0):", len(re.findall(r"[Nn]ão encontrei", body)))
print("'sem levantamento' no corpo (esperado 0):", len(re.findall(r"sem levantamento", body)))
print("ocorrências de lacuna declarada e se a mesma linha registra a busca:")
for i, l in enumerate(linhas, 1):
    if re.search(r"[Ss]em (dado|benchmark) público|sem resultado|sem total", l):
        print(f"  L{i}: busca na linha={'sim' if re.search(r'busca|Busquei', l) else 'NAO'} | {l.strip()[:105]}")

# (4b) critério da marca [secundária] pela classe da fonte
print("\n== (4b) critério da marca [secundária]: só leva a marca se TODAS as fontes do número são de classe S ==")
so_S = lambda ids: bool(ids) and all(cls.get(i, "?") == "S" for i in ids)
faltando, mistas, ok = [], [], 0
for n, l in enumerate(linhas, 1):
    if not l.startswith("|"): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) < 4 or not re.fullmatch(r"(\[\d+\])+", c[-1]): continue
    ids = re.findall(r"\[(\d+)\]", c[-1])
    marca = "[secundária]" in " ".join(c[:-1])
    if so_S(ids) and not marca: faltando.append((n, c[0][:50], ids))
    elif (not so_S(ids)) and marca: mistas.append((n, c[0][:50], [(i, cls.get(i)) for i in ids]))
    else: ok += 1
print(f"linhas de tabela com coluna só de tags: ok={ok} | só fontes S sem a marca={len(faltando)} | com fonte P ou I e com a marca={len(mistas)} (revisar: marca ao lado de número de fonte S)")
for x in faltando: print("  FALTA MARCA:", x)
for x in mistas: print("  mista:", x)
p_sem, p_marca = [], []
for n, l in enumerate(linhas, 1):
    if l.startswith("|"): continue
    ids = re.findall(r"\[(\d+)\]", l)
    if ids and so_S(ids) and "[secundária]" not in l: p_sem.append((n, ids, l.strip()[:80]))
    if "[secundária]" in l and ids and not any(cls.get(i) == "S" for i in ids): p_marca.append((n, [(i, cls.get(i)) for i in ids], l.strip()[:80]))
print(f"prosa: só fontes S e sem marca={len(p_sem)} | marca sem nenhuma fonte S na linha={len(p_marca)}")
for x in p_sem: print("  PROSA SEM MARCA:", x)
for x in p_marca: print("  PROSA MARCA SEM S:", x)
print("cabeçalho e seção 10 usam 'acessadas'?", "acessadas" in txt, "| usam 'consultadas por resumo de busca'?", "consultadas por resumo de busca" in txt or "consultada" in txt)

# (5) contas derivadas e metas de retenção
print("\n== (5) contas derivadas ==")
chk("H1 2026 IAP 39,8/40,6 (%)", (39.8 / 40.6 - 1) * 100, -2, 0.5)
chk("AppMagic puzzle 6,3 -> 7,6 (%)", (7.6 / 6.3 - 1) * 100, 20, 1)
chk("Sensor Tower: estratégia 9,3 - puzzle 8,1", 9.3 - 8.1, 1.2, 0.011)
chk("RPG 11,6/13,7 (%; documento -15,4, diferença de arredondamento)", (11.6 / 13.7 - 1) * 100, -15.4, 0.2)
chk("downloads por minuto: 95.000 x 525.600 / 1e9", 95000 * 525600 / 1e9, 49.9, 0.051)
chk("merge-2: 1,24 / 0,636 (%)", (1.24 / 0.636 - 1) * 100, 95, 1)
chk("Roblox 2025: bookings 6,8 (+55%) -> base 2024", 6.8 / 1.55, 4.39, 0.011)
print("  temporada de 6 a 8 semanas em 2 a 3 meses (8,7 a 13 semanas): ciclos", f"{8.7/8:.1f} a {13/6:.1f}", "(documento: 1 a 2 ciclos completos); 6 sem = D42, 8 sem = D56:", 6 * 7, 8 * 7)
print("\n  metas de retenção (7.3), lidas do documento:")
sec73 = body.split("### 7.3")[1].split("## 8.")[0]
metas = {}
for l in sec73.splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if l.startswith("|") and len(c) == 4 and re.fullmatch(r"D\d+", c[0]): metas[c[0]] = (num(c[1]), num(c[2]))
print("  ", metas)
seq = ["D1", "D7", "D30", "D60", "D90"]
print("  marcos presentes D1..D90:", all(d in metas for d in seq))
print("  mínimo e meta estritamente decrescentes:", all(metas[a][0] > metas[b][0] and metas[a][1] > metas[b][1] for a, b in zip(seq, seq[1:])), "| meta >= mínimo:", all(m[1] >= m[0] for m in metas.values()))
perda = lambda a, b: (1 - b / a) * 100
chk("perda D7->D30 da versão do ciclo 1 (8% -> 6%), documento 25%", perda(8, 6), 25, 0.5)
chk("perda D7->D30 Whiteout (17 -> 8), documento 53%", perda(17, 8), 53, 0.6)
chk("perda D7->D30 GameAnalytics 2026 (4 -> 0,7), documento 'mais de 80%'", perda(4, 0.7), 82.5, 3)
chk("perda D7->D30 do mínimo", perda(metas['D7'][0], metas['D30'][0]), 60, 0.5)
chk("perda D7->D30 da meta", perda(metas['D7'][1], metas['D30'][1]), 53, 0.6)
print("  perda D7->D30 Last War (11 -> 4):", f"{perda(11, 4):.0f}%", "| D30->D60 mínimo/meta:", f"{perda(metas['D30'][0], metas['D60'][0]):.0f}% / {perda(metas['D30'][1], metas['D60'][1]):.0f}%", "| D60->D90 mínimo/meta:", f"{perda(metas['D60'][0], metas['D90'][0]):.0f}% / {perda(metas['D60'][1], metas['D90'][1]):.0f}%")
txt83 = body.split("**Metas iniciais:**")[1].split("\n")[0]
pega = lambda t: {d: float(v.replace(",", ".")) for d, v in re.findall(r"(D\d+) (\d+(?:,\d+)?)%", t)}
m_min = pega(re.search(r"Mínimo para seguir:([^.]*)\.", txt83).group(1)); m_meta = pega(re.search(r"Meta:([^.]*)\.", txt83).group(1))
print("  8.3 nº 3 igual à tabela 7.3:", m_min == {d: v[0] for d, v in metas.items()} and m_meta == {d: v[1] for d, v in metas.items()})
print("  resumo cita 'D60 de 7% do AFK Journey' e 7.3 usa 7% [81]:", "D60 de 7% do AFK Journey [81]" in body, "|", "AFK Journey 7%, contra 4% do mercado" in body)

# (6) fontes por linha das tabelas de sinais
print("\n== (6) fontes por linha de sinal (tabelas com coluna Fonte) ==")
um, dois_ou_mais, total_linhas = [], 0, 0
for linha in linhas:
    if not linha.startswith("|"): continue
    cel = [c.strip() for c in linha.strip().strip("|").split("|")]
    if len(cel) < 5: continue
    if not re.fullmatch(r"(\[\d+\])+", cel[-1]): continue
    n = len(set(re.findall(r"\[(\d+)\]", cel[-1])))
    total_linhas += 1
    if n >= 2: dois_ou_mais += 1
    else: um.append(cel[0][:60])
print(f"linhas de sinais: {total_linhas} | com 2+ fontes: {dois_ou_mais} | com 1 fonte: {len(um)}")

# (7) sinais sem fonte e números soltos na prosa
print("\n== (7) sinais sem fonte e números soltos na prosa ==")
total = com_tag = 0
for l in linhas:
    if not l.startswith("|") or set(l.replace("|", "").strip()) <= set("-: "): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) != 5 or c[0] in ("Sinal", "Indicador", "Pilar do briefing [B]"): continue
    if not c[3].startswith(("estimativa", "reportado", "pesquisa", "relatório", "rastread", "análise")): continue
    total += 1
    com_tag += bool(re.search(r"\[\d+\]", c[4]))
print(f"linhas de sinais: {total} | com tag de fonte: {com_tag}")
print("linhas de prosa com número de mercado e sem tag [n] ou [B]:")
n = 0
for i, l in enumerate(linhas, 1):
    if l.startswith("|") or l.startswith("```"): continue
    if re.search(r"(US\$|R\$|\d+(?:[.,]\d+)?\s*%|\d+(?:[.,]\d+)?\s*(bi|mi)\b)", l) and not re.search(r"\[(\d+|B)\]", l):
        n += 1
        print(f"  L{i}: {l.strip()[:110]}")
print("total sinalizadas:", n)

# (8) briefing atual e VIC-6
print("\n== (8) consistência com o briefing atual e com o VIC-6 ==")
br, v6 = lê(briefing), lê(vic6)
print("briefing: 'Não há facção escolhida pelo jogador':", "Não há facção escolhida pelo jogador" in br, "| decisão 'dia 60 e no dia 90':", "dia 60 e no dia 90" in br, "| 'PvP' no briefing:", br.count("PvP"))
fac = [(i, l.strip()) for i, l in enumerate(linhas, 1) if re.search(r"facç", l, re.I)]
print(f"linhas do documento que usam 'facção/facções' (cada uma assume facção escolhida pelo jogador, salvo negação): {len(fac)}")
for i, l in fac: print(f"  L{i}: {l[:140]}")
print("linhas com 'PvP' no documento:", [i for i, l in enumerate(linhas, 1) if "PvP" in l])
print("7.2 diz que 'a escolha é do usuário' e 8.4 ainda pergunta o que 'reter 2 a 3 meses' quer dizer:", "a escolha é do usuário" in body, "|", 'O que "reter 2 a 3 meses" quer dizer' in body)
def url_v6(cod):
    m = re.search(rf"^\| {cod} \|[^|]*\| (\S+) \|", v6, flags=re.M)
    return m.group(1) if m else None
print("fontes trazidas do VIC-6 (código lá) e a URL no VIC-6 aparece na linha da fonte do VIC-5:")
for tag, cod in (("99", "R2"), ("98", "C33"), ("96", "L15"), ("97", "L17"), ("81", "C11"), ("73", "R5")):
    u6 = url_v6(cod)
    cel = next((l for l in src.splitlines() if l.startswith(f"| [{tag}] |")), "")
    print(f"  [{tag}] = VIC-6 {cod}: URL no VIC-6={'achada' if u6 else 'NÃO achada'} | presente na linha do VIC-5={bool(u6 and u6 in cel)}")
print("VIC-6 contém os fatos citados pelo VIC-5:",
      {"MapleStory US$ 164 mi": "US$ 164 mi" in v6, "7,6 milhões de instalações": "7,6 milhões de instalações" in v6, "reembolso total": "reembolso total" in v6,
       "H3 (temporadas 6 a 8 semanas)": bool(re.search(r"\| H3 \| Temporadas de 6 a 8 semanas", v6)), "ECA art. 20 e 17/03/2026": "17/03/2026" in v6 and "art. 20" in v6,
       "risco 7: D30 do RPG ~3,5%, top 1% 10%, idle D1 42%": all(s in v6 for s in ("3,5%", "10% no D30", "42% de D1"))})
sec54 = v6.split("### 5.4")[1].split("---")[0]
print("VIC-6 seção 5.4 (numeração hoje; o VIC-5 cita facções nº 5, idade nº 2 e nº 4, troca nº 1 e nº 3):")
for l in sec54.splitlines():
    if re.match(r"\d\. ", l): print("  ", l[:90])
