import streamlit as st

from pyngrok import ngrok
from joblib import load

trained_model = load('model_sentiment.pkl')

form = st.form(key='my-form')

kalimat = form.text_input('Masukkan Kalimat:')

submit = form.form_submit_button('Cari tau sentimennya!')

if submit:
  y_pred = trained_model.predict([kalimat])
  st.write('Kalimat tadi bersentimen: ', y_pred[0])

# ngrok_tunnel = ngrok.connect(8501)
# print('Public URL:', ngrok_tunnel.public_url)