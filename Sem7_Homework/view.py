def consol_out(data):
    string = ''
    for i in data.values():
        string += '  '.join(i) if type(i) is list else str(i) + '\t'

    print(string)