from ninja import Router, Query
from .models import Livros, Categorias
from .schemas import LivroSchema, AvaliacaoSchema, FiltrosSortear, LivrosViewSchema
from typing import List

livros_router = Router()

@livros_router.get('/', response={200: List[LivrosViewSchema]})
def get_livro(request):
    livros = Livros.objects.all()
    return livros

@livros_router.post('/', response={200: LivroSchema})
def create_livro(request, livro_schema: LivroSchema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias = livro_schema.dict()['categorias']
    livro = Livros(nome=nome, streaming=streaming)
    livro.save()
    for categoria in categorias:
        livro.categorias.add(Categorias.objects.get(id=categoria))
    livro.save()
    return livro

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id: int, avaliacao_schema: AvaliacaoSchema):
    comentarios = avaliacao_schema.dict()['comentarios']
    nota = avaliacao_schema.dict()['nota']
    livro = Livros.objects.get(id=livro_id)
    livro.comentarios = comentarios
    livro.nota = nota
    livro.save()
    return {'status': 'Avaliação realizada com sucesso'}

@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id: int):
    livro = Livros.objects.get(id=livro_id)
    livro.delete()
    return livro_id

@livros_router.get('/sortear/', response={200: LivroSchema, 404: dict})
def sortear_livro(request, filtros: Query[FiltrosSortear]):
    nota_minima = filtros.dict()['nota_minima']
    categoria = filtros.dict()['categorias']
    reler = filtros.dict()['reler']
    livros = Livros.objects.all()
    if not reler:
        livros = livros.filter(nota=None)
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    if categoria:
        livros = livros.filter(categorias__id=categoria)
        livro = livros.order_by('?').first()
    if livros.count() > 0:
        return 200, livro
    else:
        return 404, {'status': 'Livro não encontrado'}