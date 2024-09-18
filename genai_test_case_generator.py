#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install openai


# In[4]:


import openai
print(openai.__version__)


# In[12]:


import openai
import os

# Get the API key from an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_test_cases(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" depending on your usage
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

prompt = "Generate test cases for login functionality"
test_cases = generate_test_cases(prompt)
print(test_cases)



# In[13]:


python generate_test_cases.py


# In[14]:


pip install openai==0.28


# In[15]:


pip install --upgrade openai


# In[16]:


import openai
import os

# Ensure you have set your API key correctly
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_test_cases(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # Or use "gpt-4" if supported
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

prompt = "Generate test cases for login functionality"
test_cases = generate_test_cases(prompt)
print(test_cases)


# In[17]:


pip install --upgrade openai


# In[18]:


import openai
print(openai.__version__)


# In[ ]:


import openai
import os

# Make sure you have set your API key correctly
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_test_cases(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if supported
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

prompt = "Generate test cases for login functionality"
test_cases = generate_test_cases(prompt)
print(test_cases)

