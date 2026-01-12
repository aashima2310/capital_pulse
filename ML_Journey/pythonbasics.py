from io import StringIO
import pandas as pd
import numpy as np
data = ("col1,col2,col3\n"
 "1,2,3\n"
"a,b,c\n"
"11,12,13\n")
df = pd.read_csv(StringIO(data))
print(df)