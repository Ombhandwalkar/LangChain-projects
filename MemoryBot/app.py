import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_SUMMARIZATION_PROMPT,ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI

st.set_page_config(page_title='🧠MemoryBot🤖',layout='wide')

# Store the AI response
if 'generated' not in st.session_state:
    st.session_state['generated']=[]
# Store the user Input
if 'past' not in st.session_state:
    st.session_state['past']=[]
# Current user message in input box
if 'input' not in st.session_state:
    st.session_state['input']=''
# Stores entire past conversations 
if 'stored_session' not in st.session_state:
    st.session_state['stored_session']=[]


# Define function to get user input 
def  get_text():
    input_text=st.text_input('You:',st.session_state['input'],key='input',placeholder='Your AI assistant is here ! Ask me Anything',label_visibility='hidden')
    return input_text

# Define the new function to start new Chat
def new_chat():
    save=[]
    # This will store the conversation of User and Bot
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        save.append('User:' + st.session_state['past'][i])
        save.append('Bot:'  + st.session_state['generated'][i])
    # This will store the entire histroy of convearsation. Make available to download
    st.session_state['stored_session'].append(save)
    # This will clear the stored history.
    st.session_state['generated']=[]
    st.session_state['input']=''
    st.session_state['past']=[]
    # This will clear the entity memory buffer and store.
    st.session_state.entity_memory.entity_store={}
    st.session_state.entity_memory.buffer.clear()

# Set Side Bar with various options
with st.sidebar.expander('Settings 🔧',expanded=False):
    # Option to preview memory store
    
    if st.checkbox('Preview memory store'):
        if 'entity_memory' in st.session_state:
        #with st.expander('Memory-Store',expanded=False):
             st.write(st.session_state.entity_memory.store)
        else:
            st.warning('Memory not initialized yet')
    # Show chat history held in memory 
    if st.checkbox('Preview memory buffer'):
        if 'entity_memory' in st.session_state:
        #with st.expander('Buffer-store',expanded=False):
            st.write(st.session_state.entity_memory.buffer)
        else:
            st.warning('Memory not initialized yet')
    # User select the language model
    Model=st.selectbox(label='Model',options=['gemini-1.5-flash','gemini-1.5-pro'])
    # Sets how many past messages the memory considers.
    K=st.number_input('(#) Summary of prompt to consider ',min_value=3,max_value=1000)


st.title('🤖 Chat Bot with 🧠')
st.subheader(" Powered by 🦜 LangChain + Gemini + Streamlit")

# Ask user to enter API key
API_O=st.sidebar.text_input("🔑 Enter you API Key",type='password')
button=st.sidebar.button('Enter')

if button:
    if API_O:
        try:
            # Create instance
            llm=ChatGoogleGenerativeAI(temperature=0,model=Model,google_api_key=API_O,verbose=False)
            st.success('Model Loaded Sucessfully ')

            # Create conversationEntityMemory
            # This will remembers important entities like - name, dates, places.
            if 'entity_memory' not in st.session_state:
                st.session_state.entity_memory=ConversationEntityMemory(llm=llm,k=K)
                
            # Create conversation object- It ties everything together.
            st.session_state.Conversation=ConversationChain(
                llm=llm,
                prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
                memory=st.session_state.entity_memory
            )
        except Exception as e:
            st.error(f'Failed to load model: {e}')
    else:
        st.sidebar.warning('Please enter valid API key')


# If the user want to create new chat
st.sidebar.button('New Chat',on_click=new_chat,type='primary')
user_input=get_text()

# Generate the new output using ConversationChain
if st.button('Generate'):
    if not user_input:
        st.warning("Please enter a message first!")
    elif 'Conversation' not in st.session_state:
        st.error("Model not initialized. Please enter your API key and press Enter.")
    else:
        try:
            output = st.session_state.Conversation.run(input=user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(output)
        except Exception as e:
            st.error(f"Something went wrong during generation: {e}")


download_str=[]

# Display conversation History using expander
with st.expander('Conversation',expanded=True):
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        st.info(st.session_state['past'][i],icon='🧐')
        st.success(st.session_state['generated'][i],icon='🤖')
        download_str.append(st.session_state['past'][i])
        download_str.append(st.session_state['generated'][i])

    # Download the Chat
    download_str='\n'.join(download_str)
    if download_str:
        st.download_button('Download',download_str)
    
# Display the stored conversation.
for i, sublist in enumerate(st.session_state.stored_session):
    with st.sidebar.expander(label=f'Conversaion sessioin: {i}'):
        st.write(sublist)


# Allow the user to clear all conversation.
if st.session_state.stored_session:
    if st.sidebar.checkbox('🗑️ Clear-all'):
        del st.session_state.stored_session
