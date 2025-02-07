""""''Enunciado:
Peça ao usuário para inserir duas listas de números e depois exiba:

Os números em comum (interseção)
Todos os números sem repetição (união)
Os números que aparecem na primeira lista, mas não na segunda
💡 Dica: Converta as listas em set() e use &, | e - para operações de conjuntos."""

def intersecção (conjunto_a,conjunto_b):
    inter = [x for x in range(1,100) if x in conjunto_a and x in conjunto_b]
    print("A ∩ B = ",inter)

def exclusivos (conjunto_a,conjunto_b):
    exclusive = [x for x in range(1,100) if x in conjunto_a and x not in conjunto_b]
    print("números exclusivos do conjunto A =",exclusive)

elementos = (input("digite numeros inteiros separados por virgula: "))
A = set(map(int,elementos.split(",")))

elementos2 = (input("digite numeros inteiros separados por virgula: "))
B = set(map(int,elementos2.split(",")))



intersecção(A,B)
print("A ∪ B =",set.union(A,B))
exclusivos(A,B)
