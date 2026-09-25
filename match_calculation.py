m_skills=["python","sql","docker","html","c#"]
v_skills=["python","sql","html","css","C#"]

def match(cv_skills,vacancy_skills):
    low_my_skills=[]
    low_vacancy_skills=[]
    if vacancy_skills==[]:
        return None
    else:   
        for skill in cv_skills:
            low_my_skills.append(skill.lower())
        for skill in vacancy_skills:
            low_vacancy_skills.append(skill.lower())
        common_elements=set(low_my_skills)&set(low_vacancy_skills)
        final=(len(common_elements)/len(low_vacancy_skills))*100
        return final
    

print(len(m_skills))
print(len(v_skills))

print(match(m_skills,v_skills))

print(match(m_skills,[]))