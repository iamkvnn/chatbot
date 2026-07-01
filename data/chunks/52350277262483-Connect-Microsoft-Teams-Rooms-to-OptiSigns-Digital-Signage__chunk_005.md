# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: 52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 5/7

![OptiSigns Service Principal setup steps and the two required read-only Graph scopes — use Copy all scopes](/hc/article_attachments/52411718955411)

### Step 3 — Create a client secret

1. In the app, open **Certificates & secrets → Client secrets → + New client secret**.
2. Give it a description and an expiry, then **Add**.
3. **Copy the secret Value immediately** — Microsoft only shows it once. If you navigate away you'll have to create a new one.

### Step 4 — Connect in OptiSigns

Back on the OptiSigns **Teams Rooms** page, on the **Service Principal** card, click **Add Service Principal**. Paste:

- **Name** — any label (for example, `Contoso Teams SP`)
- **Application (client) ID** — from Step 1
- **Directory (tenant) ID** — from Step 1
- **Client Secret** — from Step 3

Click **Test Connection**. OptiSigns validates the credentials against Microsoft Graph and shows your tenant name on success — then **Save** lights up. Click **Save**.

![The Add Service Principal dialog — fill the four fields, then Test Connection before Save](/hc/article_attachments/52411702980627)

Within a few minutes your Teams Rooms appear in the **Devices** tab, each with its model and live online/offline status.

*[Screenshot to add: the connected **Devices** tab showing "Connected · <tenant> · N rooms synced" and the synced room list — captured once a Microsoft tenant with Teams Rooms is connected.]*

### Put content on a room

Discovering rooms doesn't put content on them — that still uses a signage URL. From the **Signage URLs** tab, click **New Signage URL** and follow **Method 1, Steps 1–3** above to mint a URL, assign content, and paste it into the Teams Rooms portal for that room.

---

## Licensing
