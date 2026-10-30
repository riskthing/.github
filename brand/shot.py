"""Render card.html and avatar.html in this folder to riskthing-card.png and riskthing-avatar.png."""
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, width, height in (("card", 1280, 640), ("avatar", 500, 500)):
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto((HERE / f"{name}.html").as_uri())
        page.screenshot(path=HERE / f"riskthing-{name}.png")
    browser.close()
