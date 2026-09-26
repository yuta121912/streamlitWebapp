# import streamlit as st 

# import io

# from PIL import Image

# import streamlit as st
# from streamlit_drawable_canvas import st_canvas

# # 画面のタイトル
# st.title("お絵かきアプリ")



# import streamlit as st
# from PIL import Image



# uploaded_file = st.file_uploader(
#     "画像をアップロード",
#     type=["png", "jpg", "jpeg"]
# )

# if uploaded_file:
#     image = Image.open(uploaded_file)

#     st.image(image)

# image = None

# if uploaded_file:
#     image = Image.open(uploaded_file).convert("RGBA")

# mode = st.radio("モード",["消しゴム", "筆"])



# stroke_color = st.color_picker("筆の色", "#000000")
# stroke_width = st.slider(
#     "筆の太さ",
#     min_value=1,
#     max_value=50,
#     value=5
# )

# if mode == "筆":
#     stroke_color = st.color_picker(
#         "筆の色",
#         "#000000"
#     )
# else:
#     stroke_color = "#ffffff"

# # 描く場所を表示
# canvas_result = st_canvas(
#     return_image_data=True,
#     fill_color="rgba(255, 0, 0, 0.3)",
#     stroke_color=stroke_color,
#     stroke_width=stroke_width,          
#     background_color="#ffffff",         # 背景色
#     width=700,                          # 横の大きさ
#     height=500,                         # 縦の大きさ
#     drawing_mode="freedraw",            # 自由に線を描く
#     key="canvas",

#     background_image=image,

# )


# # 描いた画像を保存したり表示したりできる

# if canvas_result.image_data is not None:
#     st.image(canvas_result.image_data, caption="あなたの絵")



# # NumPy配列 → PNG画像に変換
#     image = Image.fromarray(canvas_result.image_data.astype("uint8"))

#     # PNGとしてメモリに保存
#     buffer = io.BytesIO()
#     image.save(buffer, format="PNG")

#     # ダウンロード
#     st.download_button(
#         label="画像をダウンロード",
#         data=buffer.getvalue(),
#         file_name="お絵かき.png",
#         mime="image/png",
#     )





import streamlit as st
import io
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("お絵かきアプリ")




uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

image = None

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGBA")




mode = st.radio(
    "モード",
    ["筆", "消しゴム"]
)



if mode == "筆":

    stroke_color = st.color_picker(
        "筆の色",
        "#000000"
    )

else:

    stroke_color = "#ffffff"


stroke_width = st.slider(
    "筆の太さ・消しゴムの大きさ",
    min_value=1,
    max_value=50,
    value=5
)



canvas_result = st_canvas(
    return_image_data=True,

    fill_color="rgba(255, 0, 0, 0.3)",

    stroke_color=stroke_color,
    stroke_width=stroke_width,

    background_color="#ffffff",
    background_image=image,

    width=700,
    height=500,

    drawing_mode="freedraw",

    key="canvas",
)


if canvas_result.image_data is not None:

    st.image(
        canvas_result.image_data,
        caption="あなたの絵"
    )

    image = Image.fromarray(
        canvas_result.image_data.astype("uint8")
    )

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="PNG"
    )

    st.download_button(
        label="画像をダウンロード",
        data=buffer.getvalue(),
        file_name="お絵かき.png",
        mime="image/png",
    )


# import io

# import streamlit as st
# import pandas as pd
# from PIL import Image
# from streamlit_drawable_canvas import st_canvas


# drawing_mode = st.sidebar.selectbox(
#     "Drawing tool:",
#     ("point", "freedraw", "line", "rect", "circle", "transform")
# )

# stroke_width = st.sidebar.slider(
#     "Stroke width:",
#     1, 25, 3
# )

# if drawing_mode == "point":
#     point_display_radius = st.sidebar.slider(
#         "Point display radius:",
#         1, 25, 3
#     )

# stroke_color = st.sidebar.color_picker(
#     "Stroke color hex:",
#     "#000000"
# )

# bg_color = st.sidebar.color_picker(
#     "Background color hex:",
#     "#eee"
# )

# bg_image = st.sidebar.file_uploader(
#     "Background image:",
#     type=["png", "jpg", "jpeg"]
# )

# realtime_update = st.sidebar.checkbox(
#     "Update in realtime",
#     True
# )


# # Canvas
# canvas_result = st_canvas(
#     fill_color="rgba(255, 165, 0, 0.3)",
#     stroke_width=stroke_width,
#     stroke_color=stroke_color,
#     background_color=bg_color,
#     background_image=Image.open(bg_image) if bg_image else None,
#     update_streamlit=realtime_update,
#     height=500,
#     drawing_mode=drawing_mode,
#     point_display_radius=(
#         point_display_radius if drawing_mode == "point" else 0
#     ),
#     key="canvas",
# )


# # 画像がある場合
# if canvas_result.image_data is not None:

#     # Canvasの画像を表示
#     st.image(canvas_result.image_data)

#     # numpy配列 → PIL Image
#     image = Image.fromarray(
#         canvas_result.image_data.astype("uint8")
#     )

#     # PIL Image → PNG bytes
#     img_bytes = io.BytesIO()
#     image.save(img_bytes, format="PNG")

#     # ダウンロード
#     st.download_button(
#         label="絵をダウンロード",
#         data=img_bytes.getvalue(),
#         file_name="my_downloaded_image.png",
#         mime="image/png",
#     )
# st.title("My First Streamlit App")
# answer = st.radio("扉を置けますか？",["y","n"])
# if answer == "y":
    # st.write("扉を置くことができます。")
# else:
    # st.write("扉を置くことができません。")
