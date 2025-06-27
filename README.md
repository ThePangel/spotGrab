# spotGrab

spotGrab is a developer and user friendly solution for downloading Spotify tracks, albums, and playlists in a docker container. It provides a clean web interface, allowing users to securely and efficiently obtain their music as downloadable zip files.

## Features
- 🎵 Download Spotify tracks, albums, or playlists by URL
- 🌐 Modern, responsive web interface
- ⚡ Real-time download progress via WebSockets
- 📦 Download your music as a zip file
- 🐳 Easy deployment with Docker and Docker Compose
- 🧹 Automatic cleanup of old downloads (configurable)

## Quick Start

### 1. Clone the repository
```sh
git clone https://github.com/thepangel/spotgrab.git
cd spotgrab
```

### 2. Configure your environment
Environment variables are configured directly in the `docker-compose.yml` file using the `environment` section. Update the values in the compose file with your Spotify API credentials:

- `CLIENT_ID` and `CLIENT_SECRET`: Your Spotify API credentials
- `DOMAIN`: The base URL for your deployment (e.g., `http://localhost:8000` or your public domain)
- `FILE_CLEANUP_INTERVAL`: Interval (in seconds) between cleanup runs
- `FILE_CLEANUP_MAX_AGE`: Max age (in seconds) before a download folder is deleted

For local development, you can alternatively create a `.env` file in the `src/` directory with the same variables.

### 3. Build and run with Docker Compose
```sh
docker compose up --build
```


## Volumes
- `./music` — Stores temporary music files during download
- `./public_downloads` — Stores downloadable zip files for users

## Environment Variables
- `CLIENT_ID` and `CLIENT_SECRET`: Your Spotify API credentials
- `DOMAIN`: The base URL for your deployment (e.g., `http://localhost:8000` or your public domain)
- `FILE_CLEANUP_INTERVAL`: Interval (in seconds) between cleanup runs
- `FILE_CLEANUP_MAX_AGE`: Max age (in seconds) before a download folder is deleted

## License
MIT License — see [LICENSE](LICENSE)

---

spotGrab is built with 💖 and with [spotDL](https://github.com/spotDL/spotify-downloader), FastAPI, and Docker.

by thepangel ^_____^
