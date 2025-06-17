from agents.utils.gemini_wrapper import ask_gemini

class MatchEvaluator:
    def evaluate(self, resume_info, job_description):
        prompt = f"""Evaluate this candidate resume for the job described below.

Resume:
{resume_info}

Job Description:
{job_description}

Give a score out of 10 and a short justification."""
        return ask_gemini(prompt)
