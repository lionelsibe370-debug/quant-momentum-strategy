import matplotlib.pyplot as plt
import pandas as pd
data = {'nom':['alice','bob','charlie'],'age':[20,10,30],'ville':['paris','lyon','marseille']}
df=pd.DataFrame(data)
print(df[df['age']>10])
#plt.figure(figsize=(10, 4))
#plt.show()