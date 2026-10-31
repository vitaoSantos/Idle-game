# Verificação mecânica do documento do VIC-7 (qa-analista).
# Ciclo 1: 2026-10-31, commit 3e8e492. Ciclo 2: 2026-10-31, commit 9d31bd0.
# O que mudou no ciclo 2: as marcas agora são [V], [U], [F-resumo...], [cálculo], [I] e [N] (no ciclo 1 eram [F], [F fraca], [I], [N]);
# a tabela 3.2 ganhou a coluna Híbrido e a 3.2b; entrou a tabela 3.6; o script confere a coluna "Confiança" da seção 5, as referências
# de seção e de decisão, a forma das tabelas, trechos inacabados, o preço do Spine em todos os lugares e o cruzamento com o briefing e o VIC-6.
# Uso (na raiz do repositório):
#   python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md [docs/gdd/briefing.md] [docs/pesquisa/idle-rpg-referencias.md]
import re, sys, hashlib, collections

def lê(p): return open(p, encoding="utf-8").read()
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
def cel(l): return [c.strip() for c in l.strip().strip("|").split("|")]

doc = sys.argv[1]
briefing = sys.argv[2] if len(sys.argv) > 2 else "docs/gdd/briefing.md"
vic6 = sys.argv[3] if len(sys.argv) > 3 else "docs/pesquisa/idle-rpg-referencias.md"
txt = lê(doc)
body, src = txt.split("## 9. Fontes")
linhas = txt.splitlines()
print("entradas (sha256 parcial):", doc, sha(doc), "|", briefing, sha(briefing), "|", vic6, sha(vic6))

def linhas_de(ini, fim):
    a = txt.index(ini); b = txt.index(fim, a + 1)
    return txt[a:b].splitlines()

# (1) tags de fonte
used = set(re.findall(r"\[([MPCXG]\d{1,2})\]", body))
defined = re.findall(r"^- \[([MPCXG]\d{1,2})\]", src, flags=re.M)
print("\n== (1) tags de fonte ==")
print("tags usadas no corpo:", len(used), "| definidas na seção 9:", len(set(defined)), "| definições repetidas:", [t for t, n in collections.Counter(defined).items() if n > 1])
print("usadas e NÃO definidas:", sorted(used - set(defined)))
print("definidas e NÃO usadas no corpo:", sorted(set(defined) - used))

# (2) marcas de confiança e coluna "Confiança"
print("\n== (2) marcas ==")
todas = re.findall(r"\[([^\]\[]+)\]", body)
marcas = [m for m in todas if not re.fullmatch(r"[MPCXG]\d{1,2}", m)]
comp = collections.Counter()
for m in marcas:
    for parte in re.split(r"\s*(?:\+|,|;|:| e )\s*", m):
        p = parte.strip()
        if p.startswith("F-resumo"): comp["F-resumo"] += 1
        elif p.startswith("cálculo"): comp["cálculo"] += 1
        elif p in ("V", "U", "I", "N"): comp[p] += 1
print("marcas encontradas (por componente):", dict(comp))
print("[F] solto ou [F fraca] do ciclo 1 (esperado 0):", len(re.findall(r"\[F\]|\[F fraca\]|\[F \+", body)))
print("[F-resumo] sem qualificador / fraca / confirmar:", len(re.findall(r"\[F-resumo\]", body)), "/", len(re.findall(r"\[F-resumo, fraca\]", body)), "/", len(re.findall(r"\[F-resumo, confirmar\]", body)))
print("marcas fora do glossário (esperado nenhuma):", sorted({m for m in marcas if not re.match(r"(V|U|F-resumo|cálculo|I|N|e I)\b", m) and not re.match(r"cálculo e I", m)})[:12])
print("coluna Confiança das tabelas 5.1 e 5.2 (última célula):")
for l in linhas_de("### 5.1 Pixel art", "### 5.3"):
    c = cel(l)
    if l.startswith("|") and len(c) == 6 and c[0] not in ("Jogo",) and not set(c[0]) <= set("-: "):
        alta = "Alta" in c[5]
        ok = (not alta) or ("visual" in c[5] and "quadros" in c[5])
        print(f"  {c[0][:34]:34s} -> {c[5][:70]} | 'Alta' só com visto nos quadros: {'OK' if ok else 'REVISAR'}")

