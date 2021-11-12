import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def internacoes():
  internacoes = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/internacoes_RE.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 3, skipfooter=11, engine='python', thousands='.', decimal=',')
  internacoes = internacoes.set_index("Região")
  internacoes = internacoes.sort_values("Total", axis = 0, ascending=False)
  internacoes = internacoes.drop("Total", axis = 1)
  internacoes = internacoes.drop("Total", axis = 0)
  internacoes.index = internacoes.index.str.slice(9)
  internacoes = internacoes.iloc[:, 91:]
  return internacoes

def internacoes_covid():
  internacoes_covid = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/internacoes_covid_RE.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 4, skipfooter=11, engine='python', thousands='.', decimal=',')
  internacoes_covid = internacoes_covid.set_index("Região")
  internacoes_covid = internacoes_covid.sort_values("Total", axis = 0, ascending=False)
  internacoes_covid = internacoes_covid.drop("Total", axis = 1)
  internacoes_covid = internacoes_covid.drop("Total", axis = 0)
  internacoes_covid.index = internacoes_covid.index.str.slice(9)
  return internacoes_covid

def plot_internacoes():
  ax = internacoes().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C8', 'C3'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,73), minor=True)
  ax.set_yticks(np.arange(50000,430000, 10000), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,72])
  ax.set_ylim([50000,430000])
  ax.tick_params(labelsize=14)
  plt.ylabel("# internações", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Número de internações por mês por região do Brasil entre Agosto de 2015 e Agosto de 2021", fontsize = 16)
  plt.show()

def plot_internacoes_covid():
  ax = internacoes_covid().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C3', 'C8'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,17), minor=True)
  ax.set_yticks(np.arange(0,71000, 1000), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,16])
  ax.set_ylim([0,70000])
  ax.tick_params(labelsize=14)
  plt.ylabel("# internações", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Número de internações por COVID-19 por mês por região do Brasil entre Abril de 2020 e Agosto de 2021", fontsize = 16)
  plt.show()

def porcentagem_internacoes_covid():
  porcentagem = internacoes_covid()*100/internacoes().iloc[:, 56:]
  porcentagem = porcentagem.reindex(["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"])
  return porcentagem

def plot_porcentagem():
  ax = porcentagem_internacoes_covid().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C3', 'C8'])
  ax.legend(loc='upper left', fontsize = 'x-large')
  ax.set_xticks(np.arange(0,17), minor=True)
  ax.set_yticks(np.arange(0,22, 1), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,16])
  ax.set_ylim([0,22])
  ax.tick_params(labelsize=14)
  plt.ylabel("% internações por COVID-19", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Porcentagem de internações causadas pela COVID-19 por mês por região do Brasil entre Abril de 2020 e Agosto de 2021", fontsize = 16)
  plt.show()

def populacao():
    populacao_2020 = pd.read_excel(os.path.join(THIS_FOLDER, 'datasets/estimativa_populacao_serie_2001_2020_TCU.xls'), 
        skiprows = 4, skipfooter=10)
    populacao_2020 = populacao_2020.drop(index=0)

    populacao_2021 = pd.read_excel(os.path.join(THIS_FOLDER, 'datasets/POP2021_20211029.xls'), usecols=lambda x: 'Unnamed' not in x, 
        skiprows = 1, skipfooter=7)
    populacao_2021.columns = ["Unidades da Federação", "2021"]
    populacao_2021['2021'] = populacao_2021['2021'].astype(float)
    populacao_2021 = populacao_2020.merge(populacao_2021, on='Unidades da Federação')
    populacao_2021 = populacao_2021.iloc[[1,9,19,24,28], [0,-2,-1]]
    populacao_2021 = populacao_2021.rename(columns={"Unidades da Federação": "Região",        2020: "2020"})
    populacao_2021 = populacao_2021.set_index("Região")
    populacao_2021.index = populacao_2021.index.str.slice(7)
    return populacao_2021

def porcentagem_populacao_covid():
  merged_2020 = pd.merge(left = internacoes_covid().iloc[:, 0:9], right = populacao().iloc[:,0], how = 'inner', on = 'Região')
  merged_2021 = pd.merge(left = internacoes_covid().iloc[:, 9:], right = populacao().iloc[:,1], how = 'inner', on = 'Região')

  for i in range(0,9):
    merged_2020.iloc[:,i] = merged_2020.iloc[:,i]*100/merged_2020.iloc[:,9]
  merged_2020 = merged_2020.drop('2020', axis = 1)
  for i in range(0,8):
    merged_2021.iloc[:,i] = merged_2021.iloc[:,i]*100/merged_2021.iloc[:,8]
  merged_2021 = merged_2021.drop('2021', axis = 1)
  total_merge = pd.merge(left = merged_2020, right = merged_2021, how = 'inner', on = 'Região')
  return total_merge

def plot_porcentagem_populacao_covid():
  ax = porcentagem_populacao_covid().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C3', 'C8'])
  ax.legend(loc='upper left', fontsize = 'x-large')
  ax.set_xticks(np.arange(0,17), minor=True)
  ax.set_yticks(np.arange(0,0.11, 0.005), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,16])
  ax.set_ylim([0,0.11])
  ax.tick_params(labelsize=14)
  plt.ylabel("% população internada por COVID-19", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Porcentagem da população internada por COVID-19 por mês por região do Brasil entre Abril de 2020 e Agosto de 2021", fontsize = 16)
  plt.show()

def plot_internacoes_mobilidade():
  ax = internacoes().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C8', 'C3'])
  ax.set_xticks(np.arange(0,73), minor=True)
  ax.set_yticks(np.arange(50000,430000, 10000), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,72])
  ax.set_ylim([50000,430000])
  ax.tick_params(labelsize=14)
  plt.ylabel("# internações", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Número de internações por mês por região do Brasil entre Agosto de 2015 e Agosto de 2021 \n e a redução no uso de transporte público brasileiro", fontsize = 16)
  plt.vlines(x=54, linewidth=2, color='C0', ymin=50000, ymax=430000, linestyle='--', 
                label = '-10.86%')
  plt.vlines(x=55, linewidth=2, color='C2', ymin=50000, ymax=430000, linestyle='--', 
                label = '-60.43%')
  plt.vlines(x=58, linewidth=2, color='C3', ymin=50000, ymax=430000, linestyle='--', 
                label = '-40.57%')
  plt.vlines(x=65, linewidth=2, color='C4', ymin=50000, ymax=430000, linestyle='--', 
                label = '-22.86%')
  plt.vlines(x=70, linewidth=2, color='C1', ymin=50000, ymax=430000, linestyle='--', 
                label = '-14.29%')
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  plt.show()

def tempo_medio_internacao():
  media_internacao = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/media_permanencia_RE.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 3, skipfooter=11, engine='python', thousands='.', decimal=',')
  media_internacao = media_internacao.set_index("Região")
  media_internacao = media_internacao.sort_values("Total", axis = 0, ascending=False)
  media_internacao = media_internacao.drop("Total", axis = 1)
  media_internacao = media_internacao.drop("Total", axis = 0)
  media_internacao.index = media_internacao.index.str.slice(9)
  media_internacao = media_internacao.iloc[:, 91:]
  return media_internacao

