import pandas as pd
import streamlit as st
#from pathlib import Path
import plotly.express as px


st.set_page_config(page_title="Data Visualization App", layout="wide")


#def read_text(path: str) -> str:
    #return Path(path).read_text(encoding="utf-8")

#st.title("StreamlitでHTMLを動かしてみる")

# ファイル読み込み
#app_dir = Path(__file__).parent
#html = read_text(app_dir / "templates/index.html")
#css = read_text(app_dir / "assets/style.css")
#js = read_text(app_dir / "assets/script.js")

# HTMLにCSSとJSを挿入
#html = html.replace("</head>", f"<style>{css}</style></head>")
#html = html.replace("</body>", f"<script>{js}</script></body>")

# 埋め込み表示
#st.components.v1.html(html, height=300)

st.markdown("""

<style>
.page-title {
    font-size: 36px;
    color: #FFFFFF;
}    
</style>

<h1 class="page-title">売上ダッシュボード</h1>

""", unsafe_allow_html=True)


file = st.file_uploader("JSONファイルをアップロードしてください", type=["json"])


if file is None:
    st.stop()

try:
    df = pd.read_json(file)

    
    df["date"] = pd.to_datetime(df["date"])

    df['price'] = pd.to_numeric(df['price'])

    df['quantity'] = pd.to_numeric(df['quantity'])

except (ValueError, KeyError ,TypeError) as e:
    st.error(f"データの読み込み中にエラーが発生しました: {e}")
    st.stop()

##    

before_data = len(df)
st.info(f"データの読み込みが完了しました。行数: {before_data}")

if df.empty:
    st.warning("データが空です。")
    st.stop()

df["total"] = df["price"] * df["quantity"]

st.subheader("売上データの概要")
st.dataframe(df)

st.subheader("商品の売り上げの割合")

product_sales = df.groupby("product", as_index=False)["total"].sum()

fig = px.pie(
  product_sales,  
  names="product",
  values="total"
)

st.plotly_chart(fig)

st.subheader("日付と商品の売り上げ（円）")

pivot = df.pivot_table(
    index = "date",
    columns = "product",
    values= "total",
    aggfunc = "sum",
    fill_value = 0
)

st.dataframe(pivot)

