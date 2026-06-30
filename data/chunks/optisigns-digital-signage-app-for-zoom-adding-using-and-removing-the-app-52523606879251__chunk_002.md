# OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App

Article URL: https://support.optisigns.com/hc/en-us/articles/52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App
Source File: optisigns-digital-signage-app-for-zoom-adding-using-and-removing-the-app-52523606879251.md
Chunk: 2/6

The app requests the following Zoom scopes:

- `zoom_rooms:read:list_rooms:admin` — Allows OptiSigns to list the Zoom Rooms on your account so they can appear in your OptiSigns screen fleet.
- `zoom_rooms:read:room:admin` — Allows OptiSigns to read a single room's details when refreshing it.
- `zoom_rooms:read:list_devices:admin` — Allows OptiSigns to read room hardware details (model, OS, firmware version) shown in the room's device-info panel.
- `zoom_rooms:read:room_settings:admin` — Allows OptiSigns to read a room's current digital signage settings before making any change.
- `zoom_rooms:update:room_settings:admin` — Allows OptiSigns to assign the signage URL to a room and update its signage settings (layout, mute, display period).
- `zoom_rooms:write:digital_signage_library_contents:admin` — Allows OptiSigns to create (and later remove) its signage entry in your Zoom digital signage content library.
- `zoom_rooms:update:room_control:admin` — Allows OptiSigns to restart the Zoom Rooms app on a room, only when you request it.
- `zoom_rooms:read:alert:admin` — Allows OptiSigns to read room alerts so it can show room health.
- `user:read:user:admin` — Allows OptiSigns to read the connecting admin's basic profile (name, email), used only to label the connection in OptiSigns.

OptiSigns stores: room name and ID, device model / OS / firmware, online-offline status and last-seen time, and references to the signage content it created. Credentials (OAuth tokens, or the Server App Client Secret) are encrypted at rest and are never written to logs or returned over any API.

OptiSigns never accesses meeting content, recordings, transcripts, chat, calendars, or participant data — the integration requests no meeting scopes at all.

---

## Adding the app
