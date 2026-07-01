# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: 51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 3/5

![The Connect with Cisco Control Hub OAuth dialog — the four setup steps and all five required scopes](/hc/article_attachments/52411197221395)

> If you see a permission error, you're not signed in as a Full Administrator. Ask your Webex admin to either approve OptiSigns for the org or grant you the Full Administrator role.

---

## Step 4 — Paste your Org ID and verify

Return to the OptiSigns tab. In the **Webex Organization ID** field, paste your organization's ID (find it in Control Hub under **Organization Settings → identifier**), then click **Verify Connection**.

OptiSigns mints Service App tokens and begins syncing. Within a few seconds the header flips to **Connected**, and your Webex rooms appear in the list alongside any Android, ChromeOS, or Linux signage devices on your account. Use **Sync now** any time to pull the latest inventory.

![Connected: the Webex Rooms list showing the org, rooms synced, and per-room push state](/hc/article_attachments/52411218876819)

---

## Step 5 — Activate signage on a room

By default, rooms are listed but **not activated**. Activation is per-room billing — you pay only for rooms with signage turned on.

1. Click any Webex room in the list to open its detail drawer.
2. Click **Activate Signage License**. The drawer shows how many licenses are available.
3. Confirm — your subscription updates immediately.

![The room detail drawer with the Activate Signage License button and available license count](/hc/article_attachments/52411212058003)

---

## Step 6 — Push content

With the room activated, you can assign content like any other OptiSigns screen. In the room drawer, click **Assign Content** (or **Change Content** if something is already playing), pick an **Asset**, **Playlist**, or **Schedule**, and save. The drawer shows what's currently playing and the room's signage URL.
