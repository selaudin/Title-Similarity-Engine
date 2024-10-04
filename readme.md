# Title Similarity Engine

This project is a backend API built using FastAPI, which finds the most similar title from a list of titles based on a
reference title. It uses a pre-trained sentence embedding model from HuggingFace (sentence-transformers) to compute
vector representations of titles and calculates the similarity using cosine similarity.

### Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard
  Python type hints.
- **HuggingFace Transformers**: Pre-trained NLP models to compute vector embeddings for text.
- **Cosine Similarity**: A method to find the most similar title by measuring the cosine similarity between embeddings.

### Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── utils.py
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

- **main.py**: The main entry point of the FastAPI app, defining routes and endpoints.
- **models.py**: Contains Pydantic models for request validation.
- **utils.py**: Utility functions, including the function to compute title similarity using a pre-trained HuggingFace
  model.
- **__init__.py**: Marks the app/ directory as a package.
- **poetry.lock**: Ensures that all developers and environments use the exact same versions of dependencies.

### Requirements

- Python 3.7+
- Poetry (for dependency management)

### Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/selaudin/Title-Similarity-Engine.git
    cd title-similarity-engine
   ```
2. Install Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Initialize the Project:

   ```
   poetry install
   ```

[//]: # (4. Add Dependencies:)
[//]: # ()
[//]: # (   ```)
[//]: # (   poetry add fastapi "uvicorn[standard]" sentence-transformers)
[//]: # (   ```)

4. Activate the virtual environment:

   ```
   poetry shell
   ```

### Usage

1. Run the FastAPI server:

   ```
   poetry run uvicorn app.main:app --reload
   ```
2. The API will be available at
    ```
    http://127.0.0.1:8000
    ```

3. Use **SwaggerUI** with interactive exploration, call and test the API directly from the browser.
    ```
    http://127.0.0.1:8000/docs
    ```

![Usage Example](https://github.com/selaudin/Title-Similarity-Engine/blob/main/media/usage.gif)

4. Or the alternative **Redoc** API documentation
    ```
    http://127.0.0.1:8000/redoc
    ```

### Endpoints

#### GET

- ```/```: A welcome message to the API.

#### POST

- ```/find-title-similarit```: This endpoint takes a JSON payload with a reference title and a list of other titles, and
  returns the most similar title.
    - Request Example:
  ```
   {
       "reference_title": "Higgs boson in particle physics",
       "other_titles": [
           "Best soup recipes",
           "Basel activities",
           "Particle physics at CERN"
       ]
   }
   ```
    - Response Example:
  ```
  {
      "top_result": "Particle physics at CERN"
  }
  ```

    - Run example in terminal using ```curl```
  ```
  curl -X POST "http://127.0.0.1:8000/find-title-similarity" \
  -H "Content-Type: application/json" \
  -d '{"reference_title": "Higgs boson in particle physics", "other_titles": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]}'
  ```
  
