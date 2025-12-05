#!/usr/bin/env bash
set -euo pipefail

# Initialize and update all submodules.
git submodule update --init --recursive

echo "Submodules initialized."
