from agents.utils.gemini_wrapper import ask_gemini

class ResumeParser:
    def parse(self, raw_resume):
        prompt = f"""Extract the following from the resume:
- Name
- Email
- Skills
- Experience summary
- Education

Resume:
{raw_resume}
"""
        return ask_gemini(prompt)