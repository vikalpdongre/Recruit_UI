# app.py
import streamlit as st
# import auth # Assuming 'auth' module handles Google Identity Platform specifics
import analyzer_ui  # Assuming this module contains the main application logic

def apply_custom_css():
    """Applies custom CSS for enhanced aesthetics."""
    st.markdown(
        """
        <style>
        /* General Body Styling */
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f2f6; /* Light gray background */
        }

        /* Streamlit Main Container Styling */
        .stApp {
            background-color: #f0f2f6;
        }

        /* Custom Button Styling */
        .stButton > button {
            background-color: #4285F4; /* Google Blue */
            color: white;
            border-radius: 12px; /* More rounded corners */
            border: none;
            padding: 12px 25px; /* Slightly larger padding */
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Stronger shadow */
            transition: all 0.3s ease;
            letter-spacing: 0.5px; /* Add some letter spacing */
        }
        .stButton > button:hover {
            background-color: #357ae8; /* Darker Google Blue on hover */
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25); /* More pronounced shadow on hover */
            transform: translateY(-3px); /* Lift button slightly */
        }
        .stButton > button:active {
            background-color: #2a65cc;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transform: translateY(0);
        }

        /* Center alignment for sidebar buttons */
        [data-testid="stSidebarNav"] { /* This targets the sidebar navigation container */
            display: flex;
            flex-direction: column;
            align-items: center; /* Center items horizontally */
            padding-top: 20px; /* Add some top padding */
        }
        [data-testid="stSidebarNav"] .stButton > button {
            width: 90%; /* Adjust width for sidebar buttons */
            margin-bottom: 10px; /* Space between sidebar buttons */
        }

        /* Main content container for a polished look */
        .main-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            margin-top: 50px;
            text-align: center; /* Center content within the container */
            max-width: 800px; /* Limit width for better readability */
            margin-left: auto;
            margin-right: auto;
        }

        /* Header styling */
        .header-text {
            color: #1a202c; /* Darker, more professional text color */
            font-size: 3em; /* Larger heading */
            font-weight: 700; /* Bolder */
            margin-bottom: 25px;
            letter-spacing: -0.5px; /* Slight negative letter spacing for a cleaner look */
        }

        /* Sub-header/description text */
        .sub-header-text {
            color: #4a5568; /* Softer text color */
            font-size: 1.4em;
            line-height: 1.6; /* Better line spacing for readability */
            margin-bottom: 40px;
        }

        /* Section titles */
        .section-title {
            color: #333;
            font-size: 2em;
            font-weight: 600;
            margin-top: 40px;
            margin-bottom: 25px;
            text-align: center;
        }

        /* Feature list styling */
        .feature-list {
            list-style-type: none; /* Remove default bullet points */
            padding: 0;
            text-align: left; /* Align list items to the left */
            margin: 30px auto;
            width: fit-content; /* Adjust width to content */
        }
        .feature-list li {
            font-size: 1.15em;
            color: #2d3748;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        /* Remove custom bullet point emoji */
        .feature-list li::before {
            content: ''; /* No content for the custom bullet */
            margin-right: 0; /* Remove margin as well */
            font-size: 1em; /* Reset font size */
        }
        .feature-list li strong { /* Remove strong tag styling in this context */
            font-weight: normal;
        }


        /* Info box styling */
        .info-box {
            background-color: #e6f7ff; /* Light blue */
            border-left: 6px solid #2196F3; /* Stronger blue border */
            padding: 20px;
            margin-top: 30px;
            border-radius: 8px;
            color: #333;
            font-size: 0.95em;
            line-height: 1.5;
            text-align: left;
        }
        .info-box strong {
            color: #0056b3; /* Darker blue for strong text */
        }

        /* Admin/Standard user info boxes */
        .admin-info {
            background-color: #d4edda; /* Light green */
            border-color: #28a745; /* Green border */
            color: #155724; /* Dark green text */
        }
        .standard-user-info {
            background-color: #fff3cd; /* Light yellow */
            border-color: #ffc107; /* Yellow border */
            color: #856404; /* Dark yellow text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_login_page():
    """Displays the login page content for unauthenticated users."""
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header-text'>Welcome to GetHire AI for Recruiters!</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='sub-header-text'>"
        "Revolutionize your hiring process with GetHire AI, your intelligent assistant for streamlined resume and job analysis. "
        "Experience unparalleled efficiency and precision in finding the perfect match."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 class='section-title'>Key Benefits for Recruiters</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul class='feature-list'>
            <li>Find Ideal Candidates Faster: Leverage AI-powered matching to identify top talent quickly.</li>
            <li>Automate Screening: Drastically reduce manual resume review and analysis efforts.</li>
            <li>Boost Hiring Accuracy: Gain precise, data-driven insights for better candidate selection.</li>
            <li>Make Informed Decisions: Access comprehensive reports to enhance your hiring choices.</li>
            <li>Streamline Your Workflow: Integrate a powerful tool that simplifies your recruitment process.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 class='section-title'>How GetHire AI Works</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul class='feature-list'>
            <li>Seamless Document Uploads: Easily upload candidate resumes and your job descriptions in PDF or Word format.</li>
            <li>Instant, Detailed Analysis: Receive instant, comprehensive analysis including matching scores, keyword alignment, and identified skill gaps.</li>
            <li>Actionable Insights: Get clear, actionable recommendations to optimize your candidate shortlisting and interviewing.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='sub-header-text' style='margin-top: 40px;'>"
        "Ready to revolutionize your hiring process? Log in with your Google account to get started!"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<div style='text-align: center; margin-top: 40px;'>", unsafe_allow_html=True)
    if st.button("Login with Google", key="login_button"):
        st.login("google") # This assumes st.login is correctly implemented and linked to Google Identity Platform
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='info-box'>
            <strong>🔒 Secure & Private:</strong> We leverage the robust Google Identity Platform to ensure a secure and seamless authentication experience.
            Your privacy is our utmost priority; your credentials are handled directly by Google, and we do not store them.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True) # Close main-container div

    st.stop()

def display_authenticated_content():
    """Displays content for authenticated users, including sidebar and main app."""
    user = st.user

    # Display user information in the sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Welcome, {user.name or user.email.split('@')[0]}!", unsafe_allow_html=True)
    if user.email:
        st.sidebar.write(f"**Email:** `{user.email}`")
    if user.get("picture"):
        st.sidebar.image(user.picture, caption="Your Profile", use_container_width=True, clamp=True)
    st.sidebar.markdown("---")

    # Add a logout button in the sidebar
    if st.sidebar.button("Logout", key="sidebar_logout_button"):
        st.logout()
        st.info("You have been logged out successfully. Please refresh the page if needed.")
        st.rerun()

    # Main content for authenticated users
    analyzer_ui.main_analyzer_app()

    # Conditional content based on user email (simple authorization)
    if user.email == "vikalp.dongre@gmail.com":
        st.markdown(
            """
            <div class='info-box admin-info'>
                <strong>🎉 Admin Access Granted!</strong> This exclusive section is visible only to administrators.
                You could integrate links to user management, system diagnostics, or advanced configurations here.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class='info-box standard-user-info'>
                You are currently logged in as a standard user. Enjoy all the amazing features of GetHire AI!
            </div>
            """,
            unsafe_allow_html=True
        )

def main():
    """
    Main function for the Streamlit application.
    Handles user authentication flow and displays appropriate content.
    """
    st.set_page_config(page_title="GetHire AI for Recruiters: Intelligent Resume & Job Analyzer", page_icon="📄", layout="centered")
    apply_custom_css()

    if not st.user.is_logged_in:
        display_login_page()
    else:
        display_authenticated_content()

if __name__ == "__main__":
    main()
