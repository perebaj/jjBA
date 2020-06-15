# jjBA
Análise jogos NBA, para implementação de uma maquina de regressão logística supervisionada


### Objetivos: 
* Modelo de aprendizado online
* Probabilidade de um time ganhar uma partida
* Quantidade de pontos que serão feitos
* Steamlit para montar um app


![image](https://user-images.githubusercontent.com/39134841/84663322-5f74d680-aef3-11ea-97ba-4e6c749bc795.png)

### Diagrama Projetim
![WhatsApp Image 2020-06-15 at 10 45 12](https://user-images.githubusercontent.com/39134841/84664825-76b4c380-aef5-11ea-9f5c-d6fcf1ea6b46.jpeg)

### Conhecimentos aplicados:
* Classificador binário: Dadas as informações de um time, reproduzir a probabilidade dele vencer ou perder uma partida;
* Análise estatística: Análise de correlação entra variáveis, com utilização de gráficos, para excluir parâmetros enviesados ou que nao refletem significado no aprendizado;
* Modelos treinados: Regressão linear, DecisionTree, SVM, RandomForest e SDGClassifier;
* Medições de Acurácia: Validação Cruzada, matriz de confusão, precisão e revocação, compesação, curva ROC, F1, análise do erro.

NBA_API: Api que recolhe as estatísticas no site da NBA
### Pastas: 

jjBA/src/API_NBA
  Utils.py: Funções úteis para o manejamento dos dados
  regular_season19.py: Extração dos dados dos jogos tanto da pré-temporada como a temporada de 2019/20
  
jj/BA/Colab Analises
  data_alanisys_NBA.ipynb: Análises e manipulação estatística das informações extraidas dos jogos para formulação do modelo supervisionado mais adequado.
  classifier_methods.ipynb: Treinamentos dos classificadores e análise das acurácias
