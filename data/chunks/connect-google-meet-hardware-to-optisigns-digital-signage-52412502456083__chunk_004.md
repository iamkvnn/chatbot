# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: connect-google-meet-hardware-to-optisigns-digital-signage-52412502456083.md
Chunk: 4/6

Within about a minute the room fetches the URL and your content appears while the room is idle. Start a test meeting — content should clear when the meeting connects.

> Repeat Steps 1–3 to mint a URL for each room or OU. You manage all minted URLs (and reassign their content any time) under the **Signage URLs** tab.

---

# Method 2 — Connect with a Service Account

This connects a **read-only** Google Cloud service account so OptiSigns can discover and list all your Meet hardware automatically. (You'll still deliver content with a signage URL — see "Put content on a room" below.)

### Step 1 — Review the setup steps and scopes

On the **Service Account** card, click **View setup steps**. OptiSigns walks you through creating the service account and lists the two read-only scopes it needs.

![The setup-steps dialog — the five steps and the two read-only Admin SDK scopes; use Copy all scopes](/hc/article_attachments/52412466682259)

In the Google Cloud Console (as a Workspace super-admin):

1. Create a project and enable the **Admin SDK API**.
2. Create a **Service Account** and download its **JSON key**.
3. In the Workspace **Admin Console**, grant the service account **domain-wide delegation** for the two scopes below. Tip: click **Copy all scopes** in OptiSigns and paste them straight into the scope picker.

| Scope | What it's for |
| --- | --- |
| `…/auth/admin.directory.device.chromeos` | Reads Meet hardware (ChromeOS device) inventory. |
| `…/auth/admin.directory.device.chromeos.readonly` | Reads device health signals (online/offline, OS version). |

### Step 2 — Add the service account in OptiSigns

Back on the **Service Account** card, click **Add Service Account** and fill in:
