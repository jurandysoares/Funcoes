from pathlib import Path
from slugify import slugify

conteudo = open('./algoritmos_ex_01_funcoes.md').read().split('##')
slug_questoes = []
docs_dir = Path()/'docs'
docs_dir.mkdir(exist_ok=True)

for (i,q) in enumerate(conteudo[1:], start=1):
    linhas = q.splitlines()
    titulo = f'{i:02}. {linhas[0]}'
    slug_titulo = slugify(titulo)
    slug_questoes.append(f'- {slug_titulo}.md')

    print(f'- [{titulo}]({slug_titulo})')

    with open(docs_dir/f'{slug_titulo}.md', mode='w') as arq_questao:
        arq_questao.write(f'# {i:02}.')
        arq_questao.write(q)


print('\n'.join(slug_questoes))
