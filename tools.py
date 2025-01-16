## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

#refer from crew ai documentation 
from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities and use it in agents.py file and tasks.py for writer agent  
tool = SerperDevTool()