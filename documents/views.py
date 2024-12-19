from django.shortcuts import render, HttpResponse, redirect

from documents.forms import ReaderForm, TicketForm
from documents.models import Reader, Ticket
from djongo.models.fields import ObjectId, JSONField
# Create your views here.


models = {'reader': Reader, 'ticket': Ticket}
forms = {'reader': ReaderForm, 'ticket': TicketForm}


def index(request, instance):
    instance_type = models[instance]
    instance_str = instance
    if request.GET:
        req = dict(request.GET)
        clear_req = {}

        for key in req:
            if req[key] != ['']:
                clear_req[key] = req[key]
        print(clear_req)
        instance = instance_type.objects.filter(**clear_req)
        print(instance)

    else:
        instance = instance_type.objects.all()
    return render(request, 'documents/base.html', {'readers': instance, 'instance_type': instance_str})


def create_reader(request, instance_id, instance="reader"):
    context = {'instance_type': instance}
    instance_type = models[instance]

    form_type = forms[instance]
    if request.method == 'POST':
        if instance_id == "0":

            new_data = {}

            form = form_type(request.POST)

        else:
            instance = instance_type.objects.get(_id=ObjectId(instance_id))
            attributes = {}
            req = request.POST.dict().copy()
            print(req)
            for x in request.POST:
                if x.startswith('attr_'):
                    attributes[x[5:]] = request.POST[x]
            new_attributes = {}
            for x in request.POST:
                if x.startswith('checkbox_') and req[x] == 'on':
                    del req[f"key_{x[9:]}"]

            for x in req:
                if x.startswith('key_'):
                    new_attributes[req[x]] = attributes[x[4:]]

            print(new_attributes)
            form = form_type(request.POST, attributes=new_attributes, instance=instance)

        if form.is_valid():

            form.save()

        context["keys"] = list(instance.attributes.keys())
        context["attributes"] = dict(instance.attributes)

    else:
        if instance_id == "0":
            form = form_type()
        else:
            instance = instance_type.objects.get(_id=ObjectId(instance_id))
            form = form_type(instance=instance)
            context["keys"] = list(instance.attributes.keys())
            context["attributes"] = dict(instance.attributes)
    context['form'] = form
    context['instance'] = instance

    return render(request, 'documents/create_reader.html', context=context)


def delete_reader(request, instance_id, instance):
    instance_str = instance
    instance_type = models[instance]

    instance = instance_type.objects.get(_id=ObjectId(instance_id))
    instance.delete()
    return redirect(f'/{instance_str}')


def add_attribute(request, instance_id, instance):
    instance_type = models[instance]
    instance_str = instance
    if request.method == 'POST':
        instance = instance_type.objects.get(_id=ObjectId(instance_id))
        instance.attributes[f'new_attribute_{len(instance.attributes)}'] = f'new_attribute_{len(instance.attributes)}'
        instance_save = instance.save()
    return redirect(f'/{instance_str}/{instance_id}')