# Introdução

A COVID-19, doença causada pelo vírus SARS-COV-2, afeta todo o planeta desde o ano de 2019. Altas taxas de transmissão do vírus podem causar o colapso do sistema de saúde através, entre outro modos, da falta de leitos de UTI disponíveis para a população, o que pode gerar filas [[1]](https://g1.globo.com/bemestar/coronavirus/noticia/2021/03/20/mortes-na-fila-por-um-leito-de-uti-falta-de-insumos-e-funerarias-sem-ferias-os-sinais-do-colapso-na-saude-brasileira.ghtml). Prever se um paciente que der entrada no hospital precisará de atendimento em UTI ou não pode ser uma das formas de diminuir as chances de fila para leitos, pois assim, por exemplo, o hospital tem mais tempo para abrir novos leitos ou agendar a transferência do paciente para outro hospital com leitos disponíveis.

Usando uma [base de dados](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19) de internações por COVID-19 disponibilizada pelo hospital Sírio-Libanês e modelos de machine learning através da biblioteca scikit-learn [[2]](https://scikit-learn.org/stable/), neste projeto vamos gerar um modelo que possa prever se um paciente precisará de atendimento em UTI ou não. 

O projeto está dividido da seguinte maneira: 
- Primeiramente analisaremos a base de dados sem o uso de machine learning para tentar detectar algum padrão entre os pacientes que presisaram de atendimento de UTI;
- Posteriormente, usando algoritmos de machine learning, selecionaremos o modelo com melhor performance através de dois métodos distintos para prever se um paciente precisará ou não de atendimento em UTI.

# Arquivos:

1. Base de dados: Kaggle_Sirio_Libanes_ICU_Prediction.xlsx, a base de dados também pode ser acessada por: https://www.kaggle.com/S%C3%ADrio-Libanes/covid19
2. Jupyter notebok: Desafio_Modulo_5.ipynb, o notebook também pode ser acessado pelo Google Colab: https://drive.google.com/file/d/1v8295QT9yZB2O_M42Of3sYM9ceUI9nmg/view?usp=sharing

# Conclusão:

Neste projeto analisamos a base de dados do hospital Sírio-Libanês com o objetivo de prever se um paciente internado por COVID-19 precisará ou não de atendimento em UTI. Na primeira análise, sem o uso de modelos de machine learning, observamos que a faixa de idade do paciente podería ser um fator importante, e que o sexo masculino é mais internado do que o sexo feminino. Entretanto, resaltamos que a diferença no número de internação entre homens e mulheres pode ser por motivo socioeconomicos, por exemplo. Na segunda análise, usando modelos de machine learning, o algoritmo random forest foi o que obteve maior taxa de acurácia média por dois métodos de análise diferentes, cerca de 76% com intervalo de 65.8% a 86.5%, valor maior que o baseline de 53.8%, além disso, o modelo apresentou uma taxa de falso negativo de cerca de 30%, um valor menor quando comparado com o Dummy classifier, que apresentou uma taxa de falso negativo de 100%.
