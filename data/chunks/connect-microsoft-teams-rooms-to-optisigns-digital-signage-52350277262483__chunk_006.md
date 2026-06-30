# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-microsoft-teams-rooms-to-optisigns-digital-signage-52350277262483.md
Chunk: 6/7

Within a few minutes your Teams Rooms appear in the **Devices** tab, each with its model and live online/offline status.

*[Screenshot to add: the connected **Devices** tab showing "Connected · <tenant> · N rooms synced" and the synced room list — captured once a Microsoft tenant with Teams Rooms is connected.]*

### Put content on a room

Discovering rooms doesn't put content on them — that still uses a signage URL. From the **Signage URLs** tab, click **New Signage URL** and follow **Method 1, Steps 1–3** above to mint a URL, assign content, and paste it into the Teams Rooms portal for that room.

---

## Licensing

Activating signage on a Teams Room uses **one screen license** from your OptiSigns pool — the same licenses you use for any other screen. Discovered rooms that you haven't activated are free; you're only billed for rooms you turn signage on for. [See full pricing →](https://www.optisigns.com/pricing)

---

## Troubleshooting

**"Test Connection" fails with "Invalid client credentials."** Re-check the Application (client) ID, Directory (tenant) ID, and Client Secret — copy them exactly from the Entra app. If the secret has expired, create a new one in **Certificates & secrets** and paste the new value.

**"Test Connection" fails with a permissions error.** You haven't granted admin consent. In Entra, open the app's **API permissions**, confirm the two Microsoft Graph scopes show **Granted for <tenant>**, then click **Grant admin consent**. Consent changes take about a minute.

**My rooms don't appear after saving the Service Principal.** The first inventory sync can take a few minutes. Click **Sync now** on the Teams Rooms page to refresh. Confirm the app has `TeamworkDevice.Read.All` with admin consent.
