import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")
st.title("階段 2.5：DataFrame 數據單點座標拆解實驗")
st.caption("授權標註：edit by 闕河正")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Tasks", ttl="0")

st.write("### 目前的雲端原始表格：")
st.dataframe(df)

st.write("---")
st.write("### 精準座標抽離實驗：")

# 使用 .loc[行號, 欄位名] 精準抓取特定格子
first_title = df.loc[0, "title"]
first_owner = df.loc[1, "owner"]import streamlit as st 

from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide") 

st.title(" 階段三：外星文濾網分流與空間歸隊測試") 

st.caption("授權標註：edit by 闕河正")

conn = st.connection("gsheets", type=GSheetsConnection) 

df = conn.read(worksheet="Tasks", ttl="0")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1: 

    st.markdown("###  To Do") 

    #  內層做濾網，外層做篩選：只抓出狀態為 To Do 的小表格 

    todo_df = df[df["status"] == "To Do"] # 把它印在左邊這欄 

    st.dataframe(todo_df)

with col2: 

    st.markdown("###  In Progress") 

    #  只抓出狀態為 In Progress 的小表格 

    ip_df = df[df["status"] == "In Progress"] 

    st.dataframe(ip_df)

with col3: 

    st.markdown("###  Done") 

    #  只抓出狀態為 Done 的小表格 

    done_df = df[df["status"] == "Done"] 

    st.dataframe(done_df)

st.write(f"機器人回報：我們發現第 0 列（第一行任務）的名稱是：**{first_title}**")
st.write(f"機器人回報：這一行的負責人是：**{first_owner}**")
