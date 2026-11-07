import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="GeoTransform Lab",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    background:#172554;
    color:white;
    padding:22px 28px;
    border-radius:12px;
    margin-bottom:18px
}
.main-title h1 {
    color:white;
    margin:0
}
.main-title p {
    color:#dbeafe;
    margin:5px 0 0
}
.lesson {
    background:#eff6ff;
    padding:18px 20px;
    border-radius:12px;
    margin:12px 0;
    border-left:5px solid #2563eb
}
.question {
    background:#eff6ff;
    padding:24px;
    border-radius:14px;
    margin:16px 0;
    text-align:center
}
.question h2 {
    color:#1e3a8a
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
<h1>📐 GEOTRANSFORM LAB</h1>
<p>Laboratorium Transformasi Geometri Interaktif | Kelompok 5</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "📚 Materi",
    "🧪 Laboratorium",
    "🎯 Tantangan"
])

# ==================================
# BAGIAN 1: MATERI
# ==================================

with tab1:

    st.header("Mengenal Transformasi Geometri")

    st.write(
        "Transformasi geometri adalah perubahan posisi, arah, "
        "atau ukuran suatu titik maupun bangun pada bidang koordinat. "
        "Bangun yang mengalami transformasi akan memiliki bayangan "
        "dengan aturan tertentu."
    )

    st.subheader("1. Refleksi (Pencerminan)")

    st.markdown("""
    <div class="lesson">
    Refleksi adalah perubahan posisi titik atau bangun dengan cara
    mencerminkannya terhadap garis atau titik tertentu. Bentuk dan
    ukuran bangun tetap sama, tetapi posisinya berubah seperti
    bayangan pada cermin.
    </div>
    """, unsafe_allow_html=True)

    st.write("Aturan pencerminan:")

    st.latex(r"(x,y) \rightarrow (x,-y)")
    st.caption("Terhadap sumbu X")

    st.latex(r"(x,y) \rightarrow (-x,y)")
    st.caption("Terhadap sumbu Y")

    st.latex(r"(x,y) \rightarrow (-x,-y)")
    st.caption("Terhadap titik O")

    st.info(
        "Contoh: titik A(2, 3) dicerminkan terhadap sumbu X "
        "menjadi A′(2, −3), karena tanda koordinat y berubah."
    )

    st.subheader("2. Translasi (Pergeseran)")

    st.markdown("""
    <div class="lesson">
    Translasi adalah perpindahan titik atau bangun dari satu posisi
    ke posisi lain dengan jarak dan arah tertentu. Translasi tidak
    mengubah bentuk maupun ukuran bangun.
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "Jika suatu titik digeser sejauh a satuan secara horizontal "
        "dan b satuan secara vertikal, maka:"
    )

    st.latex(r"(x,y) \rightarrow (x+a,y+b)")

    st.info(
        "Contoh: titik A(2, 3) ditranslasikan oleh (4, 1) "
        "menjadi A′(6, 4)."
    )

    st.subheader("3. Rotasi (Perputaran)")

    st.markdown("""
    <div class="lesson">
    Rotasi adalah perubahan posisi titik atau bangun dengan cara
    memutarnya terhadap suatu pusat rotasi dengan besar sudut
    tertentu. Jika pusat rotasinya O(0,0), aturan rotasi yang
    sering digunakan adalah:
    </div>
    """, unsafe_allow_html=True)

    st.latex(
        r"90^\circ: (x,y) \rightarrow (-y,x)"
    )
    st.caption("90° berlawanan arah jarum jam")

    st.latex(
        r"180^\circ: (x,y) \rightarrow (-x,-y)"
    )

    st.latex(
        r"270^\circ: (x,y) \rightarrow (y,-x)"
    )
    st.caption("270° berlawanan arah jarum jam")

    st.info(
        "Contoh: titik A(2, 3) dirotasi 90° berlawanan arah "
        "jarum jam menjadi A′(−3, 2)."
    )

    st.subheader("4. Dilatasi (Perbesaran dan Pengecilan)")

    st.markdown("""
    <div class="lesson">
    Dilatasi adalah perubahan ukuran suatu bangun, baik menjadi
    lebih besar maupun lebih kecil, berdasarkan faktor skala tertentu.
    Bentuk bangun tetap sebangun dengan bangun asal.
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "Jika pusat dilatasi berada di O(0,0) dan faktor skalanya k, maka:"
    )

    st.latex(r"(x,y) \rightarrow (kx,ky)")

    st.write("- Jika k > 1, bangun diperbesar.")
    st.write("- Jika 0 < k < 1, bangun diperkecil.")
    st.write("- Jika k = 1, ukuran bangun tetap.")

    st.info(
        "Contoh: titik A(2, 3) didilatasikan dengan faktor skala 2 "
        "menjadi A′(4, 6)."
    )

    st.success(
        "Ingat: translasi menggeser, refleksi mencerminkan, "
        "rotasi memutar, dan dilatasi mengubah ukuran."
    )


