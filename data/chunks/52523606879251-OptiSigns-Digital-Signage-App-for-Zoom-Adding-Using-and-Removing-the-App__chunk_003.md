# OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App

Article URL: https://support.optisigns.com/hc/en-us/articles/52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App
Source File: 52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App.md
Chunk: 3/6

OptiSigns never accesses meeting content, recordings, transcripts, chat, calendars, or participant data — the integration requests no meeting scopes at all.

---

## Adding the app

In OptiSigns, sign in at [app.optisigns.com](https://app.optisigns.com), then open **Room Integrations → Zoom Rooms** in the left navigation. There are two ways to connect; both use the same Zoom permissions listed above:

- **Marketplace App** — Click **Connect with Zoom**. You are redirected to the Zoom App Marketplace to review the requested scopes and approve access (you must be the Zoom Account Owner, or an Admin with Marketplace install permission). After approval, you are returned to OptiSigns and your rooms appear within a few seconds.
- **Server App** — Create a Server-to-Server OAuth app in the Zoom Marketplace with the scopes listed above, then click **Add Server App** in OptiSigns and paste the app's Account ID, Client ID, and Client Secret. OptiSigns validates the credentials and pulls your room inventory immediately.

If approval fails or you land back in OptiSigns without a successful connection, see Troubleshooting below. For a step-by-step walkthrough with screenshots, see [Connect Zoom Rooms to OptiSigns Digital Signage](/hc/en-us/articles/52069065128723).

---

## Using the integration

When connected, your Zoom Rooms appear in OptiSigns alongside your other screens. Rooms do not consume an OptiSigns license until you activate signage on them. For each room you activate, OptiSigns assigns a signage URL to the room through Zoom's REST API; the Zoom Rooms client then displays your assigned OptiSigns content (images, videos, playlists, schedules) whenever the room is idle, and hides it during meetings.
