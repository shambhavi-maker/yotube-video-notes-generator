# YouTube Subtitle to Study Notes Generator

## Overview

This application leverages Streamlit and Google's Gemini 2.0 Flash generative AI model to create study notes from YouTube video subtitles. The subtitles can be in Hindi, English, or Hinglish, but the generated study notes will always be in English.

## Features

- Converts YouTube subtitles into structured study notes
- Supports subtitles in Hindi, English, or Hinglish
- Uses Google Gemini AI to process and generate high-quality notes
- Interactive Streamlit-based UI for easy user experience

## Installation

To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/your-repo.git
cd your-repo
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Enter your Google Gemini API key.
3. Provide the YouTube video URL.
4. Select the subtitle language.
5. Fetch subtitles and generate study notes.

## API Key Setup

Ensure that you have set up the `GEMINI_API_KEY` as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## How It Works

1. The application fetches subtitles from the provided YouTube video.
2. A structured prompt is created to ensure notes are generated in English.
3. The processed subtitle data is fed into the Google Gemini 2.0 Flash model.
4. The AI generates structured study notes based on the subtitles.
5. Notes are displayed on the Streamlit interface for easy access and download.

## Error Handling

- If the Gemini model initialization fails, users will receive an appropriate error message.
- If subtitles cannot be processed, the application will notify the user and provide possible solutions.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with enhancements or bug fixes.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [LangChain](https://www.langchain.com/)
```
