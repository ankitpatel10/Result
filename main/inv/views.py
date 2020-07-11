from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ComputerForm
from .models import Computer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import xlwt


# Create your views here.
def index(request):
    title = 'Welcome: This is the INV Page'
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)


def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()

        messages.success(request, 'Successfully Saved')
        return redirect('/inv/cl')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'computer_entry.html', context)


def computer_list(request):
    title = 'Computers List'
    queryset = Computer.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'computer_list.html', context)


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Computer.objects.filter(Q(computer_name__icontains=srch) |
                                            Q(IP_address__icontains=srch) |
                                            Q(location__icontains=srch)

                                            )
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            # return HttpResponseRedirect('search')
            # return render(request, 'search.html')
            messages.error(request, 'Please write in search')
    return render(request, 'search.html')


def computer_delete(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect('cl')


def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(request, 'Successfully Saved')
        return redirect('cl')
    context = {
        "title": 'Edit ' + str(instance.computer_name),
        "instance": instance,
        "form": form,
    }
    return render(request, 'computer_entry.html', context)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Computer.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Computer')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['computer_name', 'IP_address', 'MAC_address', 'operating_system',
               'users_name', 'location',
               'Installation_date', 'timestamp']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Computer.objects.all().values_list('computer_name', 'IP_address', 'MAC_address', 'operating_system',
                                              'users_name', 'location',
                                              'Installation_date', 'timestamp')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
