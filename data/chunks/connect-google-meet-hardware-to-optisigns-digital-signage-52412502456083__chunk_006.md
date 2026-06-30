# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: connect-google-meet-hardware-to-optisigns-digital-signage-52412502456083.md
Chunk: 6/6

**"Test Connection" fails with a delegation or scope error.** Domain-wide delegation isn't granted, or the scopes don't match. In the Workspace Admin Console, confirm the service account's client ID is delegated **both** `admin.directory.device.chromeos` scopes, then try again. Consent changes take about a minute.

**My rooms don't appear after saving the service account.** The first inventory sync can take a few minutes. Click **Sync now** on the Google Meet page. Confirm the impersonation email is a **super-admin** and the Admin SDK API is enabled.

**I pasted the URL but nothing shows on the room.** Confirm the device is **online**, and that you set the OptiSigns URL as the room's digital-signage URL on the **correct OU/device** in the Google Admin Console. Make sure you pasted the full URL (it begins with `https://`).

**Content shows but doesn't clear when a meeting starts.** This is handled by Google's Meet hardware signage behavior — content displays only while the room is idle and returns to the Meet UI on a call.

---

## Need help?

- Email: [support@optisigns.com](mailto:support@optisigns.com)
- More guides: support.optisigns.com
- Related: [Connect Zoom Rooms to OptiSigns](/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) · [Connect Microsoft Teams Rooms to OptiSigns](/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage) · [Connect Cisco Webex Rooms to OptiSigns](/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)
