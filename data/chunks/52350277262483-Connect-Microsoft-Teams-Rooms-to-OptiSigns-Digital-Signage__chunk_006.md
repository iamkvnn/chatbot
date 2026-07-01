# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: 52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 6/7

---

## Licensing

Activating signage on a Teams Room uses **one screen license** from your OptiSigns pool — the same licenses you use for any other screen. Discovered rooms that you haven't activated are free; you're only billed for rooms you turn signage on for. [See full pricing →](https://www.optisigns.com/pricing)

---

## Troubleshooting

**"Test Connection" fails with "Invalid client credentials."** Re-check the Application (client) ID, Directory (tenant) ID, and Client Secret — copy them exactly from the Entra app. If the secret has expired, create a new one in **Certificates & secrets** and paste the new value.

**"Test Connection" fails with a permissions error.** You haven't granted admin consent. In Entra, open the app's **API permissions**, confirm the two Microsoft Graph scopes show **Granted for <tenant>**, then click **Grant admin consent**. Consent changes take about a minute.

**My rooms don't appear after saving the Service Principal.** The first inventory sync can take a few minutes. Click **Sync now** on the Teams Rooms page to refresh. Confirm the app has `TeamworkDevice.Read.All` with admin consent.

**I pasted the URL but nothing shows on the room.** Confirm the room is **online** and licensed for **Teams Rooms Pro** (Basic doesn't include digital signage). Make sure you pasted the full URL (it begins with `https://`) as a **Custom URL** source, and that the source is **assigned to that device** in the Teams Rooms portal.

**Content shows but doesn't clear when a meeting starts.** This is controlled by the Teams Rooms digital-signage setting in Microsoft's portal — confirm signage is set to display only while the room is idle.

**The Teams Rooms portal says the URL is invalid.** The URL may have been truncated on copy. Return to the OptiSigns **Signage URLs** tab, click **Copy** on that URL again, and re-paste.

---

## Need help?
