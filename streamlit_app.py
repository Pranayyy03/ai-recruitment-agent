import streamlit as st
from agents.hr_agent import GeminiHR
from agents.utils.email_sender import send_email
import fitz  # PyMuPDF
import docx

agent = GeminiHR()

st.set_page_config(page_title="AI HR Agent", layout="centered")
st.title("🤖 Gemini HR Recruitment Agent")
st.markdown("Upload a resume and job description to get automatic analysis and results via email.")

uploaded_file = st.file_uploader("📄 Upload Resume (.pdf / .docx)", type=["pdf", "docx"])
jd_text = st.text_area("📝 Paste Job Description (optional for evaluation)", height=200)
email = st.text_input("📬 HR Email Address (optional to send report)").strip()

def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(para.text for para in doc.paragraphs)
    return ""

if uploaded_file:
    with st.spinner("Analyzing resume using Gemini Agent..."):
        resume_text = extract_text(uploaded_file)
        result = agent.generate_response(resume_text, jd_text)

    st.success("✅ Analysis Complete!")
    st.text_area("🧠 Gemini HR Agent Response", result, height=400)

    if email:
        if st.button("📧 Send Report via Email"):
            success = send_email("Candidate Resume Summary", result, email)
            if success:
                st.success(f"📨 Email sent to {email}")
            else:
                st.error("❌ Failed to send email. Check logs or credentials.")


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