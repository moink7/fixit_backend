
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


questions_data = {
    "Expenditure breakdown": "50/30/20 budget rule. This rule recommends dividing your after-tax income into three categories: 50% for needs, 30% for wants, and 20% for savings. Needs include essential living expenses like rent, bills, food, and transportation. Wants include discretionary spending like eating out, shopping, trips, and subscriptions.",
    "Tax proposals summary": "A 12.5% tax rate will be applied to long-term gains on all financial and non-financial assets. The exemption limit for capital gains on certain financial assets will be raised from ₹1 lakh to ₹1.25 lakh per year.",
    "Budget analysis overview": "Budget analysis is a way to evaluate a business's financial health by comparing its income and spending over a period of time. It can help business leaders make decisions about revenue and expenses, and identify areas for improvement.",
    "Disinvestment targets explained": "The divestment target is a specific financial goal set by the Indian government each fiscal year, indicating the amount it aims to raise through the process of divestment. This target is announced as part of the Union Budget",
}

class QuestionRequest(BaseModel):
    question: str


@app.post("/get-response")
def get_response(question_req: QuestionRequest):
    question = question_req.question
    response = questions_data.get(question, "Sorry, I don't have an answer for that.")
    return {"response": response}
