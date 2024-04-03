import streamlit as st
import time

# Placeholder function simulating ChatGPT interaction (replace with actual logic)
def generate_response(user_input):
    # Simulate interaction with ChatGPT or another large language model
    # (replace with API calls or other methods)
    chatgpt_response = f"Processing your request using a simulated ChatGPT interaction... (Replace with actual ChatGPT response)"
    return chatgpt_response

# Set page title and favicon
st.set_page_config(page_title="Chatbot with Login", page_icon=":robot:")

# Login state (replace with your authentication logic)
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Initialize an empty list to store chat history
chat_history = []

# Function to add message to chat history
def add_to_chat_history(sender, message):
    chat_history.append((sender, message))

# Function to generate bot response
def generate_bot_response(user_input):
    bot_response = generate_response(user_input)
    add_to_chat_history("Bot", bot_response)
    return bot_response

# Function to dynamically update bot response as if it's being typed out
# Function to dynamically update bot response as if it's being typed out
def update_bot_response(response):
    bot_output = st.empty()
    full_response = "Bot: " + response
    for char_index in range(len(full_response)):
        bot_output.text(full_response[:char_index+1])
        time.sleep(0.05)  # Adjust the sleep time for typing speed


# Main chat interface
st.title("Chatbot Interface")

if not st.session_state["logged_in"]:
    # Image
    image = 'https://www.intel.com/content/dam/www/public/us/en/images/product/hero/desktop-processors-core-i7-hero.png'
    st.image(image, caption='Intel Processor', use_column_width=True)

    # Login form in the top corner
    with st.sidebar:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            # Replace with your actual authentication logic
            if username == "123" and password == "369":
                st.session_state["logged_in"] = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")

if st.session_state["logged_in"]:
    # Chat interface elements
    with st.form(key='chat_form'):
        user_input = st.text_input("Input:", "", help="Type your message here...", key="user_input")
        submit_button = st.form_submit_button(label='Send')

        if user_input.strip() != "" and submit_button:
            user_response = user_input
            add_to_chat_history("You", user_response)
            bot_response = generate_bot_response(user_input)
            update_bot_response(bot_response)

    # Display chat history in the right corner
    st.sidebar.title("Chat History")
    for sender, message in chat_history:
        st.sidebar.text_area(f"{sender}:", message, height=len(message) // 2 + 1, max_chars=len(message))

# Gradient text effect for title
st.markdown("<h1 class='gradient-text'>Chatbot Interface</h1>", unsafe_allow_html=True
.gradient-text {
  background-image: linear-gradient(to right, #f3ec78, #af4261); /* Adjust colors and direction */
  color: transparent;  /* Make text color transparent */
  -webkit-background-clip: text;  /* Clip background to text (WebKit browsers) */
  background-clip: text;         /* Clip background to text (modern browsers) */
  text-fill-color: transparent;  /* Make text inherit gradient color (WebKit browsers) */
}

<style>
    .stButton {
        position: relative;  /* Needed for pseudo-element positioning */
    }

    .stButton>button:hover {
        font-weight:bold;
        border:none;
        color: #000000;
        background: linear-gradient(to right, #009688 , #77a69a ,#9F00FF );  /* Base button color */
    }

    .stButton>button:after {
        content: "";
        position: absolute;
        insert: 0;  /* Inset property for shorthand positioning */
        border:none;
        border-radius: inherit;
        background: linear-gradient(to right, #009688 0%, #77a69a 0%,#9F00FF 90%);
        opacity: 0;  /* Initially hidden */
        transition: opacity 0.2s ease-in-out;
    }

    .stButton>button:active,
    .stButton>button:focus {
        outline: none; /* Remove default button outline */
    }

    .stButton>button:hover:after {
        color:#000000;
        opacity: 1; /* Show gradient border on hover */
    }
    .stTextArea:hover,
    .stTextInput:hover,
    .stSelectbox:hover {
        transform: translateY(-2px);
        transition: transform 0.2s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)
