# Verificação mecânica do documento do VIC-6 (qa-analista, 2026-10-31).
# Uso: python3 -I docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py docs/pesquisa/idle-rpg-referencias.md docs/gdd/briefing.md
# Confere: (1) tags de fonte por família usadas x definidas; (2) campos por jogo comparável (idle, social, monetização);
# (3) fontes por reclamação; (4) marcas de confiança e ressalvas; (5) hosts; (6) contagens de seções; (7) contas citadas.
# Revalidação (commit d12eb4a): acrescentadas as famílias U (relato do usuário) e Q (relatório de QA); o bloco (3) confere a coluna
# "Nº de fontes"; o bloco (8), novo, traz as checagens dirigidas aos defeitos D1 a D7 e compara os fatos novos com o briefing (2º argumento).
# A versão do ciclo 1 (sem U, Q e bloco 8) está no git: commit 3e51fde.
import re, sys, collections

txt = open(sys.argv[1], encoding="utf-8").read()
briefing = open(sys.argv[2], encoding="utf-8").read() if len(sys.argv) > 2 else ""
body, src = txt.split("## 6. Fontes")

print("== (1) tags de fonte ==")
fam = {"M": 38, "C": 97, "P": 21, "T": 23, "L": 25, "R": 5, "U": 3, "Q": 1}
used = set(re.findall(r"\[([MCPTLRUQ]\d{1,2})\]", body))
defined = set(re.findall(r"^\| ([MCPTLRUQ]\d{1,2}) \|", src, flags=re.M))
for f, n in fam.items():
    u = {t for t in used if t[0] == f}; d = {t for t in defined if t[0] == f}
    print(f"família {f}: esperadas {n} | definidas {len(d)} | usadas {len(u)}")
print("usadas e NÃO definidas:", sorted(used - defined))
print("definidas e NÃO usadas:", sorted(defined - used, key=lambda x: (x[0], int(x[1:]))))
print("total definidas:", len(defined))

print("\n== (2) campos por jogo comparável (seções 2.2 a 2.12) ==")
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
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        decl = ""
        if len(cel) == 7:  # tabelas 4.1 e 4.2: # | queixa | jogos | fontes | nº de fontes | confiança | implicação
            n, conf = int(cel[4]), cel[5]
            regra = "Alta" if n >= 5 else "Média" if n >= 3 else "Baixa"  # regra do texto (a parte "imprensa especializada" é manual)
            decl = f" | nº declarado={n} {'OK' if n == len(tags) else 'DIVERGE'} | confiança={conf} (regra pelo nº: {regra}) {'OK' if conf == regra else 'DIVERGE'}"
        print(f"#{m.group(1):>2} fontes={len(tags):2d}  {m.group(2)[:60]}{decl}")

print("\n== (4) marcas de confiança e ressalvas ==")
for chave in ("confiança baixa", "Confiança", "| Alta |", "| Média |", "| Baixa |", "não verificado", "não confirmad", "atribuição provável",
              "cálculo nosso", "Cálculo nosso", "Não encontramos", "não encontramos", "não detalhad"):
    print(f"{chave:22s} {body.count(chave)}")

print("\n== (5) hosts ==")
urls = re.findall(r"https?://[^\s)\]>,|]+", src)
hosts = collections.Counter(re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls)
print("URLs:", len(urls), "| hosts:", len(hosts))
print("fontes definidas sem URL (não são páginas da web):", sorted(t for t, l in re.findall(r"^\| ([A-Z]\d{1,2}) \|(.*)$", src, flags=re.M) if "http" not in l))
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

# ---------------------------------------------------------------------------------------------------------------------------
# (8) NOVO na revalidação (commit d12eb4a): checagens dirigidas aos defeitos D1 a D7 do ciclo 1. "OK" = o esperado se confirmou;
# "DIVERGE" = olhar a linha. As linhas citadas são as do arquivo do documento (começam em 1).
# ---------------------------------------------------------------------------------------------------------------------------
print("\n== (8) revalidação (commit d12eb4a): checagens dirigidas aos defeitos D1 a D7 ==")
linhas = txt.splitlines()
corpo_linhas = body.splitlines()  # sem a seção 6; a numeração é a mesma do arquivo

def onde(p, f=0, so_corpo=True):
    return [i + 1 for i, l in enumerate(corpo_linhas if so_corpo else linhas) if re.search(p, l, f)]

def chk(rot, p, esp, f=0, so_corpo=True):
    r = onde(p, f, so_corpo)
    ok = (len(r) >= 1) if esp == "+" else (len(r) == esp)
    print(f"  [{'OK' if ok else 'DIVERGE'}] {rot}: {len(r)} linha(s) {r[:12]}")

