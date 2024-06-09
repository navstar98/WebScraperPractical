import pandas as pd
# contains one is either URL or filename or other contains entire table string
df_list=pd.read_html('https://en.wikipedia.org/wiki/List_of_top_book_lists')
# print(df_list)
print(len(df_list))   #contains 3 dataframes
print(df_list[1])