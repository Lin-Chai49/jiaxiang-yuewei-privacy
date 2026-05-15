---
title: 驾享悦维 · 隐私政策
layout: default
---

# 驾享悦维 隐私政策

**生效日期：2026 年 5 月 15 日**

「驾享悦维」（以下称"本应用"，包名 `com.drivecare.autocare`）由 **柴琳** 独立开发与发布。本隐私政策旨在向您说明本应用如何处理您的信息。

## 一、本应用收集的数据

本应用是一款**完全本地化**的工具，所有数据均仅保存在您本机的私有存储区，**不会上传至任何服务器，不会与第三方共享**。具体包括：

| 数据类别 | 说明 | 存储位置 |
| --- | --- | --- |
| 车主信息 | 姓名、电话、邮箱（您可选择性填写） | 本机 SQLite |
| 车辆信息 | 车牌号、品牌、车型、VIN 码、当前里程 | 本机 SQLite |
| 用车记录 | 加油、保养、洗车、保险记录及小票图片 | 本机 SQLite + 应用私有文件目录 |
| 提醒设置 | 您配置的保养、保险、洗车提醒阈值 | 本机 SQLite |

## 二、数据使用方式

- 上述信息仅用于在您的设备上本地展示、计算与提醒，**不会以任何形式离开您的设备**。
- 本应用不接入任何第三方分析、广告或追踪 SDK。
- 本应用**不需要互联网权限**：APK 中未声明 `android.permission.INTERNET`。

## 三、权限说明

本应用**不申请互联网权限**（`INTERNET`），从技术上即无法上传任何数据。声明的全部权限如下：

| 权限 | 用途 | 是否需要您确认 |
| --- | --- | --- |
| `POST_NOTIFICATIONS` | 在您设定的时机推送本地保养、保险等到期提醒 | **是** — 首次启动时弹窗征求同意；拒绝后仍可在 App 内查看提醒中心 |
| `RECEIVE_BOOT_COMPLETED` | 设备重启后重新调度本地提醒任务 | 否（系统级，自动授予） |
| `WAKE_LOCK` | 提醒任务执行期间防止 CPU 休眠（约 1 秒） | 否（系统级） |
| `ACCESS_NETWORK_STATE` | Android Jetpack WorkManager 检查后台任务执行条件所需 | 否（系统级，仅查询不联网） |
| `FOREGROUND_SERVICE` | 长时间任务（如数据备份）期间通过前台服务避免被系统杀死 | 否（系统级） |

> 注：`WAKE_LOCK`、`ACCESS_NETWORK_STATE`、`FOREGROUND_SERVICE` 是 [Android Jetpack WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) 的标准依赖权限，由 Google 官方库自动声明，仅用于本机后台任务调度，**绝无网络访问能力**（因为本应用未申请 `INTERNET` 权限）。

本应用使用 Android 13 引入的 **Photo Picker** 选择小票图片，**不需要** `READ_MEDIA_IMAGES`、`READ_EXTERNAL_STORAGE` 等存储权限。

## 四、数据导出与删除

- **数据导出**：在「系统设置 → 数据备份」点击"导出 JSON"，您可将全部数据保存为本地 JSON 文件。
- **数据导入**：通过同一菜单选择 JSON 文件即可恢复。
- **数据删除**：点击"清空全部本地数据"立即清除所有数据；卸载本应用同样会删除全部数据（系统机制）。

## 五、儿童信息

本应用不面向 13 周岁以下儿童，亦不会有意收集任何儿童的个人信息。

## 六、第三方开源依赖

本应用仅使用以下 OSS 兼容许可的开源库（均不联网）：

- AndroidX / Jetpack Compose · Apache-2.0
- Room · Apache-2.0
- WorkManager · Apache-2.0
- Coil · Apache-2.0
- kotlinx.serialization / kotlinx.coroutines · Apache-2.0

## 七、隐私政策更新

本政策如有变更，将通过应用内更新与 Google Play 商店列表同步公告。

## 八、联系方式

- 开发者：柴琳
- 反馈邮箱：（请在 Google Play 开发者后台填写您的真实联系邮箱后替换此处）

---

*本应用为完全离线工具，您始终是您本人车辆数据的唯一持有者。*
