# YouTube Downloader CLI (yd)

A simple command-line tool to download YouTube videos in video or audio format.

## Requirements

- Python 3.8+
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

### 2. Install Python Dependencies (Conda)

```bash
cd youtube-downloader
conda env create -f environment.yml
conda activate yd
```

**Alternative: Using pip directly**
```bash
pip install -r requirements.txt
```

### 3. Make the Script Executable (Optional)

```bash
chmod +x yd.py
```

### 4. Create Global Alias (Optional)

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
alias yd="conda run -n yd python /path/to/youtube-downloader/yd.py"
```

Then reload your shell:
```bash
source ~/.zshrc
```

**Quick setup for this project:**
```bash
echo 'alias yd="conda run -n yd python '$(pwd)'/yd.py"' >> ~/.zshrc
source ~/.zshrc
```

## Usage

**Note:** Activate the conda environment first, or use the global alias.

### Download Video

```bash
conda activate yd
python yd.py https://www.youtube.com/watch?v=VIDEO_ID -v
```

### Download Audio (MP3)

```bash
conda activate yd
python yd.py https://www.youtube.com/watch?v=VIDEO_ID -a
```

### With Global Alias (Recommended)

```bash
yd https://www.youtube.com/watch?v=VIDEO_ID -v
yd https://www.youtube.com/watch?v=VIDEO_ID -a
```

## Options

| Option | Description |
|--------|-------------|
| `-v, --video` | Download as video (MP4) |
| `-a, --audio` | Download as audio (MP3) |
| `-o, --output DIR` | Output directory (default: current) |
| `-q, --quality` | Video quality: best, 1080, 720, 480, 360 |
| `-h, --help` | Show help message |

## Examples

```bash
# Download best quality video
yd https://youtube.com/watch?v=dQw4w9WgXcQ -v

# Download 720p video
yd https://youtube.com/watch?v=dQw4w9WgXcQ -v -q 720

# Download audio to Downloads folder
yd https://youtube.com/watch?v=dQw4w9WgXcQ -a -o ~/Downloads

# Download from short URL
yd https://youtu.be/dQw4w9WgXcQ -a

# Download YouTube Shorts
yd https://youtube.com/shorts/VIDEO_ID -v
```

## Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`

## Troubleshooting

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
