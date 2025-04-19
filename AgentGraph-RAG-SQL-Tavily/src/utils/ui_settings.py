import gradio as gr

# Feedback machenism for app using Gradio
class UISettings:
    @staticmethod
    def feedback(data:gr.LikeData):
        if data.liked:
            print('You upvoted the response: '+data.value)
        else:
            print('You downvoted the response: '+data.value)