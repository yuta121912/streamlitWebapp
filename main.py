# import streamlit as st 
# st.title("My First Streamlit App")
# answer = st.radio("扉を置けますか？",["y","n"])
# if answer == "y":
    # st.write("扉を置くことができます。")
# else:
    # st.write("扉を置くことができません。")




import io

import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_drawable_canvas import st_canvas


drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider(
    "Stroke width:",
    1, 25, 3
)

if drawing_mode == "point":
    point_display_radius = st.sidebar.slider(
        "Point display radius:",
        1, 25, 3
    )

stroke_color = st.sidebar.color_picker(
    "Stroke color hex:",
    "#000000"
)

bg_color = st.sidebar.color_picker(
    "Background color hex:",
    "#eee"
)

bg_image = st.sidebar.file_uploader(
    "Background image:",
    type=["png", "jpg", "jpeg"]
)

realtime_update = st.sidebar.checkbox(
    "Update in realtime",
    True
)


# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=500,
    drawing_mode=drawing_mode,
    point_display_radius=(
        point_display_radius if drawing_mode == "point" else 0
    ),
    key="canvas",
)


# 画像がある場合
if canvas_result.image_data is not None:

    # Canvasの画像を表示
    st.image(canvas_result.image_data)

    # numpy配列 → PIL Image
    image = Image.fromarray(
        canvas_result.image_data.astype("uint8")
    )

    # PIL Image → PNG bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")

    # ダウンロード
    st.download_button(
        label="絵をダウンロード",
        data=img_bytes.getvalue(),
        file_name="my_downloaded_image.png",
        mime="image/png",
    )
