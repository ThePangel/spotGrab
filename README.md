# spotGrab

<div align="center">
  <img src="src/logo.svg" alt="spotGrab Logo" width="120" height="120">
  <br>
  <strong>Web-based Spotify music downloader with real-time progress</strong>
</div>

---

spotGrab is a developer and user friendly solution for downloading Spotify tracks, albums, and playlists in a Docker container. It provides a clean web interface with real-time progress updates, allowing users to securely and efficiently obtain their music as downloadable zip files.

## Features
- 🎵 Download Spotify tracks, albums, or playlists by URL
- 🌐 Modern, responsive web interface with custom logo and branding
- ⚡ Real-time download progress via WebSockets
- 📦 Automatic zip file creation for easy download
- 🐳 Easy deployment with Docker and Docker Compose
- 🧹 Automatic cleanup of old downloads (configurable)
- 📱 Mobile-friendly responsive design
- 🎨 Dark theme with Spotify-inspired styling

## Quick Start

### 1. Clone the repository
```sh
git clone https://github.com/thepangel/spotgrab.git
cd spotgrab
```

### 2. Configure your environment
Update the Spotify API credentials in the `docker-compose.yml` file:

- `CLIENT_ID` and `CLIENT_SECRET`: Your Spotify API credentials ([Get them here](https://developer.spotify.com/dashboard))
- `FILE_CLEANUP_INTERVAL`: Interval (in seconds) between cleanup runs (default: 1800)
- `FILE_CLEANUP_MAX_AGE`: Max age (in seconds) before a download folder is deleted (default: 3600)


For local development, you can create a `.env` file in the `src/` directory with the same variables.

### 3. Build and run with Docker Compose
```sh
docker compose up --build
```

## 🚀 Multi-Architecture Docker Build

Build for multiple architectures:
```sh
# Build multi-arch image
docker buildx build --platform linux/amd64,linux/arm64 -t yourusername/spotgrab:latest .

# Or build locally for your platform
docker build -t spotgrab .
```

## 📁 CasaOS Deployment

spotGrab includes CasaOS-compatible configuration. Simply use the included `docker-compose.yml` file in CasaOS App Store by adding it as a custom app.


## Volumes
- `./music` — Stores temporary music files during download
- `./public_downloads` — Stores downloadable zip files for users

## Environment Variables
- `CLIENT_ID` and `CLIENT_SECRET`: Your Spotify API credentials
- `BITRATE`: Audio bitrate for downloads (default: 192k). Common options: 96k, 128k, 192k, 256k, 320k
- `FILE_CLEANUP_INTERVAL`: Interval (in seconds) between cleanup runs (default: 1800)
- `FILE_CLEANUP_MAX_AGE`: Max age (in seconds) before a download folder is deleted (default: 3600)

## Getting Spotify API Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy the `Client ID` and `Client Secret`
4. Update your `docker-compose.yml` file with these credentials

## License
MIT License — see [LICENSE](LICENSE)

## Contributing
-   Feel free to open up any issues or ask for features in the issues tab!
-   If you want to contribute directly make sure to fork the repo and submit a pull request for me to review.

---

<div align="center">
  <p>spotGrab is built with 💖 and with <a href="https://github.com/thepangel/rustifydl">RustifyDL</a>, FastAPI, and Docker.</p>
  <p>by <a href="https://github.com/thepangel">thepangel</a> ^_____^</p>
</div>
