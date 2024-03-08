
import base64
import os
import streamlit as st
from pathlib import Path
from PIL import Image
from io import BytesIO


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "shark.png"
page_icon = current_dir / "assets" / "shark.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Your Name here"
# PAGE_ICON = ":wave:"
NAME = "Your Name here"
DESCRIPTION = """
Professional Description goes here"""
EMAIL = {
    "Contact Me":"https://github.com/khoubate/resume/discussions",
    }
SOCIAL_MEDIA = {

    "Contact": "https://github.com/khoubate/resume/discussions",
    "LinkedIn": "https://www.linkedin.com/in/khalid-houbate/",
    "GitHub": "https://github.com/khoubate",
    # "Twitter": "https://twitter.com",
    # "YouTube": "https://youtube.com/c/codingisfun",
}
CERTIFICATIONS= {
    # "🏆
    "🛡️ CompTIA CySA+": "https://www.credly.com/badges/dd8ec5af-60e1-4e05-b5e8-91310789b3af",
    "🛡️ CompTIA Security": "https://www.credly.com/badges/dd8ec5af-60e1-4e05-b5e8-91310789b3af", 
    "🛡️ ISC2 CC": "https://www.credly.com/badges/52b9ccac-5287-41fa-91da-651665d596f4", 
    "🐧 CompTIA Linux+": "https://www.credly.com/badges/fab9840d-adf3-4e1c-873b-d72e5e24ba4d", 
    "☁️ AWS Certified Cloud Practitioner": "https://www.credly.com/badges/c7607408-4d5b-444a-a7d4-279ace806b29", 
    "☁️ AWS Solution Architect": "https://www.credly.com/badges/f63d57dd-5c84-4d74-b57f-dc9dc589ff2e",
}


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.set_page_config(page_title=PAGE_TITLE, page_icon=Image.open(page_icon))



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")  # Adjust format if needed
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
#centered_img_html = f'<div style="text-align: center"><img src="data:image/png;base64,{image_to_base64(profile_pic)}" width=230></div>'
centered_img_html = f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{image_to_base64(profile_pic)}" width=325></div>'

with col1:
    st.markdown(centered_img_html, unsafe_allow_html=True)
    # st.image(profile_pic, width=230, use_column_width=False)
    def image_to_base64(img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    cols = st.columns(len(SOCIAL_MEDIA))
    st.write('\n')
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        logo_path = current_dir / "assets" / "social" / f"{platform}.png"
        with cols[index]:
            try:
                # Open the image and convert to RGB format
                img = Image.open(logo_path).convert('RGB')
                img_html = f'<div style="text-align: center"><a href="{link}" target="_blank"><img src="data:image/png;base64,{image_to_base64(img)}" height=40></a></div>'
                st.markdown(img_html, unsafe_allow_html=True)
            except Exception as e:
                 st.error(f"Error displaying image for {platform}: {e}")
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


# --- SOCIAL LINKS ---
# def image_to_base64(img):
#     buffered = BytesIO()
#     img.save(buffered, format="PNG")
#     return base64.b64encode(buffered.getvalue()).decode("utf-8")

# # ...

# cols = st.columns(len(SOCIAL_MEDIA))

# st.write('\n')

# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     logo_path = current_dir / "assets" / "social" / f"{platform}.png"
#     with cols[index]:
#         try:
#             # Open the image and convert to RGB format
#             img = Image.open(logo_path).convert('RGB')
#             img_html = f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{image_to_base64(img)}" height=50></a>'
#             st.markdown(img_html, unsafe_allow_html=True)
#         except Exception as e:
#             st.error(f"Error displaying image for {platform}: {e}")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- 🛠️ 8 Years experience as Technical Solutions Architect.
- ⚙️ IT Infrastructure Automation Specialist.
- 🏗️ Strong hands on in Security Automation and Orchestration.
- 🛡️ Expert in Cybersecurity Architecture
- 🤝 Excellent team-player and displaying strong sense of initiative on tasks

"""
# You can add more  details about your work history above!

)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Competencies")
st.write(
#  Add skills below and custom them as you see fit
    """
- 🤖 Automation and Orchestration: Ansible, Puppet, Chef
- 📁 Version Control: Git
- ⚙️ CI/CD: Jenkins, GitLab CI/CD, GitHub Actions
- 📊 Monitoring and Logging: ELK Stack (Elasticsearch, Logstash, Kibana)
- ☁️ Cloud Technologies: AWS, Azure, Google Cloud Platform
- 💻 Operating System: Linux, Windows, MacOS
- 🛠️ Scripting Languages: Bash, PowerShell, NodeJS
- 🔒 Security Tools: Nessus, MS Defender for Endpoint, Wazuh, OSSEC, Splunk
- 🛡️ Cybersecurity: Implementation of best practices, Vulnerability Management
- 📡 Network Security and Monitoring
- 🗄️ Databases: Postgres, MongoDB, MySQL

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("💼", "**Title/Role| Company Name**")
st.write("Oct 2022 - Present")
st.write(
    """
- ► Utilized expertise in system administration and Network security to enhance IT infrastructure for various US Department of Defense clients (Navy, Marine Corps).


"""
)

# --- JOB 2
st.write('\n')
st.write("💼", "**Title/Role| Company Namen**")
st.write("Sep 2021 - Oct 20232")
st.write(
    """
- ► Managed configuration for development environment for a US Navy Web-based Application, Contractor for US Navy.


"""
)

# --- JOB 3
st.write('\n')
st.write("💼", "**Title/Role| Company Name**")
st.write("May 2021 - Sep 2021")
st.write(
    """
- ► Built a dashboard sensor in NGIOS showing if a site is in the Active/Idle state by intermittently pinging an access-side device to confirm if a firewall is open/close before an LVC event start.


"""
)

# --- JOB 4
st.write('\n')
st.write("💼", "**Title/Role| Company Name**")
st.write("Jan 2013 - Apr 2021")
st.write(
    """
- ► Leveraged strong leadership, communication, and problem-solving skills honed through supervising teams in the U.S. Navy to excel in fast-paced environments.



"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("CERTIFICATIONS")
st.write("---")
for project, link in CERTIFICATIONS.items():
    st.write(f"[{project}]({link})")