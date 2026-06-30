# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: connect-google-meet-hardware-to-optisigns-digital-signage-52412502456083.md
Chunk: 2/6

> **Important — read this first.** Google does **not** offer a way for apps to push content to Meet hardware automatically. So with **either** method, the final step is a **one-time paste** of an OptiSigns signage URL into the **Google Admin Console**. The **Service Account** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: a Service Account to see every room, and Signage URLs to deliver the content.
>
> A third method, **Marketplace OAuth**, is shown as **Coming soon** in the app — use **Signage URL** or **Service Account** for now.

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
