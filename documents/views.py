from django.shortcuts import render, HttpResponse, redirect

from documents.forms import ReaderForm
from documents.models import Reader, Ticket
from djongo.models.fields import ObjectId, JSONField
# Create your views here.


models = {'reader': Reader, 'ticket': Ticket}


def index(request, instance="reader"):

    if request.GET:
        req = dict(request.GET)
        clear_req = {}

        for key in req:
            if req[key] != ['']:
                clear_req[key] = req[key]
        print(clear_req)
        instance = Reader.objects.filter(**clear_req)
        print(instance)

    else:
        instance = Reader.objects.all()
    return render(request, 'documents/base.html', {'readers': instance})


def create_reader(request, instance_id, instance="reader"):
    context = {}
    if request.method == 'POST':
        if instance_id == "0":

            new_data = {}
            new_data['name'] = request.POST['name']
            new_data['phone'] = request.POST['phone']

            form = ReaderForm(new_data)

        else:
            instance = Reader.objects.get(_id=ObjectId(instance_id))
            attributes = {}
            req = request.POST.copy()
            print(req)
            for x in req:
                if x.startswith('attr_'):
                    attributes[x[5:]] = request.POST[x]
            new_attributes = {}
            for x in req:
                if x.startswith('key_'):
                    new_attributes[request.POST[x]] = attributes[x[4:]]

            print(new_attributes)
            form = ReaderForm(request.POST, attributes=new_attributes, instance=instance)

        if form.is_valid():

            form.save()

        context["keys"] = list(instance.attributes.keys())
        context["attributes"] = dict(instance.attributes)

    else:
        if instance_id == "0":
            form = ReaderForm()
        else:
            instance = Reader.objects.get(_id=ObjectId(instance_id))
            form = ReaderForm(instance=instance)
            context["keys"] = list(instance.attributes.keys())
            context["attributes"] = dict(instance.attributes)
    context['form'] = form
    context['instance'] = instance
    return render(request, 'documents/create_reader.html', context=context)


def add_product(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.attributes = request.POST["attributes"]
            instance.save()
    return redirect('index')


def delete_reader(request, instance_id):
    instance = Reader.objects.get(_id=ObjectId(instance_id))
    instance.delete()


def delete_attr(request, instance_id):
    instance = Reader.objects.get(_id=ObjectId(instance_id))

    if request.POST['key'] in instance.attribute:
        del instance.attribute[request.POST['key']]
        instance.save()


def add_attribute(request, instance_id):
    if request.method == 'POST':
        instance = Reader.objects.get(_id=ObjectId(instance_id))
        instance.attributes[f'new_attribute_{len(instance.attributes)}'] = f'new_attribute_{len(instance.attributes)}'
        instance_save = instance.save()
    return redirect(f'/reader/{instance_id}')