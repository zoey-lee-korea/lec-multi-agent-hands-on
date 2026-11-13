"""세션 1 1단계: 실습 패키지와 API 키 확인"""
import os
import sys
from importlib.metadata import version

print("Python", sys.version.split()[0])

for package in ("langchain", "langgraph", "mcp", "tavily-python", "arize-phoenix"):
    print(package, version(package))
print({key: key in os.environ for key in ("MULTI_AGENT_OPENAI_API_KEY", "TAVILY_API_KEY")})

# [Result]
# @zoey-lee-korea ➜ /workspaces/lec-multi-agent-hands-on/research_agent (main) $ python check_env.py 
# Python 3.14.10
# langchain 1.4.4
# langgraph 1.2.14
# mcp 2.3.0
# tavily-python 0.8.5
# arize-phoenix 21.0.0
# {'MULTI_AGENT_OPENAI_API_KEY': True, 'TAVILY_API_KEY': True}