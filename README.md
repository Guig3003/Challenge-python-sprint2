
# Explicação Detalhada do Código

1. Importação de Bibliotecas
•	requests: Biblioteca utilizada para fazer requisições HTTP, usada para obter os dados das corridas via API.
•	numpy (np): Biblioteca para trabalhar com arrays e funções matemáticas. Aqui, é usada para gerar os dados simulados de tempos e calcular derivadas.
•	matplotlib.pyplot: Biblioteca para plotar gráficos em Python.
•	scipy.misc.derivative: Importação usada para calcular a derivada de funções.
2. Função get_formula_e_races(season)
Esta função busca informações das corridas de uma temporada específica de Fórmula E usando a API pública da Ergast (F1/Fórmula E). Ela exibe informações detalhadas sobre cada corrida e retorna esses dados.
Passo a Passo:
URL da API: Monta a URL da API para uma temporada específica usando o ano (season) fornecido pelo usuário.
Requisição HTTP: Envia a requisição GET para a API e verifica se a resposta foi bem-sucedida (código de status 200).
Processamento de Dados:
o	Os dados da resposta são convertidos para JSON, e a função extrai a lista de corridas disponíveis no campo "Races".
o	Se não houver corridas, a função exibe uma mensagem informando.
Extração e Exibição dos Dados: Para cada corrida, a função extrai o nome da corrida, nome do circuito, data, e localização (cidade e país). Esses dados são organizados em um dicionário e armazenados em uma lista chamada race_data.
Retorno: A função retorna a lista race_data, que contém os dados das corridas para a temporada solicitada.
3. Função plot_limit_derivative(race_times)
Esta função recebe uma lista de tempos de corrida simulados e realiza dois cálculos:
Simulação de uma função contínua baseada nesses tempos.
Cálculo da derivada dessa função para medir a taxa de variação dos tempos entre as corridas.
- Passo a Passo:
Simulação de Função Contínua:
o	O eixo x é construído como uma sequência de valores ao longo de 100 pontos, e os tempos de corrida reais (discretos) são interpolados para criar uma função contínua (y) que representa os tempos.
Cálculo da Derivada:
o	Utiliza np.gradient para calcular a derivada numérica da função y. A derivada nos mostra como os tempos de corrida variam entre as corridas consecutivas.
Plotagem dos Gráficos:
o	Dois gráficos são criados:
O primeiro gráfico mostra a função original dos tempos.
O segundo gráfico mostra a derivada da função, indicando a taxa de variação dos tempos de corrida.
o	Ambos os gráficos são exibidos lado a lado para facilitar a comparação visual.
Exemplo dos Gráficos:
Gráfico 1 (Função dos Tempos): Mostra os tempos de corrida (em segundos) ao longo das corridas.
Gráfico 2 (Derivada): Mostra a taxa de variação dos tempos de corrida de uma corrida para outra.
4. Função main()
Esta função orquestra a execução do programa, tornando-o interativo para o usuário.
- Interatividade:
O usuário é solicitado a fornecer o ano da temporada de Fórmula E de interesse.
A função get_formula_e_races é chamada para buscar os dados das corridas daquela temporada.
- Simulação dos Tempos de Corrida:
Tempos Simulados: Como a API utilizada não fornece diretamente os tempos de corrida, são gerados tempos simulados aleatórios entre 5000 e 6000 segundos para cada corrida, com o uso da função np.random.randint().
- Exibição dos Tempos:
Os tempos simulados são exibidos junto com o nome das corridas para facilitar a visualização do usuário.
- Plotagem dos Gráficos:
A função plot_limit_derivative é chamada para plotar os gráficos da função dos tempos e da derivada com base nos tempos simulados.
5. Execução do Programa
A função main() é executada apenas se o script for executado diretamente, permitindo que o usuário forneça a temporada de interesse e visualize as informações e gráficos correspondentes.
# Link do video
https://youtu.be/4lJdfKFwyqY
