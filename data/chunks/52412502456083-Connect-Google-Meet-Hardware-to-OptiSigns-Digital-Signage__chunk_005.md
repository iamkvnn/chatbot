# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: 52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage.md
Chunk: 5/6

Click **Test Connection**. OptiSigns validates the credentials against Google and shows your workspace domain on success — then **Save & Connect** lights up. Click it.

![The Add Service Account dialog — fill the fields, then Test Connection before Save & Connect](/hc/article_attachments/52412503183251)

Within a few minutes your Meet hardware appears in the **Devices** tab, each with its model and live online/offline status.

![The connected Devices tab — discovered Google Meet hardware with status and model](/hc/article_attachments/52412490811667)

### Put content on a room

Discovering rooms doesn't put content on them — that still uses a signage URL. From the **Signage URLs** tab, click **New Signage URL** and follow **Method 1, Steps 1–3** above to mint a URL, assign content, and paste it into the Google Admin Console for that room or OU.

---

## Licensing

Activating signage on a Meet room uses **one screen license** from your OptiSigns pool — the same licenses you use for any other screen. Discovered rooms you haven't activated are free; you're only billed for rooms you turn signage on for. [See full pricing](https://www.optisigns.com/pricing).

---

## Troubleshooting

**"Test Connection" fails with an invalid-key error.** Re-paste the **entire** JSON key file (it must include `private_key` and `client_email`). If you regenerated the key, download and paste the new one.

**"Test Connection" fails with a delegation or scope error.** Domain-wide delegation isn't granted, or the scopes don't match. In the Workspace Admin Console, confirm the service account's client ID is delegated **both** `admin.directory.device.chromeos` scopes, then try again. Consent changes take about a minute.

**My rooms don't appear after saving the service account.** The first inventory sync can take a few minutes. Click **Sync now** on the Google Meet page. Confirm the impersonation email is a **super-admin** and the Admin SDK API is enabled.
