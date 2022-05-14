# StreamLit-Practice
In this repo I show an app made by following stramlit get started doc. There explain how to develop this app using Uber dataset for pickups in New York

## ¿What is StreamLit?
Streamlit is an app framework built for ML engineers. Streamlit lets you turn data scripts into sharable web apps in minutes. It’s all Python, open-source, and free! And once you’ve created an app you can use thei cloud platform to deploy, manage, and share your app! With each prototype, the core principles of Streamlit became simpler and purer. They are:

- *1: Embrace Python scripting*. Streamlit apps are really just scripts that run from top to bottom. There’s no hidden state. You can factor your code with function calls. If you know how to write Python scripts, you can write Streamlit apps. For example, this is how you write to the screen:

```
import streamlit as stst.write('Hello, world!')
```
- *2: Treat widgets as variables.* There are no callbacks in Streamlit! Every interaction simply reruns the script from top to bottom. This approach leads to really clean code:

```
import streamlit as stx = st.slider('x')
st.write(x, 'squared is', x * x)
```

- *3: Reuse data and computation*. What if you download lots of data or perform complex computation? The key is to safely reuse information across runs. Streamlit introduces a cache primitive that behaves like a persistent, immutable-by-default, data store that lets Streamlit apps safely and effortlessly reuse information.

In short, Streamlit works like this:
   1. The entire script is run from scratch for each user interaction.
   2. Streamlit assigns each variable an up-to-date value given widget states.
   3. Caching allows Streamlit to skip redundant data fetches and computation.
  
## Installation
```
pip install streamlit
streamlit hello
```

## To work with this project

Just download or use this command in your propmt, to obtain this respositorie 
```
git clone https://github.com/JoseMRodriguezM/StreamLit-Practice.git
```
Once you've got the respository downloaded o colned, the next step is to run streamlit. Use:
Just download or use this command in your propmt, to obtain this respositorie 
```
streamli run
```
This will automatically pop open a web browser pointing to your local Streamlit app. If not, just click the locacl url.




