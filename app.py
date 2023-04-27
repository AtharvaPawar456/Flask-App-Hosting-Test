@@ -1,11 +1,13 @@
from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)

@app.route('/')
def index():
    username = 'John'  # Replace with your desired username
    return render_template('index.html', username=username)

    return render_template('index.html')
@app.route('/streamlit')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
if __name__ == '__main__':
    app.run(debug=True)
    app.run()