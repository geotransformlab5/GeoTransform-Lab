import streamlit as st
import plotly.graph_objects as go
import math

st.set_page_config(page_title="GeoTransform Lab", page_icon="📐", layout="wide")

st.title("📐 GeoTransform Lab")
st.caption("Media Pembelajaran Geometri Transformasi Berbasis Web")

tab1, tab2, tab3 = st.tabs(["📚 Materi", "🧪 Laboratorium", "🎯 Tantangan"])

with tab1:
    st.header("Mengenal Transformasi Geometri")
    st.write("Transformasi geometri adalah perubahan posisi, arah, atau ukuran suatu bangun pada bidang koordinat.")
    st.subheader("Jenis-jenis transformasi")
    st.markdown("""
    - **Translasi:** menggeser bangun.
    - **Refleksi:** mencerminkan bangun terhadap garis tertentu.
    - **Rotasi:** memutar bangun terhadap titik pusat.
    - **Dilatasi:** memperbesar atau memperkecil bangun.
    """)
    st.info("Pada laboratorium, kamu dapat mengubah koordinat segitiga ABC dan melihat bayangannya.")

def transform_point(x, y, kind, p, q):
    if kind == "Translasi":
        return x + p, y + q
    if kind == "Refleksi terhadap sumbu X":
        return x, -y
    if kind == "Refleksi terhadap sumbu Y":
        return -x, y
    if kind == "Refleksi terhadap titik O":
        return -x, -y
    if kind == "Rotasi 90° berlawanan arah jarum jam":
        return -y, x
    if kind == "Rotasi 180°":
        return -x, -y
    if kind == "Rotasi 270° berlawanan arah jarum jam":
        return y, -x
    if kind == "Dilatasi berpusat di O":
        return p*x, p*y
    return x, y

with tab2:
    st.header("Laboratorium Transformasi")
    st.write("Ubah koordinat titik segitiga, pilih transformasi, lalu tekan tombol **Terapkan Transformasi**.")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Koordinat segitiga ABC")
        A = (st.number_input("Ax", value=1, key="ax"), st.number_input("Ay", value=1, key="ay"))
        B = (st.number_input("Bx", value=4, key="bx"), st.number_input("By", value=1, key="by"))
        C = (st.number_input("Cx", value=2, key="cx"), st.number_input("Cy", value=4, key="cy"))
    with c2:
        st.subheader("Pilih transformasi")
        kind = st.selectbox("Jenis transformasi", [
            "Translasi", "Refleksi terhadap sumbu X", "Refleksi terhadap sumbu Y",
            "Refleksi terhadap titik O", "Rotasi 90° berlawanan arah jarum jam",
            "Rotasi 180°", "Rotasi 270° berlawanan arah jarum jam", "Dilatasi berpusat di O"
        ])
        p, q = 2.0, 1.0
        if kind == "Translasi":
            p = st.number_input("Geser horizontal (a)", value=2.0)
            q = st.number_input("Geser vertikal (b)", value=1.0)
        elif kind == "Dilatasi berpusat di O":
            p = st.number_input("Faktor skala (k)", value=2.0)

    if st.button("Terapkan Transformasi", type="primary"):
        st.session_state["hasil"] = [transform_point(x, y, kind, p, q) for x, y in [A, B, C]]
        st.session_state["jenis"] = kind
    hasil = st.session_state.get("hasil", [A, B, C])
    nama_transformasi = st.session_state.get("jenis", "Belum diterapkan")
    fig = go.Figure()
    def add_triangle(points, name, color, fill):
        xs = [v[0] for v in points] + [points[0][0]]
        ys = [v[1] for v in points] + [points[0][1]]
        labels = ["A", "B", "C"]
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines+markers+text",
            text=labels + [""], textposition="top center", name=name,
            line=dict(width=3, color=color), fill="toself", fillcolor=fill))
    add_triangle([A, B, C], "Segitiga ABC", "#2563eb", "rgba(37,99,235,0.12)")
    add_triangle(hasil, "Bayangan A'B'C'", "#e11d48", "rgba(225,29,72,0.12)")
    fig.update_layout(title=f"Visualisasi: {nama_transformasi}", xaxis_title="Sumbu X",
                      yaxis_title="Sumbu Y", template="plotly_white", height=520,
                      legend=dict(orientation="h", y=1.08))
    fig.update_xaxes(showgrid=True, zeroline=True, dtick=1, range=[-12, 12])
    fig.update_yaxes(showgrid=True, zeroline=True, dtick=1, range=[-12, 12], scaleanchor="x", scaleratio=1)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Garis biru menunjukkan segitiga awal, sedangkan garis merah menunjukkan bayangannya.")

with tab3:
    st.header("Tantangan")
    questions = [
        ("Titik A(2, 3) ditranslasikan oleh (4, 1). Koordinat bayangannya adalah ...", ["(6, 4)", "(−2, 2)", "(3, 7)"], 0, "Tambahkan koordinat x dengan 4 dan y dengan 1."),
        ("Bayangan titik (3, 5) terhadap sumbu X adalah ...", ["(−3, 5)", "(3, −5)", "(−3, −5)"], 1, "Refleksi sumbu X mengubah tanda koordinat y."),
        ("Bayangan titik (−2, 4) terhadap sumbu Y adalah ...", ["(2, 4)", "(−2, −4)", "(2, −4)"], 0, "Refleksi sumbu Y mengubah tanda koordinat x."),
        ("Rotasi 180° terhadap titik pusat O mengubah (a, b) menjadi ...", ["(b, a)", "(−a, −b)", "(−b, a)"], 1, "Rotasi 180° mengubah tanda kedua koordinat."),
        ("Dilatasi berpusat O dengan faktor 3 pada titik (2, 1) menghasilkan ...", ["(5, 4)", "(6, 3)", "(2, 3)"], 1, "Kalikan setiap koordinat dengan faktor skala 3."),
        ("Transformasi yang mengubah ukuran bangun disebut ...", ["Translasi", "Refleksi", "Dilatasi"], 2, "Dilatasi memperbesar atau memperkecil bangun.")
    ]
    if "jawaban_quiz" not in st.session_state:
        st.session_state["jawaban_quiz"] = {}
    score = 0
    for i, (question, options, correct, explanation) in enumerate(questions):
        st.markdown(f"**{i+1}. {question}**")
        answer = st.radio("Pilih jawaban:", options, key=f"q{i}", index=None)
        if answer is not None:
            st.session_state["jawaban_quiz"][i] = options.index(answer)
        if i in st.session_state["jawaban_quiz"] and st.session_state["jawaban_quiz"][i] == correct:
            score += 1
    if st.button("Periksa Nilai"):
        st.success(f"Nilai kamu: {score} dari {len(questions)}")
        for i, (question, options, correct, explanation) in enumerate(questions):
            if i in st.session_state["jawaban_quiz"]:
                if st.session_state["jawaban_quiz"][i] == correct:
                    st.write(f"Nomor {i+1}: Benar! {explanation}")
                else:
                    st.write(f"Nomor {i+1}: Belum tepat. Jawaban benar: {options[correct]}. {explanation}")
