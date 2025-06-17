# import streamlit as st
# from agents.hr_agent import GeminiHR
# from agents.utils.email_sender import send_email
# import fitz  # PyMuPDF
# import docx

# agent = GeminiHR()

# st.set_page_config(page_title="AI HR Agent", layout="centered")
# st.title("🤖 Gemini HR Recruitment Agent")
# st.markdown("Upload a resume and job description to get automatic analysis and results via email.")

# uploaded_file = st.file_uploader("📄 Upload Resume (.pdf / .docx)", type=["pdf", "docx"])
# jd_text = st.text_area("📝 Paste Job Description (optional for evaluation)", height=200)
# email = st.text_input("📬 HR Email Address (optional to send report)").strip()

# def extract_text(file):
#     if file.name.endswith(".pdf"):
#         doc = fitz.open(stream=file.read(), filetype="pdf")
#         return "\n".join(page.get_text() for page in doc)
#     elif file.name.endswith(".docx"):
#         doc = docx.Document(file)
#         return "\n".join(para.text for para in doc.paragraphs)
#     return ""

# if uploaded_file:
#     with st.spinner("Analyzing resume using Gemini Agent..."):
#         resume_text = extract_text(uploaded_file)
#         result = agent.generate_response(resume_text, jd_text)

#     st.success("✅ Analysis Complete!")
#     st.text_area("🧠 Gemini HR Agent Response", result, height=400)

#     if email:
#         if st.button("📧 Send Report via Email"):
#             success = send_email("Candidate Resume Summary", result, email)
#             if success:
#                 st.success(f"📨 Email sent to {email}")
#             else:
#                 st.error("❌ Failed to send email. Check logs or credentials.")


# import streamlit as st
# from agents.hr_agent import GeminiHR
# from agents.utils.email_sender import send_email
# import fitz  # PyMuPDF
# import docx

# agent = GeminiHR()

# st.set_page_config(page_title="AI HR Agent", layout="centered")
# st.title("🤖 Gemini HR Recruitment Agent")
# st.markdown("Upload a resume to get automatic analysis and send results via email.")

# uploaded_file = st.file_uploader("📄 Upload Resume (.pdf / .docx)", type=["pdf", "docx"])
# email = st.text_input("📬 HR Email Address (optional to send report)")

# def extract_text(file):
#     if file.name.endswith(".pdf"):
#         doc = fitz.open(stream=file.read(), filetype="pdf")
#         return "\n".join(page.get_text() for page in doc)
#     elif file.name.endswith(".docx"):
#         doc = docx.Document(file)
#         return "\n".join(para.text for para in doc.paragraphs)
#     return ""

# if uploaded_file:
#     with st.spinner("Analyzing resume using Gemini Agent..."):
#         resume_text = extract_text(uploaded_file)
#         result = agent.generate_response(resume_text)

#     st.success("✅ Analysis Complete!")
#     st.text_area("🧠 Gemini HR Agent Response", result, height=300)

#     if email:
#         if st.button("📧 Send Report via Email"):
#             success = send_email("Candidate Resume Summary", result, email)
#             if success:
#                 st.success(f"📨 Email sent to {email}")
#             else:
#                 st.error("❌ Failed to send email. Check logs or credentials.")





import streamlit as st
from agents.hr_agent import GeminiHR
from agents.utils.email_sender import send_email
import fitz  # PyMuPDF for PDF
import docx  # For DOCX files

agent = GeminiHR()

st.set_page_config(page_title="AI HR Agent", layout="centered")
st.title("🤖 Gemini HR Recruitment Agent")

st.markdown("### 📄 Upload Resumes (PDF/DOCX)")
uploaded_files = st.file_uploader("Upload multiple resumes", type=["pdf", "docx"], accept_multiple_files=True)

st.markdown("### 📝 Paste Job Description")
jd_text = st.text_area("Enter the job description here")

email = st.text_input("📬 HR Email Address (optional – send report to HR)")

# Helper to extract resume text
def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(para.text for para in doc.paragraphs)
    return ""

# Main logic
if uploaded_files and jd_text:
    with st.spinner("Analyzing all resumes..."):
        all_results = []
        for file in uploaded_files:
            resume_text = extract_text(file)
            result = agent.generate_response(resume_text, jd_text)
            all_results.append((file.name, result))

    st.success("✅ All resumes analyzed successfully!")

    # Display results for each resume
    for name, res in all_results:
        st.subheader(f"📄 {name}")
        st.text_area("🧠 Gemini HR Agent Evaluation", res, height=300)

    # Optional: Send all reports to HR
    if email:
        if st.button("📧 Send Combined Report to HR"):
            full_report = "\n\n---\n\n".join([f"📄 {name}\n{res}" for name, res in all_results])
            success = send_email(email, "Shortlisted Candidates Report", full_report)
            if success:
                st.success(f"📨 Report sent to {email}")
            else:
                st.error("❌ Failed to send email. Check credentials or logs.")

elif uploaded_files and not jd_text:
    st.warning("⚠️ Please paste the Job Description to start evaluation.")
