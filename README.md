# LLM Chat Generator

This script generates chat-like responses (10-40 words) using Google's Gemini API.

## Setup

1. **Get a Google API Key:**
   - Visit https://aistudio.google.com/apikey
   - Create a new API key (free tier available)

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure API key:**
   - Copy the example environment file:
   ```bash
   copy .env.example .env
   ```
   - Edit `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```

4. **Run the script:**
```bash
python main.py
```

5. **Enter your prompt** when asked (e.g., "Generate chat like response offering a young man opinion on football")

## Features

- Generates 10-40 word chat-like responses
- Uses Google Gemini 2.0 Flash Lite model
- Free tier available with rate limits
- Custom prompts via terminal input

## Rate Limits

The free tier has rate limits. If you get a `429 RESOURCE_EXHAUSTED` error, wait 30-60 seconds and try again. For more details, visit: https://ai.google.dev/gemini-api/docs/rate-limits

## Environment Variables

- `GOOGLE_API_KEY` - Your Google AI API key (required)
