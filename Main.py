from Processamento import calcularMedia, alunosRecuperacao, MelhorAluno, notasAusentes, gerarRelatorio


print("Sistema organizacional escolar")
print("-"*100)

dados = [
    ("Lucas", [8, 7, 9, 10, 6]),
    ("Ligia", [5, 6]),
    ("Fernando", []),
    ("Rodrigo Tadeu", [10,10,10,10,10])
]

topAluno = MelhorAluno(dados)
print(f"O melhor estudande do semestre com a maior média foi: {topAluno[0]} com média: {topAluno[1]}")