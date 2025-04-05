import streamlit as st
from api_utils import upload_document, list_documents, delete_document

# Sidebar Model Selection
def display_sidebar():
    model_option=['Google_gen_AI','Gpt-4o']
    st.sidebar.selectbox('Select Model',options=model_option,key='model')

    # Sidebar: Upload Document
    st.sidebar.header('Upload Document')
    uploaded_file=st.sidebar.file_uploader('Choose a File',type=['pdf','docx','html'])
    if uploaded_file is not None:
        if st.sidebar.button('Upload'):
            with st.spinner('Uploading...'):
                upload_response=upload_document(uploaded_file)
                if upload_response:
                    st.sidebar.success(f"File '{uploaded_file.name}' uploaded sucessfully with ID {upload_document['file_id']}.")
                    st.session_state.documents=list_documents()



    # Sidebar: List Document
    st.sidebar.subheader("Uploaded Documents")
    if st.sidebar.button('Refresh Document List'):
        with st.spinner('Refreshing...'):
            st.session_state.documents=list_documents()
    
    # Initialize document list  if not present
    if 'documents' not in st.session_state:
        st.session_state.documents=list_documents()

    documents=st.session_state.documents
    if documents:
        for doc in documents:
            st.sidebar.text(f"{doc['filename']} (ID:{doc['id']}, Uploaded:{doc['uploaded_timestamp']})")
        
        # Delete Documents
        selected_file_id=st.sidebar.selectbox("Select Document to delete",options=[doc['id'] for doc in documents ],format_func=lambda x: next(doc['filename']for doc in documents if doc['id']==x))
        if st.sidebar.button('Delete Selected document'):
            with st.spinner('Deleting...'):
                delete_response=delete_document(selected_file_id)
                if delete_response:
                    st.sidebar.success(f"Document with ID {selected_file_id}deleted sucessfully")
                    st.session_state.documents=list_documents()
                else:
                    st.sidebar.error(f"Failed to delete document with ID {selected_file_id}.") 
