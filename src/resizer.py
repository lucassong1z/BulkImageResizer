from pathlib import Path
from typing import Iterable, Set

from PIL import Image


def iter_images(folder: Path, formats: Set[str]) -> Iterable[Path]:
    for p in folder.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower().lstrip(".") in formats:
            yield p


def calc_size(img: Image.Image, width: int, height: int) -> tuple[int, int]:
    if height <= 0 and width <= 0:
        return img.size
    if height <= 0:
        ratio = width / img.width
        return width, max(1, int(img.height * ratio))
    if width <= 0:
        ratio = height / img.height
        return max(1, int(img.width * ratio)), height
    return width, height


def resize_folder(
    src: Path,
    dst: Path,
    *,
    width: int,
    height: int,
    quality: int,
    formats: Set[str],
    overwrite: bool,
) -> None:
    src = src.expanduser().resolve()
    dst = dst.expanduser().resolve()
    dst.mkdir(parents=True, exist_ok=True)

    for path in iter_images(src, formats):
        rel = path.relative_to(src)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists() and not overwrite:
            continue

        with Image.open(path) as im:
            target = calc_size(im, width, height)
            if im.size == target:
                im.save(out, quality=quality)
                continue
            # Pillow preserves mode; ensure RGB for JPEG
            convert = im.convert("RGB") if out.suffix.lower() in {".jpg", ".jpeg"} else im
            resized = convert.resize(target, Image.Resampling.LANCZOS)
            save_kwargs = {"quality": quality} if out.suffix.lower() in {".jpg", ".jpeg", ".webp"} else {}
            resized.save(out, **save_kwargs)

