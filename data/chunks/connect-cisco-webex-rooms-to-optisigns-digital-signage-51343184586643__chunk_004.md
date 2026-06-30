# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-cisco-webex-rooms-to-optisigns-digital-signage-51343184586643.md
Chunk: 4/6

![The room detail drawer with the Activate Signage License button and available license count](/hc/article_attachments/52411212058003)

---

## Step 6 — Push content

With the room activated, you can assign content like any other OptiSigns screen. In the room drawer, click **Assign Content** (or **Change Content** if something is already playing), pick an **Asset**, **Playlist**, or **Schedule**, and save. The drawer shows what's currently playing and the room's signage URL.

![The activated room drawer — currently-playing content, Change Content and Remove Signage, and the signage URL](/hc/article_attachments/52411202243731)

Walk to the device. Within 10–30 seconds, your content appears during Standby. Try a test call — content should clear instantly when the call connects.

---

## Configure signage behavior (optional)

In the room drawer, the **Webex Settings** card lets you tune how signage plays on that device:

| Setting | What it does | Recommended |
| --- | --- | --- |
| **Interaction Mode** | Whether touch on a Board/Desk wakes the device or interacts with content | **Non-interactive (kiosk)** for lobby/info screens; **Interactive (touch)** for kiosk-style content |
| **Auto-refresh** | How often the device reloads the signage URL (`0 = never`) | 30 minutes (default) |
| **Mute** | Whether videos play with sound | Off (default) |
| **Enable** | Master on/off for digital signage — disabling preserves the URL so you can re-enable later | On |

Click **Save** to apply. Changes reach the device within about 10 seconds via Webex's API.

![The Webex Settings card — Interaction Mode, Auto-refresh, Mute, and Enable](/hc/article_attachments/52411197957267)

---

## Disconnecting OptiSigns

**From OptiSigns:** Webex Rooms page → **Disconnect Cisco Webex**. This stops content delivery, releases the screen licenses, and removes the signage URL from all paired devices.
