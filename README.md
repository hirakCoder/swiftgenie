# SwiftGenie

SwiftGenie is an experimental platform for generating iOS applications from chat-based prompts. The goal is to automate code generation, testing, and launching iOS apps using Swift and SwiftUI, following Apple's best practices.

## MVP Overview

This repository contains a minimal proof-of-concept with a Python-based API server. The server relies on OpenAI's API to produce Swift code snippets in response to user prompts. A placeholder build script is provided for compiling the generated project using Xcode.

### Components

- **server/** – FastAPI application exposing a `/generate` endpoint to transform chat prompts into Swift code via the OpenAI API.
- **scripts/build.sh** – Example shell script to run `xcodebuild` on macOS. Requires Xcode command-line tools.
- **requirements.txt** – Python dependencies for the API server.
- Jinja2 templates power the optional web UI and are included in `requirements.txt`.

### Running the API

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key and (optionally) the model name:
   ```bash
   export OPENAI_API_KEY=your-key
   export OPENAI_MODEL=gpt-3.5-turbo  # defaults to gpt-4
   ```
3. Launch the server:
   ```bash
   uvicorn server.main:app --reload
   ```

### Running tests

Install the dev dependencies and run pytest:

```bash
pip install -r requirements.txt
pytest -q
```

### Building iOS projects

The `scripts/build.sh` script assumes a macOS environment with Xcode installed. Pass the path to your Xcode project as the first argument:

```bash
./scripts/build.sh path/to/MyApp
```

## Roadmap

1. **Chat-based interaction:** Expand the API to maintain conversation history and manage multiple user sessions.
2. **Project management:** Store generated code in a per-user directory with Git version control.
3. **Automated testing:** Run `xcodebuild test` and parse results to automatically suggest fixes.
4. **Simulator streaming:** Provide a web interface to launch and view the iOS Simulator from the browser.
5. **Extensibility:** Design services so Android support can be added later with minimal changes.

This MVP serves as a foundation for further development and experimentation.
