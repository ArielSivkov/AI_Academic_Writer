from fastapi import APIRouter, Query
from models.text_generator import generate_paper
from models.citation_handler import check_citations
from models.plagiarism_checker import check_plagiarism
from models.feedback_analyzer import analyze_feedback

router = APIRouter()

@router.get("/generate-paper")
def generate_paper_endpoint(topic: str = Query(..., description="The topic of the academic paper")):
    paper = generate_paper(topic)
    return {"paper": paper}

@router.get("/check-citations")
def check_citations_endpoint(paper: str = Query(..., description="The academic paper to check citations for")):
    citations_valid = check_citations(paper)
    return {"citations_valid": citations_valid}

@router.get("/check-plagiarism")
def check_plagiarism_endpoint(paper: str = Query(..., description="The academic paper to check for plagiarism")):
    plagiarism_detected = check_plagiarism(paper)
    return {"plagiarism_detected": plagiarism_detected}

@router.get("/analyze-feedback")
def analyze_feedback_endpoint(paper: str = Query(..., description="The academic paper to analyze feedback for")):
    feedback = analyze_feedback(paper)
    return {"feedback": feedback}
