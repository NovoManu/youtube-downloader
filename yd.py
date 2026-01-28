#!/usr/bin/env python3
"""
YouTube Downloader CLI
Download YouTube videos in video or audio format.

Usage:
    yd <url> -v    Download as video
    yd <url> -a    Download as audio (MP3)
"""

import argparse
import sys
import os
import re
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Install it with: pip install yt-dlp")
    sys.exit(1)


def is_valid_youtube_url(url: str) -> bool:
    """Validate if the URL is a YouTube video URL."""
    youtube_patterns = [
        r'^https?://(www\.)?youtube\.com/watch\?v=[\w-]+',
        r'^https?://youtu\.be/[\w-]+',
        r'^https?://(www\.)?youtube\.com/shorts/[\w-]+',
    ]
    return any(re.match(pattern, url) for pattern in youtube_patterns)


def create_progress_hook():
    """Create a progress hook for yt-dlp to display download progress."""
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\r⬇ Downloading: {percent} | Speed: {speed} | ETA: {eta}   ", end='', flush=True)
        elif d['status'] == 'finished':
            print(f"\n✓ Download complete! Processing...")
    return progress_hook


def download_video(url: str, output_dir: str, quality: str) -> bool:
    """Download YouTube video."""
    
    # Quality format mapping
    quality_formats = {
        'best': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '1080': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]',
        '720': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]',
        '480': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]',
        '360': 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360]',
    }
    
    format_string = quality_formats.get(quality, quality_formats['best'])
    
    ydl_opts = {
        'format': format_string,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [create_progress_hook()],
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🎬 Fetching video information...")
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            # Adjust extension for merged output
            if not filename.endswith('.mp4'):
                filename = os.path.splitext(filename)[0] + '.mp4'
            print(f"✅ Saved: {filename}")
            return True
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download error: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


def download_audio(url: str, output_dir: str) -> bool:
    """Download YouTube video as audio (MP3)."""
    
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [create_progress_hook()],
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🎵 Fetching audio information...")
            info = ydl.extract_info(url, download=True)
            filename = os.path.splitext(ydl.prepare_filename(info))[0] + '.mp3'
            print(f"✅ Saved: {filename}")
            return True
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download error: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        prog='yd',
        description='Download YouTube videos in video or audio format',
        epilog='Examples:\n'
               '  yd https://youtube.com/watch?v=xxxxx -v\n'
               '  yd https://youtube.com/watch?v=xxxxx -a\n'
               '  yd https://youtube.com/watch?v=xxxxx -v -q 720',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'url',
        help='YouTube video URL'
    )
    
    format_group = parser.add_mutually_exclusive_group(required=True)
    format_group.add_argument(
        '-v', '--video',
        action='store_true',
        help='Download as video (MP4)'
    )
    format_group.add_argument(
        '-a', '--audio',
        action='store_true',
        help='Download as audio (MP3)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='~/Desktop',
        help='Output directory (default: ~/Desktop)'
    )
    
    parser.add_argument(
        '-q', '--quality',
        choices=['best', '1080', '720', '480', '360'],
        default='best',
        help='Video quality (default: best)'
    )
    
    args = parser.parse_args()
    
    # Validate URL
    if not is_valid_youtube_url(args.url):
        print("❌ Error: Invalid YouTube URL")
        print("Supported formats:")
        print("  - https://www.youtube.com/watch?v=VIDEO_ID")
        print("  - https://youtu.be/VIDEO_ID")
        print("  - https://www.youtube.com/shorts/VIDEO_ID")
        sys.exit(1)
    
    # Validate and create output directory
    output_dir = os.path.abspath(os.path.expanduser(args.output))
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"📁 Created output directory: {output_dir}")
        except OSError as e:
            print(f"❌ Error: Cannot create output directory: {e}")
            sys.exit(1)
    
    print(f"📍 Output directory: {output_dir}")
    print()
    
    # Download based on format choice
    if args.video:
        success = download_video(args.url, output_dir, args.quality)
    else:
        success = download_audio(args.url, output_dir)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
