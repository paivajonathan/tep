import json
import random
import datetime


def main():
    avaliacao = {
        'data': datetime.datetime.now().strftime('%d/%m/%Y'),
        'alunos': [],
    }

    nomes_alunos = ['John', 'Mary', 'Joseph']

    for nome in nomes_alunos:
        aluno = {
            'nome': nome,
            'notas': [],
            'media': 0,
            'situacao': 'Reprovado',
        }

        for _ in range(4):
            nota = round(random.uniform(0.0, 10.0), 2)
            aluno['notas'].append(nota)
        
        media = round(sum(aluno['notas']) / len(aluno['notas']), 2)
        aluno['media'] = media

        if media > 7:
            aluno['situacao'] = 'Aprovado'
        else:
            aluno['situacao'] = 'Reprovado'

        avaliacao['alunos'].append(aluno)

    with open('avaliacao.json', 'w') as f:
        f.write(json.dumps(avaliacao, indent=2))


if __name__ == '__main__':
    main()
