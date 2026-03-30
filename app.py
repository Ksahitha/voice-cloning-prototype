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

        gr.Audio(
            type="filepath",
            label="Upload voice sample"
        ),

        gr.Textbox(
            label="Text to synthesize"
        )

    ],

    outputs=gr.Audio(
        label="Generated speech"
    ),

    title="AI Voice Cloning Prototype",

    description="""
Upload a voice sample and enter text.
The system clones the speaker voice and generates new speech.
"""
)

interface.launch(share=True)
