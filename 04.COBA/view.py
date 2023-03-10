from django.shortcuts import render


def jilnap(request):
    data = dict(judul = 'Input Ganjil Genap')
    if request.method == "POST":
        inputan = int(request.POST.get('inputanAngka'))
        if (inputan % 2) == 0:
            data['inputan'] = f'{inputan}'
            data['warna'] = "#FF00FF"
        elif (inputan %2) != 0:
            data['inputan'] = f'{inputan}'
            data['warna'] = "#008aff"

    return render(request, 'ini.html', data)