# (3) tabelas de notas
print("\n== (3) notas, soma, híbrido e sensibilidade ==")
t32 = [cel(l) for l in linhas_de("### 3.2 Tabela de notas", "### 3.2b") if l.startswith("|")]
crit = [c for c in t32 if len(c) == 6 and c[0].isdigit()]
pix, car, hib = ([int(c[i]) for c in crit] for i in (2, 3, 4))
soma_decl = [int(re.sub(r"\D", "", x)) for x in next(c for c in t32 if "Soma simples" in " ".join(c))[2:5]]
print("notas pixel:", pix, "cartoon:", car, "híbrido:", hib)
print("somas recalculadas (pixel, cartoon, híbrido):", (sum(pix), sum(car), sum(hib)), "| declaradas:", tuple(soma_decl), "->", "OK" if (sum(pix), sum(car), sum(hib)) == tuple(soma_decl) else "DIVERGE")
t32b = [cel(l) for l in linhas_de("### 3.2b", "### 3.3") if l.startswith("|")]
notas_b = [int(c[1]) for c in t32b if len(c) == 3 and c[0].isdigit()]
print("3.2b notas:", notas_b, "soma", sum(notas_b), "| igual à coluna Híbrido da 3.2:", notas_b == hib, "| soma declarada:", [c[1] for c in t32b if c[0] == "" and "**" in c[1]])
t33 = [cel(l) for l in linhas_de("### 3.3 Sensibilidade", "### 3.4") if l.startswith("|")]
cenarios = [c for c in t33 if len(c) == 4 and re.fullmatch(r"\d+", c[1])]
pesos = {"Todos os critérios com peso 1": [1]*7, "Prioridade em público e polimento (critérios 1 e 2 com peso 2)": [2, 2, 1, 1, 1, 1, 1], "Prioridade em custo e peso na web (critérios 3 e 6 com peso 2)": [1, 1, 2, 1, 1, 2, 1]}
for c in cenarios:
    w = pesos[c[0]]
    calc = tuple(sum(a*b for a, b in zip(col, w)) for col in (pix, car, hib))
    decl = tuple(int(x) for x in c[1:])
    ultimo = ["pixel", "cartoon", "híbrido"][calc.index(min(calc))] if calc.count(min(calc)) == 1 else "empate no último"
    print(f"  {c[0][:62]:62s} calculado={calc} declarado={decl} {'OK' if calc == decl else 'DIVERGE'} | último: {ultimo}")
print("critério a critério (pixel × cartoon): quem vence")
nomes = [c[1][:42] for c in crit]
for i, n in enumerate(nomes, 1):
    print(f"  {i}. {n:42s} pixel={pix[i-1]} cartoon={car[i-1]} híbrido={hib[i-1]} -> {'pixel' if pix[i-1] > car[i-1] else 'cartoon' if car[i-1] > pix[i-1] else 'EMPATE'}")
print("textos que dizem que o pixel vence em 'escala' / 'custo, peso e escala' (critério 7 é o de escala):")
for i, l in enumerate(linhas, 1):
    if re.search(r"(vence|pontua mais|ponto forte)[^|\n]{0,60}escala|custo, peso e escala|custo, peso na web e escala", l):
        print(f"  L{i}: {l.strip()[:150]}")

