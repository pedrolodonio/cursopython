"""Crie uma classe Animal com um método emitir_som() que apenas imprime "Som genérico de animal".

Depois, crie duas classes que herdam de Animal:

Cachorro → sobrescreve emitir_som() para exibir "Au au!".
Gato → sobrescreve emitir_som() para exibir "Miau!".
📌 Dicas:

Instancie objetos das classes e chame emitir_som() para verificar o polimorfismo."""

class Animal:
    def emitir_som (self):
        print("som genérico de animal")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Gato(Animal):
    def emitir_som(self):
        print("miau miau")

animais = [Animal(),Cachorro(),Gato()]

for animal in animais:
    animal.emitir_som()