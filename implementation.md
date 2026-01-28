# YouTube Downloader CLI - Implementation Plan

## Overview

A command-line application that downloads YouTube videos in either video or audio format.

## Technology Choice: Python

**Why Python over Node.js:**
- `yt-dlp` (Python) is the most reliable and actively maintained YouTube downloading library
- Better handling of YouTube's constantly changing formats and restrictions
- Simpler implementation with excellent CLI support via `argparse`
- Cross-platform compatibility out of the box

## Project Architecture

```
youtube-downloader/
├── yd.py                 # Main CLI application
├── requirements.txt      # Python dependencies
├── README.md            # Usage documentation
└── implementation.md    # This file
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `yt-dlp` | YouTube video/audio downloading engine |

## CLI Design

### Command Format
```bash
yd <youtube-url> [options]
```

### Options
| Flag | Long Form | Description |
|------|-----------|-------------|
| `-v` | `--video` | Download as video (default: best quality MP4) |
| `-a` | `--audio` | Download as audio only (MP3 format) |
| `-o` | `--output` | Custom output directory (default: current directory) |
| `-q` | `--quality` | Video quality: best, 1080, 720, 480, 360 (default: best) |

### Examples
```bash
# Download video
yd https://youtube.com/watch?v=xxxxx -v

# Download audio only
yd https://youtube.com/watch?v=xxxxx -a

# Download to specific folder
yd https://youtube.com/watch?v=xxxxx -v -o ~/Downloads

# Download specific quality
yd https://youtube.com/watch?v=xxxxx -v -q 720
```

## Implementation Details

### Core Components

1. **Argument Parser**
   - Parse CLI arguments using `argparse`
   - Validate YouTube URL format
   - Set default values for optional parameters

2. **Download Engine**
   - Configure `yt-dlp` options based on user choice
   - Handle video download with quality selection
   - Handle audio extraction with MP3 conversion

3. **Progress Display**
   - Show download progress with percentage
   - Display file size and download speed
   - Show completion message with file path

### yt-dlp Configuration

**For Video:**
```python
{
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'merge_output_format': 'mp4'
}
```

**For Audio:**
```python
{
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'outtmpl': '%(title)s.%(ext)s'
}
```

## Installation Steps

1. Install Python 3.8+
2. Install dependencies: `pip install -r requirements.txt`
3. Install FFmpeg (required for audio conversion)
4. Make script executable or create alias

## Error Handling

- Invalid/malformed YouTube URLs
- Network connectivity issues
- Age-restricted or private videos
- Region-blocked content
- Missing FFmpeg for audio conversion

## Future Enhancements (Out of Scope)

- Playlist support
- Subtitle downloading
- Thumbnail extraction
- Multiple URL batch processing
- GUI interface