# (4) contas de memória e de escala
print("\n== (4) contas de memória e de escala ==")
print("30 quadros 64x64 =", 30*64*64, "px; atlas 256x512 =", 256*512, "px =", 256*512*4/2**20, "MiB; 30 classes =", 30*256*512*4/2**20, "MiB")
print("atlas 1024x1024 =", 1024*1024*4/2**20, "MiB; 30 =", 30*4, "MiB | retrato 512x512 =", 512*512*4/2**20, "MiB; 30 =", 30*512*512*4/2**20, "MiB")
print("canvas 640x360: fatores", {h: h/360 for h in (720, 1080, 1440, 2160, 1170)}, "| altura 270:", {h: round(h/270, 2) for h in (720, 1080, 1440, 2160)})
print("1080x2400: /3 =", (1080/3, 2400/3), "/4 =", (1080/4, 2400/4), "| 1440x3200 /4 =", (1440/4, 3200/4))
print("pilha confortável de pixel: 20 + 65 =", 20 + 65, "| ícones 16x3 =", 16*3, "24x2 =", 24*2, "| contagem híbrido: 30 retratos / 900 quadros =", f"{100*30/900:.1f}%", "| 30 x 30 quadros =", 30*30)

# (5) preço do Spine em todos os lugares
print("\n== (5) Spine: preços e limite em todas as ocorrências ==")
for padrao, esperado in ((r"US\$ 99\b", "Essential cheio"), (r"US\$ 69\b|\b69 em promoção", "Essential promo"), (r"US\$ 439\b", "Professional cheio"), (r"US\$ 369\b|\b369\b", "Professional promo"), (r"379", "379 (só na frase que o retirou)"), (r"2\.499", "Enterprise"), (r"500 mil", "limite")):
    achados = [i for i, l in enumerate(linhas, 1) if re.search(padrao, l)]
    print(f"  {esperado:34s} linhas {achados}")
print("linhas do Spine sem [F-resumo, confirmar] (tabelas 4.2 e preços fora de 4.2):")
for i, l in enumerate(linhas, 1):
    if re.search(r"Spine (Essential|Professional|Enterprise)", l) and l.startswith("|") and "confirmar" not in l and "[C" not in l:
        print(f"  L{i}: {l.strip()[:110]}")

# (6) referências internas, decisões, forma das tabelas e trechos inacabados
print("\n== (6) referências, tabelas e trechos inacabados ==")
heads = set(re.findall(r"^#{2,3} (\d+(?:\.\d+)?[a-z]?)\b", txt, flags=re.M))
ausentes = []
for i, l in enumerate(linhas, 1):
    for grupo in re.findall(r"seç(?:ão|ões)\s+(\d+(?:\.\d+)?[a-z]?(?:(?:,| e | a )\s*\d+(?:\.\d+)?[a-z]?)*)", l):
        for n in re.findall(r"\d+(?:\.\d+)?[a-z]?", grupo):
            if n not in heads: ausentes.append((i, n, l.strip()[:90]))
print("referências 'seção X' que não são título deste documento (revisar: podem ser do VIC-6):")
for x in ausentes: print("  ", x)
t72 = [cel(l) for l in linhas_de("### 7.2", "## 8.") if l.startswith("|")]
dec = {int(c[0]): c for c in t72 if len(c) == 6 and c[0].isdigit()}
print("7.2: linhas de decisão:", len(dec), "| 'Agora':", sum(1 for c in dec.values() if c[1].startswith("Agora")), "| Resumo diz 12 e 4:", "12 pontos na seção 7.2, dos quais 4 são para agora" in txt)
esp = {7: "Câmera", 5: "Orientação", 4: "GPU", 9: "Orçamento de animação"}
for i, l in enumerate(linhas, 1):
    for n in re.findall(r"decisão (\d+)", l):
        n = int(n)
        if n in esp: print(f"  L{i}: 'decisão {n}' -> título na 7.2: '{dec[n][2][:40]}' esperado conter '{esp[n]}': {'OK' if esp[n] in dec[n][2] else 'REVISAR'}")
        else: print(f"  L{i}: 'decisão {n}' -> {l.strip()[:100]} (revisar; antiga numeração?)")
