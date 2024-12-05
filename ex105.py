# NOTAS DE ALUNOS
def notas(*nota, show=True):
    '''
    -> Função para ter médias das notas
    :param nota: adicionar as notas dos alunos
    :param show: (opcional) situação da turma
    :return: retorna um dicionário com informações dos alunos
    '''
    total=len(nota)
    maior=max(nota)
    menor=min(nota)
    média=sum(nota)/total
    turma = {}
    turma['total'] = total
    turma['maior'] = maior
    turma['menor'] = menor
    turma['média'] = média
    if show:
        if média<4:
            situação='RUIM!'
        if média>=4 and média<6:
            situação='RAZOAVEL!'
        if média>=6:
            situação='BOA!'
        turma['situação'] = situação
    return turma

# Programa principal
alunos=notas(2,2,2,2,show=True)
print(alunos)
#help(notas)