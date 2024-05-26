import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Function to generate text using GPT-3
def generate_text(prompt, temperature=0.7, max_tokens=200):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Title of the Streamlit app
st.title('Creative Text Generator with GPT-3')

# Sidebar for user input
st.sidebar.header('User Input')

# Multi-Level Prompting
# Step 1: Select the type of creative text
text_type = st.sidebar.selectbox('Select the type of creative text you want to generate:', 
                                 ('Story', 'Poem', 'Essay', 'Dialogue'))

# Step 2: General prompt from user
general_prompt = st.sidebar.text_area('Enter a general prompt or idea:', '')

# Step 3: Detailed prompts based on the type of text
detailed_prompt = ""
if text_type == 'Story':
    setting = st.sidebar.text_input('Setting:')
    character = st.sidebar.text_input('Main Character:')
    plot_point = st.sidebar.text_input('Plot Point:')
    detailed_prompt = f"Write a story set in {setting} with a main character named {character} who encounters {plot_point}. {general_prompt}"

elif text_type == 'Poem':
    theme = st.sidebar.text_input('Theme:')
    first_line = st.sidebar.text_input('First Line:')
    detailed_prompt = f"Write a poem with the theme {theme} and starting with the line: '{first_line}'. {general_prompt}"

elif text_type == 'Essay':
    topic = st.sidebar.text_input('Topic:')
    argument = st.sidebar.text_input('Main Argument:')
    detailed_prompt = f"Write an essay on the topic {topic} arguing that {argument}. {general_prompt}"

elif text_type == 'Dialogue':
    characters = st.sidebar.text_input('Characters:')
    situation = st.sidebar.text_input('Situation:')
    detailed_prompt = f"Write a dialogue between {characters} in the situation where {situation}. {general_prompt}"

# Generate text when button is pressed
if st.sidebar.button('Generate'):
    if detailed_prompt:
        generated_text = generate_text(detailed_prompt)
        st.subheader('Generated Text')
        st.write(generated_text)
    else:
        st.error('Please complete all fields.')
