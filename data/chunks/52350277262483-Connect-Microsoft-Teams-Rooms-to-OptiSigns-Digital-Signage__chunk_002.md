# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: 52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 2/7

---

## What you'll need

- **An OptiSigns account** on a plan that includes device management (MDM / room integrations), with the **Owner** or **Super Admin** role. [Start a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate signage on.
- **Microsoft Teams Rooms Pro.** Digital signage is a **Teams Rooms Pro** capability — rooms on Teams Rooms **Basic** can't display signage.
- At least one **Teams Room that's online and signed in**.
- **For the Service Principal method only:** a Microsoft **Entra (Azure AD) Global Administrator** who can register an app and grant admin consent.

---

## How it works

OptiSigns generates a secure **signage URL** for each screen you want to show on a room. Microsoft's Teams Rooms Pro platform has a built-in **Digital signage** feature that can display a custom URL while the room is idle. You paste the OptiSigns URL there once; from then on the room plays whatever you assign in OptiSigns, and updates are live.

When a meeting starts — or someone wakes the room — the display returns to the normal Teams Rooms UI automatically, and signage resumes when the room goes idle again. There's no impact on meeting quality, audio/video, or scheduled meetings.

---

## Open the Teams Rooms page

In OptiSigns, open **Devices** in the top navigation, then in the left sidebar under **Room Integrations**, click **Teams Rooms**. If you haven't connected yet, you'll see the two methods side by side.

![OptiSigns Teams Rooms — the two ways to connect: Signage URL (recommended) and Service Principal](/hc/article_attachments/52411707887891)

Pick your method below.

---

# Method 1 — Connect with a Signage URL (recommended)

No Azure setup. You'll mint a URL in OptiSigns, give it content, and paste it into the Teams Rooms portal.

### Step 1 — Mint a Signage URL