forma = []; vazias = collections.Counter()
i = 0
while i < len(linhas):
    if linhas[i].startswith("|"):
        j = i
        while j < len(linhas) and linhas[j].startswith("|"): j += 1
        n0 = len(cel(linhas[i]))
        for k in range(i, j):
            if len(cel(linhas[k])) != n0: forma.append((k + 1, len(cel(linhas[k])), n0))
            vazias[i + 1] += sum(1 for c in cel(linhas[k]) if c == "") if k > i + 1 else 0
        i = j
    else: i += 1
print("linhas de tabela com número de células diferente do cabeçalho (esperado nenhuma):", forma)
print("tabelas com células vazias (início da tabela: nº de células vazias):", {k: v for k, v in vazias.items() if v})
print("linhas com '**' ímpar:", [i for i, l in enumerate(linhas, 1) if l.count("**") % 2], "| colchetes desbalanceados:", [i for i, l in enumerate(linhas, 1) if l.count("[") != l.count("]")], "| crases ímpares:", [i for i, l in enumerate(linhas, 1) if l.count("`") % 2])
print("marcadores de texto inacabado (TODO, TBD, XXX, '...', '…', 'a completar', '??'):", [(i, l.strip()[:60]) for i, l in enumerate(linhas, 1) if re.search(r"TODO|TBD|XXX|\.\.\.|…|a completar|\?\?", l)])
fim = [(i, l.strip()[-50:]) for i, l in enumerate(linhas, 1) if l.strip() and not l.startswith(("#", "|", "```", "- [", ">")) and not re.search(r"[.:;?!)\]`*|]$|\d$", l.strip())]
print("linhas de texto que não terminam em pontuação (revisar se cortadas):", fim)
print("palavras repetidas em sequência:", [(i, m.group(0)) for i, l in enumerate(linhas, 1) for m in re.finditer(r"\b([A-Za-zÀ-ÿ]{2,}) \1\b", l, re.I)])
print("'A usuário' e '  ' (espaço duplo) fora de tabela:", [(i, l.strip()[:50]) for i, l in enumerate(linhas, 1) if re.search(r"\bA usuário\b", l)], [i for i, l in enumerate(linhas, 1) if "  " in l.strip() and not l.startswith("|")])

# (7) briefing e VIC-6
print("\n== (7) briefing e VIC-6 ==")
br, v6 = lê(briefing), lê(vic6)
for chave in ("bem desenhad", "Arte desenhada", "sem pixels visíveis", "Câmera 3/4", "Tanque, Atirador, Mago, Suporte e Canhão", "zero anúncios", "Varrer", "X10", "Guerra do Trono", "PvP", "grupo de heróis", "placa de vídeo dedicada", "Dead Zone", "anos 90", "fliperama", "Leviatã", "7 raridades", "chibi"):
    print(f"  briefing contém '{chave}': {chave in br} | documento contém: {chave in txt}")
print("citação entre aspas atribuída ao usuário [U] no documento:", [(i, l.strip()[:120]) for i, l in enumerate(linhas, 1) if "bem desenhados" in l])
for chave in ("21/10", "03/12/2015", "06/04/2015", "43,5", "Elex", "Galaxy Play", "Canhão", "Cannon", "Marksman"):
    print(f"  VIC-6 contém '{chave}': {chave in v6}")
for s in ("### 1.1 ", "### 1.3 ", "### 1.5 ", "### 5.4 "): print(f"  VIC-6 tem a seção '{s.strip()}': {s in v6}")
sec54 = v6.split("### 5.4")[1].split("---")[0]
print("  VIC-6 5.4 nº 4 e nº 5:", [l[:70] for l in sec54.splitlines() if re.match(r"[45]\. ", l)])
import os
print("arquivos internos citados existem:", {p: os.path.exists(p) for p in ("docs/ferramentas.md", "docs/gdd/briefing.md", "docs/pesquisa/idle-rpg-referencias.md", "docs/pesquisa/top5-categorias.md", "docs/arte/guia-de-estilo.md", "docs/arte/prompts.md")})
print("imagens no diretório docs/arte:", [f for f in os.listdir("docs/arte") if not f.endswith(".md")])
