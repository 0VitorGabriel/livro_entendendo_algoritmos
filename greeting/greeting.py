def sauda(nome):
    print("Ola " + nome + "!")
    sauda2(nome)
    print("Preparando para dizer tchau...")
    tchau()

def sauda2(nome):
    print("Como vai " + nome + "?")

def tchau():
    print("ok, tchau!")


sauda("Vitor")