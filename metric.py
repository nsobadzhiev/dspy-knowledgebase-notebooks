from dspy import Signature, InputField, OutputField, context, OllamaLocal, Predict


class Assess(Signature):
    """Assess the quality of an answer to the specified question."""

    assessed_text = InputField()
    assessment_question = InputField()
    assessment_answer = OutputField(desc="Yes or No")


def metric(gold, pred, trace=None):
    question, answer, prediction_answer = gold.question, gold.answer, pred.answer

    correct = f"The text should answer `{question}` with `{answer}`. Does the assessed text contain this answer?"
    
    # TODO: it's Mistral evaluating Mistral - it would be better to use another one
    mistral = OllamaLocal(model='mistral')
    with context(lm=mistral):
        correct =  Predict(Assess)(assessed_text=prediction_answer, assessment_question=correct)

    correct = correct.assessment_answer.lower() == 'yes'
    score = correct if correct and (len(prediction_answer) <= 280) else 0

    if trace is not None: return score >= 2
    return score / 2.0
