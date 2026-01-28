# YouTube Downloader CLI (yd)

A simple command-line tool to download YouTube videos in video or audio format.

## Requirements

- Python 3.8+ (with Conda)
- FFmpeg (required for audio conversion)

## Installation

### 1. Install FFmpeg

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### 2. Create Conda Environment

```bash
cd youtube-downloader
conda create -n yd python=3.11
conda activate yd
pip install yt-dlp
```

**Alternative: Using environment.yml**
```bash
conda env create -f environment.yml
conda activate yd
```

### 3. Create Global Alias

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
alias yd="conda run -n yd python /path/to/youtube-downloader/yd.py"
```

Then reload your shell:
```bash
source ~/.zshrc
```

**Quick setup (run from project directory):**
```bash
echo 'alias yd="conda run -n yd python '$(pwd)'/yd.py"' >> ~/.zshrc
source ~/.zshrc
```

## Usage

> **Important:** Always wrap URLs in quotes to avoid zsh interpreting special characters.

### Download Video

```bash
yd "https://www.youtube.com/watch?v=VIDEO_ID" -v
```

### Download Audio (MP3)

```bash
yd "https://www.youtube.com/watch?v=VIDEO_ID" -a
```

## Options

| Option | Description |
|--------|-------------|
| `-v, --video` | Download as video (MP4) |
| `-a, --audio` | Download as audio (MP3) |
| `-o, --output DIR` | Output directory (default: ~/Desktop) |
| `-q, --quality` | Video quality: best, 1080, 720, 480, 360 |
| `-h, --help` | Show help message |

## Examples

```bash
# Download best quality video (saves to ~/Desktop)
yd "https://youtube.com/watch?v=dQw4w9WgXcQ" -v

# Download 720p video
yd "https://youtube.com/watch?v=dQw4w9WgXcQ" -v -q 720

# Download audio
yd "https://youtube.com/watch?v=dQw4w9WgXcQ" -a

# Download to specific folder
yd "https://youtube.com/watch?v=dQw4w9WgXcQ" -a -o ~/Downloads

# Download from short URL
yd "https://youtu.be/dQw4w9WgXcQ" -a

# Download YouTube Shorts
yd "https://youtube.com/shorts/VIDEO_ID" -v
```

## Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`

## Troubleshooting

### "zsh: no matches found"
Make sure to wrap the URL in quotes:
```bash
yd "https://www.youtube.com/watch?v=VIDEO_ID" -a
```

### "FFmpeg not found"
Make sure FFmpeg is installed and available in your PATH.

### "Video unavailable"
The video might be:
- Private or deleted
- Age-restricted (requires authentication)
- Region-blocked in your country

### Slow downloads
YouTube may throttle download speeds. This is normal behavior.

## License

MIT License
