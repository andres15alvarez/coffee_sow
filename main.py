import gradio as gr
from model import model


demo = gr.Interface(
    model.predict,
    inputs=["number", "number", "number", "number", "number"],
    outputs=["text"],
    examples=[[23.0, 0.76, 1200, 150.8, 5.8]],
    title="Coffee Sow Predictor",
    description=(
        "In this project a dataset was created from a brief research on coffee plantations,"
        "it is not intended to be an excellent dataset, it is only for educational purposes"
        "about neural networks."
    )
)
demo.launch()
