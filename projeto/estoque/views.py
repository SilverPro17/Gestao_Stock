from django.shortcuts import render, resolve_url, get_object_or_404
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .models import Estoque, EstoqueItens
from .forms import EstoqueForm, EstoqueItensForm

def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    object_list = Estoque.objects.filter(movimento='e')
    context = {'object_list': object_list}
    return render(request, template_name, context)

def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = get_object_or_404(Estoque, pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque(movimento='e')  # Configura o movimento como "Entrada"
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=1,  # Sempre exibir pelo menos 1 formulário vazio
        can_delete=True  # Permitir exclusão de itens
    )
    
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.instance = form  # Associa o formset ao estoque principal
            formset.save()
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)
