import gradio as gr
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio
import pandas as pd
from datasets import load_dataset

# load dataset
dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
df = dataset.to_pandas()

with gr.Blocks() as demo:
    gr.Label("Visual Explore NYC-Airbnb data in PyGWalker and Gradio")
    gr.Markdown("This is a data app build with [pygwalker](https://docs.kanaries.net/pygwalker) and [gradio](https://www.gradio.app/) library. You can use drag-and-drop operations to explore the data, start your analysis now!")
    pyg_app = get_html_on_gradio(df, spec="./viz-config.json", debug=False)
    gr.HTML(pyg_app)
    
app = demo.launch(app_kwargs={
    "routes": [PYGWALKER_ROUTE]
})