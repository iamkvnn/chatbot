# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Source File: 52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage.md
Chunk: 1/7

Turn idle Microsoft Teams Rooms into digital signage. When a room is between meetings, OptiSigns plays your assigned content — announcements, dashboards, branding, menus — right on the room display, and clears it the instant a meeting starts.

This guide covers the **two ways to connect a Teams Room to OptiSigns**, so you can pick the one that fits how your organization works.

---

## Two ways to connect

|  | **Signage URL**  ·  *Recommended, fastest start* | **Service Principal** |
| --- | --- | --- |
| **What it gives you** | Get content on a room in minutes — no app registration. | OptiSigns **discovers and lists all your Teams Rooms** (model, online/offline, health) in one place. |
| **Microsoft setup** | None in Azure. You paste a URL in the Teams Rooms portal. | An Entra admin registers a read-only app and grants two permissions. |
| **Best for** | Getting started, a few rooms, or when you can't register an Azure app. | Managing a fleet of rooms and seeing their status alongside your other screens. |
| **Who can set it up** | A Teams Rooms admin. | A Microsoft **Entra (Azure AD) admin**, one time. |

> **Important — read this first.** Microsoft does **not** offer a way for apps to push content to Teams Rooms automatically. So with **either** method, the final step is a **one-time manual paste** of an OptiSigns signage URL into the Teams Rooms portal. The **Service Principal** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: Service Principal to see every room, and Signage URLs to deliver the content.

---

## What you'll need
