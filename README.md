# CrewAI 101: Building Multi-Agent Systems for Real-World Use Cases
This repository demonstrates how to create and utilize multiple AI agents for complex tasks using the CrewAI framework. The example focuses on automating the creation of blog posts from existing YouTube videos.

## Project Overview
- **Goal**: Automate the creation of blog posts from YouTube video content.
- **Approach**: Utilize CrewAI to orchestrate a team of AI agents:
  - **Researcher**: Analyzes YouTube videos, extracts key information, and summarizes content.
  - **Writer**: Transforms the summarized information into a compelling blog post.
- **Key Concepts**:
  - **Agents**: Represent individual AI-powered entities with specific roles and capabilities.
  - **Tasks**: Define the specific actions or objectives for each agent.
  - **Tools**: Integrate external services or libraries to assist agents in their tasks (e.g., YouTube API for video retrieval).
  - **Workflows**: Define the sequence or hierarchy of interactions between agents.

## Project Structure
- `agents.py`: Defines the Researcher and Writer agents, specifying their roles, goals, and associated LLM models.
- `tools.py`: Defines the `YouTubeSearchTool` for interacting with the YouTube API.
- `tasks.py`: Defines the `ResearchTask` and `WritingTask`, outlining the objectives and expected outputs for each agent.
- `crew.py`: Orchestrates the workflow, defining the sequence of tasks and the agents responsible for executing them.

## Getting Started
### Prerequisites

- Create a virtual environment 
- Install required libraries:
  pip install crewai langchain langchain-google_genai load-dotenv
- Obtain an Google API key and set it as an environment variable

### Run the example
python crew.py

This will trigger the following sequence:

- The Researcher agent analyzes a specified YouTube video.
- The Writer agent generates a blog post based on the Researcher's findings.
- The output will be a new Markdown file (new_blog_post.md) containing the generated blog post.

## Key Considerations
- LLM Integration: The example utilizes Google Gemini and AWS Nova models. You can explore other LLM options as well 
- Workflow Customization: Experiment with different agent configurations, task definitions, and workflows to optimize performance and explore new creative possibilities.
- Tool Integration: Integrate additional tools, such as sentiment analysis APIs or summarization tools, to enhance the capabilities of your agents.

## Acknowledgements
[Krish Naik](https://www.youtube.com/watch?v=UV81LAb3x2g&t=1704s)



