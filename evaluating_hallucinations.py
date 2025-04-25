from openevals.llm import create_llm_as_judge
from openevals.prompts import HALLUCINATION_PROMPT
from dotenv import load_dotenv

load_dotenv()

evaluator = create_llm_as_judge(
    prompt = HALLUCINATION_PROMPT, 
    model = 'openai:o3-mini',
    feedback_key= "hallucination")


# test case 1
input =  " What is the capital of Germany"
context = " The capital of Germany is Berlin. Its a beautiful city"
output = "The capital is munich"
eval_result = evaluator(inputs=input, outputs=output,context=context,reference_outputs="")
print("test case 1", eval_result)

# test case 2 
input = "India's Mars Orbiter Mission, popularly called Mangalyaan, was launched in 2013. Which launch vehicle placed it into Earth orbit, and on what exact date?"
context = "The Mars Orbiter Mission (MOM) was launched aboard ISRO's PSLV-C25 rocket. Lift-off occurred on 5th November 2013 at 09:08 IST from the Satish Dhawan Space Centre on Sriharikota Island."
output = "Mangalyaan was launched on 5 November 2013 by the PSLV-C25 launch vehicle."
eval_result = evaluator(inputs= input, outputs=output,context=context,reference_outputs="")
print("test case 2", eval_result)
