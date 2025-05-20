#!/bin/bash
# Placeholder build script for iOS projects
set -e
PROJECT_DIR=${1:-ios_project}
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Project directory $PROJECT_DIR does not exist" >&2
  exit 1
fi
# This command assumes a macOS environment with Xcode installed
xcodebuild -project "$PROJECT_DIR" -scheme "$PROJECT_DIR" -sdk iphonesimulator -configuration Debug build
