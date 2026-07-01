# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: 52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage.md
Chunk: 2/6

---

## What you'll need

- **An OptiSigns account** on a plan that includes device management (MDM / room integrations), with the **Owner** or **Super Admin** role. [Start a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate signage on.
- **Google Meet hardware** (ChromeOS-based Meet devices) enrolled in your Google Workspace.
- A **Google Workspace admin** who can paste a signage URL in the Admin Console.
- **For the Service Account method only:** a Google Workspace **super-admin** who can create a service account and grant domain-wide delegation.

---

## How it works

OptiSigns generates a secure **signage URL** for each screen you want to show on a room. You set that URL as the room's digital-signage URL in the **Google Admin Console**; from then on the room plays whatever you assign in OptiSigns, and updates are live. When a meeting starts — or someone wakes the room — the display returns to the normal Meet UI automatically, with no impact on meeting quality or scheduled meetings.

---

## Open the Google Meet page

In OptiSigns, open **Devices** in the top navigation, then in the left sidebar under **Room Integrations**, click **Google Meet**. If you haven't connected yet, you'll see the connect methods.

![OptiSigns Google Meet — choose how to connect: Signage URL (recommended), Service Account, and Marketplace OAuth (coming soon)](/hc/article_attachments/52412499875091)

Pick your method below.

---

# Method 1 — Connect with a Signage URL (recommended)

No Google Cloud setup. You'll mint a URL in OptiSigns, give it content, and paste it into the Google Admin Console.

### Step 1 — Mint a Signage URL
