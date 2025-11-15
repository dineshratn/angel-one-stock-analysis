# ---- Builder Stage ----
FROM python:3.12-slim-bookworm AS builder

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.1.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock* ./
COPY src/ ./src/

# Install dependencies (no-root to skip package install)
RUN poetry install --only main --no-interaction --no-ansi --no-root

# ---- Final Stage ----
FROM python:3.12-slim-bookworm AS final

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/src ./src/

# Copy environment file (optional - can be mounted at runtime)
COPY .env* ./

# Run the MCP server
CMD ["python", "-m", "src.stock_analysis.main"]
