
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
profile_pic = current_dir / "assets" / "photo.png"
page_icon = current_dir / "assets" / "shark.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Khalid Houbate"
# PAGE_ICON = ":wave:"
NAME = "Khalid Houbate"
DESCRIPTION = """
Results-driven Senior Cloud/DevOps Engineer with a robust background in cybersecurity and a proven track record of designing and managing complex infrastructures. Adept at automating deployment processes, ensuring high availability, and implementing CI/CD pipelines. Multilingual communicator proficient in English, French, and Arabic.
"""
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
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Competencies")
st.write(
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
st.write("💼", "**IT Security SysAdmin| Booz Allen Hamilton**")
st.write("Oct 2022 - Present")
st.write(
    """
- ► Utilized expertise in system administration and Network security to enhance IT infrastructure for various US Department of Defense clients (Navy, Marine Corps).
- ► Reduced security vulnerabilities US Navy's IT infrastructure through proactive patch management, updates, fixes, and configuration hardening.
- ► Executed SCAP compliance checks and security audits to assess and verify system configurations against predefined security baselines.
- ► Secured Windows & Linux systems, implementing best practices for access control, configuration, file systems, and application security.
- ► Applied Security Technical Implementation Guide (STIG) configurations to systems running different operating systems, enhancing overall security posture and ensuring compliance.
- ► Maintained comprehensive documentation of system configurations, security measures, and compliance status for different operating systems. Generating reports for audits and management.
- ► Serve as the System Administrator maintaining environments run IIS web server hosting .NET application operating a Window SQL Server Database, Contractor for US Marine Corps.
- ► Supported development team for a .NET application, resulting in a 20% increase in system efficiency.
- ► Automated software deployments and backups using PowerShell, improving deployment speed by 30%.
- ► Automated regularly scheduled System Admin functions via scripting language PowerShell.
- ► Delivered support for web server configuration and maintenance activities.
- ►	Implemented problem-solving strategies to identify, facilitate, and implement effective solutions.

"""
)

# --- JOB 2
st.write('\n')
st.write("💼", "**DevSecOps Engineer | Booz Allen Hamilton**")
st.write("Sep 2021 - Oct 20232")
st.write(
    """
- ► Managed configuration for development environment for a US Navy Web-based Application, Contractor for US Navy.
- ► Maintained CI /CD pipelines for Jenkins and GitHub Actions, automating build process and reducing deployment time by 25%.
- ► Ensured development environment is compliant with government-required Security Technical Implementation Guides (STIGs).
- ► Coordinated with multiple teams to deploy releases to internal and Production environments.
- ► Automated infrastructure deployments using Terraform and cloud technologies (AWS).
- ► Investigated and resolved security incidents, minimizing downtime and data loss (50 + incidents).
- ► Collaborated with information security team to identify, address and research potential vulnerabilities, ensuring a resilient IT infrastructure.
- ► Implemented and maintained Open SIEM/EDR tools (Wazuh/Elastic Stack) for enhanced threat detection and response.
- ► Utilized containerization technologies AWS EKS, Docker, and Kubernetes to deploy US Navy Web-based applications across multiple clusters, Contractor for US Navy (40% Efficiency Increase). 
- ► Automated deployment processes with Jenkins (30% reduction in manual errors).
- ► Maintained version control system repositories (GIT) for source code management.
- ► Collaborated with development teams for smooth deployments on AWS GovCloud environments.

"""
)

# --- JOB 3
st.write('\n')
st.write("💼", "**System Engineer Intern | Alion Science & Technology**")
st.write("May 2021 - Sep 2021")
st.write(
    """
- ► Built a dashboard sensor in NGIOS showing if a site is in the Active/Idle state by intermittently pinging an access-side device to confirm if a firewall is open/close before an LVC event start.
- ► Incorporated DISA compliance and accreditation requirements based on the NIST Risk Management Framework, including application of DoD Security Technical Implementation Guidelines (STIG).
- ► Ensured organization's services and systems were running efficiently and would conduct hardware/software troubleshooting and testing.
- ► Directed troubleshooting of Linux subsystems in order determine connectivity and if system was operational.

"""
)

# --- JOB 4
st.write('\n')
st.write("💼", "**Technical Support Specialist | United States Navy**")
st.write("Jan 2013 - Apr 2021")
st.write(
    """
- ► Leveraged strong leadership, communication, and problem-solving skills honed through supervising teams in the U.S. Navy to excel in fast-paced environments.
- ► Managing trouble tickets using Remedy System. Resolves escalated Helpdesk issues promptly.
- ► Demonstrated proficiency in preventing loss or compromise of sensitive and classified data through effective analysis and resolution of hardware, software, and data management issues.
- ► Recognized for coaching, training, and mentoring peers and end users. 
- ► Administered and managed user accounts, restrictions, and security levels in Active Directory.
- ► Managed & maintained critical systems, ensuring high availability & performance.


"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("CERTIFICATIONS")
st.write("---")
for project, link in CERTIFICATIONS.items():
    st.write(f"[{project}]({link})")



