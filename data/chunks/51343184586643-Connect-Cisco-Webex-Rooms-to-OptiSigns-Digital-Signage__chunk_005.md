# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: 51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 5/5

---

## Troubleshooting

**My rooms don't appear after Verify Connection.** Wait 30 seconds and click **Sync now** — the initial inventory sync can take up to a minute on large orgs. If still empty, confirm you have at least one paired device on a WebEngine-capable model (see "What you'll need" above).

**Content shows but doesn't clear when a meeting starts.** This usually means Standby is disabled on the device. In Control Hub, open the device → Configurations → search "Standby" → ensure `Standby Control = On`.

**Content looks zoomed-in or cropped.** Webex Boards and Desks render at 1920×1080. Use OptiSigns' built-in resolution settings on the asset, or design content at 1920×1080 for safe rendering across all devices.

**I get an authorization error in Control Hub.** You're not signed in as a Full Administrator. Ask your Webex admin to either approve OptiSigns at the org level or grant your account the Full Administrator role.

**A specific device shows "WebEngine not enabled."** Open the device in Control Hub → Configurations → set `WebEngine.Mode = On`. OptiSigns will retry automatically.

---

## Pricing

The OptiSigns Webex Rooms integration uses a screen license just like any other OptiSigns screen. A free trial is available — you're only billed once you activate signage on a room. [See full pricing](https://www.optisigns.com/pricing).

---

## Need help?

- Email: [support@optisigns.com](mailto:support@optisigns.com)
- More guides: support.optisigns.com
- Related: [Connect Zoom Rooms to OptiSigns](/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) · [Connect Microsoft Teams Rooms to OptiSigns](/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage)