def tempo_medio_internacao_covid():
  media_internacao_covid = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/media_permanencia_covid_RE.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 4, skipfooter=11, engine='python', thousands='.', decimal=',')
  media_internacao_covid = media_internacao_covid.set_index("Região")
  media_internacao_covid = media_internacao_covid.sort_values("Total", axis = 0, ascending=False)
  media_internacao_covid = media_internacao_covid.drop("Total", axis = 1)
  media_internacao_covid = media_internacao_covid.drop("Total", axis = 0)
  media_internacao_covid.index = media_internacao_covid.index.str.slice(9)
  return media_internacao_covid

def plot_tempo_medio_internacao():
  ax = tempo_medio_internacao().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C8', 'C3'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,73), minor=True)
  ax.set_yticks(np.arange(4,6.6, 0.1), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,72])
  ax.set_ylim([4,6.5])
  ax.tick_params(labelsize=14)
  plt.ylabel("Tempo médio de internação (dias)", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Tempo médio de internação por mês por região do Brasil entre Agosto de 2015 e Agosto de 2021", fontsize = 16)
  plt.show()

def plot_tempo_medio_internacao_covid():
  ax = tempo_medio_internacao_covid().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C3', 'C8'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,17), minor=True)
  ax.set_yticks(np.arange(5,11, 0.1), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,16])
  ax.set_ylim([5,11])
  ax.tick_params(labelsize=14)
  plt.ylabel("Tempo médio de internação (dias)", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Tempo médio de internação por COVID-19 por mês por região do Brasil entre Abril de 2020 e Agosto de 2021", fontsize = 16)
  plt.show()

def valor_medio_internacao():
  media_internacao = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/valor_medio_internacao.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 3, skipfooter=11, engine='python', thousands='.', decimal=',')
  media_internacao = media_internacao.set_index("Região")
  media_internacao = media_internacao.sort_values("Total", axis = 0, ascending=False)
  media_internacao = media_internacao.drop("Total", axis = 1)
  media_internacao = media_internacao.drop("Total", axis = 0)
  media_internacao.index = media_internacao.index.str.slice(9)
  media_internacao = media_internacao.iloc[:, 91:]
  return media_internacao

