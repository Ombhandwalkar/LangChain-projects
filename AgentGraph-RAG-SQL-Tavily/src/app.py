import gradio as gr
from chatbot.chatbot_backend import ChatBot
from utils.ui_settings import UISettings


with gr.Blocks()as demo:
    with gr.Tabs():
        with gr.TabItem('AgentGraph'):
            with gr.Row() as row_one:
                chatbot=gr.Chatbot(
                    value=[], # Need to work
                    elem_id='chatbog',
                    height=500,
                    avatar_images=('Images/human.png','Images/robo.jpg'))
                chatbot.like(UISettings.feedback,None,None)
                
            with gr.Row():
                input_txt=gr.Textbox(
                    lines=3,
                    scale=8,
                    placeholder='Enter the text and press enter',
                    container= False)

            with gr.Row() as row_two:
                text_submit_btn=gr.Button(value='Submit text')
                clear_button=gr.ClearButton([input_txt,chatbot])


            txt_msg=input_txt.submit(fn=ChatBot.respond,inputs=[chatbot,input_txt],outputs=[input_txt,chatbot],queue=False).then(lambda: gr.Textbox(interactive=True),None,[input_txt],queue=False)
            txt_msg=text_submit_btn.click(fn=ChatBot.respond,inputs=[chatbot,input_txt],outputs=[input_txt,chatbot],queue=False).then(lambda: gr.Textbox(interactive=True),None,[input_txt],queue=False)

if __name__=='__main__':
    demo.launch()