# from agents.hr_agent import GeminiHR

# if __name__ == "__main__":
 #   agent = GeminiHR()
  #  print("🤖 Gemini HR Agent is Ready. Type your query.")
   # while True:
    #    user_input = input("You: ")
     #   if user_input.lower() in ["exit", "quit"]:
      #      break
       # agent.generate_response(user_input)


# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()
# import json

# content = {
#     "contents": [
#       {
#         "parts": [
#           {
#             "text": "Explain how AI works in a few words"
#           }
#         ]
#       }
#     ]
#   }
# content = json.dumps(content)
# response = requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={os.getenv("GEMINI_API_KEY")}', 
#               data=content,
#               headers={"Content-Type": "application/json"}
#               )
# print(response.text)

from agents.hr_agent import GeminiHR
from agents.resume_parser import ResumeParser
from agents.match_evaluator import MatchEvaluator
from agents.question_generator import QuestionGenerator

def run_resume_analysis():
    raw_resume = input("\n📄 Paste the candidate resume text:\n")
    job_description = input("\n📝 Paste the job description:\n")

    parser = ResumeParser()
    evaluator = MatchEvaluator()
    generator = QuestionGenerator()

    print("\n🔍 Parsing Resume...")
    parsed_resume = parser.parse(raw_resume)
    print(parsed_resume)

    print("\n📊 Evaluating Match...")
    evaluation = evaluator.evaluate(parsed_resume, job_description)
    print(evaluation)

    print("\n🧠 Generating Interview Questions...")
    questions = generator.generate(parsed_resume, job_description)
    print(questions)

if __name__ == "__main__":
    agent = GeminiHR()
    print("\n🤖 HR Agent is Ready.")
    print("💬 Type 'chat' to talk, 'analyze resume' to run recruitment flow, or 'exit' to quit.\n")

    while True:
        user_input = input("🧑 You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        elif user_input.lower() == "analyze resume":
            run_resume_analysis()

        elif user_input.lower() == "chat":
            while True:
                chat_input = input("💬 You (chat mode): ")
                if chat_input.lower() in ["exit", "back", "quit"]:
                    print("↩️ Exiting chat mode.\n")
                    break
                agent.generate_response(chat_input)

        else:
            print("❓ Invalid command. Try 'chat', 'analyze resume', or 'exit'.")
