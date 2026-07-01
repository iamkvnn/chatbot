# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Source File: 52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage.md
Chunk: 1/6

Turn idle Google Meet hardware into digital signage. When a room is between meetings, OptiSigns plays your assigned content — announcements, dashboards, branding, menus — right on the room display, and the device returns to the normal Meet UI the moment a meeting starts.

This guide covers the **two ways to connect Google Meet hardware to OptiSigns**, so you can pick the one that fits how your organization works.

---

## Two ways to connect

|  | **Signage URL**  ·  *Recommended, fastest start* | **Service Account** |
| --- | --- | --- |
| **What it gives you** | Get content on a room in minutes — no Google Cloud setup. | OptiSigns **discovers and lists all your Meet hardware** (model, online/offline) in one place. |
| **Google setup** | None. You paste a URL in the Google Admin Console. | A Workspace super-admin registers a read-only service account with domain-wide delegation. |
| **Best for** | Getting started, a few rooms, or when you can't set up a service account. | Managing a fleet of rooms and seeing their status alongside your other screens. |
| **Who can set it up** | A Google Workspace admin. | A Google Workspace **super-admin**, one time. |

> **Important — read this first.** Google does **not** offer a way for apps to push content to Meet hardware automatically. So with **either** method, the final step is a **one-time paste** of an OptiSigns signage URL into the **Google Admin Console**. The **Service Account** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: a Service Account to see every room, and Signage URLs to deliver the content.
>
> A third method, **Marketplace OAuth**, is shown as **Coming soon** in the app — use **Signage URL** or **Service Account** for now.

---

## What you'll need
