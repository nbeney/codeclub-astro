#!/usr/bin/env bash
#
# Check for broken links in the Astro site using linkchecker.
# Runs two passes:
#   1. Against the dev server (npm run dev)
#   2. Against the production build (npm run build && npm run preview)
#
# Prerequisites: linkchecker must be installed (e.g. via uvx)
#
# Usage:
#   ./check-broken-links.sh [OPTIONS]
#
# Options:
#   -p, --port PORT   Port to use (default: 4321)
#   -h, --help        Show this help message

set -euo pipefail
set -m  # Enable job control so background jobs get their own process group

# --- Defaults ---

PORT=4321

# --- Parse arguments ---

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        -h|--help)
            sed -n '/^# Usage:/,/^$/p' "$0" | sed 's/^# \?//'
            exit 0
            ;;
        *)
            echo "ERROR: Unknown option: $1"
            echo "Use -h or --help for usage information."
            exit 1
            ;;
    esac
done

# --- Derived variables ---

URL="http://localhost:${PORT}/codeclub-astro/"
LOG_DIR="$(dirname "$0")"
DEV_LOG="${LOG_DIR}/linkchecker-dev.log"
PREVIEW_LOG="${LOG_DIR}/linkchecker-preview.log"
DEV_ERRORS=0
PREVIEW_ERRORS=0

# --- Helper functions ---

cleanup() {
    if [[ -n "${SERVER_PID:-}" ]]; then
        echo "Stopping server (PID ${SERVER_PID})..."
        kill -- -"${SERVER_PID}" 2>/dev/null || kill "${SERVER_PID}" 2>/dev/null || true
        wait "${SERVER_PID}" 2>/dev/null || true
        unset SERVER_PID
    fi
}

trap cleanup EXIT

wait_for_server() {
    local max_attempts=30
    local attempt=0
    echo "Waiting for server on port ${PORT}..."
    while ! curl -s -o /dev/null "http://localhost:${PORT}/" 2>/dev/null; do
        attempt=$((attempt + 1))
        if [[ "${attempt}" -ge "${max_attempts}" ]]; then
            echo "ERROR: Server did not start within ${max_attempts} seconds."
            exit 1
        fi
        sleep 1
    done
    echo "Server is ready."
}

run_linkchecker() {
    local log_file="$1"
    echo "Running linkchecker, saving output to ${log_file}..."
    uvx linkchecker "${URL}" \
        --no-warnings \
        --ignore-url "/dummy/" \
        -o text 2>&1 | tee "${log_file}" || true
    echo ""
}

count_errors() {
    local log_file="$1"
    local count
    count=$(grep -oP '\d+(?= errors found)' "${log_file}" 2>/dev/null || echo "0")
    echo "${count}"
}

# --- Pre-flight check ---

if ss -tlnp "sport = :${PORT}" 2>/dev/null | grep -q LISTEN; then
    echo "ERROR: Port ${PORT} is already in use. Please stop whatever is running on it first."
    exit 1
fi

# --- Pass 1: Dev server ---

echo "=========================================="
echo " Pass 1: Dev server (npm run dev)"
echo "=========================================="

npm run dev &
SERVER_PID=$!
wait_for_server
run_linkchecker "${DEV_LOG}"
DEV_ERRORS=$(count_errors "${DEV_LOG}")
cleanup

# --- Pass 2: Production build + preview ---

echo "=========================================="
echo " Pass 2: Production (npm run build && npm run preview)"
echo "=========================================="

npm run build
npm run preview &
SERVER_PID=$!
wait_for_server
run_linkchecker "${PREVIEW_LOG}"
PREVIEW_ERRORS=$(count_errors "${PREVIEW_LOG}")
cleanup

# --- Summary ---

echo "=========================================="
echo " Summary"
echo "=========================================="
echo "Dev log:     ${DEV_LOG} (${DEV_ERRORS} errors)"
echo "Preview log: ${PREVIEW_LOG} (${PREVIEW_ERRORS} errors)"

TOTAL_ERRORS=$((DEV_ERRORS + PREVIEW_ERRORS))
if [[ "${TOTAL_ERRORS}" -gt 0 ]]; then
    echo ""
    echo "FAILED: ${TOTAL_ERRORS} broken link(s) found."
    exit 1
else
    echo ""
    echo "OK: No broken links found."
fi
