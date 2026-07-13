def generate_candidate_identity(candidate_number: int) -> dict:
    """ 
    to generate anonymous candidate identity details.

    args: candidate_number: sequential candidate number
    returns: dictionary cantaining anynomous information.
    """
    candidate_suffix = f"{candidate_number:04d}"
    return {
        "candidate_id": f"Candidate_{candidate_suffix}",
        "email": f"candidate{candidate_suffix}@resumeiq.dev",
        "phone": f"+91 90000 0{candidate_suffix}",
        "github": f"guthub.com/in/candidate{candidate_suffix}",
        "linkedin": f"linkedin.com/in/candidate{candidate_suffix}",
        "location": "Banglore, India",
    }