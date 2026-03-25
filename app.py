import gradio as gr
from TTS.api import TTS

tts=TTS("tts_models/multilingual/multi-dataset/your_tts")

def clone(audio,text):

    output="output.wav"

    tts.tts_to_file(

        text=text,
        speaker_wav=audio,
        language="en",
        file_path=output

    )

    return output


interface=gr.Interface(

    fn=clone,

    inputs=[

        gr.Audio(type="filepath"),
        gr.Textbox(label="Enter text")

    ],

    outputs=gr.Audio()

)

interface.launch(share=True)
