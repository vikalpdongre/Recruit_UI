# app.py
import streamlit as st
#import auth
import analyzer_ui
import os
ST_AUTH_GOOGLE_CLIENT_SECRET =  os.getenv("ST_AUTH_GOOGLE_CLIENT_SECRET")
ST_AUTH_COOKIE_SECRET =  os.getenv("ST_AUTH_COOKIE_SECRET")
ST_AUTH_GOOGLE_CLIENT_ID =  os.getenv("ST_AUTH_GOOGLE_CLIENT_ID")
ST_AUTH_GOOGLE_SERVER_METADATA_URL =  os.getenv("ST_AUTH_GOOGLE_SERVER_METADATA_URL")
ST_AUTH_COOKIE_SECRET =  os.getenv("ST_AUTH_COOKIE_SECRET")





def main():
    """
    Main function for the Streamlit application.
    Handles user authentication flow using Google Identity Platform.
    """

    st.set_page_config(page_title="AR&JD Analyzer App", page_icon="🔒", layout="centered")

    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4285F4; /* Google Blue */
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #357ae8; /* Darker Google Blue on hover */
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }
        .stButton>button:active {
            background-color: #2a65cc;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transform: translateY(0);
        }
        .st-emotion-cache-1r6dm7f { /* This targets the sidebar button container */
            display: flex;
            justify-content: center;
            width: 100%;
        }
        .st-emotion-cache-1r6dm7f button {
            width: 80%; /* Adjust width for sidebar buttons */
        }
        .container {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            background-color: #ffffff;
        }
        .header-text {
            color: #333;
            font-size: 2.2em;
            text-align: center;
            margin-bottom: 20px;
        }
        .sub-header-text {
            color: #555;
            font-size: 1.2em;
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box {
            background-color: #e6f7ff;
            border-left: 5px solid #2196F3;
            padding: 15px;
            margin-top: 20px;
            border-radius: 5px;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Check if the user is logged in using Streamlit's experimental_user API
    # Note: st.experimental_user might become st.user in future Streamlit versions
    if hasattr(st.user, "is_logged_in"):
        st.markdown("<h1 class='header-text'>🔒 Advanced Resume & Job Description Analyzer</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header-text'>Please log in with your Google account to access the content.</p>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; margin-top: 40px;'>", unsafe_allow_html=True)
        # Display a login button for Google.
        # The string "google" refers to the [auth.google] section in .streamlit/secrets.toml
        if st.button("Login with Google"):
            st.login("google")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='info-box'>
                <strong>Note:</strong> This application uses Google Identity Platform for secure authentication. 
                Your credentials are handled directly by Google.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Stop further execution of the script if the user is not logged in
        st.stop()

    # --- Code below this line will only execute if the user is authenticated ---

    # Retrieve user information from the session
    user = st.user

    # Display user information in the sidebar
    st.sidebar.markdown(f"**👋 Hello, {user.name or user.email}!**")
    if user.email:
        st.sidebar.write(f"Email: {user.email}")
    if user.get("picture"): # 'picture' claim is often available for profile scope
        st.sidebar.image(user.picture, caption="Profile Picture", use_container_width =True, clamp=True)

    # Add a logout button in the sidebar
    if st.sidebar.button("Logout"):
        st.logout()
        st.info("You have been logged out successfully.")
        st.rerun() # Rerun the app to show the login page
    
    # Main content for authenticated users
    
    analyzer_ui.main_analyzer_app()

    # Example of conditional content based on user email (simple authorization)
    # Replace "your.admin.email@gmail.com" with an actual email you want to designate as admin
    if user.email == "vikalp.dongre@gmail.com":
        st.markdown(
            """
            <div class='info-box' style='background-color: #d4edda; border-color: #28a745;'>
                <strong>Admin Privileges Detected!</strong> This section is only visible to administrators.
                You could add links to admin panels, user management, or system settings here.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class='info-box' style='background-color: #fff3cd; border-color: #ffc107;'>
                You are logged in as a standard user. Some administrative features may be restricted.
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
