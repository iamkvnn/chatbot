# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-cisco-webex-rooms-to-optisigns-digital-signage-51343184586643.md
Chunk: 3/6

| Scope | What it's for |
| --- | --- |
| `spark-admin:devices_read` | Reads the Webex Rooms inventory and device-group membership. |
| `spark-admin:devices_write` | Pushes the signage URL to each Webex device via device configurations. |
| `spark:xapi_commands` | Sends xAPI commands (refresh, restart app) over Service App tokens. |
| `spark:xapi_statuses` | Reads device health signals (online state, peripheral status). |
| `spark-admin:organizations_read` | Reads org metadata to sanity-check the Org ID you paste. |

![The Connect with Cisco Control Hub OAuth dialog — the four setup steps and all five required scopes](/hc/article_attachments/52411197221395)

> If you see a permission error, you're not signed in as a Full Administrator. Ask your Webex admin to either approve OptiSigns for the org or grant you the Full Administrator role.

---

## Step 4 — Paste your Org ID and verify

Return to the OptiSigns tab. In the **Webex Organization ID** field, paste your organization's ID (find it in Control Hub under **Organization Settings → identifier**), then click **Verify Connection**.

OptiSigns mints Service App tokens and begins syncing. Within a few seconds the header flips to **Connected**, and your Webex rooms appear in the list alongside any Android, ChromeOS, or Linux signage devices on your account. Use **Sync now** any time to pull the latest inventory.

![Connected: the Webex Rooms list showing the org, rooms synced, and per-room push state](/hc/article_attachments/52411218876819)

---

## Step 5 — Activate signage on a room

By default, rooms are listed but **not activated**. Activation is per-room billing — you pay only for rooms with signage turned on.

1. Click any Webex room in the list to open its detail drawer.
2. Click **Activate Signage License**. The drawer shows how many licenses are available.
3. Confirm — your subscription updates immediately.
