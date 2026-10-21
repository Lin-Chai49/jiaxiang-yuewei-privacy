#!/usr/bin/env python3
"""Lock the published DriveCare policy to the facts in index.html."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PAGE = ROOT / "index.html"

REQUIRED = (
    "com.drivecare.autocare",
    "autocare.db",
    "receipts",
    "不会删除 receipts 目录中的图片",
    "does not delete pictures already copied into",
    "samincase0@gmail.com",
    "mailto:samincase0@gmail.com",
    "INTERNET",
    "POST_NOTIFICATIONS",
    "RECEIVE_BOOT_COMPLETED",
    "邮件提醒（预留）",
    "首页和每日任务都不读取",
    "does not send email",
    "Neither the home screen nor the daily job reads them",
    "Photo Picker",
    "allowBackup",
)

BANNED = (
    "不会以任何形式离开",
    "请在 Google Play 开发者后台",
    "FOREGROUND_SERVICE",
    "前台服务",
    "FishingMateDB",
    "OpenStreetMap",
)


def main():
    if not PAGE.is_file():
        print("missing index.html")
        return 1
    text = PAGE.read_text(encoding="utf-8")
    if "</html>" not in text.lower():
        print("unclosed html")
        return 1
    for phrase in REQUIRED:
        if phrase not in text:
            print("missing", phrase)
            return 1
    for phrase in BANNED:
        if phrase in text:
            print("banned", phrase)
            return 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "autocare.db" not in readme or "receipts" not in readme:
        print("readme drift")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
