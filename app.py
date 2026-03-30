import gradio as gr
from TTS.api import TTS
import time
import os

tts=TTS("tts_models/multilingual/multi-dataset/your_tts")

def clone(audio,text):

    if audio is None:
        return None,"Please upload a voice sample",None

    if text == "":
        return None,"Please enter text",None

    output="output.wav"

    start=time.time()

    tts.tts_to_file(

        text=text,
        speaker_wav=audio,
        language="en",
        file_path=output

    )

    end=time.time()

    runtime=round(end-start,2)

    status=f"Speech generated successfully in {runtime} seconds"

    return output,status,output


def example_text():

    return "This is a demonstration of an AI voice cloning application. The system learns voice characteristics and generates new speech."


with gr.Blocks() as app:

    gr.Markdown("# AI Voice Cloning Application")

    gr.Markdown(
    """
    Upload a voice sample and enter text.
    The AI will generate speech using the same voice.

    """
    )

    with gr.Tabs():

        with gr.Tab("Voice Generator"):

            with gr.Row():

                audio=gr.Audio(

                    type="filepath",

                    label="Upload Voice Sample"

                )

                text=gr.Textbox(

                    label="Text to generate",

                    placeholder="Enter text here",

                    lines=5

                )

            with gr.Row():

                example=gr.Button("Use Example Text")

                generate=gr.Button(
                    "Generate Voice",
                    variant="primary"
                )

            output_audio=gr.Audio(

                label="Generated Voice"

            )

            download=gr.File(

                label="Download Generated Audio"

            )

            status=gr.Textbox(

                label="System Status"

            )

            example.click(

                example_text,

                outputs=text

            )

            generate.click(

                clone,

                inputs=[audio,text],

                outputs=[output_audio,status,download]

            )

app.launch(share=True)