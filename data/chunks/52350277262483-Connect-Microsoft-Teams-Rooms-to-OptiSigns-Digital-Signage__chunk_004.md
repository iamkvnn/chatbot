# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: 52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 4/7

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

1. In the app, open **API permissions → + Add a permission → Microsoft Graph → Application permissions**.
2. Add the two read-only scopes OptiSigns requires: **`TeamworkDevice.Read.All`** (reads your Teams Rooms inventory) and **`TeamworkAppSettings.Read.All`** (reads device health — online/offline, peripheral issues). Tip: click **Copy all scopes** on the OptiSigns setup screen and paste them straight into the Entra picker.
3. Click **Grant admin consent for <your tenant>**. Both should show **Granted**.
