# Prompt de atualização estrutural — repositório de cliente BFG

**Uso:** copiar o bloco abaixo inteiro e colar numa sessão do Claude Code aberta na raiz
do repositório do Atacadão Posto 13.

**O que vai:** só arquitetura — comandos, skills, pastas, regras de processo e a higiene
que a auditoria encontrou. **Nada de conteúdo de cliente.** Nenhum nome de produto, peça,
paleta, persona, número de campanha ou decisão de marca do outro projeto aparece aqui.

---

```
Preciso atualizar a estrutura deste repositório com as mudanças que fizemos no
repositório-irmão. São mudanças de arquitetura: comandos, skills, pastas e regras de
processo. Nenhum conteúdo do outro cliente entra aqui — tudo que for específico deste
cliente você levanta comigo.

Antes de executar qualquer coisa: leia o CLAUDE.md, o README.md, o DECISOES.md e liste o
que existe em .claude/commands/ e .claude/skills/. Várias mudanças abaixo dependem do que
já está aqui, e algumas podem não fazer sentido para este cliente. Me traga as que você
acha que não se aplicam, em vez de executar no automático.

═══════════════════════════════════════════════════════════════════
1. HIGIENE — rode esta auditoria antes de construir qualquer coisa
═══════════════════════════════════════════════════════════════════

Cada item abaixo é um problema real que encontramos lá. Verifique se existe aqui:

a) SKILL.md solto na raiz de .claude/skills/
   Skill precisa ser .claude/skills/<nome>/SKILL.md. Um SKILL.md no diretório-pai NÃO
   carrega, mas fica no repositório contradizendo as skills válidas. Achamos um que era
   cópia antiga de outra skill, com instruções de outro ambiente (caminhos /mnt/, funções
   que não existem no Claude Code) e valores já revogados hardcoded.

b) README.md duplicado dentro de pasta de skill
   Achamos um que era cópia literal do README do repositório. Não documenta a skill,
   documenta o repo, e diverge do original na primeira edição.

c) Skills duplicadas entre repositório e escopo global do usuário
   Rode: ls ~/.claude/skills/synced/*/ e compare com .claude/skills/.
   Nome repetido = duas skills competindo pelos mesmos gatilhos em linguagem natural. A
   global costuma ser a versão antiga, que salva fora do repositório e não passa pelos
   portões. Duas saídas: criar um comando que aponte deterministicamente para a local, e
   remover a global (o diretório e a entrada no manifest.json daquela pasta).
   AVISE que remover a global é local e temporário: ela volta no próximo sync, e o
   definitivo é remover na origem, no claude.ai.

d) Encoding dos SKILL.md
   Rode um teste de decodificação UTF-8 em todos. Achamos um byte corrompido que comia
   uma letra acentuada — e estava justamente no rótulo do formato de saída obrigatório
   que todo achado copia.

e) O mapa de MCP bate com a realidade?
   Verifique cada canal que os arquivos afirmam existir ou não existir, chamando o MCP de
   verdade. Achamos quatro arquivos afirmando que um canal não tinha MCP quando ele
   estava configurado no ESCOPO GLOBAL do usuário (~/.claude.json), não no .mcp.json do
   projeto. Resultado: pedia-se export manual de um canal que dava para ler direto.
   Verifique também se há conector equivalente ativo em paralelo ao servidor do projeto —
   é comum um não autenticar enquanto o outro está de pé. Os comandos devem mandar checar
   os dois caminhos antes de declarar um canal indisponível.

═══════════════════════════════════════════════════════════════════
2. COMANDOS — remover dois, criar três
═══════════════════════════════════════════════════════════════════

REMOVER (avalie comigo antes — pode ser diferente aqui):
  /relatorio e /apresentacao

  Motivo lá: ficaram genéricos e sem uso real. Foram absorvidos pelo comando de check-in,
  que é o entregável recorrente da conta. Se aqui esses comandos têm uso, não remova.

  Se remover, duas perdas a declarar em voz alta, não engolir:
  - não sobra porta para leitura de performance avulsa fora do ciclo recorrente; ela cai
    no comando guarda-chuva
  - a skill de documento .docx pode ficar órfã, sem nenhum comando que a chame. Verifique
    quem mais a referencia antes.

CRIAR:

  /banner — só se este cliente faz e-mail marketing com arte de topo.
  Existia uma skill de banner cujos gatilhos declarados (/banner) não tinham comando
  nenhum atrás. Seis citações no repositório apontando para um comando inexistente. Se
  houver skill nessa situação aqui, crie o comando: é o que garante que a skill LOCAL
  seja chamada, e não a global concorrente.

  /check-in — o entregável recorrente de mídia deste cliente.
  Arquitetura em três camadas, que é o ponto importante:
    - o COMANDO orquestra as fases
    - uma skill LOCAL guarda o contexto da conta (fontes por canal, regras de cálculo
      pactuadas com o cliente, série histórica, temas em aberto)
    - a skill GLOBAL de check-in guarda a forma (template, componentes, scripts de build)
  Não duplique a global dentro do repositório. A separação contexto/forma é o que evita
  a duplicata do item 1c.

  Fases do comando, nesta ordem:
    1. preflight: identidade e log de decisões carregados; ler a skill de contexto
       inteira, incluindo os temas em aberto do ciclo anterior
    2. duas perguntas só (cliente recorrente: pule briefing)
    3. coletar pelos MCPs nos DOIS recortes e devolver um resumo CONFERÍVEL antes de
       construir qualquer coisa
    4. levantar bloqueios e inconsistências ANTES de construir, não depois
    5. verificar cada achado pelo portão crítico; separar diagnóstico de hipótese no
       próprio texto
    6. esperar o "pode construir"
    7. montar pelo fluxo da skill global, sem escrever CSS novo
    8. portões de saída
    9. arquivo datado + dizer o que foi decidido por conta própria e pode ser revertido

  /projeto — planejamento de projeto de escopo reduzido, com ciclo PDCA.
  Feature nova, detalhada na seção 3.

═══════════════════════════════════════════════════════════════════
3. FEATURE NOVA — planejamento de projeto (PDCA)
═══════════════════════════════════════════════════════════════════

Um projeto aqui é recorte pequeno com começo, meio e fim dentro da conta: janela de
mercado, lançamento, campanha sazonal, frente de recuperação. Não é plano anual nem peça
avulsa.

O comando é o PLAN. O DO vive no gestor de backlog da operação. O CHECK volta pelo
checkpoint. O ACT reescreve o plano no ciclo seguinte.

3.1 PASTA NOVA NA RAIZ: projetos/
    Peça autorização ao usuário antes de criar (a regra de não criar pasta na raiz sem
    perguntar deve estar no CLAUDE.md).

    projetos/
    ├── LEIA-ME.md
    ├── <modelo-de-importacao-do-gestor-de-backlog>.csv
    └── <slug-do-projeto>/
        ├── PLANO.md          Plan
        ├── BACKLOG.md        Do, legível
        ├── backlog.csv       Do, para importar
        └── checkpoints/
            └── AAAA-MM-DD.md Check + Act, um por rodada

    Adicione projetos/ aos DOIS scripts de bootstrap (.sh e .ps1) e à contagem de estado
    que eles imprimem.

    No LEIA-ME, deixe explícita a diferença para a pasta de entregas:
      entregas/ = saída pontual, datada, versão nova é arquivo novo
      projetos/ = ciclo vivo, o mesmo arquivo evolui, encerra com o projeto
    As peças que o projeto produz continuam saindo em entregas/, pelos comandos de sempre.

3.2 SKILL planejamento-projeto
    Esta é quase 100% reaproveitável — é método, não conteúdo de cliente.

    Entrevista em SEIS BLOCOS, um de cada vez, esperando resposta:
      1. Oportunidade e relógio — por que agora; a janela tem data conhecida ou é
         estimativa; QUEM disse isso e quando; datas de início e entrega
      2. Resultado — que número muda; linha de base e meta; em quanto tempo responde;
         se o número não mexer, o projeto foi inútil ou teve valor indireto
      3. Escopo e limites — verba total e por canal, nova ou realocada; MÃO DE OBRA REAL
         por semana; o que está dentro e fora, canal por canal; dependências de terceiro;
         o que NÃO vamos fazer mesmo sendo boa ideia
      4. Envolvidos — quem executa por NOME; quem aprova; quem do cliente entrega algo;
         quanto tempo leva a aprovação na prática
      5. Risco e premissa — o que precisa ser verdade; qual a mais frágil; o que fazemos
         se cair; que proibição dura do CLAUDE.md o projeto encosta
      6. Checkpoint — quando; qual dado abre; o que nos faz mudar no meio e o que nos faz
         abortar

    REGRAS DURAS DA SKILL:

    - Exceção declarada à regra de 2 a 3 perguntas da skill de método mestre. Aqui a
      entrevista É o trabalho. Escreva a exceção nos dois arquivos, em vez de deixar a
      contradição solta entre skills.
    - Regra de economia: o que já está no log de decisões, na identidade, no último
      relatório ou nos insumos NÃO se pergunta — se confirma em uma linha. É o que separa
      entrevista de interrogatório.
    - TESTE DE CAPACIDADE, obrigatório antes de escrever o backlog: peças previstas ×
      semanas do projeto contra a entrega semanal real declarada no bloco 3. Se não fecha,
      o escopo é cortado e o corte é DITO. Plano que a operação não executa não é plano.
      Dimensione no ritmo médio, nunca no teto.
    - TODA data de checkpoint vira TAREFA no gestor de backlog, com data e responsável,
      junto das tarefas de execução. Checkpoint que só está no PLANO.md não acontece —
      ninguém abre a pasta do projeto numa terça à tarde. Não é opcional e não depende de
      o usuário pedir.
    - Checkpoint FECHA EM VERBO: seguir, corrigir, cortar ou abortar. Uma das quatro,
      escolhida e justificada. Relatório sem verbo não é checkpoint.
    - Sem linha de base não existe checkpoint. Se o número de partida não existe,
      levantá-lo é a primeira tarefa do backlog.
    - Janela de oportunidade ouvida em reunião é premissa a confirmar, nunca fato.
    - CICLO CURTO COM LEITURA CEDO é o padrão preferido: a primeira leitura vale mais
      perto do início, quando ainda dá para corrigir barato, do que no fim, quando só
      resta a autópsia. Prefira um ciclo de um mês com checkpoint na primeira semana de
      veiculação a um ciclo de dois meses com checkpoint no fim.
    - Cuidado com volume baixo na leitura cedo: uma semana de campanha não sustenta
      conclusão. O checkpoint serve para ler custo e qualificação, não para declarar
      vitória. "Seguir e observar" é resultado legítimo.

    O PLANO.md abre com A APOSTA em uma frase — não o título burocrático. "Ocupar a busca
    por X nos 60 dias em que Y sai do ar" é aposta; "Projeto X" é nome de pasta.

3.3 CSV DE IMPORTAÇÃO DO GESTOR DE BACKLOG
    Peça ao usuário o modelo de importação que a ferramenta fornece e guarde em projetos/.

    NUNCA invente cabeçalho de CSV. Cabeçalho errado quebra a importação em lote e dá
    mais trabalho que criar tarefa na mão. Sem o modelo, gere só o BACKLOG.md legível e
    avise o que ficou pendente.

    Com o modelo em mãos, levante com o usuário:
      - o código de tipo de tarefa da conta (o do arquivo de exemplo costuma ser só
        demonstração e NÃO vale)
      - quais colunas ele quer vazias porque preenche à mão na ferramenta
      - as escalas de esforço e prioridade

    Gere o arquivo no MESMO encoding do modelo (confira se tem BOM — sem ele a ferramenta
    pode errar acento). Célula vazia fica vazia: nada de travessão ou "n/a".

    Se houver coluna de quantidade de peças, a soma dela no backlog inteiro TEM de bater
    com o número que passou no teste de capacidade. Se não bate, o plano cresceu depois da
    conta — refaça.

3.4 MODO CHECKPOINT
    Mesmo comando, com argumento: /projeto checkpoint <slug>. Não reabre a entrevista.
      1. ler o PLANO.md inteiro e os checkpoints anteriores
      2. validar o dado pelo portão de entrada
      3. comparar meta × realizado e cada premissa contra o que aconteceu
      4. passar cada leitura pelo portão crítico antes de virar afirmação — projeto curto
         tem volume baixo, e volume baixo não sustenta conclusão
      5. decidir o Act em verbo
      6. gravar o checkpoint; se o Act muda o plano, atualizar o PLANO.md e registrar no
         log de decisões
      7. deixar a próxima data de checkpoint como tarefa nova no backlog — enquanto o
         projeto não encerra, sempre existe um próximo agendado

═══════════════════════════════════════════════════════════════════
4. CLAUDE.md — três ajustes
═══════════════════════════════════════════════════════════════════

a) Na tabela de formatos de entregável, acrescente a linha:
   | Plano de projeto, backlog e checkpoint | Markdown + CSV do gestor | projetos/<slug>/ |

b) Na regra de não criar pasta nova na raiz, registre projetos/ como exceção concedida,
   com a data.

c) Declare que projetos/ NÃO segue a nomenclatura datada: é ciclo vivo, o mesmo arquivo
   evolui, não se versiona por cópia. As peças que o projeto produz continuam saindo na
   pasta de entregas, com data e versão.

═══════════════════════════════════════════════════════════════════
5. REGRAS TRANSVERSAIS QUE MUDARAM
═══════════════════════════════════════════════════════════════════

a) PORTÃO DE SAÍDA VISUAL PODE TER EXCEÇÃO DECLARADA
   O deck de check-in usa o design system próprio do relatório, não a paleta do cliente —
   é peça da agência para o cliente, não peça da marca. Sem essa exceção escrita, o portão
   reprova o deck toda vez. Escreva na skill QUAIS itens dela não se aplicam e quais
   continuam valendo. Não deixe a contradição implícita.

b) CONTRADIÇÃO ENTRE SKILLS SE DECLARA, NÃO SE DEIXA SOLTA
   Toda vez que uma skill nova contraria uma regra de outra (número de perguntas, paleta,
   formato), escreva a exceção NOS DOIS arquivos e registre no log de decisões. Foi assim
   com a entrevista em seis blocos e com o portão visual.

c) ANTES DE AFIRMAR QUE UM ARQUIVO DE CONTROLE ESTÁ DESATUALIZADO, RELEIA O ARQUIVO
   NA HORA
   Erramos feio nisso: escrevemos um diagnóstico inteiro concluindo que o log de decisões
   tinha parado de ser alimentado, com base numa leitura antiga do arquivo. Ele estava em
   dia — tinha crescido de 40 para 255 linhas entre a leitura e a conclusão. Num
   repositório com várias sessões, o estado muda embaixo de você. Releia antes de concluir.

d) DECLARE O ESCOPO COBERTO NO README
   Crie uma seção dizendo o que o repositório cobre hoje e, principalmente, O QUE NÃO
   COBRE, com o motivo. Repositório que promete no nome o que não entrega em comando
   confunde quem chega. Quando algo ficar fora de escopo por decisão, registre com data.

e) SKILL GENÉRICA DE OUTRO PROJETO NÃO SE USA CRUA
   Skills globais da operação não conhecem a identidade deste cliente, não passam pelos
   portões daqui e não respeitam as proibições duras do CLAUDE.md local. Se uma for
   necessária, ela é embrulhada por uma skill local de contexto — nunca chamada direto.

═══════════════════════════════════════════════════════════════════
6. AO TERMINAR
═══════════════════════════════════════════════════════════════════

- Atualize o README: árvore de pastas, tabela de comandos, tabela de skills e a seção de
  escopo. Deixe os três consistentes entre si — foi onde mais achamos divergência.
- Registre cada decisão no log, com data, quem decidiu e onde vale.
- Rode o bootstrap e confirme que ele cria e conta a pasta nova.
- Confirme que não sobrou referência órfã a comando removido. Rode uma busca pelos nomes
  antigos em CLAUDE.md, README.md e .claude/ inteiro. Referência histórica que EXPLICA a
  remoção pode ficar; instrução que manda usar o comando morto, não.
- Me diga o que você não executou e por quê.
```

---

## Para quem for colar

Três coisas que valem o aviso, porque foram onde mais perdemos tempo:

**A auditoria da seção 1 vem antes de tudo.** Metade dos problemas que encontramos não
era falta de funcionalidade — era arquivo morto, duplicata e documentação afirmando o
contrário da realidade. Construir por cima disso só aumenta a dívida.

**O teste de capacidade é o que salva o planejamento.** Foi o único ponto em que o plano
mudou de tamanho no meio da conversa, e mudou duas vezes.

**O modelo de CSV tem de vir antes do backlog.** Sem ele, ou se inventa cabeçalho e
quebra a importação, ou se gera um backlog que não sobe.