def valor_medio_internacao_covid():
  media_internacao_covid = pd.read_csv(os.path.join(THIS_FOLDER, 'datasets/valor_medio_internacao_covid.csv'), sep = ';', encoding='iso-8859-1', 
                                skiprows = 4, skipfooter=11, engine='python', thousands='.', decimal=',')
  media_internacao_covid = media_internacao_covid.set_index("Região")
  media_internacao_covid = media_internacao_covid.sort_values("Total", axis = 0, ascending=False)
  media_internacao_covid = media_internacao_covid.drop("Total", axis = 1)
  media_internacao_covid = media_internacao_covid.drop("Total", axis = 0)
  media_internacao_covid.index = media_internacao_covid.index.str.slice(9)
  return media_internacao_covid

def plot_valor_medio_internacao():
  ax = valor_medio_internacao().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C8', 'C3'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,73), minor=True)
  ax.set_yticks(np.arange(750,2800, 50), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,72])
  ax.set_ylim([750,2750])
  ax.tick_params(labelsize=14)
  plt.ylabel("Valor médio da internação (R$)", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Custo médio da internação por mês por região do Brasil entre Agosto de 2015 e Agosto de 2021", fontsize = 16)
  plt.show()

def plot_valor_medio_internacao_covid():
  ax = valor_medio_internacao_covid().T.plot(figsize = (15,13), color = ['C0', 'C1', 'C2', 'C3', 'C8'])
  ax.legend(loc='upper left', bbox_to_anchor=(0,0.77), fontsize = 'x-large')
  ax.set_xticks(np.arange(0,17), minor=True)
  ax.set_yticks(np.arange(2000,9600, 100), minor=True)
  ax.grid(which='minor', alpha = 0.2)
  ax.grid()
  ax.set_xlim([0,16])
  ax.set_ylim([2000,9500])
  ax.tick_params(labelsize=14)
  plt.ylabel("Valor médio da internação (R$)", fontsize = 16)
  plt.xlabel("Ano/mês de processamento da internação", fontsize = 16)
  plt.title("Custo médio da internação por COVID-19 por mês por região do Brasil entre Abril de 2020 e Agosto de 2021", fontsize = 16)
  plt.show()

plot_internacoes()
plot_internacoes_covid()
plot_internacoes_mobilidade()
plot_porcentagem()
plot_porcentagem_populacao_covid()
plot_tempo_medio_internacao()
plot_tempo_medio_internacao_covid()
plot_valor_medio_internacao()
plot_valor_medio_internacao_covid()