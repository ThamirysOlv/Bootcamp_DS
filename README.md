# Introdução

A COVID-19, doença causada pelo vírus SARS-COV-2, afeta todo o planeta desde o ano de 2019. Altas taxas de transmissão do vírus podem causar o colapso do sistema de saúde através, entre outro modos, da falta de leitos de UTI disponíveis para a população, o que pode gerar filas. Prever se um paciente que der entrada no hospital precisará de atendimento em UTI ou não pode ser uma das formas de diminuir as chances de fila para leitos, pois assim, por exemplo, o hospital tem mais tempo para abrir novos leitos ou agendar a transferência do paciente para outro hospital com leitos disponíveis.

Usando uma [base de dados](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19) de internações por COVID-19 disponibilizada pelo hospital Sírio-Libanês e modelos de machine learning através da biblioteca scikit-learn [[2]](https://scikit-learn.org/stable/), neste projeto vamos gerar um modelo que possa prever se um paciente precisará de atendimento em UTI ou não. 

O projeto está dividido da seguinte maneira: 
- Primeiramente analisaremos a base de dados sem o uso de machine learning para tentar detectar algum padrão entre os pacientes que presisaram de atendimento de UTI;
- Posteriormente, usando algoritmos de machine learning, selecionaremos o modelo com melhor performance através de dois métodos distintos para prever se um paciente precisará ou não de atendimento em UTI.

Link para o colab: https://drive.google.com/file/d/1v8295QT9yZB2O_M42Of3sYM9ceUI9nmg/view?usp=sharing
