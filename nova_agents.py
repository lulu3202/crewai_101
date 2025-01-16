from crewai import LLM, Agent, Crew, Task
from tools import tool
from dotenv import load_dotenv
import os
import boto3
from langchain_aws import ChatBedrockConverse

# Load environment variables
load_dotenv()

# Configure AWS session (optional if using credentials profile)
aws_session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION", "us-west-2")  # Default region: us-east-1
)

# Configure Nova Pro as the LLM from Bedrock
llm = LLM(
    model="bedrock/us.amazon.nova-pro-v1:0",
    temperature=0.3,  # Nova Pro works well with lower temperature for focused responses
    max_tokens=2000,  # Adjust based on your needs
)

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing news blogs
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