# ==================================
# FUNGSI TRANSFORMASI
# ==================================

def transform_point(x, y, kind, a, b, scale):

    if kind == "Translasi":
        return x + a, y + b

    if kind == "Refleksi terhadap sumbu X":
        return x, -y

    if kind == "Refleksi terhadap sumbu Y":
        return -x, y

    if kind == "Refleksi terhadap titik O":
        return -x, -y

    if kind == "Rotasi 90°":
        return -y, x

    if kind == "Rotasi 180°":
        return -x, -y

    if kind == "Rotasi 270°":
        return y, -x

    if kind == "Dilatasi":
        return scale*x, scale*y

    return x, y


# ==================================
# BAGIAN 2: LABORATORIUM
# ==================================

with tab2:

    st.header("Laboratorium Transformasi Geometri")

    st.write(
        "Ubah koordinat segitiga ABC dan amati bagaimana bayangannya "
        "setelah mengalami transformasi."
    )

    left, right = st.columns(2)

    with left:

        st.subheader("Koordinat Segitiga ABC")

        A = (
            st.number_input("Titik A - x", value=2, key="ax"),
            st.number_input("Titik A - y", value=2, key="ay")
        )

        B = (
            st.number_input("Titik B - x", value=5, key="bx"),
            st.number_input("Titik B - y", value=2, key="by")
        )

        C = (
            st.number_input("Titik C - x", value=3, key="cx"),
            st.number_input("Titik C - y", value=5, key="cy")
        )

    with right:

        st.subheader("Pilih Transformasi")

        kind = st.selectbox(
            "Jenis transformasi",
            [
                "Translasi",
                "Refleksi terhadap sumbu X",
                "Refleksi terhadap sumbu Y",
                "Refleksi terhadap titik O",
                "Rotasi 90°",
                "Rotasi 180°",
                "Rotasi 270°",
                "Dilatasi"
            ]
        )

        a, b, scale = 0, 0, 2.0

        if kind == "Translasi":

            a = st.number_input(
                "Pergeseran horizontal (a)",
                value=2
            )

            b = st.number_input(
                "Pergeseran vertikal (b)",
                value=1
            )

        if kind == "Dilatasi":

            scale = st.number_input(
                "Faktor skala (k)",
                min_value=0.1,
                value=2.0,
                step=0.5
            )

    original = [A, B, C, A]

    image_pts = [
        transform_point(x, y, kind, a, b, scale)
        for x, y in [A, B, C]
    ]

    transformed = image_pts + [image_pts[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[p[0] for p in original],
        y=[p[1] for p in original],
        mode="lines+markers+text",
        text=["A", "B", "C", ""],
        textposition="top center",
        name="Segitiga ABC",
        line=dict(width=3),
        marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=[p[0] for p in transformed],
        y=[p[1] for p in transformed],
        mode="lines+markers+text",
        text=["A′", "B′", "C′", ""],
        textposition="bottom center",
        name="Bayangan A′B′C′",
        line=dict(width=3, dash="dash"),
        marker=dict(size=10)
    ))

    fig.update_layout(
        title="Perbandingan Segitiga Sebelum dan Sesudah Transformasi",
        xaxis_title="Sumbu X",
        yaxis_title="Sumbu Y",
        xaxis=dict(
            zeroline=True,
            showgrid=True,
            dtick=1
        ),
        yaxis=dict(
            zeroline=True,
            showgrid=True,
            dtick=1,
            scaleanchor="x",
            scaleratio=1
        ),
        height=600,
        legend=dict(
            orientation="h",
            y=1.08
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Koordinat Bayangan")

    st.write(
        f"A′ = ({image_pts[0][0]:g}, {image_pts[0][1]:g})"
    )

    st.write(
        f"B′ = ({image_pts[1][0]:g}, {image_pts[1][1]:g})"
    )

    st.write(
        f"C′ = ({image_pts[2][0]:g}, {image_pts[2][1]:g})"
    )


# ==================================
# DATA 10 SOAL TANTANGAN
# ==================================

questions = [

    {
        "q": "Titik A(2, 3) dicerminkan terhadap sumbu X. Berapa koordinat bayangannya?",
        "answer": "2,-3",
        "display": "(2, −3)",
        "explain": "Pencerminan terhadap sumbu X menggunakan aturan (x, y) → (x, −y). Jadi A(2, 3) menjadi A′(2, −3)."
    },

    {
        "q": "Titik B(−2, 4) dicerminkan terhadap sumbu Y. Berapa koordinat bayangannya?",
        "answer": "2,4",
        "display": "(2, 4)",
        "explain": "Pencerminan terhadap sumbu Y menggunakan aturan (x, y) → (−x, y). Jadi B(−2, 4) menjadi B′(2, 4)."
    },

    {
        "q": "Titik C(3, 5) ditranslasikan oleh (2, −1). Berapa koordinat bayangannya?",
        "answer": "5,4",
        "display": "(5, 4)",
        "explain": "Tambahkan 2 pada x dan −1 pada y: (3+2, 5−1) = (5, 4)."
    },

    {
        "q": "Titik D(1, 2) ditranslasikan oleh (−3, 4). Berapa koordinat bayangannya?",
        "answer": "-2,6",
        "display": "(−2, 6)",
        "explain": "(1−3, 2+4) = (−2, 6)."
    },

    {
        "q": "Titik E(2, 3) dirotasi 90° berlawanan arah jarum jam terhadap O(0,0). Berapa bayangannya?",
        "answer": "-3,2",
        "display": "(−3, 2)",
        "explain": "Rotasi 90° berlawanan arah jarum jam menggunakan aturan (x, y) → (−y, x)."
    },

    {
        "q": "Titik F(−4, 2) dirotasi 180° terhadap O(0,0). Berapa bayangannya?",
        "answer": "4,-2",
        "display": "(4, −2)",
        "explain": "Rotasi 180° menggunakan aturan (x, y) → (−x, −y)."
    },

    {
        "q": "Titik G(2, 5) dirotasi 270° berlawanan arah jarum jam terhadap O(0,0). Berapa bayangannya?",
        "answer": "5,-2",
        "display": "(5, −2)",
        "explain": "Rotasi 270° berlawanan arah jarum jam menggunakan aturan (x, y) → (y, −x)."
    },

    {
        "q": "Titik H(3, 2) didilatasikan dengan faktor skala 2 dan pusat O(0,0). Berapa bayangannya?",
        "answer": "6,4",
        "display": "(6, 4)",
        "explain": "Kalikan kedua koordinat dengan 2: (2×3, 2×2) = (6, 4)."
    },

    {
        "q": "Titik I(−2, 3) dicerminkan terhadap titik pusat O(0,0). Berapa bayangannya?",
        "answer": "2,-3",
        "display": "(2, −3)",
        "explain": "Pencerminan terhadap titik O menggunakan aturan (x, y) → (−x, −y)."
    },

    {
        "q": "Titik J(4, −1) didilatasikan dengan faktor skala 3 dan pusat O(0,0). Berapa bayangannya?",
        "answer": "12,-3",
        "display": "(12, −3)",
        "explain": "Kalikan kedua koordinat dengan 3: (3×4, 3×−1) = (12, −3)."
    }

]


# ==================================
# BAGIAN 3: TANTANGAN
# ==================================

with tab3:

    st.header("Tantangan GeoTransform")

    st.write(
        "Kerjakan 10 soal berikut satu per satu. "
        "Masukkan jawaban dalam bentuk x,y. Contoh: 2,-3."
    )

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    if "q_checked" not in st.session_state:
        st.session_state.q_checked = {}

    if "q_answers" not in st.session_state:
        st.session_state.q_answers = {}

    idx = st.session_state.q_index

    st.progress(
        (idx + 1) / len(questions),
        text=f"Soal {idx + 1} dari {len(questions)}"
    )

    current = questions[idx]

    st.markdown(f"""
    <div class="question">
        <h2>Tantangan GeoTransform</h2>
        <h3>Soal {idx + 1} dari 10</h3>
        <p style="font-size:20px">{current['q']}</p>
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input(
        "Masukkan jawaban (contoh: 2,-3)",
        key=f"answer_{idx}",
        placeholder="Ketik koordinat bayangan"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        check = st.button(
            "Periksa Jawaban",
            type="primary",
            use_container_width=True
        )

    with col2:
        show = st.button(
            "Lihat Kunci & Pembahasan",
            use_container_width=True
        )

    with col3:
        next_q = st.button(
            "Soal Berikutnya ➜",
            use_container_width=True,
            disabled=(idx == len(questions)-1)
        )

    if check:

        cleaned = (
            answer.replace(" ", "")
            .replace("(", "")
            .replace(")", "")
            .replace("，", ",")
        )

        st.session_state.q_answers[idx] = cleaned
        st.session_state.q_checked[idx] = True

        if cleaned == current["answer"]:
            st.success("Benar! Hebat, jawabanmu tepat.")
        else:
            st.error(
                "Jawaban belum tepat. Coba periksa kembali, "
                "atau buka kunci dan pembahasannya."
            )

    if show:

        st.info(
            f"Kunci jawaban: **{current['display']}**"
        )

        st.write(current["explain"])

    if idx in st.session_state.q_checked:

        if st.session_state.q_answers.get(idx) == current["answer"]:
            st.success("Jawabanmu benar.")
        else:
            st.caption(
                "Kamu masih bisa mencoba lagi sebelum lanjut."
            )

    if next_q:

        st.session_state.q_index += 1
        st.rerun()

    if idx == len(questions)-1:

        st.success(
            "Kamu sudah sampai di soal terakhir. "
            "Terima kasih sudah mencoba Tantangan GeoTransform!"
        )

        if st.button("Ulangi dari Soal 1"):

            st.session_state.q_index = 0
            st.rerun()
