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
class FillValuesProfile(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y):
        return self
    
    def transform(self, X,y):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        target = y.copy()
        print(target)
        # Varre cada perfil e preenche os valores faltantes com base na média daquele perfil
        for perfil in list(target['PERFIL'].unique()):
          mean_value = data.loc[target['PERFIL']==perfil][self.columns[0]].mean()
          data.loc[target['PERFIL']==perfil,self.columns[0]] =  data.loc[target['PERFIL']==perfil,self.columns[0]].fillna(value=mean_value)
        # Retornamos um novo dataframe com os valores preenchidos
        return data

# Define a class to limit values ranges of a column
class LimitValues(BaseEstimator, TransformerMixin):
    def __init__(self, columns, max_value, min_value):
        self.columns = columns
        self.max_value = max_value
        self.min_value = min_value

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Varre cada perfil e ajusta os valores para dentro dos limites máximo e mínimo
        for column in self.columns:
          data.loc[data[column]>self.max_value,column] = self.max_value
          data.loc[data[column]<self.min_value,column] = self.min_value
        # Retornamos um novo dataframe com os valores preenchidos
        return data