def mostra(rot, p, f=0, so_corpo=True):
    print(f"  {rot}")
    for i, l in enumerate(corpo_linhas if so_corpo else linhas):
        m = re.search(p, l, f)
        if m:
            print(f"    linha {i + 1}: ...{l[max(0, m.start() - 45):m.end() + 70]}...")

print("D1 (Resumo x corpo)")
chk("termos antigos 'devolveu' ou '100% das compras' (esperado 0)", r"devolveu|100% das compras", 0)
chk("'ofereceu' ou 'oferecer reembolso total' (Resumo, 2.5, 3.3)", r"ofere(ceu|cer) reembolso total", "+")
chk("afirmação de devolução sem 'ofer' (oferta/ofereceu) na mesma linha (esperado 0)", r"^(?!.*ofer).*(reembolsou|reembolsad|devolveu|reembolso total|reembolso integral)", 0, re.I)
chk("'monetização nº 1' ou 'nº 1 nas avaliações' (esperado 0)", r"monetização nº 1|nº 1 nas avalia", 0)
chk("'fontes divergem sobre a principal queixa' (Resumo, 3.4, 3.6)", r"fontes divergem sobre a principal queixa", 3, re.I)
chk("'12 a 24 h' (esperado 0)", r"12 a 24 h", 0)
chk("'até 12 h no AFK Arena' (Resumo)", r"até 12 h no AFK Arena", 1)

print("D2 (ECA Digital)")
chk("'Decreto 12.880' no corpo (Resumo, 3.3, 5.2, 5.4)", r"Decreto 12\.880", "+")
chk("'art. 20' e 'art. 23' no corpo", r"art\. 2[03]", "+")
chk("'classificação indicativa' no corpo", r"classificação indicativa", "+")
chk("'Nota Técnica 55/2026' (corpo e fonte L19)", r"Nota Técnica 55/2026", "+", so_corpo=False)
chk("fonte oficial 'planalto' em qualquer parte (esperado 0: pendência declarada, sem busca)", r"planalto", 0, so_corpo=False)
chk("pendência declarada: 'texto oficial'", r"texto oficial", "+")

print("D3 (Magic Rush: respostas e vídeo do usuário)")
chk("rótulo 'vídeo e respostas do usuário'", r"vídeo e respostas do usuário", "+")
chk("papel 'Canhão'", r"Canhão", "+")
chk("'zero anúncios' (Resumo, 1.9)", r"[Zz]ero anúncios", "+")
chk("Wishing Pool VIP 8: 'a confirmar com o usuário'", r"a confirmar com o usuário", 1)
chk("'4 papéis' só na frase que corrige a versão anterior (esperado 1)", r"4 papéis|quatro papéis", 1)

print("D4 (seção 4)")
chk("subseções 4.1 e 4.2", r"^### 4\.[12] ", 2)
chk("critério para 'comum' declarado", r"Critério para \"comum\"", 1)
chk("'A ordem das linhas não indica frequência'", r"ordem das linhas não indica frequência", 1)

print("D5 (facção)")
chk("definição de 'Facção' no cabeçalho", r"\"Facção\", neste documento", 1)
chk("todas as linhas com 'facç' (cabeçalho, Resumo, 5.4 nº 5 e U1: esperado 4)", r"facç", 4, re.I, so_corpo=False)
chk("'facç' sem 'grupo', 'lado escolhido' ou 'sem lado' na linha (esperado 0)", r"^(?!.*(grupo|lado escolhido|sem lado)).*facç", 0, re.I, so_corpo=False)

print("D6 (Bonds do RuneScape)")
chk("'−63%' (3.1 e 3.5)", "−63%", 2)
chk("'atribuição incerta' (3.1, 3.5, Resumo, 5.1)", r"atribuição incerta", "+")
chk("termos antigos 'queda de 61%', '81% no ouro' ou '−61% no comércio' (esperado 0)", "queda de 61%|81% no ouro|−61% no com[ée]rcio", 0)

print("D7 (fonte C31 e '(sem VIP)')")
chk("'[C31]' citada no corpo", r"\[C31\]", 1)
chk("'(sem VIP)' junto de '3 h 20 min' (Resumo e 1.12)", r"3 h 20 min[^|]*\(sem VIP\)|\(sem VIP\)[^|]*3 h 20 min", 2)

