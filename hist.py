import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
data=pd.read_csv("D:/ram/athlete_events.csv")
print(data)
plt.hist(data['Age'])
plt.title('histogram plot')
plt.show()
