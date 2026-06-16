from faker import Faker
import random
from figurinha import Figurinha

fake = Faker("pt_BR")

SELECOES = [
    "Argentina",
    "Brasil",
    "Uruguai",
    "Paraguai",
    "Colômbia",
    "Equador",

    "Estados Unidos",
    "México",
    "Canadá",
    "Costa Rica",
    "Panamá",
    "Honduras",

    "França",
    "Alemanha",
    "Espanha",
    "Portugal",
    "Inglaterra",
    "Itália",
    "Holanda",
    "Bélgica",
    "Croácia",
    "Dinamarca",
    "Suíça",
    "Polônia",
    "Sérvia",
    "Áustria",
    "Suécia",
    "Noruega",
    "Escócia",
    "Turquia",

    "Marrocos",
    "Senegal",
    "Nigéria",
    "Camarões",
    "Gana",
    "Argélia",
    "Tunísia",
    "Costa do Marfim",
    "Egito",

    "Japão",
    "Coreia do Sul",
    "Austrália",
    "Irã",
    "Arábia Saudita",
    "Catar",
    "Uzbequistão",
    "Iraque",

    "Nova Zelândia"
]

def gerar_figurinha(numero):
    return Figurinha(
        numero,
        fake.name(),
        random.choice(SELECOES)
    )