# Astro + HTMX Demo

A minimal Astro web application demonstrating HTMX functionality with a "Hello World" page and dynamic user loading.

## Prerequisites

- Node.js (LTS version recommended)
- npm (comes with Node.js)

## Installation

1. Clone the repository
2. Navigate to the `astro` directory
3. Install dependencies:
```bash
npm install
```

## Running the Server

1. Start the Astro development server:
```bash
npm run dev
```
2. Open your browser and visit `http://localhost:4321` (or the URL shown in your terminal)

## Features

- Static "Hello World" page
- HTMX integration via unpkg CDN
- Dynamic user loading from JSONPlaceholder API
- Server-side rendered pages using Astro's built-in SSR

## Project Structure

```
astro/
├── package.json        # Node.js dependencies and scripts
├── astro.config.mjs    # Astro configuration
└── src/
    └── pages/         
        ├── index.astro # Main page
        └── users.astro # User list endpoint
```
