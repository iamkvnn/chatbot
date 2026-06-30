# OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App

Article URL: https://support.optisigns.com/hc/en-us/articles/52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App
Source File: optisigns-digital-signage-app-for-zoom-adding-using-and-removing-the-app-52523606879251.md
Chunk: 4/6

OptiSigns periodically syncs the room list and room status from Zoom, and pushes signage-setting changes (layout, mute, display period) that you make in OptiSigns. Regarding meetings and call content: OptiSigns does not join, store, or access the content of meetings; video meetings run entirely on Zoom, and Zoom's own terms and policies apply to them.

---

## Removing the app — in OptiSigns

From the **Room Integrations → Zoom Rooms** page, click **Disconnect** and confirm. OptiSigns then:

- Revokes the OAuth grant with Zoom's token-revoke endpoint (Marketplace install). For a Server App there is no revoke endpoint on Zoom's side — the short-lived token simply expires; you can also deactivate the app in your Zoom Marketplace to invalidate the credentials immediately.
- Attempts to remove the OptiSigns signage entry and the OptiSigns-created library content from each room (best-effort — if a room can't be reached, leftovers can be removed in the Zoom admin portal).
- Releases all OptiSigns screen licenses used by Zoom Rooms, removes the synced room records, and stops syncing.
- Deletes the locally stored, encrypted Zoom credentials.

Revocation is best-effort: a failure talking to Zoom does not block the local disconnect, so you can always unlink the app in OptiSigns.

---

## Removing the app — in the Zoom App Marketplace

You can also uninstall on Zoom's side: go to **marketplace.zoom.us → Manage → Added Apps**, find **OptiSigns**, and click **Remove**. Zoom notifies OptiSigns through the app deauthorization webhook; OptiSigns then automatically runs the same cleanup as the in-product disconnect for the matching Zoom account — revoking access, removing pushed signage, releasing licenses, and deleting stored credentials — and confirms data-deletion compliance back to Zoom, honoring the data-retention choice you make on Zoom's uninstall screen.

---

## What happens to your data after removal
