import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menambahkan judul dan informasi proyek
st.title('Proyek Analisis Data: E-commerce Public Dataset')
st.write('Nama: Indra Mauludani Efendi')
st.write('Email: IndraMauludani09@gmail.com')
st.write('ID Dicoding: indramauludani14')

st.markdown("""
## Pertanyaan Bisnis:
1. Apakah terdapat hubungan antara harga produk (price) dan biaya pengiriman (freight_value)?
2. Bagaimana distribusi metode pembayaran yang digunakan oleh pelanggan, dan apakah metode pembayaran tertentu cenderung digunakan untuk transaksi dengan nilai yang lebih tinggi?
""")

# Memuat dataset
order_items_clean = pd.read_csv('order_items_dataset.csv')  # Sesuaikan jalur dataset
order_payments_clean = pd.read_csv('order_payments_dataset.csv')  # Sesuaikan jalur dataset

# Sidebar untuk memilih analisis
st.sidebar.header('Pilih Analisis')
show_correlation = st.sidebar.checkbox('Korelasi antara Harga dan Biaya Pengiriman')
show_payment_distribution = st.sidebar.checkbox('Distribusi Metode Pembayaran')

# Korelasi antara harga produk dan biaya pengiriman
if show_correlation:
    st.subheader('Korelasi antara Harga Produk dan Biaya Pengiriman')
    
    # Menghitung korelasi
    correlation = order_items_clean[['price', 'freight_value']].corr()
    st.write('Matriks Korelasi:')
    st.dataframe(correlation)

    # Visualisasi korelasi dengan scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='price', y='freight_value', data=order_items_clean, color='#2ecc71')
    plt.title("Hubungan antara Harga Produk dan Biaya Pengiriman")
    plt.xlabel("Harga Produk")
    plt.ylabel("Biaya Pengiriman")
    st.pyplot(plt)

    # Insight
    st.markdown(f"**Insight:** Korelasi antara harga produk dan biaya pengiriman adalah {correlation.loc['price', 'freight_value']:.2f}. Korelasi positif yang kuat menunjukkan bahwa produk dengan harga lebih tinggi seringkali memiliki biaya pengiriman yang lebih tinggi.")

# Distribusi metode pembayaran
if show_payment_distribution:
    st.subheader('Distribusi Metode Pembayaran')

    # Frekuensi metode pembayaran
    payment_method_freq = order_payments_clean['payment_type'].value_counts()
    st.write('Frekuensi Metode Pembayaran:')
    st.dataframe(payment_method_freq)

    # Bar plot untuk distribusi metode pembayaran
    plt.figure(figsize=(10, 6))
    sns.barplot(x=payment_method_freq.index, y=payment_method_freq.values, color='#2ecc71')
    plt.title("Distribusi Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

    # Box plot untuk nilai pembayaran per metode pembayaran
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='payment_type', y='payment_value', data=order_payments_clean, showfliers=False, color='#2ecc71')
    sns.stripplot(x='payment_type', y='payment_value', data=order_payments_clean, jitter=True, color='#2ecc71', alpha=0.6)
    plt.title("Distribusi Nilai Pembayaran per Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Nilai Pembayaran")
    st.pyplot(plt)

    # Insight
    st.markdown("**Insight:** Kartu kredit adalah metode pembayaran yang paling sering digunakan, terutama untuk transaksi bernilai tinggi. Hal ini dapat menjadi pertimbangan untuk strategi promosi.")

# Menampilkan statistik deskriptif dari dataset
if st.sidebar.checkbox('Tampilkan Statistik Deskriptif'):
    st.subheader('Statistik Deskriptif')
    
    st.write('Statistik Deskriptif untuk Order Items:')
    st.dataframe(order_items_clean.describe())
    
    st.write('Statistik Deskriptif untuk Order Payments:')
    st.dataframe(order_payments_clean.describe())

# Menampilkan kesimpulan
st.subheader("Kesimpulan")
st.markdown("""
1. **Harga Produk vs Biaya Pengiriman:** Terdapat korelasi positif yang kuat antara harga produk dan biaya pengiriman. Hal ini menunjukkan bahwa produk dengan harga lebih tinggi cenderung memiliki biaya pengiriman yang lebih tinggi.
2. **Preferensi Metode Pembayaran:** Kartu kredit adalah metode pembayaran yang paling sering digunakan, terutama untuk transaksi bernilai tinggi. Strategi promosi dapat menargetkan pelanggan yang menggunakan metode ini.
""")
