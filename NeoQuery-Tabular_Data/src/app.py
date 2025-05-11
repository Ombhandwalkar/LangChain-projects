import gradio as gr
from utils.chatbot import ChatBot
from utils.ur_settings import UISettings


with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("KnowledgeGraph-Q&A-and-RAG-with-TabularData"):
       

            with gr.Row() as row_one:
                chatbot = gr.Chatbot(
                    [],
                    elem_id="chatbot",
                    bubble_full_width=False,
                    height=500,
                    avatar_images=(
                        ("images/human.png"), "images/robo.jpg")
                )
     
                chatbot.like(UISettings.feedback, None, None)

            with gr.Row():
                input_txt = gr.Textbox(
                    lines=4,
                    scale=8,
                    placeholder="Enter text and press enter",
                    container=False,
                )


            with gr.Row() as row_two:
                text_submit_btn = gr.Button(value="Submit text")
                chatbot_functionality = gr.Dropdown(
                    label="Functioncality", choices=[
                        "Q&A with GraphDB (Improved Agent)",
                        "Q&A with GraphDB (Simple Agent)",
                        "RAG with GraphDB"
                        ], value="Q&A with GraphDB (Improved Agent)")
                clear_button = gr.ClearButton([input_txt, chatbot])
     

            txt_msg = input_txt.submit(fn=ChatBot.respond,
                                       inputs=[chatbot, input_txt,
                                               chatbot_functionality],
                                       outputs=[input_txt,
                                                chatbot],
                                       queue=False).then(lambda: gr.Textbox(interactive=True),
                                                         None, [input_txt], queue=False)

            txt_msg = text_submit_btn.click(fn=ChatBot.respond,
                                            inputs=[chatbot, input_txt,
                                                    chatbot_functionality],
                                            outputs=[input_txt,
                                                     chatbot],
                                            queue=False).then(lambda: gr.Textbox(interactive=True),
                                                              None, [input_txt], queue=False)


if __name__ == "__main__":
    demo.launch()
