# Health Assistant

The Health Assistant application leverages cutting-edge language models and natural language processing techniques to provide users with information on health, nutrition, diseases, symptoms, causes, and treatments. Built using the LangChain library and Streamlit, this tool accesses a wealth of medical knowledge encoded in a CSV dataset to answer user queries in an intuitive web interface.

## Features

- **User Query Processing**: Users can input health-related questions, receiving detailed answers.
- **Advanced Retrieval**: Utilizes a FAISS vector store for efficient document retrieval from a CSV dataset.
- **Intelligent Response Generation**: Employs OpenAI's models to generate responses, ensuring relevance and accuracy.
- **Customizable Prompt Template**: Tailors responses to focus on health, nutrition, and disease-related information.

## How It Works

1. **Data Preparation**: Loads a CSV file containing medical data, including symptoms, causes, and treatments of various diseases.
2. **Document Embedding and Indexing**: Creates embeddings for the CSV data and indexes these for fast retrieval.
3. **Question Processing and Answering**: Processes user queries, retrieves relevant documents, and generates responses based on a custom prompt template.

## Prerequisites

- Python 3.6+
- Streamlit
- LangChain
- OpenAI API Key
- A CSV dataset of medical information

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   ```bash
   export GOOGLE_API_KEY='your_api_key_here'
   ```
4. Adjust the file path in the script to point to your CSV dataset.

## Running the Application

Execute the Streamlit application with:
```bash
streamlit run app.py
```
Navigate to the provided URL to interact with the Health Assistant.

## Contributing

Contributions to enhance the Health Assistant, expand its dataset, or improve its functionalities are welcome. Please submit pull requests with your proposed changes.

## License

This project is made available under the MIT License. See the LICENSE file for more information.

## Acknowledgments

- The LangChain library for providing the tools to build this application.
- OpenAI for their language models and embeddings.

---
