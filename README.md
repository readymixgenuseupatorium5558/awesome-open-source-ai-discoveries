# Awesome Open-Source AI Discoveries

Explore creative open-source AI projects for 3D, images, video, music, speech and documents, with upstream examples, setup notes and limitations.

**15 curated entries** · [Browse by task](#browse-by-task) · [Suggest a project](https://github.com/QuicqDev/awesome-open-source-ai-discoveries/issues/new?template=suggest-project.yml) · [JSON catalog](catalog.json) · [Agent index](llms.txt)

Find projects whose result is easy to understand: an image becomes a 3D object, a recording becomes editable notes, or a drawing becomes an animation. Discoveries are editorial picks, not a ranking by stars or a claim that every project is new. Research demos and archived projects are labeled when included.

## Start here

| If you want to... | Explore | Why it belongs |
|---|---|---|
| Turn an image into a 3D starting point | [TripoSR](projects/triposr.md) | A concrete visual reconstruction workflow. |
| Turn instrument audio into MIDI | [Basic Pitch](projects/basic-pitch.md) | An output you can inspect in a music workflow. |
| Separate a music recording into stems | [Audio Separator](projects/audio-separator.md) | A practical audio-processing experiment. |
| Extract masks from images or video | [SAM 2](projects/sam2.md) | A reusable visual editing building block. |
| Explore animated character drawings | [Animated Drawings](projects/animated-drawings.md) | An archived research demo with a playful result. |

## What is checked

Entries distinguish documentation review from hands-on testing. The initial collection is **documentation-reviewed**: source material was inspected, but these applications have not all been installed or benchmarked by QuicqDev. Each project card records its sources, review date, requirements and a limitation.

Hardware requirements depend on model, quantization, context length and workload. We do not infer RAM needs from parameter counts. Application code, model weights and optional hosted services can have different licenses or costs. Check the linked upstream terms for the configuration you choose.

## Browse by task

- [3D and depth](#3d-and-depth)
- [Images and video](#images-and-video)
- [Music and speech](#music-and-speech)
- [Documents and knowledge](#documents-and-knowledge)
- [Playful experiments](#playful-experiments)

## 3D and depth

| Project | Useful for | Setup and requirements |
|---|---|---|
| [TripoSR](projects/triposr.md) · [upstream](https://github.com/VAST-AI-Research/TripoSR) · [demo / examples](https://github.com/VAST-AI-Research/TripoSR/tree/main/figures) | Turn an object illustration into a mesh for an early game-asset or product-visualization prototype. | Python, PyTorch, downloaded model weights and the repository dependencies; CUDA setup must match the installed PyTorch build when using GPU acceleration. |
| [MoGe](projects/moge.md) · [upstream](https://github.com/microsoft/MoGe) · [demo / examples](https://huggingface.co/spaces/Ruicheng/MoGe-2) | Explore a room photo as a 3D scene or create geometry inputs for a visual prototype. | Python dependencies and a matching pretrained checkpoint; the documented inference example uses a CUDA device, and a local Gradio demo is included. |
| [Depth Anything V2](projects/depth-anything-v2.md) · [upstream](https://github.com/DepthAnything/Depth-Anything-V2) · [demo / examples](https://huggingface.co/spaces/depth-anything/Depth-Anything-V2) | Produce depth masks for parallax experiments, depth-aware compositing or computer-vision prototypes. | Python, PyTorch and a downloaded checkpoint; the example selects CUDA, Apple MPS or CPU according to availability. |

## Images and video

| Project | Useful for | Setup and requirements |
|---|---|---|
| [SAM 2](projects/sam2.md) · [upstream](https://github.com/facebookresearch/sam2) · [demo / examples](https://sam2.metademolab.com/) | Prototype object cutouts, video masking or annotation tools from user-supplied prompts. | Python, compatible PyTorch and TorchVision versions, and a model checkpoint; the documented installation targets a GPU machine and recommends WSL for Windows. |
| [BiRefNet](projects/birefnet.md) · [upstream](https://github.com/ZhengPeng7/BiRefNet) · [demo / examples](https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo) | Build a subject-cutout workflow or experiment with placing text behind a foreground subject. | A Python inference environment and task-appropriate weights; upstream supplies PyTorch examples, notebooks and ONNX export guidance. |
| [rembg](projects/rembg.md) · [upstream](https://github.com/danielgatis/rembg) | Batch-process product photos or prepare transparent image assets for a website. | A supported Python version and a CPU or GPU backend; local ONNX models download on first use. |
| [MFLUX](projects/mflux.md) · [upstream](https://github.com/mflux-community/mflux) | Experiment with local image generation while keeping prompts and the creative workflow on an Apple Silicon machine. | An Apple Silicon Mac with a compatible MLX environment; install with uv or Python tooling and download the selected model on first use. |
| [Upscayl](projects/upscayl.md) · [upstream](https://github.com/upscayl/upscayl) · [demo / examples](https://github.com/upscayl/upscayl/blob/main/COMPARISONS.MD) | Enlarge a small illustration or pixelated image before using it in a presentation or design draft. | Install the desktop release for your operating system and use a Vulkan-compatible GPU; many integrated GPUs are unsupported. |

## Music and speech

| Project | Useful for | Setup and requirements |
|---|---|---|
| [Audio Separator](projects/audio-separator.md) · [upstream](https://github.com/nomadkaraoke/python-audio-separator) | Create practice tracks or isolate parts of a recording you are authorized to process. | Python or Docker, FFmpeg and a selected separation model; upstream documents CPU, CUDA and Apple Silicon options. |
| [Basic Pitch](projects/basic-pitch.md) · [upstream](https://github.com/spotify/basic-pitch) · [demo / examples](https://basicpitch.spotify.com/) | Turn an instrumental recording into an editable starting point in a digital audio workstation. | A supported Python environment and compatible audio file; the README links to a browser demo and documents platform-specific model runtimes. |
| [Chatterbox](projects/chatterbox.md) · [upstream](https://github.com/resemble-ai/chatterbox) · [demo / examples](https://huggingface.co/spaces/ResembleAI/Chatterbox) | Prototype narration or a speaking character using a voice you own or have permission to use. | Python, the chatterbox-tts package and model downloads; documented generation examples use CUDA, and reference-conditioned generation needs an audio clip. |
| [Kokoro](projects/kokoro.md) · [upstream](https://github.com/hexgrad/kokoro) · [demo / examples](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/SAMPLES.md) | Add local read-aloud audio or draft narration to a small application. | Python, the kokoro package, model and voice assets, and relevant language dependencies; espeak-ng supports some languages and English fallback pronunciation. |

## Documents and knowledge

| Project | Useful for | Setup and requirements |
|---|---|---|
| [Docling](projects/docling.md) · [upstream](https://github.com/docling-project/docling) · [demo / examples](https://docling-project.github.io/docling/examples/) | Prepare a collection of reports for search, retrieval or a document-processing application. | A supported Python environment and the docling package; download the models required by the selected local parsing pipeline. |
| [Surya](projects/surya.md) · [upstream](https://github.com/datalab-to/surya) · [demo / examples](https://github.com/datalab-to/surya#examples) | Explore how a document parser identifies text, tables and page structure in a scanned document. | Python and surya-ocr plus an inference backend: the reviewed instructions use vLLM for NVIDIA GPUs or llama.cpp for CPU and Apple Silicon. |

## Playful experiments

| Project | Useful for | Setup and requirements |
|---|---|---|
| [Animated Drawings](projects/animated-drawings.md) · [upstream](https://github.com/facebookresearch/AnimatedDrawings) · [demo / examples](https://sketch.metademolab.com/) | Make a hand-drawn character move in a creative coding or educational experiment. | Follow the repository's Python and Conda setup; included example configurations demonstrate rendering an interactive scene. |

## Frequently asked questions

### Are these hidden gems with few GitHub stars?

Not necessarily. Selection is based on an interesting, understandable result and inspectable source material, not a star threshold. Established projects can be useful discoveries for a new reader.

### Are the online demos guaranteed to stay available?

No. Hosted demos can queue, require login, go offline or impose usage limits. Follow the original repository for current examples and local setup. A README demonstration is different from a live hosted application.

### Can I use the code and model weights commercially?

Check them separately. Open-source code may load weights under different terms, including noncommercial conditions. Relevant distinctions are noted in project cards, with the upstream source as the authority.

### Why include an archived project?

An archived research demo can still illustrate a useful creative technique. Its archived status is stated in the caveat, and it should not be mistaken for a maintained application. Prefer active alternatives for ongoing workflows.

## How to contribute

Add a useful project, correct an outdated entry, or submit a reproducible compatibility report. Edit `catalog.json` and run `python scripts/build.py`; the README, project cards and agent index are generated from that source. See [CONTRIBUTING.md](CONTRIBUTING.md) for selection criteria and the field format.

Automated checks validate the catalog on changes and check external links weekly. A reachable link does not establish that software works, is secure, or fits your hardware. Failed and inconclusive checks need review; metadata checks never advance an editorial review date.

## For agents and search tools

Read the [structured catalog](https://raw.githubusercontent.com/QuicqDev/awesome-open-source-ai-discoveries/main/catalog.json), its [schema](catalog.schema.json), or the compact [llms.txt index](https://raw.githubusercontent.com/QuicqDev/awesome-open-source-ai-discoveries/main/llms.txt). Each entry has a stable ID, category, use case, prerequisites, caveat, evidence level and source URLs. Cite the upstream project for its capabilities and this collection for editorial comparisons.

`llms.txt` is a navigation aid, not a promise of inclusion in any search engine or model response. Unknown requirements remain unknown; documentation-reviewed entries must not be described as personally tested.

## Related QuicqDev collections

- [Awesome AI on Your Laptop](https://github.com/QuicqDev/awesome-ai-on-your-laptop) — Find local AI apps for document chat, transcription, dictation, image editing and coding, with setup requirements, source links and practical caveats.
- [Awesome Small AI Apps](https://github.com/QuicqDev/awesome-small-ai-apps) — Practical small-model AI applications and building blocks for OCR, speech, embeddings, browser AI, mobile vision and text extraction.

## Maintainers and attribution

Curated by [Ashutosh Mishra](https://github.com/ASH1998) at [QuicqDev](https://github.com/QuicqDev). Follow [@ashu_mi_2](https://x.com/ashu_mi_2) for project discoveries and practical AI experiments.

All linked projects belong to their respective creators. This repository contains original editorial summaries and links; it does not relicense third-party software, model weights or media. No paid placement or affiliate ranking is included.

If this collection helped you find something useful, star it to bookmark it. Use GitHub Watch settings for notifications, or contribute an entry to help the next reader.

Original catalog text and maintenance scripts: [MIT License](LICENSE).
