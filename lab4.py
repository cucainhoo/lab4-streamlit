import streamlit as st
# Đọc file
st.title("Đọc file")
file = st.file_uploader("Tải lên tệp văn bản")
if file is not None:
    noi_dung = file.read().decode("utf-8")
    so_tu = len(noi_dung)
    st.write("Nội dung tệp:\n", noi_dung)
    st.write(f"Số lượng từ trong tệp \n: {so_tu} từ \n")
# Đếm từ
st.title("Đếm từ")
dem_tu = {}
for tu in noi_dung.split():
    dem_tu[tu] = dem_tu.get(tu, 0) + 1
st.write("Số lần xuất hiện:\n", dem_tu)
# Thay thế
st.title("Thay thế từ trong chuỗi")
tu_can_thay = st.text_input("Nhập từ cần thay thế:\n")
tu_moi = st.text_input("Nhập từ thay thế:\n")
if tu_can_thay and tu_moi:
    noi_dung_moi = noi_dung.replace(tu_can_thay, tu_moi)
    st.write("Nội dung sau khi thay thế:\n", noi_dung_moi)
