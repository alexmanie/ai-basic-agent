import gradio as gr

from utils.call_api import CallApi

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("Agente"):
            with gr.Row() as row_one:
                chatbot = gr.Chatbot(
                    [],
                    elem_id="chatbot",
                    bubble_full_width=False,
                    height=500
                )

            with gr.Row() as row_two:
                input_txt = gr.Textbox(
                    placeholder="Enter text and press enter",
                    container=False,
                    interactive=True,
                )

            with gr.Row() as row_three:
                text_submit_btn = gr.Button(value="Submit text")
                clear_button = gr.ClearButton([input_txt, chatbot])

            ##############
            # Process:
            ##############

            input_txt.submit(fn=CallApi.respond, inputs=[chatbot, input_txt], outputs=[input_txt, chatbot], queue=False)
            text_submit_btn.click(fn=CallApi.respond, inputs=[chatbot, input_txt], outputs=[input_txt, chatbot], queue=False)

if __name__ == "__main__":
    demo.launch()
