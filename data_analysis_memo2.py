import pandas as pd
import pandas_profiling
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------データ分析で使う関数のメモ2-----------------------------------------------------------#
#pandasやnumpyなどの使い方を例とともに説明する

#**************************探索的データ分析********************************#
#pandas.DataFrame.profile_report()-----------------
#pandas.DataFrameの概要を表示
train = pd.read_csv('../input/titanic/train.csv')
train.profile_report()

#matplotlib.pyplot.hist()----------------------------------------------------------------------------------------------------------------------
#input1: pandas.DataFrame(の一部)を指定
#input2: bins(ビン(表示する棒)の数)を指定
#input3: alpha(透過度) デフォルトだと1.0で透過しない
#input4: label(凡例で表示される表示名)
#pandas.DataFrame.loc(): 行ラベルと列ラベルを指定することで、pandas.DataFrameの一部を取得。
#ここでは、行ラベルはSurvivedが0,列ラベルはAgeを選択し、死亡者の年齢を取得している。欠損値が含まれているためpandas.Series.dropna()で欠損値を削除
plt.hist(train.loc[train['Survived'] == 0, 'Age'].dropna(), bins=30, alpha=0.5, label='0')
plt.hist(train.loc[train['Survived'] == 1, 'Age'].dropna(), bins=30, alpha=0.5, label='1')
plt.xlabel('Age')             #x軸ラベルを指定
plt.ylabel('count')           #y軸ラベルを指定
plt.legend(title='Survived')  #matplotlib.pyplot.legend()：それまでにlabel引数で指定した名前が凡例に表示される。title引数で凡例のタイトルを指定
plt.show()                    #表示
