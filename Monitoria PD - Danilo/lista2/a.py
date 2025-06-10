media_aprovacao = float(input())
nota_1a_prova = float(input())
nota_2a_prova = float(input())
valor_media = (nota_1a_prova+nota_2a_prova)/2
if (valor_media) >=  media_aprovacao:
    print(f"Aluno aprovado na disciplina! Parabens! A sua media foi: {valor_media:.2f}")