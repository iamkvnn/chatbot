# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: connect-microsoft-teams-rooms-to-optisigns-digital-signage-52350277262483.md
Chunk: 2/7

> **Important — read this first.** Microsoft does **not** offer a way for apps to push content to Teams Rooms automatically. So with **either** method, the final step is a **one-time manual paste** of an OptiSigns signage URL into the Teams Rooms portal. The **Service Principal** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: Service Principal to see every room, and Signage URLs to deliver the content.

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
