applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
        "email_address": "susan@email.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": True,
        "email_address": "sam@email.com",
    },
]

# Check which applicants qualify for an interview
for applicant in applicants:

    if (
        "python" in applicant["programming_languages"]
        or applicant["years_of_experience"] >= 5
        or applicant["has_degree"] == True
    ):
        print("Interview candidate:", applicant["name"])
        print("Email:", applicant["email_address"])

    else:
        print("Not eligible for interview:", applicant["name"])

    print()