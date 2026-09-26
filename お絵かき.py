import io
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import streamlit as st

st.title("お絵かきアプリ")

uploaded_file = st.file_uploader(
    "画像をアップロード", type=["png", "jpg", "jpeg"]
)

image = None

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGBA")

mode = st.radio("モード", ["筆", "消しゴム"])

if mode == "筆":
    stroke_color = st.color_picker("筆の色", "#000000")
else:
    stroke_color = "#ffffff"

stroke_width = st.slider(
    "筆の太さ・消しゴムの大きさ", min_value=1, max_value=50, value=5
)

file_name = st.text_input("画像の名前", value="お絵かき")

# 描画履歴をセッションステートに保持する場所
if "saved_drawing" not in st.session_state:
    st.session_state["saved_drawing"] = None

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
    initial_drawing=st.session_state["saved_drawing"],  # 過去の絵を復元
    key="canvas",
)

if canvas_result.image_data is not None:
    # キャンバスの描画データをPillow画像に変換
    canvas_image = Image.fromarray(canvas_result.image_data.astype("uint8")).convert("RGBA")

    # 背景画像があるかどうかで処理を分岐
    if image is not None:
        # アップロードされた背景画像をキャンバスサイズ（700x500）に合わせる
        resized_bg = image.resize((700, 500))
        
        # 背景画像の上に手書きの線を重ね合わせる（合成）
        final_image = Image.alpha_composite(resized_bg, canvas_image)
    else:
        # 背景がない場合は、白い背景を下敷きにして手書きの線を重ねる
        base_bg = Image.new("RGBA", (700, 500), (255, 255, 255, 255))
        final_image = Image.alpha_composite(base_bg, canvas_image)

    # 3. 合成された1枚の画像をプレビュー表示
    st.image(final_image, caption="合成された画像")

    # 4. 合成した画像をダウンロード用に保存
    buffer = io.BytesIO()
    final_image.convert("RGB").save(buffer, format="JPEG") # ここでJPEGとして保存

    st.download_button(
        label="画像をダウンロード",
        data=buffer.getvalue(),
        file_name=file_name + ".jpg",
        mime="image/jpeg",
    )