#!/usr/bin/env bash
# ============================================================
# E-Commerce Detail — Auto Runner (Agent Harness Paradigm)
# ============================================================
# Automatically reads feature_list.json and executes features
# one by one via claude -p.
#
# Usage:
#   ./auto_run.sh              # Run all pending features
#   ./auto_run.sh --status     # Show progress
#   ./auto_run.sh --dry-run    # Show pending features
#   ./auto_run.sh --help       # Show help
# ============================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
FEATURE_FILE="$PROJECT_DIR/feature_list.json"
PROGRESS_FILE="$PROJECT_DIR/claude-progress.txt"
SESSION_COUNT=0
MAX_SESSIONS=50
COMPRESS_EVERY=3

cd "$PROJECT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log()  { echo -e "${BLUE}[$(date '+%H:%M:%S')]${NC} $*"; }
ok()   { echo -e "${GREEN}[OK]${NC} $*"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
err()  { echo -e "${RED}[ERROR]${NC} $*" >&2; }

# ---------- helpers ----------
next_feature() {
    python3 -c "
import json, sys
with open('$FEATURE_FILE') as f:
    data = json.load(f)
unpassed = [f for f in data['features'] if not f['passes']]
unpassed.sort(key=lambda x: x['priority'])
if unpassed:
    f = unpassed[0]
    print(json.dumps(f, ensure_ascii=False))
else:
    print('ALL_DONE')
"
}

count_remaining() {
    python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
print(sum(1 for f in data['features'] if not f['passes']))
"
}

total_features() {
    python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
print(len(data['features']))
"
}

mark_passed() {
    local fid="$1"
    python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
for f in data['features']:
    if f['id'] == '$fid':
        f['passes'] = True
with open('$FEATURE_FILE', 'w') as out:
    json.dump(data, out, ensure_ascii=False, indent=2)
"
}

show_status() {
    python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
features = data.get('features', [])
total = len(features)
passing = sum(1 for f in features if f.get('passes'))
pct = (passing / total * 100) if total > 0 else 0

print(f'  Project: {data.get(\"project\", \"?\")}')
print(f'  Features: {passing}/{total} passing ({pct:.1f}%)')
print()
bar_len = 40
filled = int(bar_len * pct / 100)
bar = '█' * filled + '░' * (bar_len - filled)
print(f'  [{bar}] {pct:.1f}%')
print()
next_features = [f for f in features if not f.get('passes')]
next_features.sort(key=lambda x: x.get('priority', 99))
if next_features:
    print('  Next features:')
    for f in next_features[:5]:
        print(f'    [{f[\"id\"]}] P{f.get(\"priority\",\"?\")} — {f[\"description\"][:70]}')
    if len(next_features) > 5:
        print(f'    ... and {len(next_features) - 5} more')
else:
    print('  ALL FEATURES COMPLETE!')
"
}

build_prompt() {
    local fid="$1" desc="$2" steps="$3"
    cat <<PROMPT
You are the Coding Agent for the ecommerce-detail project.

## Context
- Read CLAUDE.md for project conventions
- Read claude-progress.txt for what previous sessions did
- Read feature_list.json for the full roadmap
- Project directory: $PROJECT_DIR

## Your Task
Implement feature **$fid**: $desc

## Acceptance Criteria
$steps

## Protocol
1. First read CLAUDE.md and the last 20 lines of claude-progress.txt
2. Read relevant existing source files to understand current state
3. Implement ONLY this feature — do not touch other features
4. Run tests:
   - Backend: \`cd $PROJECT_DIR/backend && source .venv/bin/activate && python -m pytest tests/ -x --tb=short -v 2>&1 | tail -30\`
   - Frontend: \`cd $PROJECT_DIR/frontend && npx tsc --noEmit 2>&1\`
5. If tests pass, update feature_list.json: set this feature's passes to true
6. Git commit: "feat($fid): brief description"
7. Append session notes to claude-progress.txt

## Rules
- Follow CLAUDE.md strictly
- If existing tests broken, FIX them first
- If you need human input, output: NEEDS_HUMAN: <reason>
- Do NOT modify features other than $fid
- Keep changes minimal and focused
PROMPT
}

# ---------- commands ----------
cmd_status() {
    log "=== E-Commerce Detail — Project Status ==="
    show_status
    if [[ -f "$PROGRESS_FILE" ]]; then
        echo ""
        log "Recent progress:"
        tail -15 "$PROGRESS_FILE" | sed 's/^/  /'
    fi
}

cmd_dry_run() {
    log "=== E-Commerce Detail — Dry Run ==="
    TOTAL=$(total_features)
    REMAINING=$(count_remaining)
    log "Total: $TOTAL, Remaining: $REMAINING"
    echo ""

    python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
unpassed = [f for f in data['features'] if not f['passes']]
unpassed.sort(key=lambda x: x['priority'])
for i, f in enumerate(unpassed, 1):
    print(f'  {i}. [{f[\"id\"]}] P{f.get(\"priority\",\"?\")} — {f[\"description\"][:80]}')
"
    echo ""
    log "Would execute $REMAINING sessions"
}

# ---------- main loop ----------
cmd_run() {
    log "=== E-Commerce Detail — Auto Runner ==="
    TOTAL=$(total_features)
    log "Total features: $TOTAL, Remaining: $(count_remaining)"

    while [ "$SESSION_COUNT" -lt "$MAX_SESSIONS" ]; do
        FEATURE_JSON=$(next_feature)

        if [ "$FEATURE_JSON" = "ALL_DONE" ]; then
            ok "ALL FEATURES COMPLETE!"
            break
        fi

        FID=$(echo "$FEATURE_JSON" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")
        DESC=$(echo "$FEATURE_JSON" | python3 -c "import json,sys; print(json.load(sys.stdin)['description'])")
        STEPS=$(echo "$FEATURE_JSON" | python3 -c "
import json, sys
f = json.load(sys.stdin)
print('\n'.join(f'- {s}' for s in f.get('steps', [])))
")

        SESSION_COUNT=$((SESSION_COUNT + 1))
        REMAINING=$(count_remaining)
        log "--- Session $SESSION_COUNT | $FID | Remaining: $REMAINING/$TOTAL ---"
        log "Feature: $DESC"

        # Build prompt
        PROMPT_FILE="/tmp/ecommerce_detail_prompt_${FID}.txt"
        build_prompt "$FID" "$DESC" "$STEPS" > "$PROMPT_FILE"

        # Execute claude
        log "Starting claude -p for $FID..."
        if claude -p "$(cat "$PROMPT_FILE")" \
             --allowedTools "Read,Edit,Write,Bash,Glob,Grep,Agent" \
             --output-format text 2>&1 | tee "/tmp/ecommerce_detail_output_${FID}.log"; then
            log "$FID completed"
        else
            log "$FID had errors — checking if feature was still implemented"
        fi

        # Check if feature was marked as passed
        PASSED=$(python3 -c "
import json
with open('$FEATURE_FILE') as f:
    data = json.load(f)
for f in data['features']:
    if f['id'] == '$FID':
        print('true' if f['passes'] else 'false')
        break
")

        if [ "$PASSED" = "true" ]; then
            ok "$FID PASSED"
        else
            warn "$FID NOT PASSED — retrying once"
            claude -p "$(cat "$PROMPT_FILE")

IMPORTANT: Previous attempt did not mark this feature as passed. Focus on getting tests to pass. If blocked, output NEEDS_HUMAN." \
                 --allowedTools "Read,Edit,Write,Bash,Glob,Grep,Agent" \
                 --output-format text 2>&1 | tee "/tmp/ecommerce_detail_output_${FID}_retry.log"
        fi

        # Check for human input needed
        if grep -q "NEEDS_HUMAN" "/tmp/ecommerce_detail_output_${FID}.log" 2>/dev/null; then
            warn "NEEDS HUMAN INPUT — stopping"
            grep "NEEDS_HUMAN" "/tmp/ecommerce_detail_output_${FID}.log"
            break
        fi

        # Periodic compression
        if [ $((SESSION_COUNT % COMPRESS_EVERY)) -eq 0 ]; then
            log "Compressing progress log"
            python3 -c "
lines = open('$PROGRESS_FILE').readlines()
if len(lines) > 60:
    with open('$PROGRESS_FILE', 'w') as f:
        f.writelines(lines[:5])
        f.write('... (earlier sessions compressed) ...\n\n')
        f.writelines(lines[-50:])
"
        fi

        # Git save point
        if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
            log "Saving uncommitted changes..."
            git add -A
            git commit -m "wip: after $FID session" --allow-empty
        fi

        log "Session $SESSION_COUNT done. Remaining: $(count_remaining)/$TOTAL"
        echo ""
    done

    log "=== Auto Runner Finished ==="
    log "Sessions: $SESSION_COUNT, Remaining: $(count_remaining)/$TOTAL"
}

# ---------- main ----------
case "${1:-run}" in
    --status|-s|status)   cmd_status ;;
    --dry-run|-d|dryrun)  cmd_dry_run ;;
    --continue|-c|run)    cmd_run ;;
    run)                  cmd_run ;;
    --help|-h|help)
        echo "E-Commerce Detail — Auto Runner"
        echo ""
        echo "Usage:"
        echo "  ./auto_run.sh              Run all pending features"
        echo "  ./auto_run.sh --status     Show progress"
        echo "  ./auto_run.sh --dry-run    Show pending features"
        echo "  ./auto_run.sh --help       Show this help"
        ;;
    *)
        echo "Unknown option: $1"
        echo "Use --help for usage"
        exit 1
        ;;
esac
