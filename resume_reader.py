from pypdf import PdfReader
from database import add_cv_skill,clear_cv_skills
reader=PdfReader("Resume.pdf")

text=""
for page in reader.pages:
    text+=page.extract_text()
    #print(text.lower())
text_lower=text.lower()
#TODO почистить split чтобы составные навыки не сплитились 
resume_words=text_lower.split()
print(resume_words)

lowercased=[]
skills=["SQL","Python","CSS","Git","Microsoft Office","GitHub","SQLite","PostgreSQL","Java","Kubernetes","React","Angular","Django","Linux","JavaScript","Visual Studio","HTML","Docker","Flask","C++","C#","LLM","R"]
for skill in skills:
    lowercased.append(skill.lower())


common_skills=[]
for skill in lowercased:
    if skill in resume_words:
        common_skills.append(skill)
print(common_skills)

clear_cv_skills()

for skill in common_skills:
    add_cv_skill(skill)


