def metade(v=0):
    v /= 2
    return v


def dobro(v=0):
    v *= 2
    return v


def aumento(v=0, p=10):
    v = ((v*p)/100)+v
    return v,p


def format_moeda(v=0):
    return (f'R${v:.2f}'.replace('.',','))
