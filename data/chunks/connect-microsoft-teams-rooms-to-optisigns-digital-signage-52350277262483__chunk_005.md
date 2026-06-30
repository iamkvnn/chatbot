# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-microsoft-teams-rooms-to-optisigns-digital-signage-52350277262483.md
Chunk: 5/7

### Step 2 — Grant the Microsoft Graph permissions

1. In the app, open **API permissions → + Add a permission → Microsoft Graph → Application permissions**.
2. Add the two read-only scopes OptiSigns requires: **`TeamworkDevice.Read.All`** (reads your Teams Rooms inventory) and **`TeamworkAppSettings.Read.All`** (reads device health — online/offline, peripheral issues). Tip: click **Copy all scopes** on the OptiSigns setup screen and paste them straight into the Entra picker.
3. Click **Grant admin consent for <your tenant>**. Both should show **Granted**.

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
