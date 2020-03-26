from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from io import BytesIO
from django.urls import reverse

def overview(request):
    modulkat_list = Modulkatalog.objects.order_by('mk_jahr', 'mk_von_studiengang')
    template = loader.get_template('adminpanel/overview.html')
    context = {
        'modulkat_list': modulkat_list,
    }
    return HttpResponse(template.render(context, request))

def generatecontext(modulkat_id):
    modulkat = Modulkatalog.objects.get(pk=modulkat_id)
    studien_name = modulkat.mk_von_studiengang.sg_name
    fak_name = modulkat.mk_von_studiengang.gehoert_zu.fk_name
    typen= Besitzt.objects.filter(modulkatalog=modulkat).order_by('typ', 'modul__md_studienjahr')
    context = {
        'modulkat': modulkat,
        'fak_name': fak_name,
        'studien_name': studien_name,
        'typen': typen
    }
    return context

def renderashtml(request, modulkat_id):
    return render(request, 'adminpanel/modulkatalog.html', generatecontext(modulkat_id))

def renderaspdf(request, modulkat_id):
    template = get_template('adminpanel/modulkatalog.html')
    html = template.render(generatecontext(modulkat_id))
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)

def copymodel(request, modulkat_id):
    modulkat = Modulkatalog.objects.get(pk=modulkat_id)
    old_module = modulkat.mk_module.all()
    old_besitzt = modulkat.besitzt_set.all()
    print(old_besitzt)
    modulkat.pk = None
    modulkat.save()
    for t in old_besitzt:
        modulkat.mk_module.add(t.modul, through_defaults={'typ': t.typ})
    return HttpResponseRedirect(reverse('index'))


