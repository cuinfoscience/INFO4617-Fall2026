# Image placeholders for `week-12`

These are auto-generated gray **placeholders** so the deck compiles. Replace each with the real asset described below (keep the same filename), then rebuild.

| File | Size | Should show |
|---|---|---|
| `oauth_flow.png` | 1200x760 | Diagram: OAuth2 client-credentials flow -- app sends client_id/secret to the authorization server, receives a scoped, revocable access token, then calls the platform API |
| `platform_spectrum.png` | 1220x540 | Diagram: governance spectrum from proprietary/enclosed (Reddit, Spotify) to open/portable (Bluesky via AT Protocol, Mastodon via ActivityPub) |
| `reddit_depth_decay.png` | 1100x820 | Chart: Reddit comment depth vs. score scatter showing engagement decaying as nesting deepens -- top-level (depth 0) comments score highest |
| `spotify_enclosure.png` | 1200x760 | Annotated figure: Spotify's November 2024 deprecation of audio-features / recommendations / related-artists endpoints, now returning 403 Forbidden to newly created apps |
| `bluesky_network.png` | 1000x820 | Network graph: a Bluesky ego network of followers and following built from AT Protocol get_followers / get_follows, with mutual connections highlighted |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request "Files changed" view with an inline review comment on ch-12-social.qmd |

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `bsky-profile.png` and `bsky-profile_annotated.png` and `bsky-profile_annotated.pdf` | `ch-12/bsky-profile` (images/ch-12/bsky-profile.png, textbook `752ae13`) | 2026-11-02 | https://bsky.app/profile/nws.noaa.gov | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
| `youtube-channel.png` and `youtube-channel_annotated.png` and `youtube-channel_annotated.pdf` | `ch-12/youtube-channel` (images/ch-12/youtube-channel.png, textbook `752ae13`) | 2026-11-02 | https://www.youtube.com/@NOAA | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
<!-- shots:end -->

**Used on** (Monday): `bsky-profile_annotated.pdf` on "Start from the page a person reads", at 0.58 of the text width; `youtube-channel_annotated.pdf` on "Friday's page: an agency's YouTube channel", at 0.64, because YouTube's smaller text needs the room to reach 16 pixels. Both widths are the recipes' `targets:` in the textbook, which `tools/shots/run check` measures.
