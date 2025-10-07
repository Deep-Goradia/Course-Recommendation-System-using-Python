import streamlit as st
from data_loader import load_courses, load_materials
from content_knn import ContentKNN

# Load data
courses = load_courses()
materials = load_materials()

# Initialize models
course_knn = ContentKNN(courses, "description")
material_knn = ContentKNN(materials, "description")

# Streamlit UI
st.sidebar.title("Select Recommendation Type:")
choice = st.sidebar.radio(
    "Options:",
    [
        "Course Recommendations (Content-Based)",
        "Material Recommendations (Content-Based)"
    ]
)

st.title("🎓 AI/ML Recommendation System")

# ----- Content-Based: Courses -----
if choice == "Course Recommendations (Content-Based)":
    st.subheader("Recommend Similar Courses")
    course_names = courses["title"].tolist()
    selected_course = st.selectbox("Pick a course:", course_names)

    if st.button("Recommend Courses"):
        idx = courses[courses["title"] == selected_course].index[0]
        recs = course_knn.recommend_by_index(idx, k=5)
        st.write("### Recommended Courses:")
        for _, row in enumerate(recs):
            st.write(f"- {row['title']}")

# ----- Content-Based: Materials -----
elif choice == "Material Recommendations (Content-Based)":
    st.subheader("Recommend Similar Study Materials")
    material_names = materials["title"].tolist()
    selected_material = st.selectbox("Pick a material:", material_names)

    if st.button("Recommend Materials"):
        idx = materials[materials["title"] == selected_material].index[0]
        recs = material_knn.recommend_by_index(idx, k=5)
        st.write("### Recommended Materials:")
        for _, row in enumerate(recs):
            st.write(f"- {row['title']}")
