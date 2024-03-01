import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
from datetime import datetime


st.header(
    """
    The most selling product
    """
)

all_df = pd.read_csv('all_data.csv')
product_count = all_df.groupby('product_category_name_english').product_id.count().reset_index()
sorted_product = product_count.sort_values(by='product_id', ascending=False)


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="product_id", y="product_category_name_english", data=sorted_product.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("products with the highest sales", loc="center", fontsize=18)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="product_id", y="product_category_name_english", data=sorted_product.sort_values(by="product_id", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("products with the lowest sales", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)
st.pyplot(fig) 


st.header(
    """
    Successful Delivery status
    """
)
delivery_status = all_df['order_status'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=delivery_status.index, 
    y=delivery_status.values, 
    order=delivery_status.index,
    palette=colors
)


plt.title("Successful Delivery", fontsize=15)
plt.xlabel("Delivery status")
plt.ylabel("Count")
plt.xticks(fontsize=12)
plt.show()
st.pyplot(plt)

st.header(
    """
    Location with the most customers
    """
)


customer = pd.read_csv('datasets/customers_dataset.csv')
geolocation = pd.read_csv('datasets/geolocation_dataset.csv')

customers_location = customer.merge(geolocation,left_on='customer_zip_code_prefix',right_on='geolocation_zip_code_prefix',how='inner')
brazil = mpimg.imread('brazil-map.jpeg')
ax = customers_location.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat", figsize=(10,10), alpha=0.3,s=0.3,c='green')
plt.axis('off')
plt.imshow(brazil, extent=[-73.98283055, -33.8,-33.75116944,5.4])
plt.title('Location with the most customer')
plt.show()
st.pyplot(plt)