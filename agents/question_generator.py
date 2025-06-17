from agents.utils.gemini_wrapper import ask_gemini

class QuestionGenerator:
    def generate(self, resume_info, job_description):
        prompt = f"""Generate 5 technical and 3 behavioral interview questions based on:

Resume:
{resume_info}

Job Description:
{job_description}"""

        return ask_gemini(prompt)
