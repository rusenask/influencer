#!/bin/bash

# This script runs every time your Studio starts, from your home directory.

# List files under fast_load that need to load quickly on start (e.g. model checkpoints).
#
# ! fast_load
# .ollama/models/blobs/sha256-2bada8a7450677000f678be90653b85d364de7db25eb5ea54136ada5f3933730
# .ollama/models/blobs/sha256-2f15b3218f0552c60647ce60ada83632d2c09755b16259b13e3e4458e9ae419d
# .ollama/models/blobs/sha256-66b9ea09bd5b7099cbb4fc820f31b575c0366fa439b08245566692c6784e281e
# .ollama/models/blobs/sha256-832dd9e00a68dd83b3c3fb9f5588dad7dcf337a0db50f7d9483f310cd292e92e
# .ollama/models/blobs/sha256-eb4402837c7829a690fa845de4d7f3fd842c2adee476d5341da8a46ea9255175
# .ollama/models/manifests/registry.ollama.ai/library/qwen2.5/latest
# bin/ollama

mkdir -p ~/log
~/bin/ollama serve > ~/log/ollama.log 2> ~/log/ollama.err &
