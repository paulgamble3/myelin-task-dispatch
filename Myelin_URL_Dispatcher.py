import streamlit as st
from firebase.firebase_utils import write_task_item
from task_url_sampler import sample_task_url, TASK_CONFIGS


FIREBASE_DB = "2_7_menu_mentoring"

active_task_names = list(TASK_CONFIGS.keys())

st.title('Myelin Task Dispatcher')

with st.form("task-form"):

    selected_task = st.selectbox("Please select your task:", active_task_names, key="task_name")

    submitted = st.form_submit_button("Generate URL")

    if submitted:
        st.write("You selected:", selected_task)
        # here's where I generate and display the URL
        call_url = sample_task_url(selected_task)
        st.subheader("[CALL URL]({})".format(call_url))

with st.form("call-id-input"):
    def log_call():
        feedback_obj = {
            "call_id": st.session_state.call_id,
            "username": st.session_state.username,
            "task_name": st.session_state.task_name,
        }
        write_task_item(feedback_obj, FIREBASE_DB)
        #reset call_id
        st.session_state.call_id = ""
        #st.experimental_rerun()
    
    # call_url, call_type = sample_call_url()

    st.text_input("Enter your name:", key='username')
    # st.subheader("[CALL URL]({})".format(call_url))
    #st.write("Call type: " + call_type.strip())
    #st.write("After a few openings lines and introductions, please ask a hospital policy question from the provided list.")
    call_id = st.text_input("Please copy and paste the call ID:", key="call_id")
    
    submit_button = st.form_submit_button(label='Log call', on_click=log_call)
        