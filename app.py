import streamlit as st
# import auth # Assuming 'auth' module handles Google Identity Platform specifics
import analyzer_ui # Assuming this module contains the main application logic.
                    # Note: This module is not provided in the current context,
                    # so the main_analyzer_app() function will be a placeholder.

def apply_custom_css():
    """
    Applies custom CSS for enhanced aesthetics and responsiveness to the Streamlit application.
    """
    st.markdown(
        """
        <style>
        /* General Body Styling */
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f2f6; /* Light gray background */
            margin: 0; /* Remove default body margin */
            padding: 0; /* Remove default body padding */
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
            width: fit-content; /* Adjust button width to content */
            display: inline-block; /* Allow horizontal alignment if needed */
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

        /* Center alignment for sidebar buttons - targets actual button, not just nav */
        /* Note: Streamlit's internal structure might change, making precise targeting tricky. */
        /* This attempts to center the button itself within the sidebar */
        [data-testid="stSidebar"] .stButton {
            display: flex;
            justify-content: center;
            width: 100%; /* Ensure button container takes full width */
            margin-bottom: 10px;
        }
        [data-testid="stSidebar"] .stButton > button {
            width: 90%; /* Adjust width for sidebar buttons */
            max-width: 250px; /* Max width for consistency */
            margin-bottom: 10px; /* Space between sidebar buttons */
        }


        /* Main content container for a polished look */
        .main-container {
            background-color: #ffffff;
            padding: 20px; /* Reduced padding for smaller screens */
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            margin-top: 20px; /* Reduced margin-top for smaller screens */
            text-align: center; /* Center content within the container */
            max-width: 900px; /* Increased max-width for better laptop view */
            margin-left: auto;
            margin-right: auto;
            box-sizing: border-box; /* Include padding in element's total width and height */
        }

        /* Header styling */
        .header-text {
            color: #1a202c; /* Darker, more professional text color */
            font-size: 2em; /* Adjusted for mobile */
            font-weight: 700; /* Bolder */
            margin-bottom: 15px; /* Adjusted margin */
            letter-spacing: -0.5px;
        }

        /* Sub-header/description text */
        .sub-header-text {
            color: #4a5568; /* Softer text color */
            font-size: 1em; /* Adjusted for mobile */
            line-height: 1.6;
            margin-bottom: 20px; /* Adjusted margin */
        }

        /* Section titles */
        .section-title {
            color: #333;
            font-size: 1.7em; /* Adjusted for mobile */
            font-weight: 600;
            margin-top: 30px; /* Adjusted margin */
            margin-bottom: 15px; /* Adjusted margin */
            text-align: center;
        }

        /* Feature list styling */
        .feature-list {
            list-style-type: none; /* Remove default bullet points */
            padding: 0;
            text-align: left; /* Align list items to the left */
            margin: 20px auto; /* Adjusted margin */
            width: 90%; /* Occupy more width on smaller screens */
            max-width: 600px; /* Limit width for readability on larger screens */
        }
        .feature-list li {
            font-size: 1em; /* Adjusted for mobile */
            color: #2d3748;
            margin-bottom: 10px; /* Adjusted margin */
            display: flex;
            align-items: flex-start; /* Align items to the start for multi-line text */
        }
        .feature-list li::before {
            content: '✅'; /* Use an emoji for bullet point */
            margin-right: 10px;
            font-size: 1.2em;
            flex-shrink: 0; /* Prevent the emoji from shrinking */
        }

        /* Info box styling */
        .info-box {
            background-color: #e6f7ff; /* Light blue */
            border-left: 6px solid #2196F3; /* Stronger blue border */
            padding: 15px; /* Reduced padding */
            margin-top: 20px; /* Adjusted margin */
            border-radius: 8px;
            color: #333;
            font-size: 0.9em; /* Adjusted font size */
            line-height: 1.5;
            text-align: left;
            box-sizing: border-box;
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

        /* Responsive Adjustments using Media Queries */
        @media (min-width: 768px) { /* For tablets and desktops */
            .main-container {
                padding: 40px; /* Restore larger padding for larger screens */
                margin-top: 50px; /* Restore larger margin-top */
            }
            .header-text {
                font-size: 3em; /* Larger heading for desktops */
            }
            .sub-header-text {
                font-size: 1.4em; /* Larger sub-header for desktops */
            }
            .section-title {
                font-size: 2em; /* Larger section title for desktops */
            }
            .feature-list li {
                font-size: 1.15em; /* Larger feature list items for desktops */
            }
            .info-box {
                font-size: 0.95em; /* Restore font size for desktops */
                padding: 20px; /* Restore padding for desktops */
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Placeholder for analyzer_ui module and its main_analyzer_app function
class AnalyzerUI:
    def main_analyzer_app(self):
        st.markdown("<h1 class='header-text'>Resume & Job Analyzer</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header-text'>Upload your resumes and job descriptions here for analysis.</p>", unsafe_allow_html=True)

        # Using columns for better layout on wider screens, stacks on mobile
        col1, col2 = st.columns([1, 1], gap="medium") # Adjusted column ratio and added gap

        with col1:
            st.markdown("<h4>Upload Resumes</h4>", unsafe_allow_html=True)
            st.file_uploader("Select Resume(s) (PDF, DOCX)", type=["pdf", "docx"], accept_multiple_files=True, key="resume_uploader")

        with col2:
            st.markdown("<h4>Upload Job Description</h4>", unsafe_allow_html=True)
            st.file_uploader("Select Job Description (PDF, DOCX)", type=["pdf", "docx"], key="job_desc_uploader")

        st.markdown("---") # Separator

        st.button("Analyze Documents", key="analyze_button", use_container_width=True) # Button takes full width of its container

        st.info("Analysis results and insights will be displayed here after processing your documents.")

analyzer_ui = AnalyzerUI()

def display_login_page():
    """
    Displays the login page content for unauthenticated users, optimized for responsiveness.
    """
    #st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header-text'>Welcome to GetHire Info! ✈️</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='sub-header-text'>"
        "Revolutionize your hiring process with GetHire info, your intelligent assistant for streamlined resume and job analysis. "
        "Experience unparalleled efficiency and precision in finding the perfect match."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 class='section-title'>Key Benefits for Recruiters </h2>", unsafe_allow_html=True)
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

    st.markdown("<h2 class='section-title'>How GetHire AI Works 💡</h2>", unsafe_allow_html=True)
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

    # Centering the login button using Streamlit's built-in column capabilities
    login_col1, login_col2, login_col3 = st.columns([1, 2, 1])
    with login_col2: # Place button in the middle column
        if st.button("Login with Google", key="login_button", use_container_width=True):
            # This line assumes st.login is correctly implemented and linked to Google Identity Platform.
            # For a functional app, you'd integrate with an actual authentication library/service.
            st.info("Login functionality would be triggered here. Simulating login...")
            st.session_state.is_logged_in = True
            st.session_state.user_email = "test.user@example.com"
            st.session_state.user_name = "Test User"
            st.session_state.user_picture = "https://picsum.photos/50/50" # A random image for demo
            st.rerun()

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

    # Stop execution if not logged in to prevent displaying authenticated content
    st.stop()

def display_authenticated_content():
    """
    Displays content for authenticated users, including sidebar user information,
    a logout button, the main analyzer application, and conditional
    authorization messages (admin vs. standard user).
    """
    # Simulate st.user object for demonstration purposes
    if 'user_email' not in st.session_state:
        # Default user if not set, for initial testing
        st.session_state.user_email = "standard.user@example.com"
        st.session_state.user_name = "Standard User"
        st.session_state.user_picture = "https://picsum.photos/50/50"

    class MockUser:
        def __init__(self, email, name, picture):
            self.email = email
            self.name = name
            self.picture = picture
        def get(self, key):
            if key == "picture":
                return self.picture
            return None

    user = MockUser(st.session_state.user_email, st.session_state.user_name, st.session_state.user_picture)

    # Display user information in the sidebar
    with st.sidebar:
        st.markdown("---")
        st.markdown(f"### Welcome, {user.name or user.email.split('@')[0]}!", unsafe_allow_html=True)
        if user.email:
            st.write(f"**Email:** `{user.email}`")
        if user.get("picture"):
            st.image(user.picture, caption="Your Profile", use_container_width=False, width=100) # Fixed width for image
        st.markdown("---")

        # Add a logout button in the sidebar
        if st.button("Logout", key="sidebar_logout_button", use_container_width=True):
            st.session_state.clear()
            st.info("You have been logged out successfully. Refreshing page...")
            st.rerun()

    # Main content for authenticated users
    st.markdown("<div class='main-container'>", unsafe_allow_html=True) # Wrap main content in container
    analyzer_ui.main_analyzer_app()

    # Conditional content based on user email (simple authorization example)
    if user.email == "vikalp.dongre@gmail.com": # Replace with actual admin email
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
    st.markdown("</div>", unsafe_allow_html=True) # Close main-container div


def main():
    """
    Main function for the Streamlit application.
    Handles user authentication flow and displays appropriate content
    (login page or authenticated application).
    """
    st.set_page_config(
        page_title="GetHire AI for Recruiters: Intelligent Resume & Job Analyzer",
        page_icon="📄",
        layout="centered", # 'centered' works well for both, 'wide' for more complex dashboards
        initial_sidebar_state="auto" # 'auto' for responsive sidebar behavior
    )
    apply_custom_css()

    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        display_login_page()
    else:
        display_authenticated_content()

if __name__ == "__main__":
    main()
