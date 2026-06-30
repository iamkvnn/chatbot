# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-zoom-rooms-to-optisigns-digital-signage-52069065128723.md
Chunk: 3/6

### Option A — Marketplace App (one-click)

1. Click **Connect with Zoom** on the Marketplace card.
2. A new tab opens at **marketplace.zoom.us** with the OptiSigns Digital Signage app install screen.
3. Review the requested scopes and click **Authorize** (or **Allow**). You must be signed in as the Account Owner, or an Admin with **Manage Marketplace Apps** privilege.
4. You'll be redirected back to OptiSigns automatically — your rooms appear in the list within a few seconds.

> If you see **"You don't have permission to install this app,"** ask your Zoom Account Owner to pre-approve OptiSigns at the account level (Marketplace Manage Permissions), or to grant you the right role.

### Option B — Server App (Server-to-Server OAuth)

1. In the Zoom Marketplace, **Build App Server-to-Server OAuth**.
2. Add the scopes shown on the card above and activate the app.
3. Click **Add Server App** on the OptiSigns card and paste your **Account ID**, **Client ID**, and **Client Secret**.
4. OptiSigns will validate the credentials and pull your room inventory immediately.

---

## Step 4 — Confirm the connection

Once connected, the status bar shows the account email and the room count. From here you can refresh the inventory or disconnect.

![Connected status bar showing Sync now and Disconnect](/hc/article_attachments/52352814631315)

- **Sync now** — re-fetch rooms from Zoom (rooms also sync automatically on a schedule).
- **Disconnect** — see [Disconnecting OptiSigns](#disconnecting-optisigns).

Your Zoom Rooms now appear in the device table alongside any Android, ChromeOS, Linux, or Webex devices on your account.

---

## Step 5 — Activate signage on a room

By default rooms are listed but **not activated** — they don't consume an OptiSigns license until you turn signage on. Activation is per-room.
