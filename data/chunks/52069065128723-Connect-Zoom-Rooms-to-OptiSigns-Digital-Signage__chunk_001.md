# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Source File: 52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 1/6

Turn idle Zoom Rooms into digital signage. When a Zoom Room is not in a meeting, OptiSigns plays your assigned content — images, videos, dashboards, web apps — between meetings, and clears it the moment a meeting starts.

This guide walks a Zoom Account Owner or Admin through the one-time setup at the account level, and then per-room signage activation.

---

## What you'll need

- A **Zoom account with the Owner or Admin role** (required to install and authorize the OptiSigns Marketplace app, or to create the Server-to-Server OAuth credentials).
- Any Zoom plan that includes **Zoom Rooms licensing**.
- An **OptiSigns account**. [Sign up for a free trial](https://app.optisigns.com) — you only pay for rooms you activate signage on.
- At least one **Zoom Room** with a recent Zoom Rooms client. OptiSigns does not filter by vendor — any Zoom Room that Zoom returns from the inventory API will appear in your fleet (Neat, Poly, Logitech, DTEN, Yealink appliances, and Zoom Rooms for Windows / macOS).

---

## How OptiSigns works on Zoom Rooms

OptiSigns uses the **Digital Signage** feature built into Zoom Rooms. There is no OptiSigns app installed on the device. Instead, OptiSigns pushes a signage URL + display schedule to each room via Zoom's REST API; the Zoom Rooms client renders that URL between meetings and hides it the moment a meeting starts.

There is **no impact on meeting quality**, screen-sharing, whiteboard, or Zoom Apps features.

---

## Step 1 — Sign in to OptiSigns

Go to [app.optisigns.com](https://app.optisigns.com) and sign in (or create your account).

---

## Step 2 — Open the Zoom Rooms page

In the left navigation under **Room Integrations**, click **Zoom Rooms**.

![Connect Zoom Rooms in the left nav](/hc/article_attachments/52352814423187)

---

## Step 3 — Choose a connection method
