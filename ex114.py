import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site PUDIM não está acessivel no momento.')
else:
    print('Consegui acesar o site PUDIM com sucesso!')