def población():
    info = "Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000; Mumbai:21_357_000;São Paulo:21_297_000"
    algo = dict(sub.split(":") for sub in info.split(";"))
    for key, values in algo.items():
        algo[key] = int(values)
    print(algo)


def contar():
    word = "boom"
    ocurrencias = dict((i, word.count(i)) for i in list(word))
    print(ocurrencias)


def porcentaje():
    info = "Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000; Mumbai:21_357_000;São Paulo:21_297_000"
    algo = dict(sub.split(":") for sub in info.split(";"))
    for key, values in algo.items():
        algo[key] = int(values)
    sum_v = sum(algo.values())
    for key, values in algo.items():
        algo[key] = (values * 100) / sum_v
    print(algo)


def notas():
    note = {
        "John": 4,
        "Marc": 7,
        "Andreas": 3,
        "Sarah": 6,
        "Meryl": 2,
        "Anthony": 8,
        "Carol": 3,
    }
    note_aprov = {name.upper(): cali for (name, cali) in note.items() if cali > 5}
    note_desap = {name.lower(): cali for (name, cali) in note.items() if cali < 5}
    print(note_aprov)
    print(note_desap)


notas()
