import streamlit as st
from agents.hr_agent import GeminiHR
from agents.utils.email_sender import send_email
import fitz  # PyMuPDF for PDF
import docx  # For DOCX files
import time

agent = GeminiHR()

st.set_page_config(page_title="AI HR Agent", layout="centered")
st.title("🤖 HR Recruitment Agent")

st.markdown("### 📄 Upload Resumes (PDF/DOCX)")
uploaded_files = st.file_uploader("Upload multiple resumes", type=["pdf", "docx"], accept_multiple_files=True)

st.markdown("### 📝 Paste Job Description")
jd_text = st.text_area("Enter the job description here")
email = st.text_input("📬 HR Email Address (optional – send report to HR)").strip()

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
            with st.spinner(f"⏳ Processing: {file.name}"):
                start_time = time.time()

                resume_text = extract_text(file)
                st.write(f"📄 Extracted text length: {len(resume_text)} characters")

                # Truncate long resume text to avoid Gemini crashes
                if len(resume_text) > 8000:
                    st.warning(f"⚠️ Truncating resume: {file.name} (too long)")
                    resume_text = resume_text[:8000]

                try:
                    result = agent.generate_response(resume_text, jd_text)
                except Exception as e:
                    result = f"❌ Error while analyzing {file.name}: {e}"
                    st.error(result)
                
                all_results.append((file.name, result))

                elapsed = time.time() - start_time
                st.success(f"✅ Done with {file.name} in {elapsed:.2f} seconds")

                time.sleep(4)  # Avoid Gemini rate limit

    st.success("✅ All resumes analyzed successfully!")

    # Display results for each resume
    for name, res in all_results:
        st.subheader(f"📄 {name}")
        st.text_area("🧠 HR Agent Evaluation", res, height=300)

    # Optional: Send all reports to HR
    if email:
        if st.button("📧 Send Combined Report to HR"):
            full_report = "\n\n---\n\n".join([f"📄 {name}\n{res}" for name, res in all_results])
            success = send_email("Shortlisted Candidates Report", result, email)
            if success:
                st.success(f"📨 Report sent to {email}")
            else:
                st.error("❌ Failed to send email. Check credentials or logs.")

elif uploaded_files and not jd_text:
    st.warning("⚠️ Please paste the Job Description to start evaluation.")
