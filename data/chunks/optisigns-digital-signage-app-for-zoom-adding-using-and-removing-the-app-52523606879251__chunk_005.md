# OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App

Article URL: https://support.optisigns.com/hc/en-us/articles/52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App
Source File: optisigns-digital-signage-app-for-zoom-adding-using-and-removing-the-app-52523606879251.md
Chunk: 5/6

---

## What happens to your data after removal

- After you disconnect or deauthorize, OptiSigns revokes (where Zoom supports it) and deletes the locally stored Zoom credentials.
- The synced room inventory and the screens created for activated rooms are removed, and their licenses are released.
- Operational audit records (for example, which admin connected or disconnected the integration, and when) may be retained where needed for audit, security, and service-integrity purposes, as described in the [OptiSigns Privacy Policy](https://www.optisigns.com/privacy-policy).
- Your OptiSigns content (assets, playlists, schedules) is not affected.

If you need account-level deletion or data access requests, contact [support@optisigns.com](mailto:support@optisigns.com).

---

## Troubleshooting

- **OAuth errors during connect:** confirm you approved the app in Zoom as the Account Owner (or an Admin with Marketplace install permission) and retry from the OptiSigns Zoom Rooms page. If Zoom shows "You don't have permission to install this app," ask your Zoom Account Owner to pre-approve OptiSigns at the account level.
- **Rooms don't appear after connecting:** click **Sync now** on the Zoom Rooms page. Confirm at least one Zoom Room is provisioned in your Zoom admin portal; initial sync can take up to a minute on large accounts.
- **Signage doesn't show on a room:** ensure Digital Signage is enabled for that room in the Zoom admin portal (**Account Settings → Zoom Rooms → Digital Signage**). The next OptiSigns push succeeds automatically once enabled.
- **If disconnect appears stuck:** retry from OptiSigns first; if the issue persists, contact us with what you observed (without pasting secrets).

---

## FAQ

**Which scopes does OptiSigns request?** The nine scopes listed under "About the OptiSigns–Zoom integration" above. Zoom also displays the full list on the authorization screen before you approve.
