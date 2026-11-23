# LLM Compatibility Scanner (TUI)

Automatically detects your PC's hardware and tells you exactly which local LLMs you can run - and how well.

![PC LLM Compatibility Scanner TUI](preview.png)

## Features

- **Hardware detection** - CPU, RAM, GPU (VRAM), disk space
- **63 LLM catalogue** - Gemma 4, Qwen3.5/3.6/3.8, Llama, DeepSeek-R1, Phi-4, Mistral, Granite, Nemotron, gpt-oss and more
- **5-tier rating system** - Excellent / Good / Possible / Slow / No-Go
- **Run mode** - GPU, CPU, partial GPU offload
- **Ollama commands** - copy-paste ready `ollama run` commands
- **Interactive TUI** - two-pane Textual UI with live filter and model detail popup
- **Export** - save results as JSON

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Interactive TUI (recommended)
python ui.py

# CLI one-shot
python main.py
```

## TUI

```bash
python ui.py
```

| Key | Action |
|-----|--------|
| `r` | Rescan hardware |
| `e` | Export results to JSON |
| `q` | Quit |
| `Enter` | Open model detail popup |
| `↑ ↓` | Navigate model list |
| Filter buttons | Filter by tier |

## CLI Usage

```bash
# Full table with top 5 picks
python main.py

# Top 10 runnable models
python main.py --top 10

# Hide models that won't run
python main.py --hide-nogo

# Only EXCELLENT tier
python main.py --tier EXCELLENT

# Detailed info for a specific model
python main.py --detail "Llama 3.1 8B"

# Export to JSON
python main.py --export-json results.json
```

## Compatibility Tiers

| Tier | Condition | Expected speed |
|------|-----------|----------------|
| 🚀 EXCELLENT | Fits in GPU VRAM with headroom | 20–80 tok/s |
| ✅ GOOD | Fits in GPU VRAM (tight) | Full GPU speed |
| ⚡ POSSIBLE | Partial GPU offload or CPU with plenty of RAM | 2–10 tok/s |
| 🐌 SLOW | CPU-only, RAM is tight | < 2 tok/s |
| ❌ NO-GO | Insufficient RAM and VRAM | Cannot load |

## Supported Models

| Family | Models |
|--------|--------|
| Llama | 3.2 1B, 3.2 3B, 3.1 8B, 3.3 70B, 3.1 405B, 4 Scout, 4 Maverick |
| Qwen | Qwen3.8 27B, Qwen3.6 27B/35B-A3B, Qwen3.5 0.8B/2B/4B/9B/27B/35B-A3B/122B-A10B, Qwen3 0.6B/4B/8B/14B/32B, Qwen3 30B-A3B, Qwen3-Coder 30B-A3B, Qwen3 235B-A22B, Qwen2.5-Coder 7B |
| Gemma | Gemma 4 E2B/E4B/12B/26B-A4B/31B, Gemma 3 1B/4B/12B/27B |
| Mistral | Medium 3.5 128B, Devstral 2 123B, Ministral 3 3B/8B/14B, Small 3.1 24B, Nemo 12B, 7B, Mixtral 8x7B |
| Phi | Phi-4 Mini 3.8B, Phi-4 14B |
| DeepSeek | R1 Distill 7B/14B/32B/70B, R1 671B |
| gpt-oss | 20B, 120B |
| Granite (IBM) | 4.2 3B/8B/30B |
| Nemotron (NVIDIA) | 3.5 Lightning 30B-A3B, 3.5 Super 120B-A12B |
| Others | Muse Glimmer 30B (Meta), GLM-4.7 Flash 30B (Z.ai), North Mini Code 30B-A3B (Cohere), Inkling 2 Mini 26B-A5B (Thinking Machines), LFM3 1.7B (Liquid AI) |

## Requirements

- Python 3.9+
- NVIDIA GPU (any OS): `nvidia-smi` must be on PATH for accurate VRAM detection
- Windows AMD/Intel GPU: detected via WMI (VRAM may show 4 GB cap on large cards due to WMI 32-bit overflow)
- Linux AMD GPU: `rocm-smi` on PATH for accurate VRAM detection, otherwise the GPU is listed with VRAM unknown (via `lspci`)
- macOS: detected via `system_profiler`; Apple Silicon GPUs report system RAM as VRAM (unified memory)

## Testing

```bash
pip install -r requirements-dev.txt
pytest
```

## How It Works

1. `scanner/hardware.py` - detects CPU, RAM, GPU, storage via `psutil`, `py-cpuinfo`, `nvidia-smi`/`rocm-smi`/`system_profiler`, and Windows WMI
2. `scanner/llm_database.py` - catalogue of 63 models with Q4_K_M quantised VRAM/RAM requirements
3. `scanner/recommender.py` - scores each model against your hardware and assigns a tier
4. `scanner/display.py` - renders results with `rich` for the CLI view
5. `ui.py` - interactive Textual TUI with live hardware panel, filterable model table, and detail popups

## Author

Chamalka Lakshan
