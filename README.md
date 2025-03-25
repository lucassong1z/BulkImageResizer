# BulkImageResizer

A small weekend project to batch-resize images from the CLI.

Usage
- `bin/bulkimg <src> <dst> --width 1024 --height 0 --quality 85`
- Supported formats: jpg, jpeg, png, webp
- Keeps aspect ratio when width or height is 0

Notes
- Written to be simple and dependency-light (Pillow only).
- No runtime setup here; just code and tests can be added later.
