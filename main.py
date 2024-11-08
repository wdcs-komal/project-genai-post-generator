import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish", "Hindi", "Gujarati"]


# Main app layout
# def main():
#     st.markdown("<h2 style='text-align: center; font-weight: bold;'>LinkedIn Post Generator: Webclues</h2>", unsafe_allow_html=True)
#     # st.subheader("LinkedIn Post Generator: Webclues")


#    st.markdown("""
#         <style>
#         /* Style for dropdown (select) elements */
#         div[data-baseweb="select"] > div {
#             border: 5px solid black !important;
#             border-radius: 2px;
#         }
#         </style>
# """, unsafe_allow_html=True)


#     # Create three columns for the dropdowns
#     col1, col2, col3 = st.columns(3)

#     fs = FewShotPosts()
#     tags = fs.get_tags()
#     with col1:
#         # Dropdown for Topic (Tags)
#         selected_tag = st.selectbox("Topic", options=tags)

#     with col2:
#         # Dropdown for Length
#         selected_length = st.selectbox("Length", options=length_options)

#     with col3:
#         # Dropdown for Language
#         selected_language = st.selectbox("Language", options=language_options)



#     # Generate Button
#     if st.button("Generate"):
#         post = generate_post(selected_length, selected_language, selected_tag)
#         st.write(post)


# # Run the app
# if __name__ == "__main__":
#     main()



import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish", "Hindi", "Gujarati"]


# Main app layout
def main():
    # Center the main heading and make it bold
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>LinkedIn Post Generator: Webclues</h2>", unsafe_allow_html=True)

    # Custom CSS to style the dropdowns and button
    st.markdown("""
        <style>
        /* Style for dropdown (select) elements */
        div[data-baseweb="select"] > div {
            border: 3px solid black !important;
            border-radius: 2px;
        }
        
        /* Style for the button */
        .stButton>button {
            display: block;
            margin: 0 auto;
            border: 3px solid black;
            border-radius: 8px;
            color: white;
            background-color: #4CAF50; /* Optional: change button color */
        }

        /* Style for labels above selectboxes */
        .css-1cpxqw2 {
            font-weight: bold;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Center and style the Generate button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()
