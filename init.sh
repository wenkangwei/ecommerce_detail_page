#!/bin/bash
# ============================================================
# Development Server Init Script
# ============================================================
# Starts both backend (FastAPI) and frontend (Vite) servers.
#
# Usage:
#   chmod +x init.sh
#   ./init.sh           # Start servers
#   ./init.sh stop      # Stop servers
#   ./init.sh restart   # Restart servers
# ============================================================
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_PORT=8000
FRONTEND_PORT=5173
PID_DIR="$PROJECT_DIR/.pids"

stop_servers() {
    echo "Stopping servers..."
    if [ -f "$PID_DIR/backend.pid" ]; then
        kill "$(cat "$PID_DIR/backend.pid")" 2>/dev/null || true
        rm "$PID_DIR/backend.pid"
    fi
    if [ -f "$PID_DIR/frontend.pid" ]; then
        kill "$(cat "$PID_DIR/frontend.pid")" 2>/dev/null || true
        rm "$PID_DIR/frontend.pid"
    fi
    rm -rf "$PID_DIR"
    echo "Servers stopped."
}

start_servers() {
    echo "Starting development servers..."
    mkdir -p "$PID_DIR"

    # --- Backend ---
    echo "Starting backend on port $BACKEND_PORT..."
    cd "$PROJECT_DIR/backend"
    if [ -d ".venv" ]; then
        source .venv/bin/activate
    fi
    uvicorn app.main:app --host 0.0.0.0 --port $BACKEND_PORT --reload &
    echo $! > "$PID_DIR/backend.pid"

    # --- Frontend ---
    echo "Starting frontend on port $FRONTEND_PORT..."
    cd "$PROJECT_DIR/frontend"
    npx vite --port $FRONTEND_PORT &
    echo $! > "$PID_DIR/frontend.pid"

    # Wait for servers to be ready
    echo "Waiting for servers to be ready..."
    sleep 3

    echo ""
    echo "========================================="
    echo "  Development servers started!"
    echo "========================================="
    echo "  Backend:   http://localhost:$BACKEND_PORT"
    echo "  Frontend:  http://localhost:$FRONTEND_PORT"
    echo "  API Docs:  http://localhost:$BACKEND_PORT/docs"
    echo "========================================="
    echo ""
    echo "To stop: ./init.sh stop"
}

case "${1:-start}" in
    start)   start_servers ;;
    stop)    stop_servers ;;
    restart) stop_servers; sleep 1; start_servers ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
