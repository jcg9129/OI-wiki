#!/usr/bin/env bash
# Entry point for the dev container (Dockerfile.dev): prepare just enough to run
# MkDocs against the mounted working tree, then serve with live reload.
#
# Every step is idempotent and guarded so restarts are fast: the theme submodule
# and vendored MathJax are only fetched when missing, and `uv sync` is a no-op
# once the (volume-persisted) .venv is in place.
set -euo pipefail

# 1. Custom Material theme (git submodule referenced by mkdocs.yml custom_dir).
if [[ ! -f mkdocs-material/material/templates/base.html ]]; then
  echo "==> Fetching theme submodule (mkdocs-material)"
  git submodule update --init --depth=1 mkdocs-material
fi

# 2. Vendored MathJax so formulas render. Non-fatal: the site still serves
#    without it (math just won't render), which is fine when offline.
if [[ ! -d mkdocs-material/material/templates/assets/vendor/mathjax ]]; then
  echo "==> Vendoring MathJax assets"
  scripts/pre-build/install-theme-vendor.sh || echo "!! MathJax vendor step failed (offline?); serving without rendered math"
fi

# 3. Python dependencies (includes mkdocs-static-i18n from uv.lock).
echo "==> Syncing Python dependencies"
uv sync

# 4. Serve on all interfaces so the port publish reaches the host.
echo "==> Starting mkdocs serve on http://0.0.0.0:8000 (zh at /, English at /en/)"
exec uv run mkdocs serve -a 0.0.0.0:8000
