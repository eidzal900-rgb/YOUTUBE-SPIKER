from moviepy.editor import TextClip, CompositeVideoClip

def build_video(title):

    txt = TextClip(
        title,
        fontsize=70,
        color="white",
        size=(1080,1920)
    ).set_duration(5)

    video = CompositeVideoClip([txt])

    video.write_videofile(
        f"output/{title}.mp4",
        fps=30
    )