print("Fontes novas (seção 6.7)")
for t in ("U1", "U2", "U3", "Q1"):
    n_corpo = len(re.findall(r"\[" + t + r"\]", body))
    definida = bool(re.search(r"^\| " + t + r" \|", src, flags=re.M))
    print(f"  [{t}] citada {n_corpo}x no corpo | definida em 6.7: {definida}")

print("Fatos novos do Magic Rush x briefing (trecho presente no briefing? presente no documento?)")
br = re.sub(r"[*`]", "", briefing).lower()
dc = re.sub(r"[*`]", "", txt).lower()
for t in ["Varrer", "X10", "Tanque, Atirador, Mago, Suporte e Canhão", "zero anúncios", "1/3 a 3/3", "Guerra do Trono", "stamina (comida)", "ouro e gemas",
          "evoluir os heróis", "PvP", "paisagem", "Auto e velocidade x1", "3 estrelas", "bastante tempo", "grupo de heróis"]:
    print(f"  briefing={str(t.lower() in br):5} documento={str(t.lower() in dc):5}  {t}")

print("Seção 2.12 (Dead Zone) e linha da tabela 2.1 x briefing (cada trecho está no briefing?)")
dz = dc.split("### 2.12 ")[1].split("\n---")[0] + dc.split("| dead zone — idle arsenal rpg |")[1].split("\n")[0]
for t in ["idle rpg web (desktop)", "em pt-br", "interface escura e moderna", "combate, esquadrão, cartas, base, expedição, árvore e passe",
          "pixel art no estilo dos jogos de ação dos anos 90", "esquadrão de soldados animais contra chefões", "cartas de soldados com raridade",
          "base em corte", "estilo abrigo", "árvore de melhorias", "baús ao derrotar chefes", "onda 30/30", "o leviatã do cais",
          "ondas por zona", "ciclos que reiniciam a campanha", "expedições com tempo", "passe de batalha por temporada", "trilha grátis", "elite"]:
    print(f"  briefing={str(t in br):5} 2.12 ou 2.1={str(t in dz):5}  {t}")
mostra("Frases de leitura (não literais do briefing) na 2.12 e nas tabelas 5.1 e 5.2:",
       r"elo idle mais claro|idle RPG de coleção|casam com as oportunidades|prova de formato|já é ocupado|precedente no idle MMO|tem ciclos que reiniciam|tem expedições com tempo")

print("Pontos que originam defeitos novos (cosméticos): linhas para conferir")
mostra("N1 (2.5): data de lançamento 5/11 x 'o lançamento (06/11/2025)':", r"Lançamento:\*\* 5 de novembro|o lançamento \(06/11/2025\)|\(Nexon e AbleGames, 05")
mostra("N2 (fonte L19): 'base do art. 23':", r"base do art\. 23", so_corpo=False)
mostra("N3 (1.3): 'o usuário confirma' os 5 papéis:", r"como o usuário confirma")
mostra("N4: PvP 'o modo de que o usuário mais gostava' x 'dois melhores momentos':", r"modo de que o usuário mais gostava|um dos dois melhores momentos|os dois melhores momentos|O melhor era o")

print("Tabelas: células por linha x células do cabeçalho")
ruins, i = [], 0
while i < len(linhas) - 1:
    if linhas[i].startswith("|") and re.match(r"^\|[\s:|-]+\|$", linhas[i + 1].strip()):
        n = len(linhas[i].strip().strip("|").split("|"))
        j = i + 2
        while j < len(linhas) and linhas[j].startswith("|"):
            k = len(linhas[j].strip().strip("|").split("|"))
            if k != n:
                ruins.append((j + 1, n, k))
            j += 1
        i = j
    else:
        i += 1
print("  linhas fora do padrão (linha, esperado, obtido):", ruins or "nenhuma")

print("Resumo x corpo: números, datas e nomes do Resumo que também aparecem no corpo")
resumo = txt.split("## Resumo executivo")[1].split("## Como a pesquisa foi feita")[0]
resto = txt.split("## Como a pesquisa foi feita")[1]
for t in ["43,5 mi", "3 h 20 min", "até 12 h", "6 h (8 h com membership)", "US$ 1,5 bi", "US$ 164 mi", "06/11/2025", "28/01/2026", "5 a 15/02/2026",
          "15.211/2025", "17/03/2026", "art. 20", "12.880/2026", "art. 23", "55/2026", "6 a 8 semanas", "AppFollow", "Unstar", "Canhão", "Dead Zone"]:
    print(f"  {t!r:28} Resumo={resumo.count(t)} corpo={resto.count(t)}{'' if resumo.count(t) and resto.count(t) else '  <-- VER'}")
