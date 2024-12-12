from fastapi import FastAPI
from app.models.templates import IncomingTemplate, Template

app = FastAPI()


@app.post('/get_form')
async def get_form(form: IncomingTemplate):
    result = form.find_matching_tempalte()
    if isinstance(result, str):
        return {'template_name': result}
    return result


@app.post("/create_template")
async def create_template(template: Template):
    return {"name": template.name, "fields": template.fields}