import streamlit as st
from PIL import Image
import io  # For byte stream

def crop_image(image, width, height):
    """
    Crop the uploaded image to fit the desired width and height.
    """
    img_width, img_height = image.size
    left = (img_width - width) / 2
    top = (img_height - height) / 2
    right = (img_width + width) / 2
    bottom = (img_height + height) / 2
    return image.crop((left, top, right, bottom))

def generate_biography(name, gender, age, profession, hobbies, about_me, favorite_quote, 
                       father_name, father_profession, mother_name, mother_profession, 
                       sibling_name, sibling_profession, pet_name, pet_type, 
                       achievements, instagram, twitter, linkedin):
    """
    Generate a formatted biography as a string.
    """
    bio = f"""
    🌟 Biography 🌟
    
    Name: {name}
    Gender: {gender}
    Age: {age}
    Profession: {profession}

    About Me:
    {about_me}

    Hobbies: {hobbies}
    Favorite Quote: "{favorite_quote}"

    Achievements:
    """
    if achievements:
        bio += f"- {achievements.replace(';', '\\n- ')}\n"
    else:
        bio += "No achievements mentioned.\n"

    bio += """
    Family:
    """
    bio += f"Father's Name: {father_name} (Profession: {father_profession})\n"
    bio += f"Mother's Name: {mother_name} (Profession: {mother_profession})\n"
    if sibling_name:
        bio += f"Siblings: {sibling_name} (Profession: {sibling_profession})\n"
    if pet_name:
        bio += f"Pet: {pet_name} ({pet_type})\n"
    
    bio += "\nSocial Media Handles:\n"
    if instagram:
        bio += f"Instagram: @{instagram}\n"
    if twitter:
        bio += f"Twitter: @{twitter}\n"
    if linkedin:
        bio += f"LinkedIn: {linkedin}\n"

    return bio

def main():
    # Page Configuration
    st.set_page_config(
        page_title="My Cute Biography",
        page_icon="🌟",
        layout="wide",
    )

    # Sidebar Inputs
    st.sidebar.title("📝 Your Profile Details")
    name = st.sidebar.text_input("👤 Name", placeholder="JENNYLYN M. CASICA")
    gender = st.sidebar.radio("⚥ Gender", options=["Male", "Female", "Non-Binary", "Prefer Not to Say"], index=0)
    age = st.sidebar.number_input("🎂 Age", min_value=1, max_value=120, step=1)
    profession = st.sidebar.text_input("💼 Profession", placeholder="STUDENT")
    hobbies = st.sidebar.text_area("🎨 Hobbies or Interests", placeholder="MUSIC, PLAYING INSTRUMENTS,TABLE TENNIS")
    about_me = st.sidebar.text_area("✍️ About Me", placeholder="I LOVE MATH AND MUSIC")
    profile_pic = st.sidebar.file_uploader("📷 Upload Your Profile Picture", type=["jpg", "png", "jpeg"])
    favorite_quote = st.sidebar.text_area("💬 Favorite Quote", placeholder="All our dreams can come true, if we have the courage to pursue them.'")

    # Achievements
    st.sidebar.title("🏆 Achievements")
    achievements = st.sidebar.text_area(
        "Enter Your Achievements (separate by semicolons)",
        placeholder="Won regional table tennis championship; Scored A+ in math exam; Published a blog"
    )

    # Family Details
    st.sidebar.title("👪 Family Details")
    father_name = st.sidebar.text_input("👨‍👦 Father's Name", placeholder="N/A")
    father_profession = st.sidebar.text_input("👨‍💼 Father's Profession", placeholder="N/A")
    mother_name = st.sidebar.text_input("👩‍👦 Mother's Name", placeholder="MERLY MONGADO")
    mother_profession = st.sidebar.text_input("👩‍💼 Mother's Profession", placeholder="HOUSE WIFE")
    sibling_name = st.sidebar.text_input("🧑‍🤝‍🧑 Sibling's Name", placeholder="N/A")
    sibling_profession = st.sidebar.text_input("💼 Sibling's Profession", placeholder="N/A")
    pet_name = st.sidebar.text_input("🐾 Pet's Name", placeholder="BARCKLY")
    pet_type = st.sidebar.text_input("🐶 Pet Type", placeholder="BULLDOG")

    # Social Media
    st.sidebar.title("🌐 Social Media")
    instagram = st.sidebar.text_input("📸 Instagram Handle", placeholder="@username")
    twitter = st.sidebar.text_input("🐦 Twitter Handle", placeholder="@username")
    linkedin = st.sidebar.text_input("🔗 LinkedIn Profile", placeholder="https://linkedin.com/username")

    # Generate Biography Button
    generate = st.sidebar.button("✨ Generate Biography")

    if generate:
        # Validate Inputs
        if not name:
            st.error("❗ Please provide your name to generate a biography.")
            return

        # Generate Biography Text
        biography = generate_biography(
            name, gender, age, profession, hobbies, about_me, favorite_quote,
            father_name, father_profession, mother_name, mother_profession,
            sibling_name, sibling_profession, pet_name, pet_type,
            achievements, instagram, twitter, linkedin
        )

        # Display Biography
        st.markdown("## 🌟 Your Generated Biography")
        st.text_area("Your Biography", biography, height=300)

        # Download Biography
        st.subheader("Download Your Biography 📝")
        bio_bytes = io.BytesIO(biography.encode('utf-8'))
        st.download_button(
            label="Download Biography as Text File",
            data=bio_bytes,
            file_name=f"{name}_Biography.txt",
            mime="text/plain",
        )

if __name__ == "__main__":
    main()
