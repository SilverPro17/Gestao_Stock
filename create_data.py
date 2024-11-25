import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto

class Utils:
	'''Metodos genéricos.'''
	@staticmethod
	def gen_digits(max_length):
		return str(''.join(choice(string.digits) for i in range(max_length)))

class ProdutoClass:
	@staticmethod
	def criar_produtos(produtos):
		Produto.objects.all().delete()
		aux = []
		for produto in produtos:
			data = dict(
				produto=produto,
				importado=choice((True, False)),
				ncm=Utils.gen_digits(8),
				preco=random()*randint(10,50),
				estoque=randint(10,200),
			)
			obj = Produto(**data)
			aux.append(obj)
		Produto.objects.bulk_create(aux)



produtos = (
    'Prumo de Ferro',
    'Tábua de 40cm',  
    'Tábua de 20cm', 
    'Tábua de 10cm', 
    'Viga de Madeira 2m', 
    'Viga de Madeira 3m', 
    'Viga de Madeira 6m', 
    'Chapa Preta', 
    'Bloco 20x10x40(Vazados)', 
    'Bloco 20x10x40(Massiços)',
    'Bloco 20x15x40(Vazados)', 
    'Bloco 20x20x40(Vazados)',
    'Bloco 20x20x40(Massiços)', 
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()

print('Tempo: ', toc -tic)