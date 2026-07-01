# Room Integrations: Turn Your Meeting Rooms into Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52113036672403-Room-Integrations-Turn-Your-Meeting-Rooms-into-Digital-Signage
Source File: 52113036672403-Room-Integrations-Turn-Your-Meeting-Rooms-into-Digital-Signage.md
Chunk: 2/5

> Zoom and Webex deliver signage fully automatically — OptiSigns publishes your content to the room over each vendor's official API. Microsoft Teams Rooms and Google Meet hardware don't offer a push API, so for those you paste an OptiSigns signage URL into the vendor's admin console once — the setup guide walks you through it.

---

## How Room Integrations work

Every platform follows the same flow — connect once, then manage all your rooms from one place.

**1. Connect your platform account.**
From the OptiSigns left navigation under **Room Integrations**, choose your platform. An admin connects OptiSigns at the organization level (via OAuth, a service account, or a pasted signage URL), so one connection covers every room on that platform. Admins, permission scopes, and syncing are handled centrally — there's no room-by-room setup.

**2. Your rooms sync into OptiSigns.**
Once connected, OptiSigns pulls in your rooms and keeps them in sync, each with its live Online / Offline status straight from the vendor. New rooms appear on the next sync, and you can click **Sync** to refresh on demand.

**3. Activate a signage license.**
Rooms start as "discovered, not yet signage." Open a room and select **Activate Signage License** to turn it into an OptiSigns screen, then configure its settings. Each activated room uses **one screen license** from your plan (see *Licensing* below).

**4. A Virtual Screen URL is generated.**
OptiSigns mints a stable, secure **Virtual Screen URL** for each activated room — your screen, delivered as a URL.

**5. The URL is pushed to the room system.**
OptiSigns pushes that URL to the room over the platform's official API, where it becomes the room's idle-screen content. (For platforms without a push API, OptiSigns generates the URL and walks you through a one-time paste in the vendor portal.)
