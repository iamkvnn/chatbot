# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Source File: 52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 4/6

---

## Step 6 — Assign content

Once the room is activated, content is assigned the same way as any other OptiSigns screen:

1. From the room drawer, click **Assign Content** (or **Change Content** if content is already assigned).
2. Pick an Asset, Playlist, or Schedule.
3. Save.

Within **10–30 seconds**, your content will appear on the Zoom Room between meetings. Start a test call — content clears the instant the meeting connects, and reappears when the room becomes idle.

---

## Configure Zoom Settings (optional)

The **Zoom Settings** card in the room drawer exposes the signage behavior that OptiSigns pushes to the device:

| Setting | What it does | Notes |
| --- | --- | --- |
| **Mode** | Layout used by the Zoom Rooms digital signage renderer | Defaults to the standard content-only layout. The HDMI layout is intentionally not exposed (Zoom rejects it over REST). |
| **Display Period** | Two minute offsets that control when signage shows: **start displaying N min after a meeting ends** and **stop displaying N min before the next meeting**. | Toggle off to show signage whenever the room is idle. |
| **Mute** | Mute audio on the signage playback. | On by default — recommended for meeting rooms. |
| **Enable** | Master toggle for the signage feature on this room. | Turn off temporarily without releasing the OptiSigns license. |

Changes apply within **~10 seconds** via Zoom's REST API.

---

## Disconnecting OptiSigns

1. From the OptiSigns Zoom Rooms page, click **Disconnect** on the status bar.
2. Confirm in the dialog:

![Disconnect Zoom confirmation dialog](/hc/article_attachments/52352754968339)

Disconnecting releases all OptiSigns screen licenses currently consumed by Zoom Rooms and stops syncing rooms from Zoom.
