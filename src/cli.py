import argparse
from pathlib import Path
from .resizer import resize_folder


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="bulkimg",
        description="Batch resize images in a folder",
    )
    p.add_argument("src", type=Path, help="Source folder with images")
    p.add_argument("dst", type=Path, help="Destination folder for output")
    p.add_argument("--width", type=int, default=1024, help="Target width")
    p.add_argument("--height", type=int, default=0, help="Target height (0 keeps aspect)")
    p.add_argument("--quality", type=int, default=85, help="JPEG quality (1-95)")
    p.add_argument("--formats", nargs="*", default=["jpg", "jpeg", "png", "webp"], help="Extensions to include")
    p.add_argument("--overwrite", action="store_true", help="Overwrite if exists")
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    resize_folder(
        src=args.src,
        dst=args.dst,
        width=args.width,
        height=args.height,
        quality=args.quality,
        formats=set(x.lower().lstrip(".") for x in args.formats),
        overwrite=args.overwrite,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

