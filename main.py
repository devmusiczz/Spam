import streamlit as st
import joblib as jb
def main(model,cv):
    st.title('Spam Filter'.upper())
    st.markdown("<h1 style = 'text-align : center; font-size: 25px; color: blue ;'></h1>",unsafe_allow_html=True)
    result =''

    text_message = st.text_input('Enter your text message')
    if st.button('Predict'):
        text = cv.transform([text_message])
        prediction = model.predict(text)
        if prediction[0] == 1:
            result = 'Spam'
        else:
            result = 'Not Spam'

        st.success('Prediction : {}'.format(result))
        # st.write(st.__version__) # give current version of pkg that is being used
        # st.write(jb.__version__)



model_load = jb.load('F:\ML\Learning\Spam_model.pkl')
cv = jb.load('F:\ML\Learning\C_vector.pkl')
main(model_load,cv)
