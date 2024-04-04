import streamlit as st
import time

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Placeholder function simulating ChatGPT interaction (replace with actual logic)
def generate_response(user_input):
    # Simulate interaction with ChatGPT or another large language model
    # (replace with API calls or other methods)
    chatgpt_response = f"Processing your request using a simulated ChatGPT interaction... (Replace with actual ChatGPT response)"
    return chatgpt_response

# Set page title and favicon
st.set_page_config(page_title="Chatbot with Login", page_icon=":robot:")

# Function to add message to chat history
def add_to_chat_history(sender, message):
    st.session_state.chat_history.append((sender, message))

# Function to generate bot response
def generate_bot_response(user_input):
    bot_response = generate_response(user_input)
    add_to_chat_history("Bot", bot_response)
    return bot_response

# Function to dynamically update bot response as if it's being typed out
def update_bot_response(response):
    bot_output = st.empty()
    full_response = "Bot: " + response
    for char_index in range(len(full_response)):
        bot_output.text(full_response[:char_index+1])
        time.sleep(0.05)  # Adjust the sleep time for typing speed

# Main chat interface
st.title("Chatbot Interface")

# Add custom CSS styles
custom_css = """
<style>
.gradient-text {
  background-image: linear-gradient(to right, #73a0ff, #3d5af1);
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  text-fill-color: transparent;
}

      .stButton {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1000px;
  overflow: hidden;
  height: 3rem;
  background-size: 300% 300%;
  backdrop-filter: blur(1rem);
  border-radius: 5rem;
  transition: 0.5s;
  animation: gradient_301 5s ease infinite;
  border: double 4px transparent;
  background-image: linear-gradient(#212121, #212121),  linear-gradient(137.48deg, #ffdb3b 10%,#FE53BB 45%, #8F51EA 67%, #0044ff 87%);
  background-origin: border-box;
  
  background-clip: content-box, border-box;
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

#container-stars {
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  overflow: hidden;
  transition: 0.5s;
  backdrop-filter: blur(1rem);
  border-radius: 5rem;
}
.stButton>button{
width:inherit;
}
strong {
  z-index: 2;
  font-family: 'Avalors Personal Use';
  font-size: 12px;
  letter-spacing: 5px;
  color: #FFFFFF;
  text-shadow: 0 0 4px white;
}

#glow {
  position: absolute;
  display: flex;
  width: 12rem;
}

.circle {
  width: 100%;
  height: 30px;
  filter: blur(2rem);
  animation: pulse_3011 4s infinite;
  z-index: -1;
}

.circle:nth-of-type(1) {
  background: rgba(254, 83, 186, 0.636);
}

.circle:nth-of-type(2) {
  background: rgba(142, 81, 234, 0.704);
}

.stButton:hover #container-stars {
  z-index: 1;
  background-color: #212121;
}

.stButton:hover {
  transform: scale(1.1)
}

.stButton:active {
  border: double 4px #FE53BB;
  background-origin: border-box;
  background-clip: content-box, border-box;
  animation: none;
}

.stButton:active .circle {
  background: #FE53BB;
}

#stars {
  position: relative;
  background: transparent;
  width: 200rem;
  height: 200rem;
}

#stars::after {
  content: "";
  position: absolute;
  top: -10rem;
  left: -100rem;
  width: 100%;
  height: 100%;
  animation: animStarRotate 90s linear infinite;
}

#stars::after {
  background-image: radial-gradient(#ffffff 1px, transparent 1%);
  background-size: 50px 50px;
}

#stars::before {
  content: "";
  position: absolute;
  top: 0;
  left: -50%;
  width: 170%;
  height: 500%;
  animation: animStar 60s linear infinite;
}

#stars::before {
  background-image: radial-gradient(#ffffff 1px, transparent 1%);
  background-size: 50px 50px;
  opacity: 0.5;
}

@keyframes animStar {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-135rem);
  }
}

@keyframes animStarRotate {
  from {
    transform: rotate(360deg);
  }

  to {
    transform: rotate(0);
  }
}

@keyframes gradient_301 {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

@keyframes pulse_3011 {
  0% {
    transform: scale(0.75);
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.7);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(0, 0, 0, 0);
  }

  100% {
    transform: scale(0.75);
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0);
  }
}  
<button class="btn" type="button">
  <strong>SPACE</strong>
  <div id="container-stars">
    <div id="stars"></div>
  </div>

  <div id="glow">
    <div class="circle"></div>
    <div class="circle"></div>
  </div>
</button>


.stTextArea:hover,
.stTextInput:hover,
.stSelectbox:hover {
  transform: translateY(-2px);
  transition: transform 0.2s ease-in-out;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

if not st.session_state["logged_in"]:
    # Image
    image = "C:\\Users\\iamab\\OneDrive\\Desktop\\intel (2)\\intel\\Intel.png"
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
                # Clear login form after successful login
                st.empty()
            else:
                st.error("Invalid username or password")

if st.session_state["logged_in"]:
    # Chat interface elements
    with st.form(key='chat_form'):
        user_input = st.text_input("You:", "", help="Type your message here...", key="user_input")
        submit_button = st.form_submit_button(label='Send')

        if user_input.strip() != "" and submit_button:
            user_response = user_input
            add_to_chat_history("You", user_response)
            bot_response = generate_bot_response(user_input)
            update_bot_response(bot_response)

    # Display chat history in the sidebar
    st.sidebar.title("Chat History")

    # Add logo to the history box
    logo_image = "C:\\Users\\iamab\OneDrive\\Desktop\\intel (2)\\intel\\oneapi.jpg"
    st.sidebar.image(logo_image, caption='Logo', use_column_width=True)

    for index, (sender, message) in enumerate(st.session_state.chat_history, start=1):
        st.sidebar.text_area(f"{sender} ({index}):", message, height=len(message) // 2 + 1, max_chars=len(message), key=f"chat_history_{index}")

# Gradient text effect for title
st.markdown("<h1 class='gradient-text'>Chatbot Interface</h1>", unsafe_allow_html=True)
