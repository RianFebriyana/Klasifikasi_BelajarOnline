import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('student.sav', 'rb'))

st.title('Klasifikasi Adaptasi Siswa Dalam Belajar Online')
c1, c2 = st.columns(2)

with c1:
   Education_Level = st.number_input('Jenjang Pendidikan')
   IT_Student = st.number_input('Belajar Sebagai Pelajar IT (0= Tidak, 1= Ya)')
   Load_shedding = st.number_input('Tingkat Jam Pelajaran (1= Tinggi, 2= Rendah)')
   Internet_Type = st.number_input('Jenis Internet Yang Digunakan (0= Data Seluler, 1= Wifi)')
   Class_Duration = st.number_input('Durasi Kelas Dalam Sehari')
   Device = st.number_input('Perangkat Yang Digunakan')

with c2:
   Institution_Type = st.number_input('Tipe Institusi (0= Negeri, 1= Swasta)')
   Location = st.number_input('Lokasi Sekolah Di Kota (0= Tidak, 1= Ya)')
   Financial_Condition = st.number_input('Kondisi Finansial (0= Menegah, 1= Di Bawah, 2= Kaya)')
   Network_Type = st.number_input('Koneksi Jaringan Yang Digunakan (0= 2G, 1= 3G, 2= 4G)')
   Self_Lms = st.number_input('Memiliki LMS Sendiri (1= Tidak, 2= Ya)')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Education_Level, Institution_Type, IT_Student, Location, Load_shedding,
                                Financial_Condition, Internet_Type, Network_Type, Class_Duration, Self_Lms, Device]])

    if (prediksi [0] == 0):
        prediksi = ('Pelajar Sangat Bisa Beradaptasi Dalam Belajar Online')
    elif (prediksi == 1):
        prediksi = ('Pelajar Tidak Bisa Beradaptasi Dalam Belajar Online')
    else:
        prediksi = ('Pelajar Bisa Beradaptasi Dalam Belajar Online')
st.success(prediksi)