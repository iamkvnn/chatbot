# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-cisco-webex-rooms-to-optisigns-digital-signage-51343184586643.md
Chunk: 2/6

---

## How OptiSigns works on Webex devices

OptiSigns uses the **Webex Digital Signage / Standby** feature built into RoomOS. We do not install an app on the device — instead, we set the device's signage URL via Webex's official Device Configurations API. Your content plays through the WebEngine browser only when the room is idle, and the device automatically returns to its normal meeting UI on any incoming call, scheduled meeting, or wake-on-presence.

There is no impact on meeting quality, screen-sharing, or Webex Assistant features.

---

## Step 1 — Sign in to OptiSigns

Go to [**app.optisigns.com**](https://app.optisigns.com/) and sign in (or create your account).

---

## Step 2 — Open the Webex Rooms page

In the top navigation, open **Devices**. In the left sidebar under **Room Integrations**, click **Webex Rooms**. Since you haven't connected yet, you'll see the **Control Hub OAuth** card with everything you need to get started.

![OptiSigns Devices — Room Integrations — Webex Rooms, the not-connected Control Hub OAuth card](/hc/article_attachments/52411191588755)

---

## Step 3 — Authorize OptiSigns in Cisco Control Hub

Click **View setup steps** to review exactly what OptiSigns will do and the permissions it needs, then click **Authorize in Cisco Control Hub**.

A new browser tab opens at Cisco Control Hub. Sign in as a **Webex Full Administrator** and approve the **OptiSigns Digital Signage** Service App for your organization. OptiSigns requests five scopes:
