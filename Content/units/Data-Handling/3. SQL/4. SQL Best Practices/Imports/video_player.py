from IPython import display
from base64 import b64encode

def play_video(video_name):
    mp4 = open(f"/content/{video_name}",'rb').read()
    mp4 = f"data:video/mp4;base64,{b64encode(mp4).decode()}"
    return display.HTML(f"""<video height=50% width=50% controls autoplay
        src={mp4} >
    </video>""")