# 驾享悦维 privacy policy

This repository publishes the privacy policy for **驾享悦维 (DriveCare AutoCare)**.

Live page: <https://lin-chai49.github.io/jiaxiang-yuewei-privacy/>

The page is `index.html`. It describes app version 1.0.0, package `com.drivecare.autocare`, as built in the local app project. It is Chinese first, with a full English copy under the same URL.

## What the page says

Records stay in the private SQLite database `autocare.db`. First launch stores the owner's name, plate number, and current mileage. Phone, email, and VIN are optional fields on the owner screen.

Fuel and car-wash photos chosen with the system Photo Picker are copied into the private `receipts` directory. Deleting one of those records deletes its file. **Clear all local data** deletes the database rows and does not delete pictures already in `receipts`. Uninstall removes them.

Export writes a JSON file to a location the user picks. The file includes record rows and receipt paths, not the image bytes. The app does not upload it. Import replaces the database rows from a JSON file the user picks.

The manifest declares `POST_NOTIFICATIONS` and `RECEIVE_BOOT_COMPLETED`. It does not declare `INTERNET`. The home screen calculates reminders locally when opened. A WorkManager job posts the same rules as system notifications about every 24 hours and does not require a network. An overdue insurance notification can show the insurer and policy number on the device. A not-yet-expired one shows the insurer and days left, not the policy number. The three notification switches are stored. Neither the home screen nor the daily job reads them, and the reserved email switch does not send mail.

`android:allowBackup` is false, and the backup rules exclude the database and files from Android automatic backup.

Contact on the page: `samincase0@gmail.com`. Developer: 柴琳.

```bash
python3 check.py
```

The check fails if the page loses the database name, the receipt limitation, the package name, or the contact address, or if it claims that data never leaves the device in any form.
