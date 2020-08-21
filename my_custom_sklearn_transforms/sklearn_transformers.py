from sklearn.base import BaseEstimator, TransformerMixin


# Define a class to drop columns of a pandas dataframe
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# Define a class to fill NaN values based on student profile
class fillValuesProfile(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Varre cada perfil e preenche os valores faltantes com base na média daquele perfil
        for perfil in list(data['PERFIL'].unique()):
          mean_value = data.loc[data['PERFIL']==perfil][self.columns[0]].mean()
          data.loc[data['PERFIL']==perfil,self.columns[0]] =  data.loc[data['PERFIL']==perfil,self.columns[0]].fillna(value=mean_value)
          print(data.loc[data['PERFIL']==perfil,self.columns[0]])
        # Retornamos um novo dataframe com os valores preenchidos
        return data

# Define a class to limit values ranges of a column
class limitValues(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X,max_value,min_value):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Varre cada perfil e ajusta os valores para dentro dos limites máximo e mínimo
        for column in self.columns:
          data.loc[data[column]>max_value,column] = max_value
          data.loc[data[column]<min_value,column] = min_value
        # Retornamos um novo dataframe com os valores preenchidos
        return data