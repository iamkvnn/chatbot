# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-zoom-rooms-to-optisigns-digital-signage-52069065128723.md
Chunk: 2/6

There is **no impact on meeting quality**, screen-sharing, whiteboard, or Zoom Apps features.

---

## Step 1 — Sign in to OptiSigns

Go to [app.optisigns.com](https://app.optisigns.com) and sign in (or create your account).

---

## Step 2 — Open the Zoom Rooms page

In the left navigation under **Room Integrations**, click **Zoom Rooms**.

![Connect Zoom Rooms in the left nav](/hc/article_attachments/52352814423187)

---

## Step 3 — Choose a connection method

OptiSigns offers two ways to connect, side-by-side:

![Empty Zoom Rooms page showing Server App and Marketplace App cards](/hc/article_attachments/52352797082387)

| Method | Best for | What you do |
| --- | --- | --- |
| **Server App** | IT-led rollout / strict change control | Create a Server-to-Server OAuth app in your Zoom Marketplace, paste the Account ID + Client ID + Client Secret into OptiSigns. |
| **Marketplace App** *(recommended for most customers)* | SMB / fast onboarding | One-click install of the OptiSigns Digital Signage app from the Zoom Marketplace. |

Both methods request the same Zoom permissions:

- **Read Zoom Rooms inventory** — to list your rooms
- **Push signage URLs** — to assign content to a room
- **Read room events** — to know when a room is idle vs. in a meeting

> Under the hood these map to Zoom's 2024 granular scope taxonomy (`zoom_rooms:read:list_rooms:admin`, `zoom_rooms:update:room_settings:admin`, `zoom_rooms:read:digital_signage_library_contents:admin`, etc.). The exact scope list is shown by Zoom on the install screen.

### Option A — Marketplace App (one-click)
