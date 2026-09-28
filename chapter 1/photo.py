from pathlib import Path
import shutil

source_files = [
    "/mnt/data/Screenshot 2026-09-20 at 4.46.23 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.46.44 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.47.46 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.48.33 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.49.45 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.50.24 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.54.04 PM.png",
    "/mnt/data/Screenshot 2026-09-20 at 4.56.03 PM.png",
]

out_dir = Path("/mnt/data/Elastiflix-PNG-Photos")
out_dir.mkdir(exist_ok=True)

created = []
for i, src in enumerate(source_files, 1):
    src_path = Path(src)
    if src_path.exists():
        dest = out_dir / f"elastiflix-{i}.png"
        shutil.copy2(src_path, dest)
        created.append(dest)

zip_path = shutil.make_archive("/mnt/data/Elastiflix-PNG-Photos", "zip", root_dir=out_dir)

print(f"Created {len(created)} PNG files.")
for p in created:
    print(p)
print(f"ZIP: {zip_path}")
