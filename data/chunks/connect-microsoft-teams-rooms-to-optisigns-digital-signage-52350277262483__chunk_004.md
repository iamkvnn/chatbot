# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-microsoft-teams-rooms-to-optisigns-digital-signage-52350277262483.md
Chunk: 4/7

In the **Paste your Signage URL in Teams Rooms portal** dialog, click **Open Teams Admin Portal**. Then, in Microsoft's portal:

1. Sign in and open **Digital signage**.
2. Click **Add source** and give it a clear name (matching your room or group).
3. Choose **Custom URL**, paste the OptiSigns URL, then **Review → Finish**.
4. Select the new source → **Assign to devices** → pick your Teams Room(s) → **Apply**.

![The paste-instructions dialog — copy the URL, then click Open Teams Admin Portal](/hc/article_attachments/52411723276051)

Within about 30 seconds the room fetches the URL and your content appears during idle. Start a test meeting — content should clear instantly when the meeting connects.

> Repeat Steps 1–3 to mint a URL for each room or room group. You manage all minted URLs (and reassign their content any time) under the **Signage URLs** tab.

---

# Method 2 — Connect with a Service Principal

This connects a **read-only** Microsoft Entra app so OptiSigns can discover and list all your Teams Rooms automatically. (You'll still deliver content with a signage URL — see "Put content on a room" below.)

### Step 1 — Register an app in Microsoft Entra

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a **Global Administrator**.
2. Go to **Identity → Applications → App registrations → + New registration**.
3. **Name** it (for example, `OptiSigns Teams Rooms`), choose **single tenant**, and leave **Redirect URI** blank. Click **Register**.
4. On the app's **Overview** page, copy the **Application (client) ID** and **Directory (tenant) ID** — you'll paste these into OptiSigns.

### Step 2 — Grant the Microsoft Graph permissions
