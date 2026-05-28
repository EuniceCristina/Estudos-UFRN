#🎬 SISTEMA DE GESTÃO DE CINEMAS

#├── 👤 Módulo de Usuários
#├── 🎥 Módulo de Filmes
#├── 🪑 Módulo de Salas e Assentos
#├── 🎟️ Módulo de Ingressos
##├── 📅 Módulo de Sessões
#├── 🍿 Módulo de Bomboniere
#├── 💰 Módulo Financeiro
#├── 📊 Módulo de Relatórios
#├── ⚙️ Configurações do Sistema
#├── ℹ️ Sobre o Sistema
#└── 🚪 Sair

chave = 'S'
print("#"*30)
print(
      """
Sistema de Gestão de Cinemas
      """)
print("#"*30)

while chave=='S':
    print("""
0 - Módulo de Usuários
1 - Módulo de Filmes
2 - Módulo de Salas e Assentos
3 - Módulo de Ingressos
4 - Módulo de Bomboniere
5 - Módulo Financeiro
6 - Módulo de Relatórios
7 - Sobre o Sistema
8 - Sair
          
          """)
    opcao = int(input('Escolha o módulo que deseja acessar. [0-8] :'))
    
    if opcao == 8:
        chave = 'N'