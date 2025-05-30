import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

translator = Translator()
st.title('Uso de textblob')

st.subheader("Vergil va a juzgar el poder y la motivación de lo que le digas. Puedes decirle cualquier cosa, si te atreves.")
with st.sidebar:
               st.subheader("Motivación y Poder")
               ("""
                Motivación: Indica si el sentimiento expresado en el texto representa mucha motivación, le falta motivación o es neutral. 
                Su valor oscila entre -1 (muy poco motivado) y 1 (muy motivado), con 0 representando un nivel neutral de motivación.
                
               Poder: Mide el nivel de poder de tu sentimiento expresado (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo (muy poco poder) y 1 es completamente subjetivo (demasiado poder).

                 """
               ) 

image = Image.open('Vergil.png')
st.image(image, width=350)

with st.expander('Analizar Motivación y Poder en un texto'):
    text1 = st.text_area('Háblame si te atreves: ')
    if text1:

        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        #blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
