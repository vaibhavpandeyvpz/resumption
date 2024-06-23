Resume = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Full name of the candidate.",
        },
        "emails": {
            "type": "array",
            "description": "List of email addresses of the candidate.",
            "items": {"type": "string"},
        },
        "phones": {
            "type": "array",
            "description": "List of phone numbers of the candidate, in E.164 format.",
            "items": {"type": "string"},
        },
        "date_of_birth": {
            "type": "string",
            "description": "Date of birth of the candidate in YYYY-MM-DD format.",
        },
        "nationality": {
            "type": "string",
            "description": "Nationality of the candidate as ISO 3166-1 alpha-2 code.",
        },
        "about": {
            "type": "string",
            "description": "Text content from about section of the candidate.",
        },
        "skills": {
            "type": "array",
            "description": "List of skills mentioned by the candidate.",
            "items": {"type": "string"},
        },
        "hobbies": {
            "type": "array",
            "description": "List of hobbies mentioned by the candidate.",
            "items": {"type": "string"},
        },
        "languages": {
            "type": "array",
            "description": "List of languages known by the candidate as ISO 639 codes.",
            "items": {"type": "string"},
        },
        "links": {
            "type": "array",
            "description": "List of valid URLs (website, social media etc.) mentioned by the candidate.",
            "items": {"type": "string"},
        },
        "qualifications": {
            "type": "array",
            "description": "List of educational qualifications mentioned by the candidate sorted in descending order.",
            "items": {
                "type": "object",
                "properties": {
                    "degree": {
                        "type": "string",
                        "description": "Name of the degree which was achieved.",
                    },
                    "institution": {
                        "type": "string",
                        "description": "Name of the institution where this educational qualification was achieved.",
                    },
                    "started_at": {
                        "type": "string",
                        "description": "Start date of pursuing this educational qualification in YYYY-MM format.",
                    },
                    "ended_at": {
                        "type": "string",
                        "description": "End date of pursuing this educational qualification in YYYY-MM format."
                        "Exclude if not mentioned of currently pursuing.",
                    },
                },
                "required": ["degree", "institution"],
            },
        },
        "experiences": {
            "type": "array",
            "description": "List of work experiences mentioned by the candidate sorted in descending order.",
            "items": {
                "type": "object",
                "properties": {
                    "company": {
                        "type": "string",
                        "description": "Name of the company or organization.",
                    },
                    "designation": {
                        "type": "string",
                        "description": "Name of the role or designation at this company.",
                    },
                    "location": {
                        "type": "string",
                        "description": "Location of the company.",
                    },
                    "description": {
                        "type": "string",
                        "description": "Job description, responsibilities or project details while working here.",
                    },
                    "started_at": {
                        "type": "string",
                        "description": "Joining date at this company in in YYYY-MM format.",
                    },
                    "exited_at": {
                        "type": "string",
                        "description": "Leaving or exit date at this company in YYYY-MM format."
                        "Exclude if not mentioned of currently working.",
                    },
                    "skills": {
                        "type": "array",
                        "description": "List of skills learned or utilised while working here.",
                        "items": {"type": "string"},
                    },
                },
                "required": ["company", "designation", "from"],
            },
        },
    },
    "required": ["name"],
}
