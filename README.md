# 🤖 AI Recruitment Agent (Gemini + Streamlit)

This is an AI-powered recruitment agent that helps HR teams by automating resume parsing, evaluating candidates against a job description (JD), generating intelligent interview questions, and sending reports via email.

---

## 🚀 Features

- 📄 Upload multiple resumes (.pdf / .docx)
- 🧠 Gemini-based AI analysis and intent recognition
- 📝 Automatic resume parsing & JD evaluation
- ✅ Candidate shortlisting based on JD fit
- ❓ Interview question suggestions
- 📧 One-click report email sending (SMTP)
- 🌐 Streamlit Web UI

---

## 📂 Folder Structure

ai-recruitment-agent/
│
├── agents/
│ ├── utils/
│ │ ├── gemini_wrapper.py # Gemini API integration
│ │ └── email_sender.py # Sends emails
│ ├── resume_parser.py # Extracts data from resume
│ ├── match_evaluator.py # Evaluates resume vs JD
│ ├── question_generator.py # Suggests interview questions
│ └── hr_agent.py # Core HR agent logic
│
├── streamlit_app.py # Frontend app using Streamlit
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (e.g., venv/, pycache)
└── README.md # You're reading it!


---

## 🛠️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/yourusername/ai-recruitment-agent.git
cd ai-recruitment-agent
2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
3. Install Dependencies
pip install -r requirements.txt
4. Add Your API Key
In agents/utils/gemini_wrapper.py, add your Gemini API key:

api_key = "YOUR_GEMINI_API_KEY"
5. Configure Email
In agents/utils/email_sender.py, replace with your Gmail App Password:

from_email = "youremail@gmail.com"
password = "your_app_password"
Enable 2FA in Gmail → Generate App Password

▶️ Run the App

streamlit run streamlit_app.py
Then open: http://localhost:8501

✉️ Email Report Support
Enter your HR email in the field.

Click "📧 Send Report" after parsing resumes.

Uses smtplib to send reports securely.

📌 To Do / Future Additions
✅ Multi-resume upload & auto shortlisting

⏳ Admin dashboard for tracking candidates

⏳ WhatsApp or Slack notifications

⏳ LangGraph/AutoGen integration for autonomy

👨‍💻 Developed By
Pranay Raj
AI enthusiast | Python Developer | HR Tech Innovator










