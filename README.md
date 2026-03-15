# LLM-based Question Generator

A lightweight LLM-powered application that generates multiple-choice questions automatically from a given text input.

## Overview

This project is designed to transform raw educational text into structured quiz content.  
It reads a text file, sends the content to a large language model, parses the response, validates the generated questions, and saves the output in JSON format.

The project was built as a simple but practical example of:
- prompt-based question generation
- structured JSON parsing
- response validation
- API integration with Gemini
- educational content automation

## Features

- Generates multiple-choice questions from text
- Produces answer choices, correct answers, and explanations
- Validates model output before saving
- Exports generated questions as JSON
- Uses Gemini API for live content generation

## Project Structure

```text
.
├── app.py
├── prompt_builder.py
├── validator.py
├── sample_texts/
│   └── biyoloji.txt
├── outputs/
│   └── sorular.json
└── .env