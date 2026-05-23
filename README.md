Blackjack (21) no Terminal com IA

Um simulador interativo do clássico jogo de cartas **Blackjack (21)** desenvolvido em Python. O projeto roda inteiramente via linha de comando e conta com um sistema de apostas funcional e um Bot (Dealer) com lógica própria de tomada de decisão.

Funcionalidades

*   **Interface em Modo Texto:** Cartas renderizadas em ASCII diretamente no terminal.
*   **Contagem Automatizada:** Lógica inteligente para o valor do Ás (computando como 1 ou 11 de acordo com a vantagem do jogador).
*   **Tomada de Decisão do Bot:** O Bot não joga às cegas; ele possui dois comportamentos aleatórios (um conservador focado em atingir 17 pontos e outro baseado em estimar as cartas visíveis do jogador).
*   **Sistema de Economia Virtual:** O jogador inicia com $100 e pode realizar ações como "Dobrar a Aposta" durante o seu turno.

Lógica de Decisão do Bot

O Bot avalia o jogo em cada rodada utilizando duas estratégias possíveis sorteadas no início do turno dele:
1.  **Modo Estratégico:** O Bot analisa a primeira carta aberta do jogador, assume um valor hipotético para a segunda carta e define uma pontuação alvo para tentar superar.
2.  **Modo Conservador:** O Bot segue a regra clássica dos cassinos, comprando cartas obrigatoriamente até atingir pelo menos 17 pontos.

Tecnologias Utilizadas

*   **Python 3.10+** (Utilização de estruturas modernas como `match-case`)
*   Biblioteca padrão `random` para o sorteio e embaralhamento das cartas
