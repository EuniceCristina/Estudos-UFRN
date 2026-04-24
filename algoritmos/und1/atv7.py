print("Como sao os seus habitos de estudo?")
print("""
1. Voce costuma estudar com horario 
definido?
a) Sempre (+2 pontos)
b) As vezes (+1 ponto)
c) Nunca (0 pontos)
      """)
q1 = int(input("Sua pontuacao : "))

print("""
2. Quando recebe uma atividade, 
você:
a) Começa logo (+2 pontos)
b) Deixa para depois, mas faz (+1 
ponto)
c) So lembra no ultimo momento (0 
pontos)
      """)
q2 = int(input("Sua pontuacao : "))
print("""
3. Você anota prazos e 
compromissos?
a) Sim, sempre (+2 pontos)
b) As vezes (+1 ponto)
c) Nao (0 pontos)
      """)
q3 = int(input("Sua pontuacao : "))

print("""
4. Durante os estudos, você se distrai
com facilidade?
a) Raramente (+2 pontos)
b) As vezes (+1 ponto)
c) Frequentemente (0 pontos)
      """)
q4 = int(input("Sua pontuacao : "))
total = q1+q2+q3+q4

print("""
Classificacao final
7 a 8 pontos → Perfil muito organizado
4 a 6 pontos → Perfil moderadamente organizado
0 a 3 pontos → Perfil pouco organizado
""")

print("Sua pontuacao final foi de : ", total)