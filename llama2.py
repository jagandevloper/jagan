from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/p3avjf43as4h/llama-2/workflows/workflow-6808dd"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="4fc03539106b44c99555f536eb2e3432"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
