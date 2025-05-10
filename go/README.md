# Go + HTMX Demo

A minimal Go web server demonstrating HTMX functionality with a "Hello World" page and dynamic user loading.

## Prerequisites

- Go 1.24 or later

## Installation

1. Clone the repository
2. Navigate to the `go` directory
3. Initialize Go modules (already done):
```bash
go mod init htmx-demo
```

## Running the Server

1. Start the Go server:
```bash
go run main.go
```
2. Open your browser and visit `http://localhost:8080`

## Features

- Static "Hello World" page
- HTMX integration via unpkg CDN
- Dynamic user loading from JSONPlaceholder API
- Server-side rendered HTML templates

## Project Structure

```
go/
├── main.go           # Main Go application
├── go.mod           # Go module definition
└── templates/       
    ├── index.html   # Main page template
    └── users.html   # User list template fragment
```
