def filters_by_request(request):
    filters = {}

    param_nameDevice = request.GET.get('name')
    param_typeDevice = request.GET.get('type')
    param_statusDevice = request.GET.get('status')

    if param_nameDevice:
        nameDevice = {'nameDevice__icontains': param_nameDevice}
        filters.update(nameDevice)

    if param_statusDevice:
        statusDevice = {'statusDevice__description__icontains': param_statusDevice}
        filters.update(statusDevice)

    if param_typeDevice:
        typeDevice = {'typeDevice__nameType__icontains': param_typeDevice}
        filters.update(typeDevice)


    return filters