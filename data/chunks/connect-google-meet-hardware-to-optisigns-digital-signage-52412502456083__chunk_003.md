# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: connect-google-meet-hardware-to-optisigns-digital-signage-52412502456083.md
Chunk: 3/6

![OptiSigns Google Meet — choose how to connect: Signage URL (recommended), Service Account, and Marketplace OAuth (coming soon)](/hc/article_attachments/52412499875091)

Pick your method below.

---

# Method 1 — Connect with a Signage URL (recommended)

No Google Cloud setup. You'll mint a URL in OptiSigns, give it content, and paste it into the Google Admin Console.

### Step 1 — Mint a Signage URL

On the **Signage URL** card, click **Mint URLs**. In the **New Signage URL** dialog, give the URL a **Name** (for example, your room or location). The optional **Target label** is just a note to help you remember where you'll paste it; it doesn't control anything. Click **Next**.

![The New Signage URL dialog — name the URL, then click Next](/hc/article_attachments/52412466531475)

### Step 2 — Assign content

Clicking **Next** creates the URL and opens the **Signage URLs** tab. On the new row, click **+ Assign content**, choose a **Content Type** — **Asset**, **Playlist**, or **Schedule** — pick the item to play, and **Save**. OptiSigns copies the signage URL to your clipboard.

### Step 3 — Paste the URL in the Google Admin Console

Open the [Google Admin Console](https://admin.google.com/ac/meet/devices), go to **Devices → Google Meet hardware**, select the device or organizational unit (OU) you want, and set its **digital signage URL** to the OptiSigns URL you copied. (OptiSigns shows the exact steps in the **paste instructions** dialog, and you can reopen them any time with **Show me how to paste** on the Signage URLs tab.)

Within about a minute the room fetches the URL and your content appears while the room is idle. Start a test meeting — content should clear when the meeting connects.
