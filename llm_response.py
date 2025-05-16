import streamlit as st  
import google.generativeai as genai
from langchain.prompts import PromptTemplate
            
def llm_generator(subtitles, api_key):
    
    """Calling LLM and Generate Study Notes from the Subtitles"""
    # Configure
    if api_key:
        genai.configure(api_key=api_key)
    else:
        st.error("Please set the GEMINI_API_KEY environment variable.")

    try:
        # For multi-modal (text+image) tasks, you'd use 'gemini-pro-vision'

        llm = genai.GenerativeModel('gemini-2.0-flash')
    except Exception as e:
        st.error(f"Failed to initialize the Generative Model: {e}")
        st.warning("Please check your GOOGLE_API_KEY and ensure the Gemini 2.0 Flash model is available in your region.")
        st.stop()

    # Create a prompt template
    prompt = PromptTemplate(
        inputs=['subtitles'],
        template='''
        
        Here You have to make a study note from the below YouTube video subtitles. These subtitles mostly come in two languages: Hindi and English, and sometimes Hinglish.
        But you have to make notes in English only. The video subtitles are given below:

        {subtitles}
        '''
    )
    
    #chain = prompt | llm
    
    try:
        llm_output= prompt.format(subtitles=subtitles)
        response= llm.generate_content(llm_output)
            #prompt=llm_output,
            #max_output_tokens=1000,
            #temperature=0.5,
            #top_p=0.9,
            #top_k=40,
            #stop_sequences=["\n\n"]        
        return response.text
    
    except Exception as e:

        return f"Exception occurred at {e}"

