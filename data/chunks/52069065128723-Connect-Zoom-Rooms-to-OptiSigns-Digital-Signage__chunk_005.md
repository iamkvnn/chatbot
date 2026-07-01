# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Source File: 52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 5/6

![Disconnect Zoom confirmation dialog](/hc/article_attachments/52352754968339)

Disconnecting releases all OptiSigns screen licenses currently consumed by Zoom Rooms and stops syncing rooms from Zoom.

> **Heads-up:** Disconnecting from OptiSigns does **NOT** remove any signage URL already pushed to your Zoom Rooms. To clear content from a room, push an empty signage URL before disconnecting, or remove it manually from the Zoom admin portal.

3. (Optional, for Marketplace install) To fully revoke OptiSigns' Zoom access token, go to **marketplace.zoom.us Manage Added Apps OptiSigns Digital Signage Remove**.

---

## Troubleshooting

**My rooms don't appear after connecting.**
Click **Sync now** on the status bar. If the table is still empty, confirm at least one Zoom Room is provisioned and recently online in your Zoom admin portal. Initial sync can take up to a minute on large accounts.

**The room drawer shows "Could not load settings" in the Zoom Settings card.**
The room has not returned settings to Zoom yet (most common when the room appliance is offline or has been recently reset). Wait until the room is online (Health = active), click **Sync now**, then reopen the drawer.

**Content shows but doesn't clear when a meeting starts.**
Check the **Display Period** toggle in the Zoom Settings card — if it's on with a very small "stop displaying ... before meeting" offset, content can hang on for a few seconds. Either lower the start offset or disable Display Period to use Zoom's default behavior.

**"You don't have permission to install this app" on the Zoom Marketplace.**
You're not signed in as the Account Owner or an Admin with Marketplace install permission. Ask your Zoom account owner to pre-approve OptiSigns at the account level, or to grant your account the appropriate role.
