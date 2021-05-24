import pandas as pd
import pandas_profiling

#---------------------------------------------データ分析で使う関数のメモ2-----------------------------------------------------------#
#pandasやnumpyなどの使い方を例とともに説明する

#**************************探索的データ分析********************************#
#pandas.DataFrame.profile_report()
#pandas.DataFrameの概要を表示
train = pd.read_csv('../input/titanic/train.csv')
train.profile_report()