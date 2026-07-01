# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Source File: 51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 2/5

There is no impact on meeting quality, screen-sharing, or Webex Assistant features.

---

## Step 1 — Sign in to OptiSigns

Go to [**app.optisigns.com**](https://app.optisigns.com/) and sign in (or create your account).

---

## Step 2 — Open the Webex Rooms page

In the top navigation, open **Devices**. In the left sidebar under **Room Integrations**, click **Webex Rooms**. Since you haven't connected yet, you'll see the **Control Hub OAuth** card with everything you need to get started.

![OptiSigns Devices — Room Integrations — Webex Rooms, the not-connected Control Hub OAuth card](/hc/article_attachments/52411191588755)

---

## Step 3 — Authorize OptiSigns in Cisco Control Hub

Click **View setup steps** to review exactly what OptiSigns will do and the permissions it needs, then click **Authorize in Cisco Control Hub**.

A new browser tab opens at Cisco Control Hub. Sign in as a **Webex Full Administrator** and approve the **OptiSigns Digital Signage** Service App for your organization. OptiSigns requests five scopes:

| Scope | What it's for |
| --- | --- |
| `spark-admin:devices_read` | Reads the Webex Rooms inventory and device-group membership. |
| `spark-admin:devices_write` | Pushes the signage URL to each Webex device via device configurations. |
| `spark:xapi_commands` | Sends xAPI commands (refresh, restart app) over Service App tokens. |
| `spark:xapi_statuses` | Reads device health signals (online state, peripheral status). |
| `spark-admin:organizations_read` | Reads org metadata to sanity-check the Org ID you paste. |

![The Connect with Cisco Control Hub OAuth dialog — the four setup steps and all five required scopes](/hc/article_attachments/52411197221395)
