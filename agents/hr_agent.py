from agents.utils.gemini_wrapper import ask_gemini
from agents.resume_parser import ResumeParser
from agents.match_evaluator import MatchEvaluator
from agents.question_generator import QuestionGenerator

class GeminiHR:
    def __init__(self):
        self.name = "Gemini_HR_Agent"
        self.parser = ResumeParser()
        self.evaluator = MatchEvaluator()
        self.generator = QuestionGenerator()

    # def generate_response(self, message):
    #     print(f"[{self.name}] Processing...")

    #     intent = ask_gemini(f"What is the intent of this message? Choose from: ['resume_upload', 'job_description', 'chat']\nMessage: {message}")
        
    #     if "resume_upload" in intent.lower():
    #         parsed = self.parser.parse(message)
    #         print("\n🔍 Parsed Resume:\n", parsed)
    #         return parsed

    #     elif "job_description" in intent.lower():
    #         print("📝 Job description noted.")
    #         return "Job description saved (future implementation: match resumes to this automatically)."

    #     else:
    #         return ask_gemini(message)
        



    def generate_response(self, message, jd_text=None):  # ✅ Now inside class
        print(f"[{self.name}] Processing...")

        intent = ask_gemini(
            f"What is the intent of this message? Choose from: ['resume_upload', 'job_description', 'chat']\nMessage: {message}"
        )

        if "resume_upload" in intent.lower():
            parsed_resume = self.parser.parse(message)
            print("\n🔍 Parsed Resume:\n", parsed_resume)

            if jd_text:
                evaluation = self.evaluator.evaluate(parsed_resume, jd_text)
                questions = self.generator.generate(parsed_resume, jd_text)
                return f"📋 **Parsed Resume:**\n{parsed_resume}\n\n✅ **Evaluation:**\n{evaluation}\n\n❓ **Questions:**\n{questions}"
            else:
                return parsed_resume

        elif "job_description" in intent.lower():
            print("📝 Job description noted.")
            return "Job description saved (future implementation: match resumes to this automatically)."

        else:
            return ask_gemini(message)




