blacklist = [';', '-', '\'', 'all', 'and', 'any', 'as', 'asc', 'avg', 'between', 'by', 'case', 'count', 'create', 'cross', 'database',  'delete', 'desc', 'distinct', 'drop', 'else', 'end', 'exists', 'false', 'from', 'group', 'having', 'in', 'inner',  'insert', 'is', 'join', 'left', 'like', 'limit', 'max', 'min', 'natural', 'not', 'null', 'on', 'or', 'order', 'outer',  'regexp', 'right', 'schema', 'select', 'some', 'sum', 'table', 'then', 'true', 'union', 'update', 'using', 'when',  'where', 'xor']

while True:
    word = input()
    print(any((x in word.lower() for x in blacklist)))