import streamlit as st

st.set_page_config(page_title="حاسبة المعدل التراكمي (CGPA)", layout="centered")
st.title("📚 حاسبة المعدل التراكمي (CGPA)")
st.markdown("أدخل عدد الساعات و GPA لكل مادة وسيتم حساب المعدل التراكمي.")

num_courses = st.number_input("عدد المواد", min_value=1, max_value=100, step=1, value=3)
total_points = 0.0
total_hours = 0.0

st.markdown("---")
st.subheader("🔢 بيانات المواد:")

for i in range(int(num_courses)):
    col1, col2 = st.columns(2)
    with col1:
        hours = st.number_input(f"عدد الساعات للمادة {i+1}", min_value=0.0, key=f"h{i}")
    with col2:
        gpa = st.number_input(f"GPA للمادة {i+1}", min_value=0.0, max_value=4.0, step=0.01, key=f"g{i}")
    total_points += hours * gpa
    total_hours += hours

st.markdown("---")
if total_hours > 0:
    cgpa = total_points / total_hours
    st.success(f"✅ المعدل التراكمي (CGPA): **{cgpa:.2f}** من 4")
else:
    st.warning("⚠️ يرجى إدخال بيانات صحيحة لحساب المعدل.")

st.markdown("🎓 أنشئ بواسطة Python و Streamlit")
