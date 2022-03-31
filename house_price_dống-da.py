#%%
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import seaborn as sns
#%%
df = pd.read_excel('house_price_dống-da.xlsx')
df.info()
#%%
df = df.dropna()
df = df.sort_values(
     by="price",
     ascending=False
     )

# %%
#Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng ngủ với giá nhà, giữa số toilet với giá nhà.
plt.scatter(df['price'],df['area'])
plt.xlabel('diện tích')
plt.ylabel('giá nhà')
plt.show()

# %%
plt.scatter(df['price'],df['bedroom'])
plt.xlabel('giá nhà')
plt.ylabel('số phòng ngủ')
plt.show()

# %%
plt.scatter(df['price'],df['toilet'])
plt.xlabel('giá nhà')
plt.ylabel('số toilet')
plt.show()

# %%
#Vẽ biểu đồ so sánh giá nhà trung bình trên 1/m2 giữa các hình thức nhà (type_of_land).
df['type_of_land'].unique
#%%
plt.bar(df['type_of_land'],df['price'])
plt.xlabel('hình thức nhà')
plt.ylabel('giá nhà')
plt.show()
# %%
#Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ.
plt.plot(df['price'],df['bedroom'])
plt.xlabel('giá nhà')
plt.ylabel('số phòng ngủ')
plt.show()

# %%
