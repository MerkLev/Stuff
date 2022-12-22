def type_of_view(Data):
    if Data == 'все контакты':
        Data = True
    elif Data == 'по фильтру':
        Data = False
    else:
        while Data != 'все контакты' and Data != 'по фильтру':
            Data = input('некорректный тип запроса, ввод типа строго маске (все контакты/по фильтру):')
        if Data == 'все контакты':
            Data = True
        else:
            Data = False
    return (Data)