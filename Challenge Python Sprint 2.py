import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

# Função para obter as corridas de Fórmula E da temporada escolhida]
def get_formula_e_races(season):
    url = f"https://ergast.com/api/f1/{season}.json"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Falha ao recuperar os dados: {response.status_code}")
        return []

    data = response.json()
    races = data.get("MRData", {}).get("RaceTable", {}).get("Races", [])

    if not races:
        print(f"Nenhuma corrida encontrada para a temporada {season}")
        return []

    race_data = []
    for race in races:
        race_name = race.get("raceName")
        circuit_name = race.get("Circuit", {}).get("circuitName")
        date = race.get("date")
        location = race.get("Circuit", {}).get("Location", {})
        locality = location.get("locality", "N/A")
        country = location.get("country", "N/A")

        race_info = {
            'race_name': race_name,
            'circuit_name': circuit_name,
            'date': date,
            'location': f"{locality}, {country}"
        }

        race_data.append(race_info)

        # Exibe as informações da corrida
        print(f"Corrida: {race_name}")
        print(f"Circuito: {circuit_name}")
        print(f"Data: {date}")
        print(f"Localização: {locality}, {country}")
        print("="*40)

    return race_data

# Função para calcular e plotar o limite e derivadas
def plot_limit_derivative(race_times):
    # Simulação de tempos de corrida como uma função contínua
    x = np.linspace(0, len(race_times), 100)
    y = np.interp(x, np.arange(len(race_times)), race_times)

    # Derivada da função que simula os tempos
    dydx = np.gradient(y, x)

    # Plotando o gráfico original e a derivada
    plt.figure(figsize=(12, 6))

    # Gráfico original
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label='Função (tempos de corrida)', color='blue')
    plt.title('Função que Simula Tempos de Corrida')
    plt.xlabel('Corridas')
    plt.ylabel('Tempo de Corrida')
    plt.grid(True)

    # Gráfico da derivada
    plt.subplot(1, 2, 2)
    plt.plot(x, dydx, label='Derivada da Função', color='red')
    plt.title('Derivada dos Tempos de Corrida')
    plt.xlabel('Corridas')
    plt.ylabel('Derivada (Taxa de Variação)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Função principal para interatividade e execução do programa
def main():
    # Interatividade com o usuário para escolher a temporada
    season = int(input("Digite o ano da temporada de Fórmula E que deseja visualizar (ex: 2024): "))

    # Obter dados das corridas da temporada especificada
    race_data = get_formula_e_races(season)

    if race_data:
        # Simulando tempos de corrida (em segundos) para cada corrida para fins de cálculo
        # Normalmente, você obteria esses dados da API
        race_times = np.random.randint(5000, 6000, len(race_data))  # Tempos aleatórios entre 5000 e 6000 segundos

        print("\nTempos simulados de corrida (em segundos):")
        for i, race in enumerate(race_data):
            print(f"{race['race_name']}: {race_times[i]} segundos")

        # Plotar limite e derivada dos tempos simulados
        plot_limit_derivative(race_times)

if __name__ == "__main__":
    main()