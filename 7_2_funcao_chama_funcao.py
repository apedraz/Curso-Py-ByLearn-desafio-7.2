# A primeira função recebe duas notas do usuário e a segunda calcula a média.

def media():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    return calcular_media(nota1, nota2)

def calcular_media(nota1, nota2):
    media =  (nota1 + nota2) / 2
    return media

minha_media = media()
print('Minha média é: ', minha_media)