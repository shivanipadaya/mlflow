import mlflow

# Register Hugging Face model in MLflow
mlflow.register_model(model_uri='huggingface_hub_model_uri', name='hf_model')

# Serve the model
mlflow.models.serve(model_uri='models:/hf_model/1', port=8000)
