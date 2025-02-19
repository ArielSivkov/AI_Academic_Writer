# AI Academic Writer

This project aims to build an AI-powered academic writing assistant that helps generate structured academic papers, ensures correct citations, fixes writing errors, and provides real-time feedback.

## Project Structure

- `backend/`: Contains the backend code for the AI models and API.
  - `models/`: AI models for various tasks such as text generation, citation handling, and more.
  - `api/`: FastAPI entry point and routes for handling API requests.
  - `utils/`: Utility scripts for preprocessing and fetching sources.
  - `memory/`: AI's long-term knowledge storage and retrieval system.
  - `db/`: Database-related scripts for storing metadata and optimizing queries.
- `frontend/`: Contains the frontend code for the user interface.
  - `app.py`: Streamlit app for user interaction.
  - `dashboard.py`: Writing analytics and AI-generated insights.
  - `components/`: Modular UI components.
- `data/`: Contains user-uploaded documents and processed text data.
  - `uploads/`: User-uploaded documents.
  - `processed/`: AI-processed text data.
  - `high_scores/`: Storage of high-scoring academic papers.
  - `embeddings/`: Vector embeddings for memory.
- `models/`: Contains the AI models used in the project.
  - `llama3/`: Fine-tuned LLaMA 3 model.
  - `mistral/`: Alternative fine-tuned Mistral model.
  - `hebrew_bert/`: HeBERT model for Hebrew correction.
- `tests/`: Contains tests for the various components of the project.
  - `test_api.py`: API functionality tests.
  - `test_memory.py`: Memory retrieval/storage tests.
  - `test_grading.py`: Tests AI's ability to detect strong/weak points.
  - `test_feedback.py`: Tests AI's real-time feedback system.
  - `test_grade_prediction.py`: Ensures accuracy of grade predictor.
  - `test_citation_verification.py`: Tests AI’s ability to verify sources.
  - `test_plagiarism_checker.py`: Tests AI’s plagiarism detection.
  - `test_adaptive_grading.py`: Ensures AI adjusts writing to professor criteria.
- `scripts/`: Contains scripts for training models and setting up the database.
  - `train_model.py`: Fine-tunes the AI model.
  - `setup_db.py`: Initializes the database structure.
  - `optimize_embeddings.py`: Updates vector memory for efficiency.
- `config.py`: Global settings for the project.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables.
- `.gitignore`: Git version control ignore list.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (for frontend development)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI_Academic_Writer.git
    cd AI_Academic_Writer
    ```

2. Install the backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    ```bash
    cp .env.example .env
    # Edit .env to include your API keys and other settings
    ```

4. Initialize the database:
    ```bash
    python scripts/setup_db.py
    ```

5. Run the backend server:
    ```bash
    uvicorn backend.api.main:app --reload
    ```

6. Install the frontend dependencies and run the frontend server:
    ```bash
    cd frontend
    npm install
    npm start
    ```

### Usage

- Access the frontend at `http://localhost:3000`
- Use the API endpoints defined in `backend/api/routes.py`

### Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### original folder structure

AI_Academic_Writer/
│── backend/                    
│   ├── models/                  
│   │   ├── text_generator.py       # AI generates structured academic papers
│   │   ├── citation_handler.py     # Ensures correct citations & sources
│   │   ├── hebrew_corrector.py     # Fixes Hebrew writing errors (HeBERT)
│   │   ├── embeddings.py           # Creates text embeddings for AI memory
│   │   ├── ranking_model.py        # Ranks past papers based on scoring & credibility
│   │   ├── grading_analyzer.py     # Detects strong & weak points in papers
│   │   ├── feedback_analyzer.py    # Provides real-time feedback on writing quality
│   │   ├── grade_predictor.py      # Predicts expected academic score
│   │   ├── learning_optimizer.py   # AI learns from user feedback & improves
│   │   ├── explanation_generator.py # AI explains writing choices
│   │   ├── multilingual_handler.py  # Supports multiple languages in academic writing
│   │   ├── citation_verifier.py     # Checks citation validity
│   │   ├── plagiarism_checker.py    # Detects plagiarism
│   │   ├── editing_assistant.py     # AI reviews & suggests edits
│   │   ├── adaptive_grading.py      # AI adapts writing based on grading styles
│   │   ├── user_adaptation.py       # AI learns user-specific writing styles
│   ├── api/                        
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── routes.py               # Organized API routes (for clean structure)
│   │   ├── dependencies.py         # Middleware & shared services
│   ├── utils/                      
│   │   ├── preprocess.py           # Prepares input text for AI processing
│   │   ├── fetch_sources.py        # Searches academic sources online
│   │   ├── hebrew_normalizer.py    # Hebrew text normalization
│   ├── memory/                     # MEMORY SYSTEM (AI's Long-Term Knowledge)
│   │   ├── vector_memory.py        # FAISS/Pinecone vector memory
│   │   ├── structured_memory.py    # PostgreSQL stores structured knowledge
│   │   ├── grading_memory.py       # Saves high-scoring papers
│   │   ├── retrieval.py            # Smart retrieval of past knowledge
│   │   ├── ml_optimizer.py         # AI learns from corrections & improvements
│   ├── db/                         
│   │   ├── metadata_store.py       # Stores research questions & structure
│   │   ├── query_optimizer.py      # Improves search efficiency over time
│── frontend/                      
│   ├── app.py                      # Streamlit app for user interaction
│   ├── dashboard.py                 # Writing analytics & AI-generated insights
│   ├── components/                 # Modular UI components
│── data/                          
│   ├── uploads/                    # User-uploaded documents
│   ├── processed/                   # AI-processed text data
│   ├── high_scores/                 # Storage of high-scoring academic papers
│   ├── embeddings/                  # Vector embeddings for memory
│── models/                        
│   ├── llama3/                     # Fine-tuned LLaMA 3 model
│   ├── mistral/                    # Alternative fine-tuned Mistral model
│   ├── hebrew_bert/                # HeBERT model for Hebrew correction
│── tests/                         
│   ├── test_api.py                 # API functionality tests
│   ├── test_memory.py              # Memory retrieval/storage tests
│   ├── test_grading.py             # Tests AI's ability to detect strong/weak points
│   ├── test_feedback.py            # Tests AI's real-time feedback system
│   ├── test_grade_prediction.py    # Ensures accuracy of grade predictor
│   ├── test_citation_verification.py # Tests AI’s ability to verify sources
│   ├── test_plagiarism_checker.py  # Tests AI’s plagiarism detection
│   ├── test_adaptive_grading.py    # Ensures AI adjusts writing to professor criteria
│── scripts/                       
│   ├── train_model.py              # Fine-tunes the AI model
│   ├── setup_db.py                 # Initializes the database structure
│   ├── optimize_embeddings.py      # Updates vector memory for efficiency
│── config.py                        # Global settings (API keys, paths, configs)
│── requirements.txt                 # Python dependencies
│── README.md                        # Documentation
│── .env                             # Environment variables (secure API keys)
│── .gitignore                       # Git version control ignore list