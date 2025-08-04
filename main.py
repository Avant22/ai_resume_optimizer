# main.py

# Step 1: Load the prompt template
with open("prompts/resume_improver.txt", "r") as file:
    prompt_template = file.read()

# Step 2: Load the resume and job description
with open("resumes/resume1.txt", "r") as file:
    resume_text = file.read()

with open("jobs/job1.txt", "r") as file:
    job_text = file.read()

# Step 3: Replace placeholders with actual content
final_prompt = prompt_template.replace("{{job_description}}", job_text)
final_prompt = final_prompt.replace("{{resume}}", resume_text)

# Step 4: Print the full prompt (simulating sending to an LLM)
print("📄 Final Prompt to Send:\n")
print(final_prompt)
# Step 5: Simulated response (pretending this came from GPT)
simulated_response = """
1. Mention experience with CRM tools like HubSpot.
2. Include a line about collaborating with product or onboarding teams.
3. Reword 'email handling' to sound more strategic, e.g., 'managing client communications.'
"""

# Step 6: Save the response to a file
with open("output/response.txt", "w") as file:
    file.write(simulated_response)

# Step 7: Notify user
print("\n✅ Simulated GPT response saved to: output/response.txt")
