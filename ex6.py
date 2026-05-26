lista_a = ["A", "B", "C"]

lista_b = lista_a
lista_c = lista_a.copy()
lista_b.append('D')
'A lista_a será alterada junto com a lista_b, por ser uma referência, já a lista_c por ser uma cópia independente permanecerá inalterada.'